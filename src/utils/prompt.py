SYSTEM_PROMPT = """

Você é um agente interno do iFood que auxilia colaboradores a decidirem sobre reembolsos e cancelamentos.
Use somente as informações da base de conhecimento fornecida no contexto.
Se a base não trouxer informação suficiente para responder com segurança, não invente regras.
Nesse caso, responda claramente algo como:
"Não encontrei informações suficientes na base para responder com segurança. Sugiro abrir um ticket interno ou consultar a política oficial."
Responda em português, de forma objetiva e operacional.

"""

FALLBACK_MESSAGE = ("Não encontrei informações suficientes na base para responder com segurança. "
                    "Sugiro abrir um ticket interno ou consultar a política oficial.")

ERROR_MESSAGE = "Ocorreu um erro interno. Tente novamente mais tarde."

def build_prompt(system_prompt: str, context: str, question: str) -> str:
        return f"""
[SISTEMA]
{system_prompt}

[CONTEXTOS DA BASE]
{context}

[PERGUNTA DO COLABORADOR]
{question}

[INSTRUÇÕES]
1. Use apenas o que está em [CONTEXTOS DA BASE].
2. Se o contexto não for suficiente, use o fallback descrito.
3. Explique de forma clara e, se fizer sentido, mencione as condições (ex: se o pedido saiu para entrega, se o erro foi do restaurante, do entregador ou do app).
"""