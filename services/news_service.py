import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

def get_agriculture_news():
    """
    Fetches agriculture-related news using SerpApi's Google News engine.
    """
    params = {
  "engine": "google_news",
  "gl": "in",
  "hl": "en",
  "topic_token": "CAAqJAgKIh5DQkFTRUFvSEwyMHZNR2hyWmhJRlpXNHRSMElvQUFQAQ",
  "api_key": os.getenv("NEWS_API_KEY")
}

    search = GoogleSearch(params)
    results = search.get_dict()
    news_results = results.get("news_results", [])

    news_data = []
    for item in news_results:
        news_data.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "source": item.get("source"),
            "snippet": item.get("snippet"),
            "date": item.get("date"),
            "thumbnail": item.get("thumbnail"),
        })
    return news_data
