# ! By the help of agent, we can fetch current data.
# ! We can search in google, wikipedia and so on
# ! There are lots of tools(google search, wikipedia, brave search, so on) available for agent
# ! https://python.langchain.com/docs/integrations/tools

import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, initialize_agent, load_tools


# ! Openai API Key From HexFlow Fetch Api ,
# Which located in another file
with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

# ? Search in Wikipedia
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
tool_list = ["wikipedia", "llm-math"]  # ! List of Agent Tools, we are going to use
tool = load_tools(tool_list, llm=llm)
agent = initialize_agent(tool, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

output = agent.run("How Old is Salman Khan in 2040?")
print(output)

# ! Tools .\langchain_agent-tools-google_search.py

