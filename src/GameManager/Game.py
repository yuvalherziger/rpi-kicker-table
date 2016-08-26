class Game:

    matches = { }
    team_a = None
    team_b = None
    match_index = None

    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.match_index = 0

    def __finishMatch(match_index, right_score, left_score):
        if (match_index % 2 == 0):
            matches[match_index] = { "team_a": right_score, "team_b": left_score }
        else:
            matches[match_index] = { "team_a": left_score, "team_b": right_score }

    # TODO: submit to kicker fork
    def __finishGame(self):
        
