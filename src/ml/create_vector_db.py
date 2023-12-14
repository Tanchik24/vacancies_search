from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import pandas as pd

from src.ml.documents import get_documents
from src.ml.embeddings import get_embeddings

def db_create_and_save():
    
    resume_job_df = pd.read_excel('./data/resume_job.xlsx')

    jobs_documents_list, resume_documents_list = get_documents(resume_job_df)

    hf_embeddings = get_embeddings()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=3500)
    jobs_docs = text_splitter.split_documents(jobs_documents_list)
    resume_docs = text_splitter.split_documents(resume_documents_list)

    db_jobs = FAISS.from_documents(jobs_docs, hf_embeddings)
    db_resume = FAISS.from_documents(resume_docs, hf_embeddings)
    
    db_jobs.save_local("./vector_db/db_jobs")
    db_resume.save_local("./vector_db/db_resume")
    

if __name__ == '__main__':
    db_create_and_save()
    