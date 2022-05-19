import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "covid -is:retweet"

response = client.search_recent_tweets(
    query=query,
    max_results=100,
    user_fields=["profile_image_url"],
    expansions=["author_id"],
)

users = {u["id"]: u for u in response.includes["users"]}

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(tweet.id)
        print(user.profile_image_url)
