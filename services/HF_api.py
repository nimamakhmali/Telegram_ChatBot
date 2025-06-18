import requests
from config.settings import HF_API_KEY  # مطمئن شو این مقدار رو درست ست کردی

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"  # مدل گفتگومحور
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def ask_openai(prompt: str) -> str:
    try:
        payload = {
            "inputs": f"User: {prompt}\nAssistant:",  # فرمت پرسش برای مدل‌های گفتگومحور
            "parameters": {
                "temperature": 0.7,
                "max_new_tokens": 200,
                "return_full_text": False
            },
            "options": {
                "wait_for_model": True
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        elif "error" in result:
            return f"Hugging Face API Error: {result['error']}"
        else:
            return "پاسخی از مدل دریافت نشد."
    except Exception as e:
        return f"ERROR CONNECTING TO HF: {str(e)}"
