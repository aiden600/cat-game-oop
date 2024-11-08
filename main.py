class Cat:
    #the constructor will create a cat for us in code
    #to create a cat we need a given_name and given_colour
    def __init__(self, given_name,given_colour):
        self.name = given_name
        self.colour = given_colour
# an instance of cat, an instance is an occurence of a class
mimi = Cat("Mimi", "Brown")
        