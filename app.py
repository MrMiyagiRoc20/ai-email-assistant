import openai

openai.api_key = "YOUR_API_KEY"

email = input("Paste email you received: ")

prompt = f"""
Write a professional response to this email:

{email}

Keep it clear, polite, and business appropriate.
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response['choices'][0]['message']['content'])
