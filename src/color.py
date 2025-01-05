
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
    ERROR = 10
    
    def __int__(self):
        return self.value
    def __str__(self):
        return str(self.name)

# LILY[r][y][w]
ROSE = [[[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)] for s in range(3)]
TULIP = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
HYASINTHS = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
ANEMONE = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
FANJI = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
MUM = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
COSMOS = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
LILY = [[[ Color.ERROR for w in range(3)] for y in range(3)] for r in range(3)]
def init_rose_color():
    
    ROSE[1][0][0][0] = Color.RED
    ROSE[1][0][1][0] = Color.RED
    ROSE[1][0][2][0] = Color.RED
    ROSE[1][1][1][0] = Color.RED
    ROSE[1][1][2][0] = Color.RED
    ROSE[1][2][2][0] = Color.RED
    ROSE[2][0][0][1] = Color.RED
    ROSE[2][0][1][1] = Color.RED
    ROSE[2][0][2][1] = Color.RED
    ROSE[2][1][1][0] = Color.RED
    ROSE[2][1][1][1] = Color.RED
    ROSE[2][1][2][1] = Color.RED
    ROSE[2][2][2][1] = Color.RED
    
    ROSE[1][1][0][0] = Color.ORANGE
    ROSE[1][2][0][0] = Color.ORANGE
    ROSE[1][2][1][0] = Color.ORANGE
    ROSE[2][1][0][0] = Color.ORANGE
    ROSE[2][1][0][1] = Color.ORANGE
    ROSE[2][2][0][0] = Color.ORANGE
    ROSE[2][2][0][1] = Color.ORANGE
    ROSE[2][2][1][0] = Color.ORANGE
    ROSE[2][2][1][1] = Color.ORANGE
    
    ROSE[1][1][0][1] = Color.YELLOW
    ROSE[1][1][0][2] = Color.YELLOW
    ROSE[1][2][0][1] = Color.YELLOW
    ROSE[1][2][0][2] = Color.YELLOW
    ROSE[1][2][1][1] = Color.YELLOW
    ROSE[1][2][1][2] = Color.YELLOW
    ROSE[2][1][0][2] = Color.YELLOW
    ROSE[2][2][0][2] = Color.YELLOW
    ROSE[2][2][1][2] = Color.YELLOW
    ROSE[0][1][0][0] = Color.YELLOW
    ROSE[0][1][0][1] = Color.YELLOW
    ROSE[0][1][0][2] = Color.YELLOW
    ROSE[0][2][0][0] = Color.YELLOW
    ROSE[0][2][0][1] = Color.YELLOW
    ROSE[0][2][0][2] = Color.YELLOW
    ROSE[0][2][1][0] = Color.YELLOW
    ROSE[0][2][1][1] = Color.YELLOW
    ROSE[0][2][1][2] = Color.YELLOW
    
    ROSE[2][2][2][0] = Color.BLUE
    
    ROSE[1][0][2][2] = Color.PURPLE
    ROSE[1][1][2][2] = Color.PURPLE
    ROSE[2][1][2][2] = Color.PURPLE
    ROSE[0][1][2][2] = Color.PURPLE
    ROSE[0][1][2][1] = Color.PURPLE
    ROSE[0][0][2][0] = Color.PURPLE
    ROSE[0][0][2][1] = Color.PURPLE
    ROSE[0][1][2][0] = Color.PURPLE
    ROSE[0][0][2][2] = Color.PURPLE
    
    ROSE[1][0][0][1] = Color.PINK
    ROSE[1][0][1][1] = Color.PINK
    ROSE[1][0][2][1] = Color.PINK
    ROSE[1][1][1][1] = Color.PINK
    ROSE[1][1][2][1] = Color.PINK
    ROSE[1][2][2][1] = Color.PINK
    ROSE[2][0][0][2] = Color.PINK
    ROSE[2][0][1][2] = Color.PINK
    ROSE[2][0][2][2] = Color.PINK
    
    ROSE[2][0][0][0] = Color.BLACK
    ROSE[2][0][1][0] = Color.BLACK
    ROSE[2][0][2][0] = Color.BLACK
    ROSE[2][1][2][0] = Color.BLACK
    
    ROSE[1][0][0][2] = Color.WHITE
    ROSE[1][0][1][2] = Color.WHITE
    ROSE[1][1][1][2] = Color.WHITE
    ROSE[1][2][2][2] = Color.WHITE
    ROSE[2][1][1][2] = Color.WHITE
    ROSE[2][2][2][2] = Color.WHITE
    ROSE[0][0][0][1] = Color.WHITE
    ROSE[0][0][1][1] = Color.WHITE
    ROSE[0][1][1][0] = Color.WHITE
    ROSE[0][1][1][1] = Color.WHITE
    ROSE[0][1][1][2] = Color.WHITE
    ROSE[0][2][2][0] = Color.WHITE
    ROSE[0][2][2][1] = Color.WHITE
    ROSE[0][0][1][2] = Color.WHITE
    ROSE[0][0][0][2] = Color.WHITE
    ROSE[0][0][1][0] = Color.WHITE
    ROSE[0][0][0][0] = Color.WHITE
    ROSE[0][2][2][2] = Color.WHITE
 

def init_tulip_color():
    TULIP[1][0][0] = Color.RED
    TULIP[2][0][1] = Color.RED
    TULIP[2][0][2] = Color.RED
    TULIP[2][1][1] = Color.RED
    TULIP[2][1][2] = Color.RED

    TULIP[1][1][0] = Color.ORANGE
    TULIP[1][2][0] = Color.ORANGE
    
    TULIP[1][1][1] = Color.YELLOW
    TULIP[1][1][2] = Color.YELLOW
    TULIP[1][2][1] = Color.YELLOW
    TULIP[1][2][2] = Color.YELLOW
    TULIP[0][1][0] = Color.YELLOW
    TULIP[0][1][1] = Color.YELLOW
    TULIP[0][2][1] = Color.YELLOW
    TULIP[0][2][2] = Color.YELLOW
    TULIP[0][2][0] = Color.YELLOW

    TULIP[2][2][0] = Color.PURPLE
    TULIP[2][2][1] = Color.PURPLE
    TULIP[2][2][2] = Color.PURPLE
    
    TULIP[1][0][1] = Color.PINK

    TULIP[2][0][0] = Color.BLACK
    TULIP[2][1][0] = Color.BLACK

    TULIP[1][0][2] = Color.WHITE
    TULIP[0][0][1] = Color.WHITE
    TULIP[0][1][2] = Color.WHITE
    TULIP[0][0][0] = Color.WHITE
    TULIP[0][0][2] = Color.WHITE

def init_hyasinths_color():

    HYASINTHS[1][0][0] = Color.RED
    HYASINTHS[2][0][0] = Color.RED
    HYASINTHS[2][0][1] = Color.RED
    HYASINTHS[2][0][2] = Color.RED
    HYASINTHS[2][1][1] = Color.RED
    HYASINTHS[2][1][2] = Color.RED

    HYASINTHS[1][1][0] = Color.ORANGE
    HYASINTHS[1][2][0] = Color.ORANGE

    HYASINTHS[1][1][1] = Color.YELLOW
    HYASINTHS[1][1][2] = Color.YELLOW
    HYASINTHS[1][2][1] = Color.YELLOW
    HYASINTHS[1][2][2] = Color.YELLOW
    HYASINTHS[0][2][1] = Color.YELLOW
    HYASINTHS[0][2][0] = Color.YELLOW
    HYASINTHS[0][2][2] = Color.YELLOW
    HYASINTHS[0][1][1] = Color.YELLOW
    HYASINTHS[0][1][0] = Color.YELLOW

    HYASINTHS[2][1][0] = Color.BLUE
    HYASINTHS[0][0][2] = Color.BLUE

    HYASINTHS[2][2][0] = Color.PURPLE
    HYASINTHS[2][2][1] = Color.PURPLE
    HYASINTHS[2][2][2] = Color.PURPLE

    HYASINTHS[1][0][1] = Color.PINK

    HYASINTHS[1][0][2] = Color.WHITE
    HYASINTHS[0][1][2] = Color.WHITE
    HYASINTHS[0][0][0] = Color.WHITE
    HYASINTHS[0][0][1] = Color.WHITE

def init_anemone_color():
    
    ANEMONE[1][0][0] = Color.RED
    ANEMONE[1][0][1] = Color.RED
    ANEMONE[2][0][0] = Color.RED
    ANEMONE[2][0][1] = Color.RED
    ANEMONE[2][1][0] = Color.RED
    ANEMONE[2][1][1] = Color.RED

    ANEMONE[1][2][0] = Color.ORANGE
    ANEMONE[1][2][1] = Color.ORANGE
    ANEMONE[1][2][2] = Color.ORANGE
    ANEMONE[0][1][0] = Color.ORANGE
    ANEMONE[0][1][1] = Color.ORANGE
    ANEMONE[0][2][0] = Color.ORANGE
    ANEMONE[0][2][1] = Color.ORANGE
    ANEMONE[0][2][2] = Color.ORANGE

    ANEMONE[1][0][2] = Color.BLUE
    ANEMONE[0][0][2] = Color.BLUE
    ANEMONE[0][1][2] = Color.BLUE

    ANEMONE[2][0][2] = Color.PURPLE
    ANEMONE[2][1][2] = Color.PURPLE
    ANEMONE[2][2][2] = Color.PURPLE

    ANEMONE[1][1][0] = Color.PINK
    ANEMONE[1][1][1] = Color.PINK
    ANEMONE[1][1][2] = Color.PINK
    ANEMONE[2][2][0] = Color.PINK
    ANEMONE[2][2][1] = Color.PINK

    ANEMONE[0][0][0] = Color.WHITE
    ANEMONE[0][0][1] = Color.WHITE

def init_fanji_color():
    
    FANJI[1][0][0] = Color.RED
    FANJI[1][0][1] = Color.RED
    FANJI[2][0][0] = Color.RED
    FANJI[2][0][1] = Color.RED
    FANJI[2][1][0] = Color.RED
    FANJI[2][1][1] = Color.RED
    
    FANJI[1][1][0] = Color.HYBRID
    FANJI[1][1][1] = Color.HYBRID
    FANJI[1][1][2] = Color.HYBRID
    FANJI[2][2][0] = Color.HYBRID
    FANJI[2][2][1] = Color.HYBRID
    
    FANJI[1][2][0] = Color.YELLOW
    FANJI[1][2][1] = Color.YELLOW
    FANJI[1][2][2] = Color.YELLOW
    FANJI[0][2][1] = Color.YELLOW
    FANJI[0][1][1] = Color.YELLOW
    FANJI[0][1][0] = Color.YELLOW
    FANJI[0][2][2] = Color.YELLOW
    FANJI[0][2][0] = Color.YELLOW
    
    FANJI[1][0][2] = Color.BLUE
    FANJI[0][1][2] = Color.BLUE
    FANJI[0][0][2] = Color.BLUE
    
    FANJI[2][0][2] = Color.PURPLE
    FANJI[2][1][2] = Color.PURPLE
    FANJI[2][2][2] = Color.PURPLE
    
    FANJI[0][0][1] = Color.WHITE
    FANJI[0][0][0] = Color.WHITE

def init_mum_color():
    MUM[1][1][1] = Color.RED
    MUM[2][0][0] = Color.RED
    MUM[2][0][1] = Color.RED
    MUM[2][0][2] = Color.RED
    MUM[2][1][2] = Color.RED
    MUM[2][2][2] = Color.RED
    
    MUM[1][1][0] = Color.YELLOW
    MUM[0][1][0] = Color.YELLOW
    MUM[0][1][1] = Color.YELLOW
    MUM[0][2][1] = Color.YELLOW
    MUM[0][2][0] = Color.YELLOW
    MUM[0][2][2] = Color.YELLOW
    
    MUM[2][2][0] = Color.GREEN
    MUM[2][2][1] = Color.GREEN
    
    MUM[1][2][0] = Color.PURPLE
    MUM[1][2][1] = Color.PURPLE
    MUM[1][2][2] = Color.PURPLE
    MUM[2][1][0] = Color.PURPLE
    MUM[2][1][1] = Color.PURPLE
    MUM[0][0][2] = Color.PURPLE
    
    MUM[1][0][0] = Color.PINK
    MUM[1][0][1] = Color.PINK
    MUM[1][0][2] = Color.PINK
    MUM[1][1][2] = Color.PINK
    
    MUM[0][0][1] = Color.WHITE
    MUM[0][0][0] = Color.WHITE
    MUM[0][1][2] = Color.WHITE

def init_cosmos_color():
    
    COSMOS[2][0][0] = Color.RED
    COSMOS[2][0][1] = Color.RED
    COSMOS[2][0][2] = Color.RED
    COSMOS[2][1][2] = Color.RED
    COSMOS[2][2][2] = Color.RED
    
    COSMOS[1][1][0] = Color.ORANGE
    COSMOS[1][1][1] = Color.ORANGE
    COSMOS[1][2][0] = Color.ORANGE
    COSMOS[1][2][1] = Color.ORANGE
    COSMOS[1][2][2] = Color.ORANGE
    COSMOS[2][1][0] = Color.ORANGE
    COSMOS[2][1][1] = Color.ORANGE
    
    COSMOS[0][1][1] = Color.YELLOW
    COSMOS[0][1][0] = Color.YELLOW
    COSMOS[0][2][1] = Color.YELLOW
    COSMOS[0][2][2] = Color.YELLOW
    COSMOS[0][2][0] = Color.YELLOW
    
    COSMOS[1][0][0] = Color.PINK
    COSMOS[1][0][1] = Color.PINK
    COSMOS[1][0][2] = Color.PINK
    COSMOS[1][1][2] = Color.PINK
    
    COSMOS[2][2][0] = Color.BLACK
    COSMOS[2][2][1] = Color.BLACK
    
    COSMOS[0][0][0] = Color.WHITE
    COSMOS[0][0][1] = Color.WHITE
    COSMOS[0][0][2] = Color.WHITE
    COSMOS[0][1][2] = Color.   WHITE

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
    init_rose_color()
    init_tulip_color()
    init_hyasinths_color()
    init_anemone_color()
    init_fanji_color()
    init_mum_color()
    init_cosmos_color()
    init_lily_color()
    
def get_rose_color(r:int, y:int, w:int, s = 0):
    return  ROSE[r][y][w][s] 

def get_tulip_color(r:int, y:int, w:int, s = 0):
    return TULIP[r][y][w]

def get_hyasinths_color(r:int, y:int, w:int, s = 0):
    return  HYASINTHS[r][y][w] 

def get_anemone_color(r:int, y:int, w:int, s = 0):
    return  ANEMONE[r][y][w] 

def get_fanji_color(r:int, y:int, w:int, s = 0):
    return  FANJI[r][y][w] 

def get_mum_color(r:int, y:int, w:int, s = 0):
    return  MUM[r][y][w] 

def get_cosmos_color(r:int, y:int, w:int, s = 0):
    return  COSMOS[r][y][w] 

def get_lily_color(r:int, y:int, w: int, s = 0):
    return LILY[r][y][w]


func_get_flower_color=[
    get_rose_color,
    get_tulip_color,
    get_hyasinths_color,
    get_anemone_color,
    get_fanji_color,
    get_mum_color,
    get_cosmos_color,
    get_lily_color,
        
]
