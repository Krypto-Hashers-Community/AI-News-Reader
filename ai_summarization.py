import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
locale = os.getenv('LOCALE')

def summarize_text(text, word_limit=40):
    prompt = f"please summarize the news using no more than {word_limit} words. The content of the news is: {text}. The language of the result is {locale}"
    response = openai.responses.create(
        model="gpt-4.1-mini",
        input= prompt,
        max_output_tokens=200
    )
    return response.output_text
