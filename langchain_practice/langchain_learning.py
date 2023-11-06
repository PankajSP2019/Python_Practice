import openai
import os
from langchain.llms import OpenAI

with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
print(llm.predict("How conversation buffer memory works in langchain, tell me in short with an example?"))
