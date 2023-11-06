import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
prompt = PromptTemplate.from_template("Suggest the name of e-commerce store that sells {product}?")
chain = LLMChain(llm=llm, prompt=prompt, memory=ConversationBufferMemory())


while True:
    command = input("-->")
    if command == 'exit':
        break
    else:
        output = chain.run(command)
        print(output)
        # ! To see the conversation
        # print(chain.memory)
        # print(chain.memory.buffer)
