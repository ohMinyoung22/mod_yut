from enum import Enum
from team import Team

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