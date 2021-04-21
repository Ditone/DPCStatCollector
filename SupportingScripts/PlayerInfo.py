# Custom data structure to store relevant data
# Needs to store player name, player id, team name, team id, # of pings (default 0)

class PlayerInfo:

    def __init__(self, name, name_id, team, pings, match_time) -> object:
        self.name = name
        self.name_id = name_id
        self.team = team
        # What variables do we want to track?

        # Number of pings
        self.pings = pings

        # Number of matches
        self.matches = 1

        # Total amount of match time
        self.match_time = match_time

        # Heroes played
        self.hero_played = {}

    def __repr__(self):
        return self.name + " of team " + self.team + ". This player has " + str(self.pings) + " total pings."

    def __str__(self):
        return self.name + " of team " + self.team + ". This player has " + str(self.pings) + " total pings."

    def update_pings(self, count: int):
        if count >= 0:
            self.pings = self.pings + count

        else:
            print("Error updating " + self.name + ".")
            exit(666)

    def update_hero_played(self, hero: str):
        if hero in self.hero_played:
            val = self.hero_played.get(hero) + 1
            self.hero_played.update({hero: val})

        else:
            print("Hero not found. Adding " + hero + " to " + self.name)
            self.hero_played.update({hero: 1})

    def update_matches(self):
        self.matches += 1

    def update_match_time(self, time: int):
        self.match_time += time

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def get_pings(self):
        return self.pings

    def get_match_time(self):
        return self.match_time

    def get_matches(self):
        return self.matches

    def clear_pings(self):
        self.pings = 0
        print("Cleared " + self.name + "'s pings.")

