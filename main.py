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

import schedule
import time
import twitter_bot as ultron


def main() -> None:
    """
    Get trending tags from different countries.

    Note: If you are working with a free developer account, you have a very limited
    number of requests.
    """
    lang = "en"
    locations = ["london", "dublin", "toronto", "vancouver", "zurich", "amsterdam"]
    api = ultron.init_api()
    ultron.twitter_bot(api, locations, lang)

    # Uncomment the following lines to keep the program running all the time.
    # The bot will fetch the data daily, you can customize it if you want.
    #
    # schedule.every().day.at("00:00").do(ultron.twitter_bot, api, locations, lang)
    # schedule.every(10).seconds.do(ultron.twitter_bot, api, locations)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


if __name__ == "__main__":
    main()
