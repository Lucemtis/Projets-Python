import openai
import json

openai.api_key = "your key"

def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

while True:
    user_input = input("User: ")
    response = ask_chatgpt(user_input)
    print("ChatGPT: " + response)
