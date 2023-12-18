import streamlit as st

from src.app.views.ResumeTabView import ResumeTabView
from src.app.views.VacancyTabview import VacancyTabView

class ColumnsView:
    def __init__(self, target='vacancies'):
        self.target = VacancyTabView if target == 'vacancies' else ResumeTabView
        self.flag = st.session_state.show_resumes if target == 'vacancies' else st.session_state.show_vacancies
        self.data = st.session_state.resumes if target == 'vacancies' else st.session_state.vacancies
        self.init_colimns()

    def init_colimns(self):
        if self.flag:
            col1, space_col, col2 = st.columns([3, 1, 6])

            with col1:
                self.target()

            with col2:
                self.target.display(self.data, col2)

        else:
            space_col1_1, col2_1, space_col1_2 = st.columns([1, 3, 1])
            with col2_1:
                self.target()