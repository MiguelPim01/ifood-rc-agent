from pathlib import Path
import csv
import logging
import sys

from src.core.agent import Agent

# Configurando logging
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s - %(levelname)s] - %(message)s',
                    stream=sys.stdout)

TEST_QUESTIONS = [
    "O cliente quer reembolso, mas o pedido já saiu para entrega. O reembolso ainda é permitido?",
    "O restaurante cancelou por falta de ingrediente. O reembolso é automático?",
    "O cliente foi cobrado após o cancelamento. O que fazer?"
]

def main():
    logging.info("Iniciando validação do agente iFood.")

    agent = Agent()
    resultados = []

    for pergunta in TEST_QUESTIONS:
        resposta = agent.answer_question(pergunta)

        resultados.append({
            "pergunta": pergunta,
            "resposta": resposta,
        })

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "respostas_agente_ifood.csv"

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["pergunta", "resposta"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(resultados)

    logging.info("Perguntas processadas com sucesso.")

if __name__ == "__main__":
    main()