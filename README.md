# AI News Reader

AI News Reader is a Python-based application that aggregates and summarizes news articles using artificial intelligence. It helps users stay updated with the latest news efficiently. The news can be pushed to social medias like Telegram. The image below is an example of pushed message.

<img src="https://github.com/WindZZzzZZzz/images/blob/main/ai-news-reader/kill.png" width="200" />

## Features

- Aggregates news from multiple RSS sources
- Summarizes articles using AI
- Store news into database
- Push news to Telegram channel using bot

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai_news_reader.git
    cd ai_news_reader
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configuration:
    - Create file .env and copy content in .env.example
    - Replace the config with your own keys
## Usage

Run the application:
```bash
python main.py #collect news
python tg_bot/tg_news.py #push news to tg channels
```
