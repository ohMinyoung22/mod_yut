from random import randint, random

from piece import MOVING_MODE


class UIManager:
    def __init__(self):
        pass

    def throw(self, team):
        thrower = team.getNextThrower()
        print("current thrower : " + thrower.playerID)

        input("press any to throw")
        delta = randint(-1, 5)
        print(f"나온 숫자 {str(delta)}")
        piece_num = input("press 0 ~ 1 to choose piece : ")
        piece = team.getPiece(piece_num)

        print(f"UIManager 고른 piece : {piece.__str__()}")
        return (delta, piece)

    def movePiece(self, piece, nextPosition):
        currentMode = piece.movingMode
        currentPosition = piece.currentPosition
        # currentPos -> nextPos로 움직임

    def selectDirection(self, piece):
        selection = input("1 - 일반 / 2 - 지름길")

        return True if int(selection) == 2 else False

        #piece 밑에 방향 표시?
    
    def endPiece(self, piece):
        if piece.movingMode == MOVING_MODE.DEFAULT:
            # piece currentPos -> 20
            # 말 없애기
            pass
        else:
            # piece currnetPos -> 6
            # 말 없애기
            pass

