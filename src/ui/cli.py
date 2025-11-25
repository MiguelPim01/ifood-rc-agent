from src.core.agent import Agent

def main():
    print("Agente iFood - Reembolsos e Cancelamentos (digite 'sair' para encerrar)")
    
    # Criando um agente IFood
    agent = Agent()
    
    while True:
        pergunta = input("\nPergunta do colaborador: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break

        resposta = agent.answer_question(pergunta)
        print("\nResposta do agente:")
        print(resposta)

if __name__ == "__main__":
    main()