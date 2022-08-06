from piece import MOVING_MODE, Piece
from player import Player
from team import Team

class TeamManager:
    def __init__(self):
        self.initialize()


    def initialize(self):
        self.teamList = []

        piece_red_0 = Piece("red0", 0)
        piece_red_1 = Piece("red1", 1)

        player1 = Player("red1")
        player2 = Player("red2")

        team_red = Team('RED', [piece_red_0, piece_red_1], [player1, player2])

        piece_blue_0 = Piece("blue0", 0)
        piece_blue_1 = Piece("blue1", 1)

        player3 = Player("blue1")
        player4 = Player("blue2")

        team_blue = Team('BLUE', [piece_blue_0, piece_blue_1], [player3, player4])

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
            return self.currentThrowingTeam
        else:
            currentIndex = self.teamList.index(self.currentThrowingTeam)
            nextIndex = -1

            if currentIndex == (len(self.teamList) - 1):
                nextIndex = 0
            else:
                nextIndex = currentIndex + 1

            self.currentThrowingTeam = self.teamList[nextIndex]

            return self.currentThrowingTeam

    def getWinTeam(self):
        return self.winTeam

    def removePiece(self, piece, isStacked=False):
        for team in self.teamList:
            if team.removePiece(piece, isStacked):
                return
        
        print("no piece removed")

    def registerPiece(self, piece):
        team = self.getTeam(piece)
        team.registerPieceFromStacked()

    def isGameEnd(self):
        for team in self.teamList:
            if team.isAllPieceEnd():
                self.winTeam = team
                return True

        return False

    def getTeam(self, piece):
        for team in self.teamList:
            if team.matchPiece(piece) != None:
                return team

    def getCatchPieces(self, piece):
        currentMode = piece.movingMode
        currentPosition = piece.currentPosition
        pieceTeam = self.getTeam(piece)

        pieceList = []

        for team in self.teamList:
            for piece in team.pieces:
                if piece.movingMode == currentMode and piece.currentPosition == currentPosition:
                    if team != pieceTeam:
                        pieceList.append(piece)

        return pieceList

    def getStackPieces(self, piece):
        currentMode = piece.movingMode
        currentPosition = piece.currentPosition
        pieceTeam = self.getTeam(piece)

        pieceList = []

        for _piece in pieceTeam.pieces:
            if _piece.movingMode == currentMode and _piece.currentPosition == currentPosition:
                if (currentMode != MOVING_MODE.DEFAULT or currentPosition != 0) and _piece != piece:
                    pieceList.append(_piece)

        for p in pieceList:
            print(p.__str__())
        return pieceList


