pip3 install tweepy nltk google-cloud-language python-telegram-bot
# https://www.freecodecamp.org/news/how-to-make-your-own-sentiment-analyzer-using-python-and-googles-natural-language-api-9e91e1c493e/
import tweepy
from datetime import datetime, timedelta
import re
from nltk.tokenize import WordPunctTokenizer
#SIGN ONTO TWITTER AND COMPLETE STEPS TWO THROUGH FOUR ON "WRITE THE PROGRAM" Part I
# ACC_TOKEN = 'YOUR_ACCESS_TOKEN'
# ACC_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'
# CONS_KEY = 'YOUR_CONSUMER_API_KEY'
# CONS_SECRET = 'YOUR_CONSUMER_API_SECRET_KEY'
#Part II
def authentication(cons_key, cons_secret, acc_token, acc_secret):
    auth = tweepy.OAuthHandler(cons_key, cons_secret)
    auth.set_access_token(acc_token, acc_secret)
    api = tweepy.API(auth)
    return api
  
today_datetime = datetime.today().now()
yesterday_datetime = today_datetime - timedelta(days=1)
today_date = today_datetime.strftime('%Y-%m-%d')
yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)

search_result = tweepy.Cursor(api.search, 
                              q=keyword, 
                              since=yesterday_date,
                              result_type='recent', 
                              lang='en').items(total_tweets)
def search_tweets(keyword, total_tweets):
    today_datetime = datetime.today().now()
    yesterday_datetime = today_datetime - timedelta(days=1)
    today_date = today_datetime.strftime('%Y-%m-%d')
    yesterday_date = yesterday_datetime.strftime('%Y-%m-%d')
    api = authentication(CONS_KEY,CONS_SECRET,ACC_TOKEN,ACC_SECRET)
    search_result = tweepy.Cursor(api.search, 
                                  q=keyword, 
                                  since=yesterday_date, 
                                  result_type='recent', 
                                  lang='en').items(total_tweets)
    return search_result
user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet.decode('utf-8'))
link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
