# The purpose of this file is to test my connectivity to the Steamworks dev API
# Also looking test the GetMatchDetails call, and experiment with the returned data type.
# Will most likely return the dataset to a local file so that I'm not spamming the network.
#
# IDOTA2Match_<ID>
# URL: GET http://api.steampowered.com/IDOTA2Match_<ID>/GetMatchDetails/v1
#
# match_id (string)
#   Match id
#
# Your Steam Web API Key
# Key: 66C3D405427A17EECDA4280DA8D65851
# Domain Name: https://quinreidy.me

# going to start with one specific match - EG vs Quincy Crew, Tie Breakers
def get_specific_match():
    status = 0

    # open file
    try:
        output = open("SupportingScripts/match_output", "w")
        status = 1

    except FileNotFoundError:
        print("Couldn't find file")
        status = 0

    if status == 0:
        return False

    # write to the file
    output.write("match details")

    # close file
    output.close()

    # return true for complete
    return True

