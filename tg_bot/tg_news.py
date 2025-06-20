import os
from telegram import Bot
from dotenv import load_dotenv

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from supabase_handler import supabase_handler

import asyncio

class tg_news:

    def __init__(self,):

        load_dotenv()
        self.sh = supabase_handler()
        self.BOT = Bot(token=os.getenv("TELEGRAM_TOKEN"))
        self.CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    async def push_news(self):
        pushed_id = self.sh.query_pushed_id()
        news_data = self.sh.query_news_by_mini_id(pushed_id)
        if news_data:
            for nd in news_data:
                caption = f"<b>{nd['title']}</b>\n\n{nd['summarization']}\n\n📰 Source: {nd['source']}\n🔗 <a href='{nd['link']}'>Read Full News</a>"

                await self.BOT.send_photo(
                    chat_id=self.CHAT_ID,
                    photo=nd['image'],
                    caption=caption,
                    parse_mode="HTML"
                )
            pushed_id = nd['id']
            self.sh.upsert_pushed_id(pushed_id)
        
def main():

    tn = tg_news()
    asyncio.run(tn.push_news())

if __name__ == "__main__":
    main()