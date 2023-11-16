"""
Ask THE AI
PDF with set of rules, AI will generate the reply based on the rules
"""
with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


# ? Provide Path of PDF
pdfreader = PdfReader("C:\\Users\\ASUS\\Desktop\\Langchain learning\\Rules_Document\\test.pdf")
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
print(type(text[0]))

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
# ? Download embeddings from OpenAI
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# ? Convert the Text(Separated token) into Vector point embeddings
document_search = FAISS.from_texts(text, embeddings)



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


output = overall_chain({'rules': text[0], 'query': "Generate a code sum 2 numbers in c++"})
for i in output:
    print(output[i])

# ? PYPDF2 ->Overlap the text,
# ? The below approach, Working well to extract text from pdf, without overlapping

""" #! pip install pymupdf
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text += page.get_text()

    pdf_document.close()
    return text

# Example usage
pdf_path = "C:\\Users\\ASUS\\Desktop\\Langchain learning\\Rules_Document\\test.pdf"
result_text = extract_text_from_pdf(pdf_path)

# Print or use the result_text as needed
print(type(result_text))
print(result_text.replace("\n", " ")) """




