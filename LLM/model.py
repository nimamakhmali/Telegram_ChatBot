import requests
from config.settings import HF_API_KEY  # باید نام متغیر API رو به HF_API_KEY تغییر بدی

# مدل هماهنگ با کل پروژه (HuggingFaceH4/zephyr-7b-beta)
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def get_LLM_response(prompt):
    try:
        payload = {
            "inputs": f"User: {prompt}\nAssistant:",
            "parameters": {
                "temperature": 0.7,
                "max_new_tokens": 200,
                "return_full_text": False
            },
            "options": {"wait_for_model": True}
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
            return f"Error from HF: {result['error']}"
        else:
            return "مدل پاسخ مشخصی نداد."
    except Exception as e:
        return f"Error connecting to Hugging Face API: {str(e)}"
