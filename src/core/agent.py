import os
from dotenv import load_dotenv
import logging

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

from src.utils import prompt

load_dotenv()

os.makedirs("logs", exist_ok=True)

# Configurando logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s - %(levelname)s] - %(message)s',
                    filename="logs/ifood_agent.log",
                    filemode="w",
                    encoding="utf-8")

API_KEY = os.getenv("OPENAI_API_KEY")

class Agent:
    
    def __init__(self):
        embeddings = OpenAIEmbeddings(openai_api_key=API_KEY)
        
        # Obtendo o vectorstore previamente criado
        self._vectorstore = Chroma(
            collection_name="ifood_reembolso_cancelamento",
            embedding_function=embeddings,
            persist_directory="chroma_db"
        )
        
        # Adicionando uma baixa temperatura para repostas mais estáveis
        self._llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.1
        )
        
        # Carregando o prompt do sistema
        self._system_prompt = prompt.SYSTEM_PROMPT
    
    def answer_question(self, question: str) -> str:
        logging.info("Buscando documentos similares.")
        try:
            searched_docs = self._vectorstore.similarity_search_with_score(question, k=4)
        except Exception as e:
            logging.error(f"Erro ao buscar documentos similares: {e}")
            return prompt.ERROR_MESSAGE
        
        if not searched_docs:
            return prompt.FALLBACK_MESSAGE
        
        score_threshold = 0.4
        relevant_docs = [doc for doc, score in searched_docs if score < score_threshold]
        
        if not relevant_docs:
            return prompt.FALLBACK_MESSAGE
        
        context = "\n\n".join(
            [f"[TRECHO {i}]\n{doc.page_content}" for i, doc in enumerate(relevant_docs)]
        )
        
        logging.info("Construindo prompt.")
        _prompt = prompt.build_prompt(
            system_prompt=self._system_prompt,
            context=context,
            question=question
        )
        
        logging.info("Gerando resposta da LLM")
        try:
            llm_answer = self._llm.invoke(_prompt)
        except Exception as e:
            logging.error(f"Erro ao gerar resposta do LLM: {e}")
            return prompt.ERROR_MESSAGE
        
        return llm_answer.content.strip()