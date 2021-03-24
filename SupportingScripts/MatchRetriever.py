# Point of this file is to store functionality of retrieving match information, and storage options
# No analysis here, just the retrieval and storage
# 'DPC Winter 21 League (NA) presented by BTS' : ID 12735

import requests
import json
from SupportingScripts.PlayerInfo import PlayerInfo


class MatchRetriever:
    _instance = None

    # Singleton pattern - want just one retriever / information store
    # Could eventually be used to update a DB
    def __new__(cls):
        if cls._instance is None:
            print("Creating new Match Retriever.")
            cls._instance = super(MatchRetriever, cls).__new__(cls)
            #
        return cls._instance

    # placeholder urls for testing
    get_und_4z_url = "https://api.opendota.com/api/matches/5849513507?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
    get_qc_eg_url = "https://api.opendota.com/api/matches/5861478139?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"
    get_sad_at_url = "https://api.opendota.com/api/matches/5861662720?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"

    # player_list
    player_list = []

    # Input: int Match ID
    # Output: JSON results
    def get_specific_match(self, match_id: int):
        # url for the api request
        get_url = "https://api.opendota.com/api/matches/" + str(
            match_id) + "?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"

        # request_test = requests.get(url, headers=headers)
        try:
            request_test = requests.get(get_url).json()

        except IOError as io_err:
            print("Something went wrong with the request: ", io_err)

        return request_test

    # Input JSON
    # Output: Updated file
    # Default is a file named "match_output" found in the SupportingScripts folder
    # Use: Report data by writing to file
    def write_match_to_file(self, result_set):
        if result_set:

            # dumping the result
            json_results = json.dumps(result_set, indent=4)

            # attempt to open the file / open the file
            try:
                results_file = open("SupportingScripts/match_output", 'w')

                # clear the file before adding
                print("Clearing file.")
                results_file.write("")

                # writing to the file
                print("Writing to file.")
                results_file.write(json_results)

                # close the file
                print("Finished writing. Closing.")
                results_file.close()

            except FileNotFoundError:
                print("File doesn't exist. Creating the file: ")
                open("SupportingScripts/match_output", "x")
                self.write_match_to_file(result_set)

        else:
            print("No valid input or result set.")
            exit(666)

    #  Clear global player list - may be needed for testing / debugging
    def clear_player_list(self):
        if self.player_list is None:
            print("player_list doesn't exist.")

        elif len(self.player_list) == 0:
            print("player_list is already empty.")

        else:
            self.player_list.clear()

    # Print out the player list - may be needed for testing / debugging
    def print_player_list(self):
        if self.player_list is None:
            print("player_list doesn't exist.")

        elif len(self.player_list) == 0:
            print("player_list is empty.")

        else:
            for player in self.player_list:
                print(player)

    # Input: JSON of Match Details
    # Output: Number of updated entries, updated global player list specifically for pings
    def update_player_list_ping(self, result_set):
        # tracker for number of updated entries
        num_updated = 0
        player_found = False

        # update player if they exists
        # else, append global list with new player with info
        for player in result_set['players']:
            # nested for loop, but the worst case time is only 10n (since max players per result is 10)
            for existing_player in self.player_list:
                # track if the name exists
                player_found = False

                # check if the name exists, if it does, update
                if player['name'] == existing_player.get_name():
                    # update here
                    existing_player.update_pings(player['pings'])
                    num_updated += 1
                    # sets the tracker to true, so that it doesn't run the block below
                    player_found = True

            # this will only run if the previous for loop didn't exit / find a match
            if not player_found:
                if player['isRadiant']:
                    self.player_list.append(PlayerInfo(player['name'], player['account_id'],
                                                       result_set['radiant_team']['name'], player['pings']))
                    num_updated += 1
                else:
                    self.player_list.append(PlayerInfo(name=str(player['name']), name_id=int(player['account_id']),
                                                       team=result_set['dire_team']['name'],
                                                       pings=int(player['pings'])))
                    num_updated += 1

        # returns number of updated entries, should be 10
        return num_updated

    # Input: List of JSON of Match Details
    # Output: Fully updated global player list
    def update_multiple_player_list(self, *args: int):
        status = 0

        if len(args) == 0:
            print("No arguments.")
            exit(666)

        for match_id in args:
            # calls update_player_list after getting the result set from the get_specific_match call for each argument
            status = status + self.update_player_list_ping(self.get_specific_match(match_id))
            # each call to update_player_list should return 10
            # thus if status%10 isn't 0, then somewhere there was an issue updating
            if status % 10 != 0:
                print("potential error updating on match_id: " + str(match_id))
            else:
                print("Match id: " + str(match_id) + " has been successfully updated.")

        print(str(len(args)) + " matches have been entered.")
