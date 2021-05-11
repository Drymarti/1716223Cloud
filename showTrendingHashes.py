#import tweepy libraries
import tweepy 

#Login access and secret keys of app from Twitter API
access_token="1863328567-aKhvMhOmqvlamHyMeSlyq7to6s8xp2DsBgFpRX3"
access_token_secret="y5127b1wA80U87SBnQGUD3jdHUDs4RtrTVD10YkgJbQ5T"

api_key="jpzMRsUnewtcY4zINWX99bz9N"
api_key_secret="tN92orzYxGlqhN6ex4SuJRqbw7KFXPVMjiMFOVA9rXRnj4auXH"

#Authenticate software
auth=tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

#Connect with Twitter API to our project
api=tweepy.API(auth)
print(api)

india_woeid=23424848 #geo-localization set to India with India Code

trend_result=api.trends_place(india_woeid) #Show trends from India only



#Loop for receiving hashtags and number of tweets in which hashtag is used. For top 10 popular topics
for trend in trend_result[0]["trends"][:10]:
    print(trend["name"]) #Output the hashtag name
    print(trend["tweet_volume"]) #Output of how much popular the hashtag is
    print(trend["url"])  #Output the url for the hashtag in search
    
    
#Loop for receiving hashtags and number of tweets in which hashtag is used. For top 30 popular topics
for trend in trend_result[0]["trends"][:30]:
    print(trend["name"]) #Output the hashtag name
    print(trend["tweet_volume"]) #Output of how much popular the hashtag is
    print(trend["url"])  #Output the url for the hashtag in search
        
#Loop for receiving hashtags and number of tweets in which hashtag is used. For top 50 popular topics
for trend in trend_result[0]["trends"][:50]:
     print(trend["name"]) #Output the hashtag name
    print(trend["tweet_volume"]) #Output of how much popular the hashtag is
    print(trend["url"])  #Output the url for the hashtag in search

