# Copyright 2020 - Olman Ureña. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import csv
import datetime
import json
import os
import tweepy


def init_api() -> tweepy.API:
    """
    Initiate the API with the access keys in 'config.json' file and returns the API instance.

    Ref:
        `OAuth 2 Authentication <http://docs.tweepy.org/en/v3.9.0/auth_tutorial.html#oauth-2-authentication>`_

    Returns:
        api (tweepy.API): API instance.
    """
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        auth = tweepy.AppAuthHandler(config["API_KEY"], config["API_SECRET"])
        api = tweepy.API(auth)
        return api
    except (FileNotFoundError, TypeError):
        print("init_api(): Error creating the API instance.")


def get_woeid(api, locations) -> list:
    """
    Returns the list of WOEIDs for specific locations if they have trending
    topics.

    Ref:
        `WOEID <https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html>`_
        `api.trends_available() <http://docs.tweepy.org/en/latest/api.html?highlight=trends_available#API.trends_available>`_

    Args:
        api (tweepy.API): API instance.
        locations (list): A list of str values with locations names.

    Returns:
        A list of str values with WOEIDs.
    """
    trending_locations = api.trends_available()
    # dictionary with all trending locations and their respective woeid.
    location_woeid = {trending_location["name"].lower(): trending_location["woeid"]
                      for trending_location in trending_locations}
    # fill the woeids list for the specific locations.
    woeids = []
    for location in locations:
        if location in location_woeid.keys():
            woeids.append(location_woeid[location])
        else:
            print(f"get_woeid(api, locations): Error - {location} woeid does not exist in trending topics.")
    return woeids


def get_tweets(api, query, lang) -> list:
    """
    Returns a list of tweets for the given hashtag and language.

    Ref:
        `tweepy.Cursor() <http://docs.tweepy.org/en/latest/cursor_tutorial.html?highlight=cursor>`_
        `api.search() <http://docs.tweepy.org/en/latest/api.html?highlight=api.search#API.search>`_
        `ISO 639-1 codes <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_

    Args:
        api (tweepy.API): API instance.
        query (str): Hashtag.
        lang (str): Tweets for the given language. Use ISO 639-1 code.

    Returns:
        A list of tweets, each tweet includes Id, hashtag, creation time, user handle, and tweet body.
    """
    tweets = []
    # iterate over a fetched list for the given hashtag and language with a max of 1000 results per page
    for status in tweepy.Cursor(api.search,
                                q=query,
                                count=1000,
                                result_type="popular",
                                lang=lang).items():
        # insert a tweet in a list
        tweets.append([status.id_str,
                       query,
                       status.created_at.strftime('%d-%m-%Y %H:%M'),
                       status.user.screen_name,
                       status.text])
    return tweets
