import requests
def get_web_urls(search_term: str, num_results: int = 10) -> list[str]:
    """Performs a web search using SearxNG and returns URLs allowed by robots.txt."""
    #http://localhost:4000/search?q=ind%20vs%20eng%203rd%20test%20scorecard&language=en-IN&time_range=&safesearch=0&pageno=2&categories=general
    params = {
        "q": search_term,
        "language": "en-IN",
        "time_range": "",
        "safesearch":0,
        "categories": "general",
        "format": "json",

    }
    searxng_url = "http://localhost:4000/search"
    response = requests.get(searxng_url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])[:num_results]
        #print(results)

        formatted_results = [
                {
                    "url": r.get("url"),
                    "title": r.get("title"),
                    "content": r.get("content"),
                }
                for r in results
                if r.get("url")
            ]
        #urls = [result["url"] for result in results]
        #return check_robots_txt(urls)
        return formatted_results
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []