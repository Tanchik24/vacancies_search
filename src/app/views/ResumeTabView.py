import streamlit as st

from src.ml.recommendations import get_job_recommendations
from src.app.data import Resume
from src.app.views import TabView
from src.app import VacanciesFormat



class ResumeTabView(TabView):
    def __init__(self):
        super().__init__("Резюме")
        self.text_info: Resume = self.get_text_info()
        self.get_candidates()
        self.visualize_text_info()


    def get_text_info(self) -> Resume:
        return Resume(
            name=st.text_input("Имя"),
            surname=st.text_input("Фамилия"),
            city=st.text_input("Город"),
            experience=st.slider("Опыт работы (годы)", 0, 50, 1),
            desired_salary=st.number_input("Желаемая зарплата", min_value=0),
            description=st.text_area("Резюме", height=300)
        )

        st.experimental_rerun()

    def visualize_text_info(self):
        if st.button("Показать резюме"):
            st.header("Введенная информация")
            fields_titles = {
                'Имя:': self.text_info.name,
                'Фамилия:': self.text_info.surname,
                'Город:': self.text_info.city,
                'Опыт работы:': str(self.text_info.experience) + ' ' + "год(а/лет)",
                'Желаемая зарплата:': self.text_info.desired_salary,
                'Резюме:': self.text_info.description
            }

            for title, value in fields_titles.items():
                st.write(title, value)

    def get_candidates(self):

        if st.button("Получить вакансии"):
            st.session_state.show_vacancies = True
            if "city_resume" in st.session_state:
                st.write("Введенные данные:", st.session_state.user_input)
            info_dict = {'Город': self.text_info.city, 'Опыт работы': self.text_info.experience,
                         'Желаемая зарплата': self.text_info.desired_salary}

            if len(info_dict['Город']) > 0:
                city = info_dict['Город']
            else:
                city = None

            vacancies_list = get_job_recommendations(text=self.text_info.description, city=city)
            st.session_state.vacancies = vacancies_list
            st.experimental_rerun()

    @staticmethod
    def display(vacancies, col):
        format = VacanciesFormat()
        for vacancy in vacancies:
            url = False
            if 'Название' in vacancy:
                text = format.format_vacancy2(vacancy)
            else:
                text, title, url = format.format_vacancy(vacancy)
            col.markdown(text, unsafe_allow_html=True)
            if url:
                link = f"[Подробнее о {title}]({url})"
                col.markdown(link, unsafe_allow_html=True)
            col.write("---")
