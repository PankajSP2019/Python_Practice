# In Sequential chain we can pass multiple input and output
# We can define how will be the output form

import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = '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'

# This is an LLM chain to write a synopsis(summarizes the plot, main characters, locations, and text of a play) given title of a play(drama) and the era it is set in.

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
synopsis_template = """You are a playwright. Given the title of play and the era of it set in, it is your job to write a synopsis for that title
Title : {title}
Era : {era}
Playwright : This is a synopsis for the above play : """

synopsis_prompt_template = PromptTemplate(input_variables=["title", "era"], template=synopsis_template)
synopsis_chain = LLMChain(llm=llm, prompt=synopsis_prompt_template, output_key="synopsis")

# ! This is an LLMChain to write a review of a play given a synopsis
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
review_template = """You are play critic from the New Work Times. Given the synopsis of play, it is your job to write a review for that play.
Play Synopsis : {synopsis}
Review from a New Work Times play critic of the above play: """

review_prompt_template = PromptTemplate(input_variables=["synopsis"], template=review_template)
review_chain = LLMChain(llm=llm, prompt=review_prompt_template, output_key="review")

# ! This is the overall  chain where we run these chains in sequence
from langchain.chains import SequentialChain
overall_chain = SequentialChain(
    chains=[synopsis_chain, review_chain],
    input_variables=["era", "title"],
    output_variables=['synopsis', 'review'],  # ? Define what will be out output
    verbose=True
)

# ? The input value will pass in dictionary
# ? The output will be in dictionary form, where the inputs and the defined output will exist.
output = overall_chain({'title': "A murder in a beach", 'era': "Modern Myths"})
for i in output:
    print(output[i])

# h = "hello world"
# import time
#
# for i in h:
#     print(i, end=" ")
#     time.sleep(2)