class Mammal:
    def __init__ (self, name, type_of_mammal, breed, legs):
        self.name = name
        self.type_of_mammal = type_of_mamal
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "%s is eating" % (self.name)

class Cat(Mammal):
    def__init__(self, type_of_mammal, breed, legs)
    super().__init__(type_of_mammal, breed, legs)
    self.fur = fur

    def__str__(self):
    return "%s is a %s %s with %d legs and %s fur" %

    def eat(self):
        return "THE CAT EATS DIFFRENTLY FOR REASONS!!!"

guster = Cat
harry = Mammal
print(guster.eat()

)        