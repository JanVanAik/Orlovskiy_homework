from random import choice
class Car:
    def __init__(self, speed, color, name, ispolice = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = ispolice


    def go(self):
        print(f'Move on, {self.color} {self.name}')
    def stop(self):
        if not self.ispolice:
            print('Stop, you are not a policeman')
        else:
            print("Keep going, if you want, Lietnaunt")
    def turn(self):
        positions = ["left", "right", "to hell"]
        side = choice(positions)
        print(f"You are going {side} now")
    def ShowSpeed(self):
        print(self.speed)

class TownCar(Car):
    def ShowSpeed(self):
        print(self.speed)
        if self.speed > 60:
            print("Slow down, your speed is over the limit!")
class SportCar(Car):
    def ShowSpeed(self):
        print(self.speed)
        if self.speed < 120:
            print("You are out, mr.Turtle")
class WorkCar(Car):
    def ShowSpeed(self):
        print(self.speed)
        if self.speed > 40:
            print("Slow down, your speed is over the limit!")
class PoliceCar(Car):
    pass

base = Car(100, "green", 'Lexus')
town = TownCar(100, "yellow", 'Lada')
sport = SportCar(109, "red", 'Koenigsegg')
work = WorkCar(41, "brown", 'Mazda')
police = PoliceCar(100, "ugly", 'Musorovoz', True)

base.go()
town.ShowSpeed()
sport.ShowSpeed()
work.turn()
police.stop()
print(police.name)