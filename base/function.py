import os
import json
import openai


def lambda_handler(event, context):
    prompt = event["queryStringParameters"]["prompt"]
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_engine = "gpt-3.5-turbo"
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=500)
    text_result = response.choices[0].text
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(text_result, ensure_ascii=False, indent=4)
    }
