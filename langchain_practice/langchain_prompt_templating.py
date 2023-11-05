# Prompt templating used for make a template for prompt text,by making a chain, declare a section under {} this,
# for pass user define value.

import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# OPENAI_API_KEY = ""
OPENAI_API_KEY = ''  

prompt = PromptTemplate.from_template("What is the capital of {place}?")  # here under {} this, will be pass by user

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)  # Create LLM for openai
chain = LLMChain(llm=llm, prompt=prompt)  # Create chain
output = chain.run("India")  # Pass the value in the prompt

print(output)

# For cities, in a list
cities = ['india', 'USA', 'Canada', 'saudi arab']
for i in cities:
    output = chain.run(i)  # Pass the value in the prompt
    print(output.strip())
    # import time
    # time.sleep(10)

