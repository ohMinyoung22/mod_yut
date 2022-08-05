class Team:

    def __init__(self, teamName, pieces):
        self.teamName = teamName
        self.players = []
        self.pieces = pieces
    
    def addPlayer(self, player):
        self.players.append(player)