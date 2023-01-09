import tweepy


#API Key
consumer_key = "" 
# API Key Secret
consumer_secret = ""   
#Bearer Token 
access_token = "" 
access_token_secret = ""

# Authenticate the bot using the API key and secret
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing the "ESTIAM" hashtag
query = "ESTIAM"
tweets = api.search_tweets(q=query)

# Like and retweet each tweet
for tweet in tweets:
    api.favorite_status(tweet.id)
    api.retweet_status(tweet.id)

# Follow users who mentioned the "ESTIAM" hashtag and have more than 100 followers
for tweet in tweets:
    user = tweet.user
    if user.followers_count > 100:
        api.create_friendship(user.id)
