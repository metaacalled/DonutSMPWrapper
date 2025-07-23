import requests
import json

# Base API conf.
DSMPApiVersion = "v1"
DSMPApiBaseUrl = f"https://api.donutsmp.net/{DSMPApiVersion}"

# List with all the endpoints.
DSMPApiUrls = {
    "auction": {
        "list": f"{DSMPApiBaseUrl}/auction/list/",
        "transactions": f"{DSMPApiBaseUrl}/transactions/"
    },
    "leaderboards": {
        "brokenblocks": f"{DSMPApiBaseUrl}/brokenblocks/",
        "deaths": f"{DSMPApiBaseUrl}/deaths/",
        "kills": f"{DSMPApiBaseUrl}/kills/",
        "mobskilled": f"{DSMPApiBaseUrl}/mobskilled/",
        "money": f"{DSMPApiBaseUrl}/mobskilled/",
        "placedblocks": f"{DSMPApiBaseUrl}/placedblocks/",
        "playtime": f"{DSMPApiBaseUrl}/placedblocks/",
        "sell": f"{DSMPApiBaseUrl}/sell/",
        "shards": f"{DSMPApiBaseUrl}/shards/",
        "shop": f"{DSMPApiBaseUrl}/shop/"
    },
    "lookup": f"{DSMPApiBaseUrl}/auction/list/",
    "shield": f"{DSMPApiBaseUrl}/shield/metrics/",
    "statistics": f"{DSMPApiBaseUrl}/stats/"
}

# Sorting options.
class DSMPApiSorting:
    lowest_price = "lowest_price"
    highest_price = "highest_price"
    recently_listed = "recently_listed"
    last_listed = "last_listed"

class DSMPApi:
    def __init__(self, api_key):
        if (api_key == None):
            raise Exception("No API key provided.")
        self.api_key = api_key
        self.session = requests.session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        
    def getAuctionRequest(self, item_id, sorting_mode = DSMPApiSorting.lowest_price, page = 0):
        search_params = {}
        search_params["search"] = item_id
        search_params["sort"] = sorting_mode
        response = self.session.get(DSMPApiUrls["auction"]["list"] + page, json=search_params)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))
        
    def getAuctionTransaction(self, page = 1):
        response = self.session.get(DSMPApiUrls["auction"]["transactions"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardBrokenBlocks(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["brokenblocks"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardDeaths(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["deaths"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardKills(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["kills"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardMobsKilled(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["mobskilled"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardMoney(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["money"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardPlacedBlocks(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["placedblocks"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardPlaytime(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["playtime"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardSell(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["sell"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardShards(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["shards"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getLeaderboardShop(self, page = 0):
        response = self.session.get(DSMPApiUrls["leaderboards"]["shop"] + page)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def userLookup(self, user):
        response = self.session.get(DSMPApiUrls["lookup"] + user)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getShieldMetrics(self, service_id):
        response = self.session.get(DSMPApiUrls["shield"] + service_id)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))

    def getPlayerStatistics(self, user):
        response = self.session.get(DSMPApiUrls["statistics"] + user)
        if (response.status_code == 200):
            return (response.status_code, response.json())
        else:
            return (response.status_code, json.load({}))
