import pandas as pd
from langchain.schema.document import Document


def get_jobs_documents_list(resume_job_df: pd.DataFrame):
    
    jobs_list = list(resume_job_df['Job Description'].drop_duplicates())
    jobs_documents_list = []
    
    for i in range(len(jobs_list)):
        doc = Document(page_content=jobs_list[i])
        jobs_documents_list.append(doc)
        
    return jobs_documents_list

    
def get_resume_documents_list(resume_job_df: pd.DataFrame):
    
    resume_list = list(resume_job_df['Resume Description'].drop_duplicates())
    resume_documents_list = []
    
    for i in range(len(resume_list)):
        doc = Document(page_content=resume_list[i])
        resume_documents_list.append(doc)
        
    return resume_documents_list


def get_documents(resume_job_df: pd.DataFrame):
    
    jobs_documents_list = get_jobs_documents_list(resume_job_df)
    resume_documents_list = get_resume_documents_list(resume_job_df)
    
    return jobs_documents_list, resume_documents_list
