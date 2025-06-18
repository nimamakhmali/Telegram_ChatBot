import requests
from config.settings import HF_API_KEY  # باید نام متغیر API رو به HF_API_KEY تغییر بدی

API_URL = "https://api-inference.huggingface.co/models/gpt2"  # می‌تونی مدل رو عوض کنی
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def get_LLM_response(prompt):
    try:
        payload = {
            "inputs": prompt,
            "options": {"wait_for_model": True}  # اگر مدل آماده نباشه، صبر کنه
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        result = response.json()

        # بررسی نوع پاسخ
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        elif "error" in result:
            return f"Error from HF: {result['error']}"
        else:
            return "مدل پاسخ مشخصی نداد."
    except Exception as e:
        return f"Error connecting to Hugging Face API: {str(e)}"
