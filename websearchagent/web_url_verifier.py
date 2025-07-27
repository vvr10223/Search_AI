from pydantic import BaseModel, Field
from .connect import llm
class ResponseFormatter(BaseModel):
    """this is list of urls formatter."""
    final_urls: list[str] = Field(description="it is list of urls")
def web_url_verifier(url_list,query):

    s_llm=llm.with_structured_output(ResponseFormatter)
    final_urls=s_llm.invoke(f"**Evaluate Search Results:** Review the `url`, `title`, and `content` (snippet) for each result .\nContext: {url_list}\n remove unnecssary which are unrelevant and give relevant url  and this url given to web scraping based on query{query} and Return a JSON object with key 'urls' and a value as list of urls")
    return final_urls.final_urls