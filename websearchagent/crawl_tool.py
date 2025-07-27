from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
    BrowserConfig,
    CacheMode,
    DefaultMarkdownGenerator,
    BM25ContentFilter,
)
from crawl4ai.async_dispatcher import SemaphoreDispatcher
browser_config = BrowserConfig(headless=True, text_mode=True, light_mode=True,verbose=False) #urls: list[str]
async def crawl_webpages(urls , prompt: str) -> list:
    """
    Crawls multiple webpages using Crawl4AI and extracts relevant markdown content
    based on the provided prompt.
    """
    bm25_filter = BM25ContentFilter(user_query=prompt, bm25_threshold=1.2)
    md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)
    crawler_config = CrawlerRunConfig(
        markdown_generator=md_generator,
        excluded_tags=[
            "nav",
            "footer",
            "header",
            "form",
            "img",
            "script",
            "style",
            "aside",
            "figure",
            "svg",
            "iframe",
            "button",
            "input",
            "select",
            "textarea",
        ],
        only_text=True,
        exclude_social_media_links=True,
        exclude_external_images=True,
        exclude_all_images=True,
        exclude_external_links= True,
        exclude_internal_links= True,
        delay_before_return_html= 0.05,
        scroll_delay= 0.05,
        cache_mode=CacheMode.BYPASS,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        page_timeout=30000,
        verbose=False# 30 seconds in ms
    )
    dispatcher = SemaphoreDispatcher(
    semaphore_count=10,
    #max_session_permit=10,

    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(urls, config=crawler_config,dispatcher=dispatcher)
        #results = await crawler.arun(urls, config=crawler_config)
        return results
