from random import random


class UIManager:
    def __init__(self):
        pass

    def throw(self, team):
        print("UIManager throw current Team : " + team.teamName)
        thrower = team.getNextThrower()
        print("current thrower : " + thrower.playerID)

        input("press any to throw - "  + thrower.playerID + " : ")
        delta = random.randint(-1, 5)
        piece_num = input("press 1 ~ 3 to choose piece : ")
        piece = team.getPiece(piece_num)

        print("piece info UI ------------------- ")
        print("piece pos : " + piece.currentPosition + " : piece mode : " + str(piece.movingMode))
        return (delta, piece)

    def movePiece(self, piece, nextPosition):
        currentMode = piece.movingMode
        currentPosition = piece.currentPosition
        # currentPos -> nextPos로 움직임

    def selectDirection(self, piece):
        selection = input("1 - 일반 / 2 - 지름길")

        return True if selection == 2 else False

        #piece 밑에 방향 표시?