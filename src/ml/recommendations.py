import streamlit as st


def get_job_recommendations(text: str, city: str = None):
    if city is not None:
        if city == 'Удаленная работа':
            docs = st.session_state.db_jobs.similarity_search_with_score(text, k=10, filter={'city': city})  # если кандидат ищет удаленку - так и ищем
        else:
            docs_city = st.session_state.db_jobs.similarity_search_with_score(text, k=10, filter={'city': city})  # иначе попробуем найти и локально и удаленку
            docs_dist = st.session_state.db_jobs.similarity_search_with_score(text, k=10, filter={'city': 'Удаленная работа'})
            docs = docs_city + docs_dist

            docs.sort(key=lambda doc: doc[1])  # sort by score (distance)
            docs = docs[:10]
    else:
        docs = st.session_state.db_jobs.similarity_search_with_score(text, k=10)
            
    vacancies_list = [doc[0].page_content for doc in docs]
    return vacancies_list


def get_resume_recommendations(text: str, city: str = None):
    
    if city is not None:
        if city == 'Удаленная работа':
            docs = st.session_state.db_resume.similarity_search_with_score(text, k=10)  # у компании удаленка -> не важно где кандидат
        else:
            docs = st.session_state.db_resume.similarity_search_with_score(text, k=10, filter={'city': city})  # если в конкретном городе (без удаленки)
    else:
        docs = st.session_state.db_resume.similarity_search_with_score(text, k=10)
            
    resume_list = [doc[0].page_content for doc in docs]
    return resume_list