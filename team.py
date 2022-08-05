
class Team:

    def __init__(self, teamName, pieces, players):
        self.teamName = teamName
        self.players = players
        self.pieces = pieces

        self.thrower = players[0]
    
    def getPiece(self, index):
        for piece in self.pieces:
            if piece.index == index:
                return piece
    
    def isAllPieceEnd(self):
        return len(self.pieces) == 0

    def removePiece(self, piece):
        if self.pieces.__contains__(piece):
            print("teamName : " + self.teamName + " piece : " + str(piece.index))
            self.pieces.remove(piece)
            return True
        
        return False

    def getNextThrower(self):
        currentIndex = self.players.index(self.thrower)
        nextIndex = -1

        if currentIndex == (len(self.players) - 1):
            nextIndex = 0
        else:
            nextIndex = currentIndex + 1

        self.thrower = self.players[nextIndex]

        return self.thrower