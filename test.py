
from teammanager import TeamManager

from piece import MOVING_MODE
from uimanager import UIManager

# 플레이어 엔티티 자유롭게 움직일 수 있도록 구현(게임 플레이에는 영향 없게)

# 업을지 말지 결정
class Test:
    def __init__(self):
        self.teamManager = TeamManager()
        self.UIManager = UIManager()

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
        self.UIManager.win(team)
    
    def clearGame(self):
        self.teamManager.clear()

    #ThrowingEvent       
    def throw(self, team):
        delta, piece = self.UIManager.throw(team)

        print("throw recieved piece : " + piece.__str__())

        return self.move(piece, int(delta))

    def move(self, piece, delta):

        nextPosition = piece.currentPosition + delta

        if delta == 0:
            print("낙")

            return False

        if delta == -1:
            self.back(piece)

            print("적용 후 " + piece.__str__())
            print("----------------------------------------------")

            listStack = self.teamManager.getStackPieces(piece)
            if len(listStack) > 0:
                self.stack(listStack, piece)

            listCatch = self.teamManager.getCatchPieces(piece)
            if len(listCatch) > 0:
                self.catch(listCatch)

                if delta == 4 or delta == 5:
                    return False
                else:
                    return True 

            return False

        if self.checkEnd(piece, nextPosition) == False:
            self.movePiece(piece, nextPosition)
            self.selectDirection(piece)

            print("적용 후 " + piece.__str__())
            print("----------------------------------------------")

            listStack = self.teamManager.getStackPieces(piece)
            if len(listStack) > 0:
                self.stack(listStack, piece)

            listCatch = self.teamManager.getCatchPieces(piece)
            if len(listCatch) > 0:
                self.catch(listCatch)

                if delta == 4 or delta == 5:
                    return False
                else:
                    return True        

            if delta == 4 or delta == 5:
                return True
            else:
                return False
        else:
            self.endPiece(piece)
            return False

    def stack(self, listStack, piece):

        print(f" -- listStack -- {map(lambda e : e.__str__(), listStack)}")

        print(f"before Stacked {self.teamManager.getTeam(piece)} : {self.teamManager.getTeam(piece).pieces.__str__()}")
        for _piece in listStack:
            piece.stackedList.append(_piece)
            self.teamManager.removePiece(_piece, True)

        print("after Stacked" )
        print(f"{self.teamManager.getTeam(piece)} : {self.teamManager.getTeam(piece).pieces.__str__()}")

    def deStack(self, piece):
        print("-- deStacked --")

        piece.stackedList = []

        self.teamManager.registerPiece(piece)

        for _piece in self.teamManager.getTeam(piece).pieces:
            self._pieceToStartPoint(_piece)

        print("-- after deStacked --")
        print(f"{self.teamManager.getTeam(piece)} : {self.teamManager.getTeam(piece).pieces.__str__()}")

    def catch(self, listCatch):
        print("catch called")
        for piece in listCatch:
            if len(piece.stackedList) > 0:
                self.deStack(piece)                
            else:
                self._pieceToStartPoint(piece)

    def _pieceToStartPoint(self, piece):
        piece.movingMode = MOVING_MODE.DEFAULT
        self.movePiece(piece, 0)

    def back(self, piece):
        print("back called")

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
        print("move 적용 piece(전) : " + piece.__str__())
        self.UIManager.movePiece(piece, nextPosition)
        piece.currentPosition = nextPosition
        print("move 적용 piece(후) : " + piece.__str__())


    def selectDirection(self, piece):
        print("direction 적용 piece " + piece.__str__())
        if (piece.currentPosition == 5 or piece.currentPosition == 10) and piece.movingMode == MOVING_MODE.DEFAULT:
            # UI 상에서 플레이어가 어느 길로 갈지 선택하는 로직
            isAheadShortCut = self.UIManager.selectDirection(piece)

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
        print("endPiece 적용 전 : " + piece.__str__())
        self.UIManager.endPiece(piece)
        self.teamManager.removePiece(piece)

Test()
