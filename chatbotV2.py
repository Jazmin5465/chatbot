from openai import OpenAI
import tiktoken
import logging
import datetime

logger = logging.getLogger("token_log")
logging.basicConfig(filename="token_log.log", level = logging.INFO)

client = OpenAI()

# accepts a preferred model and a list of messages
# makes chat completions API call
# returns the response message content
def get_api_chat_response_message(model, messages):
    # make the API call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    # return the response text
    return response_content

model = "gpt-3.5-turbo"
encoding = tiktoken.encoding_for_model(model)
print(encoding)
chat_history = []
token_input_limit = 12289
total_token_count = 0

print("Chatbot: Welcome! I am your assistant, how may I help you today? (type in 'exit' at any time to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        logger.info("Total tokens: " + str(total_token_count) + " on " + str(datetime.datetime.now())+"\n\n")
        break
    
    # returns a list of token integers
    user_input_encoded = encoding.encode(user_input)
    print(user_input_encoded)

    # returns the count of tokens
    token_count = len(encoding.encode(user_input))
    print(token_count)

    if(token_count>token_input_limit):
        print("Your prompt is too long. Please try again.")
        continue # starts a new iteration of the while loop

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    response = get_api_chat_response_message(model, chat_history)
    total_token_count += response.usage.total_tokens

    print("Chatbot: ", response)

    chat_history.append({
        "role": "assistant",
        "content": response
    })