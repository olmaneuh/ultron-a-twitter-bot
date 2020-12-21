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


def init_api():
    """
    Initiate the API with the access keys in 'config.json' file and returns the API instance.

    Returns:
        tweepy.api.API
    """
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        auth = tweepy.AppAuthHandler(config["API_KEY"], config["API_SECRET"])
        api = tweepy.API(auth)
        return api
    except tweepy.TweepError:
        print("init_api(): Error creating the API instance.")
        return None
