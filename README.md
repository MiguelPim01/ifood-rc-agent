# POC Agente de Reembolso e Cancelamento (RAG)

## Sobre

Este projeto consiste em uma Prova de Conceito (POC) de um agente de Inteligência Artificial desenvolvido para auxiliar na tomada de decisões internas sobre reembolsos e cancelamentos.

Utilizando técnicas de **RAG (Retrieval-Augmented Generation)**, o agente consulta uma base de conhecimento simulada para fornecer respostas consistentes e fundamentadas em políticas operacionais.

**Principais características:**
*   **Base de Conhecimento:** Utiliza um arquivo CSV (`base_conhecimento_ifood_genai-exemplo.csv`) como fonte de verdade.
*   **Fallback de Segurança:** Configurado para identificar situações de baixa confiança e sugerir validação manual ou abertura de tickets, evitando alucinações.
*   **Cenários Críticos:** Validado contra cenários complexos como pedidos já em entrega, cancelamentos por falha do restaurante e cobranças indevidas.
*   **Foco:** Consistência operacional e redução de respostas incorretas.

**Tecnologias utilizadas:**
*   Python
*   LangChain
*   ChromaDB (Vector Store)
*   OpenAI API

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd IFood
    ```

2.  **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/Mac
    # ou
    .\venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração de Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:
    ```env
    OPENAI_API_KEY=<sua-chave>
    ```

## Como Usar

O projeto possui um script principal que executa uma bateria de perguntas de teste contra o agente e salva os resultados.

Para executar o agente:

```bash
python -m src.run_agent
```

Após a execução, os resultados (perguntas e respostas geradas) estarão disponíveis no arquivo:
`results/respostas_agente_ifood.csv`

## Autor

Desenvolvido por [Miguel Vieira Machado Pim](https://github.com/MiguelPim01) como parte de um portfólio técnico demonstrando aplicação de GenAI em fluxos operacionais.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
