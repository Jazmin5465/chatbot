from openai import OpenAI

# client = OpenAI()

# user_input = input("\nAsk something for the chatbot: \n")

# model = "gpt-3.5-turbo"
# messages = [
#     {"role":"system","content":"You are an assistant that always answers in the form of a poem."},
#     {"role": "user", "content": user_input}
# ]

# response = client.chat.completions.create(
#     model = model,
#     messages = messages
# )

# response_for_user = response.choices[0].message.content

# print(response_for_user)

client = OpenAI()

def set_user_input_category(user_input):
    question_keywords = ["who","what","when","where","why","how","?"]
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
        return "statement"

def get_response_from_chatbot(model, messages):

    response = client.chat.completions.create(
        model = model,
        messages = messages
    )


    return response.choices[0].message.content


user_input = input("\nAsk something for the chatbot: \n")

model = "gpt-3.5-turbo"
messages = [
    {"role":"system","content":"You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]

response_for_user = get_response_from_chatbot(model, messages)

if set_user_input_category(user_input) == "question":
    response_for_user = "Good question! " + response_for_user

print(response_for_user)