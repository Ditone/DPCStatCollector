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
#
# First stage of development will be to pull the # of pings by each pro player
#   1. One match    2. Several matches (different players)  3. Several matches (some same players)
#   4. Whole NA Region  5. Each individual region   6. Group by teams   7. Overview

# get_und_4z_url = "https://api.opendota.com/api/matches/5849513507?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
# get_qc_eg_url = "https://api.opendota.com/api/matches/5861478139?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
# get_sad_at_url = "https://api.opendota.com/api/matches/5861662720?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"

# Testing IDs : 5849513507, 5861478139, 5861662720

from SupportingScripts.MatchRetriever import MatchRetriever
from SupportingScripts.PlayerInfo import PlayerInfo


def main():
    recorder = MatchRetriever()
    testing_matches = [5849513507, 5861478139, 5861662720]
    match_list = []
    status = 0

    recorder2 = MatchRetriever()
    print()
    print()
    for x in range(2):
        print()
        print()
        print("Repeat " + str(x+1))
        recorder.update_multiple_player_list(testing_matches)
        recorder2.print_player_list()
        print()
        print()


if __name__ == "__main__":
    main()
