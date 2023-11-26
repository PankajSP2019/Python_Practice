"""
Ask THE AI
PDF with set of rules, AI will generate the reply based on the rules
Here PyPDF2 not working properly, it's overlapping the text
That's why fitz ( PyMuPDF) Used
pip install pymupdf
"""
with open("C:\\Users\\ASUS\\Desktop\\office\\OpenAI API Key For me.txt") as f:
    OPENAI_API_KEY = f.readlines()[0]

# ? fetch data from pdf file
import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text += page.get_text()

    pdf_document.close()
    return text.replace("\n", " ")


pdf_path = "C:\\Users\\ASUS\\Desktop\\Langchain learning\\Rules_Document\\test.pdf"
result_text = extract_text_from_pdf(pdf_path)
# print(result_text)

# ? Chains
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Code generate chain
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
code_generate_template = """Act as a program generator. Utilize the provided rules to create a program that accurately addresses the given query.

Rules:
{rules}

Query:
{query}

Generated Program:
Below is the generated program designed to fulfill the requirements of the query: “””
"""

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

# instruction = input("-->>")

instruction_list = ["Suggest me a code sum of 2 numbers in java",
                    "suggest me code in java for multiply two matrix.",
                    "Who is the tallest man in the world?",
                    "Generate a code sum 2numbers in javascript. "]


# ? For Showing Message while sleep, Target this function.
def show_message(message):
    print(message)


for i in range(len(instruction_list)):
    print(f"------------------------------{i + 1}------------------------------")
    output = overall_chain({'rules': result_text, 'query': instruction_list[i]})
    for i in output:
        print(output[i])
    print(f"****************************************************************")
    # ? For Showing Message while sleep
    import time
    import threading
    message_thread = threading.Thread(target=show_message, args=("Working on Another Query, Please Wait...",))
    message_thread.start()
    time.sleep(10)
    message_thread.join()
