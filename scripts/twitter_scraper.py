import tweepy
import argparse

# Set up Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to the Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def get_twitter_info(username):
    try:
        # Fetch the user by username
        user = api.get_user(screen_name=username)
        
        # Print basic information
        print(f"User: {user.name}")
        print(f"Screen Name: {user.screen_name}")
        print(f"Bio: {user.description}")
        print(f"Location: {user.location}")
        print(f"Followers: {user.followers_count}")
        print(f"Following: {user.friends_count}")
        
        # Get recent tweets
        tweets = api.user_timeline(screen_name=username, count=5, tweet_mode="extended")
        print("\nRecent Tweets:")
        for tweet in tweets:
            print(f"- {tweet.full_text}")
    
    except tweepy.TweepError as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSINT Twitter Scraper")
    parser.add_argument("--username", help="Target Twitter username", required=True)
    args = parser.parse_args()
    
    get_twitter_info(args.username)
