import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
consumer_key='Cee7mRBQZiJWENmUunEy3A4TW'
consumer_secret='s2SiEwYY04TtMDiHyzfeUhgLR1FQfGpRzEN0c09VglVjwUlllS'
access_token='820412155258277888-sqwGLXB7Wx2uFjx8mX0IAvMRk7yN6HN'
access_secret='RO0QaLcrEFEKB1omV94JviuB66FqgFBR7xW9d7Uh8vnob'
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_secret)
api=tweepy.API(auth)
test=api.lookup_users([34373370, 26257166, 12579252])
for user in test:
	print user.screen_name
	print user.name
	print user.description
	print user.followers_count
	for friend in user.friends():
		print friend.screen_name
	print user.url
class MyListener(StreamListener):
	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
                		f.write(data)
                		return True
        	except BaseException as e:
            		print 'error'
        	return True
	def on_error(self, status):
        	print status
        	return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#weather','#Chicago']) 
