# Define attributes of World Cup editions

class WorldCupEdition(object):
    def __init__(self, edition, team_number, match_played, goal_scored, average_goal, average_attendance):
        self.edition = edition
        self.team_number = team_number
        self.match_played = match_played
        self.goal_scored = goal_scored
        self.average_goal = average_goal
        self.average_attendance = average_attendance
    