class Vehicle:
    wheels = "4"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "My %s %s is a %d model year" % (self.make, self.model, self.year)
        
rex = Vehicle("Mazda", "CX5", 2015)  
print(rex)

