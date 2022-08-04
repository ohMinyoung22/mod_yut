import random
from enum import Enum

from piece import Piece, TEAM, MOVING_MODE


class Player:
    def __init__(self, team, playerID):
        self.team = team
        self.playerID = playerID


# 여러 개 말 있을 때 상황 구현 (업기, 말 선택해서 이동)
# 턴 종료 시 상대팀으로 턴 넘기기 구현 + 팀 플레이어 마다 번갈아 가면서 던지는 것 구현
# 플레이어 엔티티 자유롭게 움직일 수 있도록 구현(게임 플레이에는 영향 없게)

class Test:
    def __init__(self):
        self.piece = Piece(TEAM.BLUE, "abc")

        # 시작점에서 백도
        # self.move(self.piece, -1) # 정상 작동

        # 코너에서 백도
        # self.move(self.piece, 5)
        # self.move(self.piece, -1) # 정상 작동

        self.move(self.piece, 4)
        self.move(self.piece, 3)
        self.move(self.piece, 3)
        self.move(self.piece, 3)
        

        # 플레이어가 주사위를 던짐 -> 숫자 지정(도/개/걸/윷/모/백도에 대응) -> 말 들어왔는지 여부 확인 ->
        # 백도 체크 -> 말 움직이기 -> 코너 여부 확인(지름길) -> 다시 던지기 여부 확인(윷/모)

    def move(self, piece, delta):

        nextPosition = piece.currentPosition + delta
        print("nextpos in move : " + str(nextPosition))

        if (delta == -1):
            self.back(piece)

            print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
            print("----------------------------------------------")
            return True

        if self.checkEnd(piece, nextPosition) == False:
            self.movePiece(piece, nextPosition)
            self.selectDirection(piece)

            if delta == 4 or delta == 5:
                print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
                print("----------------------------------------------")
                return False
            else:
                print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
                print("----------------------------------------------")
                return True
        else:
            self.endPiece(piece)
            return True

    def back(self, piece):
        print("back called")
        print("current pos : " + str(piece.currentPosition))
        if piece.currentPosition == 0:
            if piece.movingMode == MOVING_MODE.DEFAULT:
                print("is default")
                self.endPiece(piece)
            elif piece.movingMode == MOVING_MODE.FROM_RIGHT_CORNER:
                print("is right")
                piece.movingMode = MOVING_MODE.DEFAULT
                nextPosition = 4
                self.movePiece(piece, nextPosition)
            elif piece.movingMode == MOVING_MODE.FROM_LEFT_CORNER:
                print("is left")
                piece.movingMode = MOVING_MODE.DEFAULT
                nextPosition = 9
                self.movePiece(piece, nextPosition)
        else:
            piece.currentPosition = piece.currentPosition - 1

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
        print("move piece called")
        piece.currentPosition = nextPosition

        if piece.movingMode == MOVING_MODE.DEFAULT and piece.currentPosition == 20:
            pass
            # 말 시작점에 위치 -> 게임 시작 시와 구분되어야 함

        print("piece moved - " + str(piece.currentPosition) + " : " + str(piece.movingMode))
        # UI 상에서 엔티티 옮기는 로직

    def selectDirection(self, piece):
        print("direction called")
        if (piece.currentPosition == 5 or piece.currentPosition == 10) and piece.movingMode == MOVING_MODE.DEFAULT:
            isAheadShortCut = True  # 지름길 이용
            # UI 상에서 플레이어가 어느 길로 갈지 선택하는 로직

            if isAheadShortCut:
                if piece.currentPosition == 5:
                    piece.movingMode = MOVING_MODE.FROM_RIGHT_CORNER

                    print("right")
                    piece.currentPosition = 0
                elif piece.currentPosition == 10:
                    piece.movingMode = MOVING_MODE.FROM_LEFT_CORNER
                    print("left")
                    piece.currentPosition = 0
            else:
                piece.movingMode = MOVING_MODE.DEFAULT

    def endPiece(self, piece):
        # self.pieces.remove(piece)
        print("말 제거")


Test()
