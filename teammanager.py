from piece import Piece
from team import Team

class TeamManager:
    def __init__(self):
        self.initialize()


    def initialize(self):
        self.teamList = []

        piece_red_0 = Piece("abs", 0)
        piece_red_1 = Piece("absd", 1)

        team_red = Team('RED', [piece_red_0, piece_red_1])

        piece_blue_0 = Piece("abs", 0)
        piece_blue_1 = Piece("absd", 1)

        team_blue = Team('BLUE', [piece_blue_0, piece_blue_1])
        
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
