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
    print("STEAM WEB API KEY: 66C3D405427A17EECDA4280DA8D65851")
    print("The domain I used: https://quinreidy.me")

    # Authorization Header
    test_url = "https://api.opendota.com/api/matches/5861478139?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
    url = "https://api.opendota.com/api/matches/5861478139"
    headers = {'Authorization: Bearer 3ca47c01-644c-48fc-b81c-ca2032313edc'}

    # request_test = requests.get(url, headers=headers)
    request_test = requests.get(test_url).json()

    if request_test:

        # dumping the result
        json_results = json.dumps(request_test, indent=4)

        # open the file
        try:
            results_file = open("SupportingScripts/match_output", 'w')

        except FileNotFoundError:
            print("Couldn't find the file")
            exit(666)

        # clear the file
        print("clearing file")
        results_file.write("")

        # writing to the file
        print("writing to file")
        results_file.write(json_results)


if __name__ == "__main__":
    main()
