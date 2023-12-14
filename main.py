import streamlit as st

from src.app.views.ResumeTabView import ResumeTabView
from src.app.views.VacancyTabview import VacancyTabView

if __name__ == '__main__':
    tab1, tab2 = st.tabs(["Резюме", "Вакансии"])
    with tab1:
        resume_view = ResumeTabView()

    with tab2:
        vacancy_view = VacancyTabView()
