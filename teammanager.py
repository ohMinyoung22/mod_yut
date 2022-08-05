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
        
    def getPieceFromTeam(self, team, index):
        pass


    def getNextThrowingTeam():
        pass