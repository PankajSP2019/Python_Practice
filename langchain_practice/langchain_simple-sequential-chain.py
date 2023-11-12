# In Simple Sequential chain, make a chain from multiple chain
# we make multiple chains, and we can pass one chain's output to another chain's input.

import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

# LLM to get a name of a e-commerce store
prompt = PromptTemplate.from_template("Suggest me name of the e-commerce store that sells {product}?")
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
chain1 = LLMChain(llm=llm, prompt=prompt)
# output = chain1.run("Tea")
# print(output)

# LLM to get comma separated names of products from an e-commerce store name
prompt = PromptTemplate.from_template("What are the names of the products at {store}?")
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
chain2 = LLMChain(llm=llm, prompt=prompt)

# Create a Overall chain from simple sequential chain
chain = SimpleSequentialChain(
    chains=[chain1, chain2],
    # verbose=True # It will show output automatically, just run the chain
)
out = chain.run("CPU")
print(out)
print(type(out))









