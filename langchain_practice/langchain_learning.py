import openai
import os
from langchain.llms import OpenAI

OPENAI_API_KEY = ""


llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
print(llm.predict("what is python?"))