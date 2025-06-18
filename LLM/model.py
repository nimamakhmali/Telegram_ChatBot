import requests
from config.settings import OPENROUTER_API_KEY

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}
MODEL = "mistralai/mixtral-8x7b-instruct"

def get_LLM_response(prompt):
    try:
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200,
            "temperature": 0.7
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code != 200:
            return f"HTTP Error {response.status_code}: {response.text}"
        try:
            result = response.json()
        except Exception as e:
            return f"JSON Parse Error: {str(e)} | Raw response: {response.text}"
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"].strip()
        elif "error" in result:
            return f"OpenRouter API Error: {result['error']}"
        else:
            return "پاسخی از مدل دریافت نشد."
    except Exception as e:
        return f"ERROR CONNECTING TO OpenRouter: {str(e)}"
