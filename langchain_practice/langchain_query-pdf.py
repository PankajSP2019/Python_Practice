# ! The purpose of this program is to, query a pdf
# ! Like upload a pdf file, and ask the AI to fetch specific information for that pdf

"""
pip install langchain
pip install openai
pip install tiktoken
pip install faiss-cpu
"""

# ? Faiss-cpu
"""
Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that 
search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for
evaluation and parameter tuning.
"""

# ! Fetch OPENAI API KEY from my local
with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

# ? Provide Path of PDF
pdfreader = PdfReader(
    "C:\\Users\\ASUS\\Downloads\\pankaj_kumar_das.pdf")  # ? Path Of Pdf

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

# ? Download embeddings from OpenAI
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# ? Convert the Text(Separated token) into Vector point embeddings
document_search = FAISS.from_texts(text, embeddings)

# ? Create Chain
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.3)
chain = load_qa_chain(llm=llm, chain_type="stuff")

query = "projects the cadidate have done" \
        ""
docs = document_search.similarity_search(query)
output = chain.run(input_documents=docs, question=query)
print(output)
