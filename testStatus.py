import os
import openai

# Read the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print("❌ OPENAI_API_KEY not found in environment variables.")
else:
    try:
        response = openai.models.list()
        print("✅ API connection successful. Models available:")
        for model in response.data:
            print(model.id)
    except openai.error.AuthenticationError:
        print("❌ Invalid API key.")
    except openai.error.RateLimitError:
        print("❌ API key is valid, but quota is exhausted or usage is restricted.")
    except openai.error.OpenAIError as e:
        print(f"❌ Other error: {e}")
