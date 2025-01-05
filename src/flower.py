from color import Color
from color import func_get_flower_color
from enum import Enum




MENDELS_LAW = {
    (0, 0) : [4, 0, 0],
    (0, 1) : [2, 2, 0],
    (0, 2) : [0, 4, 0],
    (1, 0) : [2, 2, 0],
    (1, 1) : [1, 2, 1],
    (1, 2) : [0, 2, 2],
    (2, 0) : [0, 4, 0],
    (2, 1) : [0, 2, 2],
    (2, 2) : [0, 0, 4]
}

class FlowerType(Enum):
    ROSE = 0
    TULIP = 1
    HYASINTHS = 2
    ANEMONE = 3
    FANJI = 4
    MUM = 5
    COSMOS = 6
    LILY = 7

    def __int__(self):
        return self.value
    def __str__(self):
        return str(self.name)



class Flower:
    
    
    def __init__(self, flower_type:FlowerType, R:int, Y:int, W:int, S=0):
        self.R = R
        self.Y = Y
        self.W = W
        self.S = S
        self.flower_type = flower_type
        # self.id = 0
        # self.desc = ""
    
    def __str__(self):
        if self.flower_type == FlowerType.ROSE:
            return f"({self.R}{self.Y}{self.W}{self.S})"
        else:
            return f"({self.R}{self.Y}{self.W})"

def print_gene_result(gene_result:dict):
    for key, value in gene_result.items():
        print(f"{key}: {value:2d}  ",end="")
        if(key[-1] == 2) :
            print("")

def breed(f1:Flower, f2:Flower):
    R = MENDELS_LAW[(f1.R, f2.R)]
    Y = MENDELS_LAW[(f1.Y, f2.Y)]
    W = MENDELS_LAW[(f1.W, f2.W)]
    S = MENDELS_LAW[(f1.S, f2.S)]

    gene_result ={}
    color_gene_count = [0 for _ in range(len(Color))]
    color_result = [0 for _ in range(len(Color))]
    n = 4 if f1.flower_type == FlowerType.ROSE else 3

    get_flower_color = func_get_flower_color[int(f1.flower_type)]


    if n == 3:
        for r in range(3):
            for y in range(3):
                for w in range(3):
                    temp = R[r] * Y[y] * W[w]
                    gene_result[(r, y, w)] = temp
                    if(temp != 0) : 
                        color = int(get_flower_color(r,y,w))
                        if(color == int(Color.ERROR)):
                            print(f"\n error color: {(r,y,w)}\n")
                        color_gene_count[color] += temp
                        color_result[color] += 1
    else: # n==4
        
        for r in range(3):
            for y in range(3):
                for w in range(3):
                    for s in range(3):

                        temp = R[r] * Y[y] * W[w] * S[s]
                        gene_result[(r, y, w, s)] = temp
                        if(temp != 0) : 
                            color = int(get_flower_color(r,y,w,s))
                        if(color == int(Color.ERROR)):
                            print(f"\n error color: {(r,y,w,s)}\n")
                            color_gene_count[color] += temp
                            color_result[color] += 1
        
        pass
    
    print(f"{f1.flower_type} breeding result of {get_flower_color(f1.R, f1.Y, f1.W, f1.S)}{f1} X {f2}{get_flower_color(f2.R, f2.Y, f2.W, f2.S)}")
    print("=== GENE_RESULT ===")
    print_gene_result(gene_result)
    print("=== COLOR_RESULT ===")
    for c in range(len(Color)):
        if color_result[c] > 0:
            print(f"{Color(c):>7} = {color_result[c]:<2d} ({color_gene_count[c]/(4**n) * 100 :3.2f} %) ", end="")
            if color_result[c] == 1:
                print("   !SPECIAL!")
            else:
                print(" ")

                
    
    





