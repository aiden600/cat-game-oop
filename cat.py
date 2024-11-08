class Cat:
    #the constructor will create a cat for us in code
    #to create a cat we need a given_name and given_colour
    def __init__(self, given_name,given_colour):
        self.name = given_name
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5

    def train(self):
        print(f"{self.name} is training..")
        self.intelligence += 1
        self.energy -= 5
    
    def feed(self):
        print(f"{self.name} is eating..")
        self.energy += 5
        self.weight += 1
    def play(self):
        print(f"{self.name} is playing..")
        self.energy -= 5
        self.weight -= 1
    def sleep(self):
        print(f"{self.name} is sleeping..")
        self.energy += 5
    def stats(self):
        print(f"Intelligence = {self.intellligence}, Energy = {self.energy}, Weight = {self.weight}")



