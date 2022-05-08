import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "korea -is:retweet"

response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["created_at", "lang"],
    expansions=["author_id"],
)

for tweet in response.data:
    print(tweet.id)
    print(tweet.lang)

