from supabase import ClientOptions, create_client, Client
import os
from news_info import news_info

class supabase_handler:

    def __init__(self):
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_KEY")
        self.supabase: Client = create_client(url, key)


    def is_data_exist(self, title: str):
        existing = self.supabase.table("news_information").select("*").eq("title", title).execute()
        return bool(existing.data)
    
    def save_news(self, news_info: news_info):
        rst = self.supabase.table("news_information").insert(
            {'title':news_info.title,
                'source':news_info.source,
                'description':news_info.description,
                'link':news_info.link,
                'image':news_info.image,
                'summarization':news_info.summarization,
                'publish_date':news_info.publish_date}).execute()
        
    def query_pushed_id(self,):
        rst = self.supabase.table("pushed_news").select('pushed_id').execute()
        if rst.data:
            return rst.data[0]['pushed_id']
        return 0
    
    def upsert_pushed_id(self, id):
        self.supabase.table("pushed_news").upsert({'id':1, 'pushed_id': id}).execute()

    def query_news_by_mini_id(self, id):
        rst = self.supabase.table("news_information").select('*').gt("id", id).execute()
        return rst.data