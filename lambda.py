import openai
import json
import random

openai.api_key = "PUT_YOUR_KEY_HERE"


def lambda_handler(event, context):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Give me one random quote with it author and explain it. the quote should be from mohamed prophete or Jesus or Moise (PBUH)",
        temperature=1,
        max_tokens= random.randint(150, 1000),
        top_p= 0.7
    )
    answer = response['choices'][0]['text']

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "answer": answer
        })
    }

    return response
