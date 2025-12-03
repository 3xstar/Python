import openai
question = input("Запрос к DeepSeek: ")
client = openai.OpenAI(
    api_key="io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6ImRmZDc0NzY1LTE5M2EtNDlhNS1iOWY1LWI3ZTE1NDYzMDFjNyIsImV4cCI6NDkwMDE0NDE0MH0.gQAu3RZq5BCQT_9BP8_uDT8NCPT8BMerNQh4_nTDijd14XW9zzhawhnxAOEQTaodVPze-cUqZb_vGn5n0DS50w",
    base_url="https://api.intelligence.io.solutions/api/v1/",
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B",
    messages=[
        {"role": "user", "content": question},
    ],
    temperature=0.7,
    stream=False,
    max_completion_tokens=50
)

print(response.choices[0].message.content)