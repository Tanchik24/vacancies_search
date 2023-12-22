from langchain.embeddings import HuggingFaceEmbeddings


def get_embeddings(model_name: str = "intfloat/multilingual-e5-large"):
    hf_embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cuda'},
        encode_kwargs={'normalize_embeddings': True}
    )

    return hf_embeddings
