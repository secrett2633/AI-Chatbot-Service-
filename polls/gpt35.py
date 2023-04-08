import os
import openai
from dotenv import load_dotenv
load_dotenv()

def answer(query):
  openai.api_key = os.getenv("OPENAI_API_KEY")
  response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [
          {"role": "system", "content": "Please answer the questions below in one line.\n"},
          {"role": "user", "content": query}
      ]
  )
  return response['choices'][0]['message']['content']