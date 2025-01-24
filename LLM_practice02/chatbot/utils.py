import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(user_input, messages):

    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    ai_response = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": ai_response})

    return ai_response, messages
