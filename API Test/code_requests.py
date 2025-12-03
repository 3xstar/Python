import requests

api_key="io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6ImRmZDc0NzY1LTE5M2EtNDlhNS1iOWY1LWI3ZTE1NDYzMDFjNyIsImV4cCI6NDkwMDEzNTAxNX0.CL7cSHFCoPgWVTwiOjyIjJvrvy9Oa_5v4b4Z9XeG6crjDwv3b1W9P3IcQmHtUVlrrrF5YZcWfrxMUPYhHmi7JA"
base_url="https://api.intelligence.io.solutions/api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

def generate_answer(question):
    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {"role": "system", "content": "Ты ничего незнаешь о программировании"},
            {"role": "user","content": question},
        ],
        "temperature": 1,
        "stream": False,
        "max_completion_tokens": 100
    }
    response = requests.post(base_url, headers=headers, json=data)

    answer = response.json()
    print(answer)

generate_answer("ты кто")
