from enum import Enum

class MOVING_MODE(Enum):
    DEFAULT = 1
    FROM_RIGHT_CORNER = 2
    FROM_LEFT_CORNER = 3

class Piece:
    def __init__(self, entity, index):
        self.currentPosition = 0
        self.movingMode = MOVING_MODE.DEFAULT
        self.entity = entity
        self.index = index
        self.stackedList = []

    def __str__(self):
        strd = self.stackedList if self.stackedList != None else "False"
        return f"모드 : {self.movingMode} 위치 : {self.currentPosition} 인덱스 : {self.index} 스택 : {strd}"  