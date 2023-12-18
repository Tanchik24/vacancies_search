import re


class ResumesFormat:
    def __init__(self):
        self.patterns = {
            'Пол, возраст': r"Пол, возраст: (.+?);",
            'Зарплата': r"ЗП: (.+?);",
            'Должность': r"Ищет работу на должность: (.+?);",
            'Город, переезд, командировки': r"Город, переезд, командировки: (.+?);",
            'Занятость': r"Занятость: (.+?);",
            'График': r"График: (.+?);",
            'Опыт работы': r"Опыт работы: (.+)",
            'Последнее место работы': r"Последнее/нынешнее место работы: (.+?);",
            'Последняя должность': r"Последняя/нынешняя должность: (.+?);",
            'Образование': r"Образование и ВУЗ: (.+?);",
            'Обновление резюме': r"Обновление резюме: (.+?);",
            'Авто': r"Авто: (.+)"
        }

    def format(self, text):
        if ('Пол, возраст' not in text) and ('Должность' not in text):
            return text
        formatted_resume = ""

        if match := re.search(self.patterns['Должность'], text, re.DOTALL):
            match_text = match.group(1).strip().split(' ')
            match_text[0] = match_text[0].title()
            formatted_resume += f"<h1 style='color: white;'> {' '.join(match_text)}</h1>\n\n"

        for key, pattern in self.patterns.items():
            if key != 'Должность':
                match = re.search(pattern, text, re.DOTALL)
                if match:
                    formatted_resume += f"<h4 style='color: white;'>{key}:</h4><p style='color: grey;'>{match.group(1).strip()}</p>\n\n"

        return formatted_resume.strip()
