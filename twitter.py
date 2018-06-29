from api import Consumer_key,Consumer_secret,Access_token,Access_secret
import tweepy

oauth =tweepy.OAuthHandler(Consumer_key,Consumer_secret)
oauth.set_access_token(Access_token,Access_secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))
user=api.get_user("nikhilcool2571")
print(user.screen_name)
print(user.followers_count)
