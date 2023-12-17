import pandas as pd
from langchain.schema.document import Document


def get_jobs_documents_list(resume_job_df: pd.DataFrame):
    
    df_no_dup = resume_job_df[['Job Description', 'city_job']].drop_duplicates().reset_index(drop=True)
    
    jobs_list = list(df_no_dup['Job Description'])
    jobs_documents_list = []
    
    for i in range(len(jobs_list)):
        doc = Document(page_content=jobs_list[i], metadata={'city': df_no_dup.loc[i, ['city_job']].iloc[0]})
        jobs_documents_list.append(doc)
        
    return jobs_documents_list

    
def get_resume_documents_list(resume_job_df: pd.DataFrame):
    
    df_no_dup = resume_job_df[['Resume Description', 'city_resume']].drop_duplicates().reset_index(drop=True)
    
    resume_list = list(df_no_dup['Resume Description'].drop_duplicates())
    resume_documents_list = []
    
    for i in range(len(resume_list)):
        doc = Document(page_content=resume_list[i], metadata={'city': df_no_dup.loc[i, ['city_resume']].iloc[0]})
        resume_documents_list.append(doc)
        
    return resume_documents_list


def get_documents(resume_job_df: pd.DataFrame):
    
    jobs_documents_list = get_jobs_documents_list(resume_job_df)
    resume_documents_list = get_resume_documents_list(resume_job_df)
    
    return jobs_documents_list, resume_documents_list
