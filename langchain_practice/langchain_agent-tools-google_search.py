"""
First, you need to set up the proper API keys and environment variables.
To set it up, create the GOOGLE_API_KEY in the Google Cloud credential console
(https://console.cloud.google.com/apis/credentials) and a GOOGLE_CSE_ID using the
Programmable Search Engine
(https://programmablesearchengine.google.com/controlpanel/create).
Next, it is good to follow the instructions found here.
"""

"""
# ! If any error occur , enable the google api key
Custom Search API has not been used in project 433715617022 before or it is disabled. 
Enable it by visiting 
https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview?project=433715617022 t
hen retry. If you enabled this API recently, 
wait a few minutes for the action to propagate to our systems and retry.
"""

# ! pip install google-api-python-client>=2.100.0

import os

# ! Set environ variables for google search
os.environ["GOOGLE_CSE_ID"] = "a151cf82b6c2b4c8c"
os.environ["GOOGLE_API_KEY"] = "AIzaSyDpXVRV37-eb8X2iQFhwEnFAWevHGyeZE0"

from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

# ! Simple
# search = GoogleSearchAPIWrapper()
# tools = Tool(
#     name="Google Search",
#     description="Search Google for recent results,",
#     func=search.run,
# )
# output = tools.run("what is python")
# print(output)

# ! For Number of search result
# search = GoogleSearchAPIWrapper(k=3)  # ? Here k is the serial number of search result.
# tools = Tool(
#     name="I'm Feeling Lucky",
#     description="Search Google and return the first result.",
#     func=search.run,
# )
# output = tools.run("What is python")
# print(output)

# ! Metadata Results
"""
Run query through GoogleSearch and return snippet, title, and link metadata.
Snippet: The description of the result.
Title: The title of the result.
Link: The link to the result

The result will be in dictionary format - {'tittle':"", 'link':", 'snippet':""}
"""
search = GoogleSearchAPIWrapper()


def top5_resul(query):
    return search.results(query, 5)  # ? It will provide 5 result in list format


tool = Tool(
    name="Google Search Snippets",
    description="Search Google for recent results",
    func=top5_resul,
)

output = tool.run("What is the current dollar rate?")
for i in output:
    print("----------------------------------------------------------------------------")
    for key, item in i.items():
        print(f"{key} : {item}")


