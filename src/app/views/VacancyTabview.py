import pandas as pd

import streamlit as st

from src.app.data import Vacancy
from src.app.views import TabView


def display_resumes(resumes):
    for resume in resumes:
        st.sidebar.write(resume)
        st.sidebar.write("---")



class VacancyTabView(TabView):
    def __init__(self):
        super().__init__("Вакансия")
        self.text_info: Vacancy = self.get_text_info()
        self.visualize_text_info()
        self.get_candidates()

    def get_text_info(self) -> Vacancy:
        return Vacancy(
            name=st.text_input('Название вакансии'),
            city=st.text_input("Город работы"),
            salary=st.number_input("Предлагаемая зарплата", min_value=0),
            description=st.text_area("Вакансия", height=300)
        )

    def visualize_text_info(self):
        if st.button("Показать вакансию"):
            st.sidebar.header("Введенная информация")
            fields_titles = {
                'Название вакансии:': self.text_info.name,
                'Город:': self.text_info.city,
                'Предлагаемая зарплата:': self.text_info.salary,
                'Вакансия:': self.text_info.description
            }

            for title, value in fields_titles.items():
                st.sidebar.write(title, value)

    def get_candidates(self):
        df = pd.read_excel('./data/resume_job.xlsx')
        random_rows = df.sample(n=10)
        resumes = random_rows['Resume Description'].tolist()
        if st.button("Получить кандидатов"):
            info_dict = {'Город': self.text_info.city, 'Предлагаемая зарплата': self.text_info.salary}
            # метод для получения списка из резюме
            display_resumes(resumes)