import streamlit as st
from src.ml.init_vector_db import init_vector_db

db_jobs, db_resume = init_vector_db()

def get_db_resume_state(db_resume: object) -> object:
    if 'db_resume' not in st.session_state:
        st.session_state.db_resume = db_resume


def get_db_jobs_state(db_jobs):
    if 'db_jobs' not in st.session_state:
        st.session_state.db_jobs = db_jobs


def get_show_vacancies_state():
    if 'show_vacancies' not in st.session_state:
        st.session_state.show_vacancies = False


def get_show_resumes_state():
    if 'show_resumes' not in st.session_state:
        st.session_state.show_resumes = False


def get_vacancies_state():
    if 'vacancies' not in st.session_state:
        st.session_state.vacancies = []


def get_resumes_state():
    if 'resumes' not in st.session_state:
        st.session_state.resumes = []


def get_state_config():
    get_db_jobs_state(db_jobs)
    get_db_resume_state(db_resume)
    get_show_vacancies_state()
    get_show_resumes_state()
    get_vacancies_state()
    get_resumes_state()
