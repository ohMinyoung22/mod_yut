import random
from enum import Enum
from unittest.mock import DEFAULT

from piece import Piece, TEAM, MOVING_MODE

class Player:
    def __init__(self, team, playerID):
        self.team = team
        self.playerID = playerID


class GameSystem:
    def __init__(self, playerIDs):
        self.players = []
        self.pieces = []

        if len(playerIDs) == 2:
            random.shuffle(playerIDs)
            self.players.append(Player(TEAM.RED, playerIDs[0]))
            self.players.append(Player(TEAM.BLUE, playerIDs[1]))
        elif len(playerIDs) == 4:
            random.shuffle(playerIDs)
            self.players.append(Player(TEAM.RED, playerIDs[0]))
            self.players.append(Player(TEAM.RED, playerIDs[1]))
            self.players.append(Player(TEAM.BLUE, playerIDs[2]))
            self.players.append(Player(TEAM.BLUE, playerIDs[3]))

        self.startGame()

    def startGame(self):
        for i in range(0, 3):
            self.pieces.append(Piece(TEAM.BLUE, "abc"))
            self.pieces.append(Piece(TEAM.RED, "abc"))

    def move(self, piece, delta):

        nextPosition = piece.currentPosition + delta

        if(delta == -1):
            self.back(piece)
            return True

        if ~self.checkEnd(piece, nextPosition):
            self.movePiece(piece, nextPosition)
            self.selectDirection()

            if delta == 4 or delta == 5:
                return False
            else:
                return True
        else:
            self.endPiece()
            return True

    def back(self, piece):
        if piece.currentPosition == 0:
            if piece.movingMode == MOVING_MODE.DEFAULT:
                self.endPiece(piece)
            elif piece.movingMode == MOVING_MODE.FROM_RIGHT_CORNER:
                piece.movingMode = MOVING_MODE.DEFAULT
                nextPosition = 4
                self.movePiece(piece, nextPosition)
            elif piece.movingMode == MOVING_MODE.FROM_LEFT_CORNER:
                piece.movingMode = MOVING_MODE.DEFAULT
                nextPosition = 9
                self.movePiece(piece, nextPosition)    


    def checkEnd(self, piece, nextPosition):
        if piece.movingMode == MOVING_MODE.DEFAULT:
            if nextPosition > 20:
                return True
            else:
                return False
        else:
            if nextPosition > 6:
                return True
            else:
                return False

    def movePiece(self, piece, nextPosition):
        piece.currentPosition = nextPosition
        # UI 상에서 엔티티 옮기는 로직

    def selectDirection(self, piece, player):
        if piece.currentPosition == 5 or piece.currentPosition == 10:
            isAheadShortCut = player.chooseDirectionUI()
            # UI 상에서 플레이어가 어느 길로 갈지 선택하는 로직

            if isAheadShortCut:
                if piece.currentPosition == 5:
                    piece.movingMode = MOVING_MODE.FROM_RIGHT_CORNER
                    piece.currentPosition = 0
                elif piece.currentPosition == 10:
                    piece.movingMode = MOVING_MODE.FROM_LEFT_CORNER
                    piece.currentPosition = 0
            else:
                piece.movingMode = MOVING_MODE.DEFAULT

    def endPiece(self, piece):
        self.pieces.remove(piece)


    def throw(self, team):
        delta = 0
        delta = self.getNextThrower(team).throw()
        piece = self.getNextThrower(team).getSelectedPiece(team)
        if(self.move(piece, delta, self.getNextThrower(team))):
            self.getNextThrower(team).endTurn()
        else:
            self.throw(team)

    def getNextThrower(self, team):
        pass