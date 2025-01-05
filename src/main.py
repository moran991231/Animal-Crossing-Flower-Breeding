from flower import Flower, FlowerType, breed
from color import init_flower_color_tb
def main():

    init_flower_color_tb()

    f1 = Flower(FlowerType.ROSE, 1,1,1,1)
    f2 = Flower(FlowerType.ROSE, 1,1,1,1)
    
    breed(f1, f2)
    pass


if __name__ == "__main__":
    main()
