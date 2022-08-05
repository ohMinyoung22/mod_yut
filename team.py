
class Team:

    def __init__(self, teamName, pieces):
        self.teamName = teamName
        self.players = []
        self.pieces = pieces
    
    def addPlayer(self, player):
        self.players.append(player)
    
    def getPiece(self, index):
        #for piece in self.pieces:
        #    if piece.index == index:
        #        return piece
        return self.pieces[0]
    
    def isAllPieceEnd(self):
        return len(self.pieces) == 0

    def removePiece(self, piece):
        if self.pieces.__contains__(piece):
            print("teamName : " + self.teamName + " piece : " + str(piece.index))
            self.pieces.remove(piece)
            return True
        
        return False