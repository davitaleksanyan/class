class Animal:

    def __init__(self, eat, skin, sound, foots):
        self.eat = eat
        self.skin = skin
        self.sound = sound
        self.foots = foots
    def Eat(self):
        print(f"Animal diet {self.eat} \n")
    def Skin(self):
        print(f"Animal body {self.skin} per second\n")
    def AnimalsSound(self):
        print(f"Animal make sound {self.sound} \n")

class Sheep(Animal):
    def __init__(self, eat, pfur,skin, sound, foots):
        super().__init__(eat, skin, sound, foots)
        self.eat = eat
        self.pfur = pfur
    def Fur(self):
        if self.pfur >= 0.85:
            print('ԽՈՒԶԵԼ')
    def Eat(self):
        print(f"Սրանց կերակրել միայն մաքուր {self.eat} -ով\n")

class Duck(Animal):
    def __init__(self, eat, sound,skin, foots):
        super().__init__(eat, skin, sound, foots)
        self.sound = sound
        self.foots = foots
    def get_info(self):
        print(f"If you listen the sound {self.sound} then ruuuuuuuuuuuuuuuuun\n")

animal_Sheep = Sheep('grass', 0.90, 'fur', 'beeee', 4)
animal_Duck = Duck('hatik', 'kryak','bmbul', 2)
animal_Sheep.Fur()
print(animal_Sheep.eat)
print(animal_Duck.foots)
