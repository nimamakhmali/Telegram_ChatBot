import openai
from config.settings import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def get_LLM_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt_3.5_turbo",
            message=[{"role":"user", "content": prompt}]
        )
        return response.choice[0].message.content.strip()
    except Exception as e:
        return f"Error can not connect to language model: {str(e)}"