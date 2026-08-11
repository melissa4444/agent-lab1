import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI()

# 1. Fun fact
messages = [{"role": "user", "content": "Tell me a fun fact"}]
response = client.chat.completions.create(model="gpt-5.4-nano", messages=messages)
print("Fun fact:", response.choices[0].message.content)
print()

# 2. Generate a hard question
prompt = (
    "Please propose a hard, challenging question to assess someone's IQ. "
    "Respond only with the question."
)
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": prompt}],
)
question = response.choices[0].message.content
print("Question:", question)
print()

# 3. Answer the question
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": question}],
)
answer = response.choices[0].message.content
print("Answer:", answer)
print()

# 4. Evaluate the answer
evaluation_prompt = f"""
Here is a question:
{question}

And here is a possible answer that might be correct or incorrect:
{answer}

Please evaluate if the answer is correct or incorrect.
"""
response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[{"role": "user", "content": evaluation_prompt}],
)
print("Evaluation:", response.choices[0].message.content)
