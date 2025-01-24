import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "너는 영어 선생님이야. user의 영어 공부를 도와줘."

messages = [{"role": "system", "content": prompt}]

with open("text.txt", "w", encoding="utf-8") as file:
    file.write("대화시작: " + prompt + "\n")

    while True:
        user_input = input("USER: ")

        if user_input.lower() == "그만":
            print("종료합니다.")
            break

        messages.append({"role": "user", "content": user_input})
        
        file.write("USER: " + user_input + "\n")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        ai_response = response['choices'][0]['message']['content']

        print("AI: " + ai_response)

        file.write("AI: " + ai_response + "\n")
