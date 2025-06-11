class Vehicle:

    def __init__(self):
        pass

    def get_name(self, name):
        print(f"My name is{name}")

    
class Car:

    def __init__(self, name = "car"):
        super().__init__()
        self.name = name

    def get_name(self):
        super.get_name(self, self.name)



    