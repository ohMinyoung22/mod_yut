from matplotlib.pyplot import pie


class Team:

    def __init__(self, teamName, pieces):
        self.teamName = teamName
        self.players = []
        self.pieces = pieces
    
    def addPlayer(self, player):
        self.players.append(player)
    
    def getPiece(self, index):
        for piece in self.pieces:
            if piece.index == index:
                return piece