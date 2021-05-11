# O#import tweepy libraries
import tweepy 
import os
import json
import sys
import geocoder


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



if __name__ == "__main__":
    # Available Locations
    available_loc = api.trends_available()
    # writing a JSON file that has the available trends around the world
    with open("available_locs_for_trend.json","w") as wp:
        wp.write(json.dumps(available_loc, indent=1))

    # Trends for Specific Country
    loc = sys.argv[1]     # location as argument variable 
    g = geocoder.osm(loc) # getting object that has location's latitude and longitude

    closest_loc = api.trends_closest(g.lat, g.lng)
    trends = api.trends_place(closest_loc[0]['woeid'])
    # writing a JSON file that has the latest trends for that location
    with open("twitter_{}_trend.json".format(loc),"w") as wp:
        wp.write(json.dumps(trends, indent=1))