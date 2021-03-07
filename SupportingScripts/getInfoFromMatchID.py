# Point of this file is to store functionality of retrieving match information, and storage options
# No analysis here, just the retrieval and storage

import requests
import json


# Default get_specific_match will specifically get QC vs EG, NA DPC S1 Group Stage Tiebreakers
# Encapsulated the request call here so that I don't have to run too many requests
# returns a JSON of the match details to be filtered
def get_specific_match():
    # url for the API request
    get_qc_eg_url = "https://api.opendota.com/api/matches/5861478139?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"

    # request_test = requests.get(url, headers=headers)
    try:
        request_test = requests.get(get_qc_eg_url).json()
        json_results = json.dumps(request_test, indent=4)

    except IOError as io_err:
        print("Something went wrong with the request: ", io_err)

    return json_results


# Input: int Match ID
# Output: json results
def get_specific_match(match_id: int):
    # url for the api request
    get_url = "https://api.opendota.com/api/matches/" + str(match_id) + "?api_key=3ca47c01-644c-48fc-b81c-ca2032313edc"

    # request_test = requests.get(url, headers=headers)
    try:
        request_test = requests.get(get_url).json()
        json_results = json.dumps(request_test, indent=4)

    except IOError as io_err:
        print("Something went wrong with the request: ", io_err)

    return json_results


# Will take an input (type json) and write it to a file
# Default is a file named "match_output" found in the SupportingScripts folder
# Eventually will use helper methods to filter out the relevant data
def write_match_to_file(result_set: json):

    if result_set:

        # dumping the result
        json_results = json.dumps(result_set, indent=4)

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
        results_file.write(json_results)

        # close the file
        print("finished writing, closing")
        results_file.close()

    else:
        print("No valid input or result set")
        exit(666)
