# Define stats attributes for each clubs attend Champions League in tournament phase

class ChampionsLeagueStats(object):
    def __init__(self, team_name, goals_scored, goals_against, yellow_cards, red_cards, attempts_on_target,
                 attempts_off_target, offsides, corners, fouls_committed, possession_time, possession_percent):
        self.team_name = team_name
        self.goals_scored = goals_scored
        self.goals_against = goals_against
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.attempts_on_target = attempts_on_target
        self.attempts_off_target = attempts_off_target
        self.offsides = offsides
        self.corners = corners
        self.fouls_committed = fouls_committed
        self.possession_time = possession_time
        self.possession_percent = possession_percent