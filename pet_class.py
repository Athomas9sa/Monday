class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

        #...
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()
                  
        #...
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)  

class Treat:(self, ColdPizza, Bacon, VeganSnack)
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.ColdPizza = ColdPizza
        self.Bacon = Bacon
        self.VeganSnack = VeganSnack
    # SHOULD HAVE EFFECT ON FULLNESS AND HAPPINESS, BUT HOE TO DO?

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
    
    def be_alive(self):
        super().__be_alive__(name, fullness, 100, hunger, 1)
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        
    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()
            from pet import Pet, CuddlyPet

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        ExtraCuddly: %d
        """ % (self.name, self.fullness, self.happiness, self.extrecuddly) 

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Do nothing",
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

    def choices_to_string(choice_list):
        choice_string = ""
        num = 1
        for choice in choice_list:
            choice_string += "%d: %s\n" % (num, choice)
            num += 1
            choice_string += "Please choose an option: "
        return choice_string

    def get_user_choice(choice_list):
        choice = -1
        choice_string = choices_to_string(choice_list)
        while choice == -1:
            try:
                choice = int(input(choice_string))
                if choice <= 0 or choice > len(choice_list):
                    raise ValueError
            except ValueError:
                print_menu_error()
            return choice

    def main():    
        while True:
            choice = get_user_choice(main_menu)

CuddlyPet = Pet
print(CuddlyPet)


