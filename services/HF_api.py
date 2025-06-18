import requests
from config.settings import HF_API_KEY  # مطمئن شو این مقدار رو درست ست کردی

# استفاده از مدل کوچک و رایگان HuggingFaceH4/zephyr-7b-beta
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
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
        if response.status_code != 200:
            return f"HTTP Error {response.status_code}: {response.text}"

        try:
            result = response.json()
        except Exception as e:
            return f"JSON Parse Error: {str(e)} | Raw response: {response.text}"

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
        elif "error" in result:
            return f"Hugging Face API Error: {result['error']}"
        else:
            return "پاسخی از مدل دریافت نشد."
    except Exception as e:
        return f"ERROR CONNECTING TO HF: {str(e)}"
