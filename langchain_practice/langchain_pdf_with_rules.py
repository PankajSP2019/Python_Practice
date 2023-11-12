"""
Ask THE AI
PDF with set of rules, AI will generate the reply based on the rules
"""
with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


# ? Provide Path of PDF
pdfreader = PdfReader("C:\\Users\\ASUS\\Desktop\\Rules_Document\\test.pdf")
# ? Read Text From PDF
from typing_extensions import Concatenate
raw_text = ''  # ! All text will store in this variable
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content
# print(raw_text)
# ! We need to split the text using character text split such that it should not increase Token size
text_splitter = CharacterTextSplitter(
    separator="\n",  # ? Based on this separate
    chunk_size=2000,  # ? Word Count, basically token size
    chunk_overlap=200,
    length_function=len,  # ? funtion name to know the length, print(len) -> word size
)
text = text_splitter.split_text(raw_text)
# print(text)

# ? Chains
import openai
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Code generate chain
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
code_generate_template = """Act like a program generator. Given rules set and query, according to the rules or following the rules 
generate answer for query.
Rules : {rules}
Query : {query}
ProgramGenerator : This is the code for above query :"""
code_generate_prompt_template = PromptTemplate(input_variables=["rules", "query"], template=code_generate_template)
code_generator_chain = LLMChain(llm=llm, prompt=code_generate_prompt_template, output_key="code_generator")

# Explain Code chain
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
code_explain_template = """You are code explainer. Given the code, explain the code in simple formal language tone
that reader can understand easily.
Code Generator : {code_generator}
Explanation of the above code : """
code_explain_prompt_template = PromptTemplate(input_variables=["code_generator"], template=code_explain_template)
code_explain_chain = LLMChain(llm=llm, prompt=code_explain_prompt_template, output_key="code_explain")

# ? Overall Sequential Chain
from langchain.chains import SequentialChain
overall_chain = SequentialChain(
    chains=[code_generator_chain, code_explain_chain],
    input_variables=["rules", "query"],
    output_variables=['code_generator', 'code_explain'],  # ? Define what will be out output
    # verbose=True
)


output = overall_chain({'rules': text, 'query': "according to the rules Generate a code sum 2 numbers in c++"})
for i in output:
    print(output[i])




