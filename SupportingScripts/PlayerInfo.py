# Custom data structure to store relevant data
# Needs to store player name, player id, team name, team id, # of pings (default 0)

class PlayerInfo:

    def __init__(self, name, name_id, team, pings) -> object:
        self.name = name
        self.name_id = name_id
        self.team = team
        self.pings = pings

    def __repr__(self):
        return self.name + " of team " + self.team + ". For test, this player has " + str(self.pings) + " pings."

    def __str__(self):
        return self.name + " of team " + self.team + ". For this test, this player has " + str(self.pings) + " pings."

    def update_pings(self, count: int):
        if count > 1:
            self.pings = self.pings + count

        else:
            print("Error updating " + self.name + ".")
            exit(666)

    def clear_pings(self):
        self.pings = 0
        print("Cleared " + self.name + "'s pings.")

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def get_pings(self):
        return self.team
