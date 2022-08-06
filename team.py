
from piece import Piece


class Team:

    def __init__(self, teamName, pieces, players):
        self.teamName = teamName
        self.players = players
        self.pieces = pieces
        self.stackedPieces = []

        self.thrower = players[0]

        self.isFirstThrow = True

    def getPiece(self, _index):
        for piece in self.pieces:
            if int(piece.index) == int(_index):
                return piece

    def getPiece(self, _piece):
        for piece in self.pieces:
            if piece == _piece:
                return piece
        return None

    def isAllPieceEnd(self):
        return len(self.pieces) == 0

    def removePiece(self, piece, isStacked):
        if self.pieces.__contains__(piece):
            if isStacked:
                self.stackedPieces.append(piece)
                self.pieces.remove(piece)  
                return True
            else:
                print("removed " + self.teamName + " " + piece.__str__())
                self.pieces.remove(piece)
                return True

        return False

    def registerPieceFromStacked(self):
        for _piece in self.stackedPieces:
            self.pieces.append(_piece)
            self.stackedPieces.remove(_piece)

    def getNextThrower(self):
        if self.isFirstThrow:
            self.isFirstThrow = False
            return self.thrower

        else:
            currentIndex = self.players.index(self.thrower)
            nextIndex = -1

            if currentIndex == (len(self.players) - 1):
                nextIndex = 0
            else:
                nextIndex = currentIndex + 1

            self.thrower = self.players[nextIndex]

            return self.thrower
