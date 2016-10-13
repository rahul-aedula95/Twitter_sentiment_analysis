import tweepy
import codecs
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
consumer_key = 'xCVooH1T1Ao9rjEBvMnC9QR3u'
consumer_secret = 'wFau0GNQFgB1n4iDoGdQ9geqsXiwLpYoV0iak8Mh0AwT73mZLY'
access_token = '214512527-MEdGSOfpBlKplFzudxZwlQQm5Fl6jr84hZIEVRwS'
access_secret = 'ypLZOrgCbIUbHsUNfQN7Z1z9DovSgmZwqlpVjNhzGX06o'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
hashtag = raw_input("Enter #tag here")
f = codecs.open('file.txt','w',encoding='utf-8')

for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,\
                           lang="en",\
                           since_id=2016-10-11).items():
    print tweet.created_at, tweet.text
    f.write("%s,%s\ufeff" %(tweet.created_at, tweet.text))
f.close()
