from feed_processor import feed_processor
from ai_summarization import summarize_text

from supabase_handler import supabase_handler

from dotenv import load_dotenv

def main():
    load_dotenv()
    fp = feed_processor()
    feeds = fp.process_feed()
    sh = supabase_handler()
    for feed in feeds:
        if not sh.is_data_exist(feed.title):
            news_sum = summarize_text(feed.description, 40)
            feed.summarization = news_sum
            sh.save_news(feed)

if __name__ == "__main__":
    main()