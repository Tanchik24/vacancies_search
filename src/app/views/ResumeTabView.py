import pandas as pd
import streamlit as st

from src.ml.recommendations import get_job_recommendations
from src.app.data import Resume
from src.app.views import TabView
from src.app import Format


def display_vacancies(vacancies):
    format = Format()
    for vacancie in vacancies:
        url = False
        if 'Название' in vacancie:
            text = format.format_vacancy2(vacancie)
        else:
            text, title, url = format.format_vacancy(vacancie)
        st.sidebar.write(text)
        if url:
            link = f"[Подробнее о {title}]({url})"
            st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write("---")


class ResumeTabView(TabView):
    def __init__(self):
        super().__init__("Резюме")
        self.text_info: Resume = self.get_text_info()
        self.visualize_text_info()
        self.get_candidates()

    def get_text_info(self) -> Resume:
        return Resume(
            name=st.text_input("Имя"),
            surname=st.text_input("Фамилия"),
            city=st.text_input("Город"),
            experience=st.slider("Опыт работы (годы)", 0, 50, 1),
            desired_salary=st.number_input("Желаемая зарплата", min_value=0),
            description=st.text_area("Резюме", height=300)
        )

    def visualize_text_info(self):
        if st.button("Показать резюме"):
            st.sidebar.header("Введенная информация")
            fields_titles = {
                'Имя:': self.text_info.name,
                'Фамилия:': self.text_info.surname,
                'Город:': self.text_info.city,
                'Опыт работы:': str(self.text_info.experience) + ' ' + "год(а/лет)",
                'Желаемая зарплата:': self.text_info.desired_salary,
                'Резюме:': self.text_info.description
            }

            for title, value in fields_titles.items():
                st.sidebar.write(title, value)

    def get_candidates(self):

        if st.button("Получить вакансии"):
            info_dict = {'Город': self.text_info.city, 'Опыт работы': self.text_info.experience,
                         'Желаемая зарплата': self.text_info.desired_salary}
            
            vacancies_list=get_job_recommendations(text=self.text_info.description)
            
            display_vacancies(vacancies_list)
