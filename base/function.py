import os
import json
import openai

def lambda_handler(event, context):
    prompt = event["queryStringParameters"]["prompt"]
    api_key = os.environ["API_KEY"]  # Access the API key from environment variables
    openai.api_key = api_key
    model_engine = "gpt-3.5-turbo"

    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=500)
    text_result = response.choices[0].text

    return {
        'statusCode': 200,
        'body': json.dumps(text_result, ensure_ascii=False, indent=4)
    }
