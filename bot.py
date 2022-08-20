import discord
import pymongo
import requests
import os
from auth import ozz_stats

client = pymongo.MongoClient(
    "mongodb+srv://admin:Carlos0712@wzkdbot.9tx92.mongodb.net/?retryWrites=true&w=majority"
)

sso_token = os.environ.get("SSO_TOKEN")
cookies = {"ACT_SSO_COOKIE": sso_token}


# First define the database name
dbname = client.wzbot


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        """Fetches user netrxc stats from api"""
        if message.content.startswith("!nerio"):
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

            kills = data["kills"]
            kd = data["kdRatio"]
            assists = data["assists"]
            killspergame = data["killsPerGame"]
            deaths = data["deaths"]
            damagedone = data["damageDone"]

            embedVar = discord.Embed(
                title="Warzone Summary",
                description="Last 20 match summary",
                color=discord.Color.blue(),
            )
            embedVar.set_author(
                name=message.author.display_name,
                url="",
                icon_url=message.author.avatar_url,
            )
            embedVar.set_thumbnail(
                url="https://gamerforfun.com/wp-content/uploads/2020/04/Call-of-Duty-Warzone-Review-Icon-1024x1024.jpg"
            )
            embedVar.add_field(name="Player", value="netrxc", inline=False)
            embedVar.add_field(name="Kills", value=int(kills), inline=True)
            embedVar.add_field(name="Deaths", value=int(deaths), inline=True)
            embedVar.add_field(name="KD", value="{0:.2f}".format(kd), inline=True)
            embedVar.add_field(
                name="Kills per game", value="{0:.2f}".format(killspergame), inline=True
            )
            embedVar.add_field(name="Assists", value=int(assists), inline=True)
            embedVar.add_field(name="Damage done", value=int(damagedone), inline=True)
            embedVar.set_footer(
                text="Information requested by: {}".format(message.author.display_name)
            )
            await message.channel.send(embed=embedVar)

        if message.content.startswith("!neriodmg"):
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

            damagedone = data["damageDone"]
            damagetaken = data["damageTaken"]
            
            embedVar = discord.Embed(
                title="Warzone Summary",
                description="Last 20 match summary",
                color=discord.Color.blue(),
            )
            embedVar.set_author(
                name=message.author.display_name,
                url="",
                icon_url=message.author.avatar_url,
            )
            embedVar.set_thumbnail(
                url="https://gamerforfun.com/wp-content/uploads/2020/04/Call-of-Duty-Warzone-Review-Icon-1024x1024.jpg"
            )
            embedVar.add_field(name="Player", value="netrxc", inline=False)
            embedVar.add_field(name="Damage done", value=int(damagedone), inline=True)
            embedVar.add_field(name="Damage taken", value=int(damagetaken), inline=True)
            embedVar.set_footer(
                text="Information requested by: {}".format(message.author.display_name)
            )
            await message.channel.send(embed=embedVar)
    

        """Fetches user cojecalla stats from db"""
        if message.content.startswith("!ramon"):
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
            kills = data["kills"]
            kd = data["kdRatio"]
            assists = data["assists"]
            killspergame = data["killsPerGame"]
            deaths = data["deaths"]
            damagedone = data["damageDone"]

            embedVar = discord.Embed(
                title="Warzone Summary",
                description="Last 20 match summary",
                color=discord.Color.blue(),
            )
            embedVar.set_author(
                name=message.author.display_name,
                url="",
                icon_url=message.author.avatar_url,
            )
            embedVar.set_thumbnail(
                url="https://gamerforfun.com/wp-content/uploads/2020/04/Call-of-Duty-Warzone-Review-Icon-1024x1024.jpg"
            )
            embedVar.add_field(name="Player", value="cojecalla", inline=False)
            embedVar.add_field(name="Kills", value=int(kills), inline=True)
            embedVar.add_field(name="Deaths", value=int(deaths), inline=True)
            embedVar.add_field(name="KD", value="{0:.2f}".format(kd), inline=True)
            embedVar.add_field(
                name="Kills per game", value="{0:.2f}".format(killspergame), inline=True
            )
            embedVar.add_field(name="Assists", value=int(assists), inline=True)
            embedVar.add_field(name="Damage done", value=int(damagedone), inline=True)
            embedVar.set_footer(
                text="Information requested by: {}".format(message.author.display_name)
            )
            await message.channel.send(embed=embedVar)

        
        """Fetches user ozz stats from db"""
        if message.content.startswith("!oso"):
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

            kills = data["kills"]
            kd = data["kdRatio"]
            assists = data["assists"]
            killspergame = data["killsPerGame"]
            deaths = data["deaths"]
            damagedone = data["damageDone"]

            embedVar = discord.Embed(
                title="Warzone Summary",
                description="Last 20 match summary",
                color=discord.Color.blue(),
            )
            embedVar.set_author(
                name=message.author.display_name,
                url="",
                icon_url=message.author.avatar_url,
            )
            embedVar.set_thumbnail(
                url="https://gamerforfun.com/wp-content/uploads/2020/04/Call-of-Duty-Warzone-Review-Icon-1024x1024.jpg"
            )
            embedVar.add_field(name="Player", value="TheOZzG3", inline=False)
            embedVar.add_field(name="Kills", value=int(kills), inline=True)
            embedVar.add_field(name="Deaths", value=int(deaths), inline=True)
            embedVar.add_field(name="KD", value="{0:.2f}".format(kd), inline=True)
            embedVar.add_field(
                name="Kills per game", value="{0:.2f}".format(killspergame), inline=True
            )
            embedVar.add_field(name="Assists", value=int(assists), inline=True)
            embedVar.add_field(name="Damage done", value=int(damagedone), inline=True)
            embedVar.set_footer(
                text="Information requested by: {}".format(message.author.display_name)
            )
            await message.channel.send(embed=embedVar)

        """Fetches user bbz stats from db"""
        if message.content.startswith("!bebo"):
            resp_profile = requests.get(
                "https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/xbl/gamer/thebbz26/matches/wz/start/0/end/0/details",
                cookies=cookies,
            )
            uno = resp_profile.json()["data"]["matches"][0]["player"]["uno"]
            uno_matches = requests.get(
                f"https://www.callofduty.com/api/papi-client/crm/cod/v2/title/mw/platform/uno/uno/{uno}/matches/wz/start/0/end/0/details",
                cookies=cookies,
            )
            data = uno_matches.json()["data"]["summary"]["all"]

            kills = data["kills"]
            kd = data["kdRatio"]
            assists = data["assists"]
            deaths = data["deaths"]
            damagedone = data["damageDone"]
            killspergame = data["killsPerGame"]

            embedVar = discord.Embed(
                title="Warzone Summary",
                description="Last 20 match summary",
                color=discord.Color.blue(),
            )
            embedVar.set_author(
                name=message.author.display_name,
                url="",
                icon_url=message.author.avatar_url,
            )
            embedVar.set_thumbnail(
                url="https://gamerforfun.com/wp-content/uploads/2020/04/Call-of-Duty-Warzone-Review-Icon-1024x1024.jpg"
            )
            embedVar.add_field(name="Player", value="TheBBz26", inline=False)
            embedVar.add_field(name="Kills", value=int(kills), inline=True)
            embedVar.add_field(name="Deaths", value=int(deaths), inline=True)
            embedVar.add_field(name="KD", value="{0:.2f}".format(kd), inline=True)
            embedVar.add_field(name="Assists", value=int(assists), inline=True)
            embedVar.add_field(name="Damage done", value=int(damagedone), inline=True)
            embedVar.add_field(
                name="Kills per game", value="{0:.2f}".format(killspergame), inline=True
            )
            embedVar.set_footer(
                text="Information requested by: {}".format(message.author.display_name)
            )
            await message.channel.send(embed=embedVar)

        if message.content.startswith("!scoreboard"):
            scoreboard()
            await message.reply(file=discord.File("scoreboard.png"))


client = MyClient()
client.run("MTAwNDA5NTE0MzYwMDcyMTk1MQ.G7sHqx.5d0ZpcKVV5DUiGGDaCYODG0bdA1lZ-dJ4niI8Q")
