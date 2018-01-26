# coding=UTF-8
import twitter
from requests.utils import quote
from openpyxl import Workbook

kw_list = [
    'dog',
    'cat'
]

enc_str = quote(' OR '.join(kw_list))


api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

results = api.GetSearch(
    raw_query="q=" + enc_str + "&result_type=recent&since=2017-01-14&count=5&tweet_mode=extended")
#texts = [tweet.full_text for tweet in results]

def get_details(tweet):
    tweet_json = tweet.AsDict()
    if 'retweeted_status' in tweet_json:
        return ['https://twitter.com/statuses/' + str(tweet_json['id']), str(tweet_json['created_at']), tweet_json['retweeted_status']['full_text']]
    else:
        return ['https://twitter.com/statuses/' + str(tweet_json['id']), str(tweet_json['created_at']), tweet_json['full_text']]

tweet_list = [get_details(tweet) for tweet in results]

wb = Workbook()
ws = wb.active
for tweet_line in tweet_list:
    ws.append(tweet_line)
wb.save('tweets.xlsx')
