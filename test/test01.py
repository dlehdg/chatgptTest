import os
import openai
openai.api_key = "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"


messages = []

while True:
    user_content = "다음 글에서 감정을 fear 또는 sadness 또는 joy 또는 disgust 또는 anger로 분류하세요, 결과값은 fear 또는 sadness 또는 joy 또는 disgust 또는 anger와 감정비율을  나타나게 하세요" + input("users : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    assistant_content = completion.choices[0].message["content"].strip()

    messages.append({"role":"assistant", "content": f"{assistant_content}"})

    print(f"gpt : {assistant_content}") # 챗gpt api를 이용한 챗봇 구현