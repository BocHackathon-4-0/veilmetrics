'''
    This class is to scrape today's news and accompany them
    with sentiment analysis score.
'''
import requests
import json
import pandas as pd
import time
from datetime import datetime, timedelta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
# chrome_options.add_argument("--headless")
from pathlib import Path
from sentiment_analysis import SentimentAnalyzers


def get_news_today():
    print(">> Scraping today's news from  CoinGecko")
    sa = SentimentAnalyzers()
    url = 'https://www.coingecko.com/en/news'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(2)
    post_list = []
    posts = driver.find_elements(By.TAG_NAME,'article')

    for post in posts:
        header = post.find_element(By.TAG_NAME,'header')
        title = header.find_element(By.TAG_NAME,'h2').find_element(By.TAG_NAME,'a').text
        link = header.find_element(By.TAG_NAME,'h2').find_element(By.TAG_NAME,'a').get_attribute('href')
        source = header.find_element(By.TAG_NAME,'p').find_element(By.CLASS_NAME,'font-weight-bold').text
        excerpt = post.find_element(By.CLASS_NAME,'post-body').text

        post_item = {
            'source': source,
            'link': link,
            'title': title,
            'excerpt': excerpt
        }
        post_list.append(post_item)
        print("Post:",title)

    final_post_list = []
    for post in post_list:
        va_title = sa.vader_score(post['title'])
        tb_title = sa.tb_score(post['title'])
        flair_title = sa.flair_score(post['title'])
        av_sentiment_title = (va_title+tb_title+flair_title)/3
        post_item = {
            'source': post['source'],
            'link':post['link'],
            'title': post['title'],
            'excerpt': post['excerpt'],
            'vader_sentiment_title': va_title,
            'tb_sentiment_title': tb_title,
            'flair_sentiment_title': flair_title,
            'av_sentiment_title':av_sentiment_title,
            'vader_sentiment_excerpt': sa.vader_score(post['excerpt']),
            'tb_sentiment_excerpt': sa.tb_score(post['excerpt']),
            'flair_sentiment_excerpt': sa.flair_score(post['excerpt'])
        }
        final_post_list.append(post_item)
        print("Processed posts: ", len(final_post_list), " out of ", len(post_list))

    df = pd.DataFrame(final_post_list)
    df.to_csv('latest_news.csv')

if __name__ == '__main__':
    print(">AEL LAOS PROTATHLIMA REEEEEEEEEEEE")
    get_news_today()