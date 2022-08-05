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

        self.currentThrowingTeam = self.teamList[0]

        self.isFirstTurn = True
        self.winTeam = None

    def clear(self):
        self.initialize()

    def getNextThrowingTeam(self, isDouble):
        if self.isFirstTurn:
            print("It's First Turn")
            self.isFirstTurn = False
            return self.currentThrowingTeam

        if isDouble:
            print("isDouble : " + str(self.currentThrowingTeam.teamName))
            return self.currentThrowingTeam
        else:
            currentIndex = self.teamList.index(self.currentThrowingTeam)
            nextIndex = -1

            if currentIndex == (len(self.teamList) - 1):
                nextIndex = 0
            else:
                nextIndex = currentIndex + 1

            self.currentThrowingTeam = self.teamList[nextIndex]

            print("Not isDouble : " + str(self.currentThrowingTeam.teamName))
            return self.currentThrowingTeam

    def getWinTeam(self):
        return self.winTeam

    def removePiece(self, piece):
        for team in self.teamList:
            if team.removePiece(piece):
                return
        
        print("no piece removed")

    def isGameEnd(self):
        for team in self.teamList:
            if team.isAllPieceEnd():
                self.winTeam = team
                return True

        return False
