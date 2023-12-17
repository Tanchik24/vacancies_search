import pandas as pd

import streamlit as st

from src.app.data import Vacancy
from src.app.views import TabView

from src.ml.recommendations import get_resume_recommendations
from src.ml.init_vector_db import init_vector_db

db_jobs, db_resume = init_vector_db()


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

        if st.button("Получить кандидатов"):
            info_dict = {'Город': self.text_info.city, 'Предлагаемая зарплата': self.text_info.salary}
            
            if len(info_dict['Город'])>0:
                city = info_dict['Город']
            else:
                city = None
                
            vacancies_list=get_resume_recommendations(text=self.text_info.description, city=city)
            
            display_resumes(vacancies_list)