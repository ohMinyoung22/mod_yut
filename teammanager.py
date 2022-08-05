from team import Team

class TeamManager:
    def __init__(self):
        self.initialize()


    def initialize(self):
        self.teamList = []

        team_red = Team('RED')
        team_blue = Team('BLUE')
        self.teamList.append(team_red)
        self.teamList.append(team_blue)

    def getNextThrowingTeam():
        pass

    def getWinTeam():
        pass

    def removePiece():
        pass

    def isGameEnd():
        pass
