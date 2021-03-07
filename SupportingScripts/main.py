# This is the main file to run / test run different python scripts.
# Need to find and test the relevant API calls for functionality.

# Notify program when a new match is played. <-- can be implemented last
# After a DPC match is played, pull the full match details
# Need the following information:
#       team name, player names, heroes played, game time, region, picks and bans
#           > might need to interpret the region by team or by server cluster
#
# Some ideas for data analysis:
#       game time when a team was 10k ahead of the other team (gold or exp), or disparity between expm / gpm of roles
#       separate database to track "role" or "position #" of each team player.
#           >Would most likely be manually implemented (yuck)
#       barrack status per hero, compared to game time (ex, lycan 2 barracks avg <20 min, .5 barracks avg > 40)
#
# Your Steam Web API Key
# Key: 66C3D405427A17EECDA4280DA8D65851
# Domain Name: https://quinreidy.me
# OPENDOTA API KEY
# 3ca47c01-644c-48fc-b81c-ca2032313edc


from SupportingScripts import getInfoFromMatchID
import requests
import json


def main():
    match_id = 1
    print("https://api.opendota.com/api/matches/" + str(match_id) + "?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc")


if __name__ == "__main__":
    main()
