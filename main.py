from openai import OpenAI

client = OpenAI()

user_input = input("\nAsk something for the chatbot: \n")

model = "gpt-3.5-turbo"
messages = [
    {"role":"system","content":"You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]

response = client.chat.completions.create(
    model = model,
    messages = messages
)

response_for_user = response.choices[0].message.content

print(response_for_user)