import random

from team import Team
from teammanager import TeamManager

from piece import MOVING_MODE
from uimanager import UIManager

# 여러 개 말 있을 때 상황 구현 (업기, 말 선택해서 이동)
# 플레이어 구현
# 플레이어 엔티티 자유롭게 움직일 수 있도록 구현(게임 플레이에는 영향 없게)

# 플레이어 구현 -> 말 선택해서 이동 -> 업기 -> MOD로 옮기기
class Test:
    def __init__(self):
        self.teamManager = TeamManager()
        while(True):
            self.startGame()
            input("any key")
        
        # 플레이어가 주사위를 던짐 -> 숫자 지정(도/개/걸/윷/모/백도에 대응) -> 말 들어왔는지 여부 확인 ->
        # 백도 체크 -> 말 움직이기 -> 코너 여부 확인(지름길) -> 다시 던지기 여부 확인(윷/모)

    def startGame(self):
        self.endGameFlag = False
        isDouble = False

        while(self.endGameFlag == False):      

            if self.teamManager.isGameEnd() == False:
                team = self.teamManager.getNextThrowingTeam(isDouble)
                isDouble = self.throw(team)
            else:
                self.endGameFlag = True
                team = self.teamManager.getWinTeam()
                self.win(team)
                self.clearGame()

    def win(self, team):
        print("-----------------------------------")
        print(team.teamName + "팀 승리")
    
    def clearGame(self):
        self.teamManager.clear()

    #ThrowingEvent       
    def throw(self, team):
        delta, piece = UIManager.throw(team)

        return self.move(piece, delta)

    def move(self, piece, delta):

        nextPosition = piece.currentPosition + delta
        print("nextpos in move : " + str(nextPosition))

        if delta == 0:
            print("낙")

            print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
            print("----------------------------------------------")
            return False

        if delta == -1:
            self.back(piece)

            print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
            print("----------------------------------------------")
            return False

        if self.checkEnd(piece, nextPosition) == False:
            self.movePiece(piece, nextPosition)
            self.selectDirection(piece)

            if delta == 4 or delta == 5:
                print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
                print("----------------------------------------------")
                return True
            else:
                print("after move pos : " + str(piece.currentPosition) + " mod : " + str(piece.movingMode))
                print("----------------------------------------------")
                return False
        else:
            self.endPiece(piece)
            return False

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

        UIManager.MovePiece(piece, nextPosition)

    def selectDirection(self, piece):
        print("direction called")
        if (piece.currentPosition == 5 or piece.currentPosition == 10) and piece.movingMode == MOVING_MODE.DEFAULT:
            # UI 상에서 플레이어가 어느 길로 갈지 선택하는 로직
            isAheadShortCut = UIManager.selectDirection(piece)

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

        #UIManager.MovePiece(piece, delta)

        self.teamManager.removePiece(piece)


Test()
