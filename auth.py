from enum import unique
import os
import requests
import bson
import pandas as pd
import pymongo
from bson.objectid import ObjectId


sso_token = os.environ.get("SSO_TOKEN")
cookies = {"ACT_SSO_COOKIE": sso_token}

client = pymongo.MongoClient(
    "mongodb+srv://admin:Carlos0712@wzkdbot.9tx92.mongodb.net/?retryWrites=true&w=majority"
)

dbname = client.wzbot


def bbz_stats():
    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/thebbz26/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    """Fetches the summary of the last 20 games played by the user"""
    data = uno_matches.json()["data"]["summary"]["all"]
    collection_name = dbname["bbzstats"]
    collection_name.insert_one(data)


def cojecalla_stats():
    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/psn/gamer/cojecalla/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    data = uno_matches.json()["data"]["summary"]["all"]
    collection_name = dbname["cojecallastats"]
    collection_name.insert_one(data)


def netrxc_stats():
    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/psn/gamer/netrxc/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    data = uno_matches.json()["data"]["summary"]["all"]
    collection_name = dbname["netrxcstats"]
    collection_name.insert_one(data)


def ozz_stats() :
    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/theozzg3/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    data = uno_matches.json()["data"]["summary"]["all"]
    


def allmatches():
    """Connects to the API and fetch UNO id to gather user stats"""

    collection_name = dbname["allmatches"]
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/thebbz26/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    matches = resp_profile.json()["data"]["matches"]
    matchid = len(matches)
    bebo_lista = []
    i = 0
    while i < matchid:
        bebo_lista.append(
            {
                "matchID": matches[i]["matchID"],
                "kills": matches[i]["playerStats"]["kills"],
                "player": matches[i]["player"]["username"],
                "k/d": matches[i]["playerStats"]["kdRatio"],
            }
        )

        i += 1

    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/psn/gamer/cojecalla/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    matches = resp_profile.json()["data"]["matches"]
    matchid = len(matches)
    ramon_lista = []
    i = 0
    while i < matchid:
        ramon_lista.append(
            {
                "matchID": matches[i]["matchID"],
                "kills": matches[i]["playerStats"]["kills"],
                "player": matches[i]["player"]["username"],
                "k/d": matches[i]["playerStats"]["kdRatio"],
            }
        )

        i += 1

    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/psn/gamer/netrxc/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    matches = resp_profile.json()["data"]["matches"]
    matchid = len(matches)
    nerio_lista = []
    i = 0
    while i < matchid:
        nerio_lista.append(
            {
                "matchID": matches[i]["matchID"],
                "kills": matches[i]["playerStats"]["kills"],
                "player": matches[i]["player"]["username"],
                "k/d": matches[i]["playerStats"]["kdRatio"],
            }
        )

        i += 1

    """Connects to the API and fetch UNO id to gather user stats"""
    resp_profile = requests.get(
        "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/theozzg3/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
    uno_matches = requests.get(
        f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
        cookies=cookies,
    )
    matches = resp_profile.json()["data"]["matches"]
    matchid = len(matches)
    oso_lista = []
    i = 0
    while i < matchid:
        oso_lista.append(
            {
                "matchID": matches[i]["matchID"],
                "kills": matches[i]["playerStats"]["kills"],
                "player": matches[i]["player"]["username"],
                "k/d": matches[i]["playerStats"]["kdRatio"],
            }
        )

        i += 1
        try:
            collection_name.insert_many(oso_lista)
            collection_name.insert_many(nerio_lista)
            collection_name.insert_many(ramon_lista)
            collection_name.insert_many(bebo_lista)
            collection_name.create_index(
                [("matchID", pymongo.DESCENDING), ("player", pymongo.ASCENDING)],
                unique=True,
            )
        except pymongo.errors.BulkWriteError as e:
            print("All matches duplicated data, skipping")
            break


if __name__ == "__main__":
    netrxc_stats()
    ozz_stats()
    cojecalla_stats()
    bbz_stats()
    allmatches()
