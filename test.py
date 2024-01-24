import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

MODEL = "gpt-3.5-turbo"

OPEN_AI_SECRET = os.environ.get("OPEN_AI_SECRET")

if OPEN_AI_SECRET is None:
    raise EnvironmentError("Please set OPEN_AI_SECRET in your .env file")


client = OpenAI(
    api_key = OPEN_AI_SECRET,
)

initialContext = [
    {
        "role": "system",
        "content": "Você é um chatbot que deve ajudar os clientes "
                   "de uma escola a se matricularem em um dos cursos "
                   "oferecidos pela instituição."
    },
    {
        "role": "system",
        "content": "Os cursos oferecidos são: "
                   "Curso de Inglês, Curso de Espanhol, Curso de Francês, "
                   "Curso de Alemão, Curso de Italiano, Curso de Japonês. "
                   "Todos os cursos são oferecidos em três níveis: "
                   "Básico, Intermediário e Avançado."
                   "Todos os cursos custam R$ 100,00 por mês."
    },
    {
        "role": "system",
        "content": "Para se matricular em um curso, "
                   "o cliente deve informar o nome do curso, "
                   "o nível do curso e o nome do cliente."
    },
    {
        "role": "system",
        "content": "Após recebido esses dados o chatbot deve "
                   "informar o valor da matrícula e perguntar "
                   "se o cliente deseja confirmar a matrícula."
    },
    {
        "role": "system",
        "content": "Caso o cliente confirme a matrícula, "
                   "o chatbot deve informar que a matrícula foi "
                   "realizada com sucesso."
                   "E agradecer o cliente pelo contato, e dizer que "
                   "o time de atendimento entrará em contato para "
                   "informar os dados de acesso ao curso."
    },
    {
        "role": "system",
        "content": "Você deve evitar respostas muito longas, "
                   "e deve responder de forma simples e direta."
    }
]

messages = initialContext

utilizedTokens = 0

print("### Welcome to the chatbot!###\n")
print("Type 'quit' to exit the chatbot.\n")

while True:

    message = input("You: ")

    if message.lower().strip() == "quit":
        print("Chatbot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        messages=messages,
        model=MODEL,
        temperature=0
    )

    utilizedTokens += response.usage.total_tokens
    responseText = response.choices[0].message.content

    print("\nChatbot: " + responseText)
    print(f"Sum of Tokens used: {utilizedTokens}\n")
    
    messages.append({
        "role": "system",
        "content": responseText
    })
