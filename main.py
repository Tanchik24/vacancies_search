import streamlit as st
from src.app.states_config import get_state_config
from src.app.views.ColumnsView import ColumnsView

st.set_page_config(layout="wide")
get_state_config()


if __name__ == '__main__':

    st.markdown('<h1 style="text-align: left; color: #FF2A00">Найдите работу мечты/ кандидата мечты</h2>',
                unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Резюме", "Вакансии"])

    with tab1:
        resume_view = ColumnsView('resumes')


    with tab2:
        vacancy_view = ColumnsView('vacancies')

