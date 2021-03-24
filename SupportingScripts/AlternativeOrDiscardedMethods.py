# Default match type, but as a Response object, not a JSON
# Experimenting with response type
import requests
import json

get_und_4z_url = "https://api.opendota.com/api/matches/5849513507?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
get_qc_eg_url = "https://api.opendota.com/api/matches/5861478139?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
get_sad_at_url = "https://api.opendota.com/api/matches/5861662720?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"


# Write to a file using the response type
def write_match_to_file_response(result_set: requests.models.Response):
    if result_set is not None:

        print("we got here")
        # attempt to open the file / open the file
        try:
            results_file = open("SupportingScripts/match_output", 'w')

        except FileNotFoundError:
            print("Couldn't find the file")
            exit(666)

        # clear the file before adding
        print("clearing file")
        results_file.write("")

        # writing to the file
        print("writing to file")
        results_file.write(str(result_set.content))

        # close the file
        print("finished writing, closing")
        results_file.close()

    else:
        print("No result given")
        exit(666)


def get_default_match_response():
    # request_test = requests.get(url, headers=headers)
    try:
        request_test = requests.get(get_qc_eg_url)
        return request_test

    except IOError as io_err:
        print("Something went wrong with the request: ", io_err)


# input: JSON Match Details
# output: Player
def ping_from_match(result_set):
    ping_dict = {}

    radiant_name = result_set['radiant_team']['name']
    dire_name = result_set['dire_team']['name']

    for player in result_set['players']:
        if player['isRadiant']:
            ping_dict[(player['name'], radiant_name)] = player['pings']
        else:
            ping_dict[(player['name'], dire_name)] = player['pings']

    return ping_dict


# Uses the ping_from_match and get_specific_match functions to loop through a series of matches and retrieve all pings
# Most likely will be replaced later on, but good to have as a one off function to fill in starting values
# Input: list of match id's (ints)
# Output: list [dict (player, team) : pings]
def get_pings_from_matches(*args: int):
    ping_list = []

    for game_id in args:
        ping_list.append(ping_from_match(get_specific_match(match_id=game_id)))

    return ping_list


# Input: int Match ID
# Output: JSON results
def get_specific_match(match_id: int):
    # url for the api request
    get_url = "https://api.opendota.com/api/matches/" + str(match_id) + "?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"

    # request_test = requests.get(url, headers=headers)
    try:
        request_test = requests.get(get_url).json()

    except IOError as io_err:
        print("Something went wrong with the request: ", io_err)

    return request_test
