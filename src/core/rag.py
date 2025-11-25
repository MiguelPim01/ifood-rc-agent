import os
import pandas as pd
from dotenv import load_dotenv
import logging
import sys

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from openai import RateLimitError

# Carrega variáveis de ambiente
load_dotenv()

# Configurando logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s - %(levelname)s] - %(message)s',
                    stream=sys.stdout)

API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    df = pd.read_csv("base_conhecimento_ifood_genai-exemplo.csv")
    
    texts = []
    metadatas = []
    
    # Unificar todos os textos
    for _, row in df.iterrows():
        # Obtendo colunas da base de conhecimento
        resposta = str(row.get("resposta", ""))
        pergunta = str(row.get("pergunta", ""))
        categoria = str(row.get("categoria", ""))
        
        full_text = f"Pergunta: {pergunta}\nResposta: {resposta}\nCategoria: {categoria}"
        
        texts.append(full_text)
        metadatas.append({
            "pergunta": pergunta,
            "categoria": categoria
        })
    
    # Transformar os textos em embeddings e salvar todos eles em um banco de dados vetorial
    embeddings = OpenAIEmbeddings(api_key=API_KEY)
    
    try:
        vectorstore = Chroma.from_texts(
            texts=texts,
            embedding=embeddings,
            metadatas=metadatas,
            collection_name="ifood_reembolso_cancelamento",
            persist_directory="chroma_db"
        )
        
        logging.info("Vector store criado e salvo em ./chroma_db")
    except RateLimitError as e:
        logging.error(f"Erro de limite/quota na API de embeddings: {e}")
    except Exception as e:
        logging.error(f"Erro inesperado ao criar vector store: {e}")

if __name__ == "__main__":
    main()