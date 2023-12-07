import os
import json
import openai


def lambda_handler(event, context):
    prompt = event["queryStringParameters"]["prompt"]
    openai.api_key = os.getenv("API_KEY")  # Retrieve API key from environment variables

    model_engine = "gpt-3.5-turbo"

    # Chat Completion endpoint for chat models
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are a personal Gujarati language teacher."},
                  {"role": "assistant", "content": "Hi there, I’m Jolly. Welcome to the first step of your "
                                                   "Gujarati language journey! Are you ready?"},
                  {"role": "user", "content": prompt}]
    )

    # Extracting the text from the response
    text_result = response.choices[0].message['content']

    return {
        'statusCode': 200,
        'body': json.dumps(text_result, ensure_ascii=False, indent=4)
    }
