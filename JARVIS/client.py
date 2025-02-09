from openai import OpenAI

client = OpenAI(
  api_key = " ")  # Your API key here

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
   {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is the weather like today?"}
  ]
)

print(completion.choices[0].message);
