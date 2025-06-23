import feedparser

from bs4 import BeautifulSoup
from newspaper import Article

import os
import json

from news_info import news_info

class feed_processor:

    def process_feed(self):
        rss_resources = self.parse_rss()
        all_news = []
        for rss_resource in rss_resources:
            name = rss_resource['name']
            link = rss_resource['link']
            feed = feedparser.parse(link)
            for entry in feed.entries[:5]:
                news = news_info(entry.title, name, self.extract_article_content(entry.link), entry.link, self.extract_first_media(entry), entry.published)
                if news.valid_fields():
                    all_news.append(news)
        return all_news


    def parse_rss(self):
        with open('rss_sources.json', 'r', encoding='utf-8') as f:
            rss_sources = json.load(f)
        return rss_sources

    def extract_first_media(self, entry):
        # 1. media:content
        if 'media_content' in entry:
            for m in entry.media_content:
                url = m.get('url')
                if url:
                    return url

        # 2. media:thumbnail
        if 'media_thumbnail' in entry:
            for thumb in entry.media_thumbnail:
                url = thumb.get('url')
                if url:
                    return url

        # 3. enclosures
        if 'enclosures' in entry:
            for e in entry.enclosures:
                url = e.get('href')
                if url:
                    return url

        # 4. <img> in summary/content
        html_content = entry.get('summary', '') or entry.get('content', [{}])[0].get('value', '')
        soup = BeautifulSoup(html_content, 'html.parser')
        img = soup.find('img')
        if img and img.get('src'):
            return img.get('src')

        return None

    def extract_article_content(self, url):
        try:
            article = Article(url, language='en')
            article.download()
            article.parse()
            return article.text.strip()
        except Exception as e:
            print(f"Error fetching article: {e}")
            return None
