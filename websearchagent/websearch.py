import asyncio
#import nest_asyncio
#nest_asyncio.apply()
from .rag_pipeline import rag_pipeline
from .web_url_verifier import web_url_verifier
from .web_urls import get_web_urls
from .crawl_tool import crawl_webpages
import time
def websearch(query):
    # Initialize with your Gemini API key
    #rag = FastSingleQueryRAG()
    '''query="Nitish Kumar Reddy's batting total score in the 3rd test India vs England in 2025"'''
    url_list=get_web_urls(query)

    final_urls=web_url_verifier(url_list,query)
    #print(final_urls)

    #x=time.time()
    result=asyncio.run(crawl_webpages(final_urls,query))
    #y=time.time()
    #print(y-x)
    #return result
    #x=time.time()
    output=rag_pipeline(result,query)
    #y=time.time()
    #print(y-x)
    return output
if __name__ == '__main__':
    print(websearch("Nitish Kumar Reddy's batting total score in the 3rd test India vs England in 2025"))