class Animal:

    def __init__(self):
        pass


    def make_noise(self, noise):
        print(noise)


class Mammal(Animal):

    def __init__(self):
        super().__init__()

class Bison(Mammal):

    def __init__(self):
        super().__init__()

class Reptile(Animal):

    def __init__(self):
        super().__init__()

class Snake(Reptile):

    def __init__(self, noise="Hssssssss"):
        super().__init__()
        self.noise = noise

    def make_noise(self):
        super().make_noise(self.noise)

    
def main():
    name = input("choose a name for your snake: ")
    snake = Snake()
    print(f'{name} says: ')
    snake.make_noise()

if __name__ == "__main__":
    main()