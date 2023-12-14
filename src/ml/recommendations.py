from src.ml.init_vector_db import init_vector_db
db_jobs, db_resume = init_vector_db()


def get_job_recommendations(text: str):
    docs = db_jobs.similarity_search(text, k=10) 
    vacancies_list = [doc.page_content for doc in docs]
    return vacancies_list


def get_resume_recommendations(text: str):
    docs = db_resume.similarity_search(text, k=10) 
    resume_list = [doc.page_content for doc in docs]
    return resume_list