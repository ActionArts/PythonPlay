#requires tweepy be installed

import tweepy
import twitter

my_followers = twitter.api.followers()

def get_followers():
	followers = []
	for follower in twitter.api.followers():
		followers.append(follower.name)
	return followers

	
#print 'Followers:', '\n'.join(get_followers())

def post_a_tweet(tweet):
	#tweet = 'Tweeting from my Python app using tweepy! Yeah!'
	twitter.api.update_status(status=tweet_msg)

def get_from_hash(hash_tag, count):
	hash = hash_tag
	#if(!hash.starts_with('#')):
	#	hash = '#' + hash_tag
	tweets = tweepy.Cursor(twitter.api.search,\
							q=hash,
							since_id="2015-05-13",
							until="2015-05-14",
							).items(count)
	return tweets
	
def write_to_file(file_name, tweets):

	#create the file: 
	#	w+ opens a file for both writing and reading. 
	#	   it will create new file or overwrite existing
	f = open(file_name,'w+')
	
	for tweet in tweets:
		line ='{},{}\n\n'.format(tweet.created_at,\
									tweet.text)
		f.write(line)
	f.close()

def main():
	redsox_tweets = get_from_hash('#redsox', 15)
	
	#print the tweets first
	for tweet in redsox_tweets:
		print tweet.text

	#save them
	write_to_file('redsox_tweets.txt', redsox_tweets)

main()
