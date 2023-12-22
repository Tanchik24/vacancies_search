import re

class VacanciesFormat:
    def __int__(self):
        pass

    @staticmethod
    def extract_vacancy_title(text):
        lines = text.strip().split('\n')
        title = next((line.strip() for line in lines if line.strip()), "Вакансия")
        return title

    @staticmethod
    def extract_vacancy_url(text):
        urls = re.findall(r'https?://\S+', text)
        return urls[0] if urls else None

    @staticmethod
    def format_vacancy(text):
        if 'Header' in text:
            title_match = re.search(r"Header: (.+?); Emoji:", text) or re.search(r"^(.+)\n", text)
            title = title_match.group(1).strip() if title_match else "Unknown Title"
        else:
            title = VacanciesFormat.extract_vacancy_title(text)
        formatted_text = f"# {title}\n\n"

        patterns = {
            'Мы ждем, что вы': r"Мы ждем, что вы:\n(.+?)(?=Что нужно делать:)",
            'Что нужно делать': r"Что нужно делать:\n(.+?)(?=Будет плюсом, если вы:)",
            'Будет плюсом, если вы': r"Будет плюсом, если вы:\n(.+)"
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.DOTALL)
            if match:
                content = match.group(1).strip()
                pattern = r"•\s*([^•]+)"
                content = re.sub(pattern, r"- \1", content)
                formatted_text += f"## {key}\n{content}\n\n"

        url = VacanciesFormat.extract_vacancy_url(formatted_text)
        formatted_text = re.sub(re.escape(url), '', formatted_text) if url else formatted_text
        formatted_text = re.sub(r'#\S+', '', formatted_text)

        return formatted_text.strip(), title, url

    @staticmethod
    def format_vacancy2(text):
        title = VacanciesFormat.extract_vacancy_title(text)
        formatted_text = f"# {title.split(':')[1]}\n\n"

        patterns = {
            'Цена': r"Цена: (.+?)(?=, Условия:)",
            'Условия': r"Условия: (.+?)(?=, Расположение:)",
            'Расположение': r"Расположение: (.+?)(?= Описание:)",
            'Описание': r"Описание: (.+)"
        }

        extracted_sections = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.DOTALL)
            if match:
                extracted_sections[key] = match.group(1).strip()

            if key == 'Условия':
                conditions_dict = eval(extracted_sections[key])
                for key, value in conditions_dict.items():
                    formatted_text += f"- **{key}:** {value}\n"
            else:
                formatted_text += f"## {key}: \n"
                pattern = r"•\s*([^•]+)"
                extracted_sections[key] = re.sub(pattern, r"- \1", extracted_sections[key])
                formatted_text += f'{extracted_sections[key]} \n'

        url = VacanciesFormat.extract_vacancy_url(formatted_text)
        formatted_text = re.sub(re.escape(url), '', formatted_text) if url else formatted_text
        formatted_text = re.sub(r'#\S+', '', formatted_text)

        return formatted_text
