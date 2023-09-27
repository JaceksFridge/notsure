
import os
import openai
from openai.secret import OPEN_KEY



key = OPEN_KEY


openai.api_key = key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
            "role": "user",
            "content": "Write 10 Bullet Points why Java sucks."
        }],
    temperature=0,
    max_tokens=1024
)

print(response['choices'][0]['message']['content'])
