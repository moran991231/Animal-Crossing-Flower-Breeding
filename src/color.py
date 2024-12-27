
from enum import Enum

class Color(Enum) :
    RED = 0
    ORANGE = 1
    YELLOW = 2
    BLUE = 3
    PURPLE = 4
    PINK = 5
    BLACK = 6
    WHITE = 7
    HYBRID = 8
    GREEN = 9
    
    def __int__(self):
        return self.value
    def __str__(self):
        return str(self.name)

# LILY[r][y][w]
LILY = [[[ 0 for w in range(3)] for y in range(3)] for r in range(3)]

def init_lily_color():
    LILY[1][0][0] = Color.RED
    LILY[2][0][1] = Color.RED
    LILY[2][1][1] = Color.RED

    LILY[1][1][0] = Color.ORANGE
    LILY[1][2][0] = Color.ORANGE
    LILY[2][2][0] = Color.ORANGE
    LILY[2][2][1] = Color.ORANGE

    
    LILY[1][1][1] = Color.YELLOW
    LILY[1][1][2] = Color.YELLOW
    LILY[1][2][1] = Color.YELLOW
    LILY[1][2][2] = Color.YELLOW
    LILY[0][2][1] = Color.YELLOW
    LILY[0][1][0] = Color.YELLOW
    LILY[0][2][0] = Color.YELLOW

    
    LILY[1][0][1] = Color.PINK
    LILY[2][0][2] = Color.PINK
    LILY[2][1][2] = Color.PINK

    LILY[2][0][0] = Color.BLACK
    LILY[2][1][0] = Color.BLACK

    LILY[1][0][2] = Color.WHITE
    LILY[2][2][2] = Color.WHITE
    LILY[0][1][2] = Color.WHITE
    LILY[0][2][2] = Color.WHITE
    LILY[0][1][1] = Color.WHITE
    LILY[0][0][1] = Color.WHITE
    LILY[0][0][0] = Color.WHITE
    LILY[0][0][2] = Color.WHITE
    
    pass

def init_flower_color_tb():
    init_lily_color()
    

def get_lily_color(r:int, y:int, w: int, s = 0):
    return LILY[r][y][w]

func_get_flower_color=[
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    get_lily_color,
    
]
