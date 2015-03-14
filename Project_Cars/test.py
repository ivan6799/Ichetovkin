class Car:
    def __init__(self, speed):
        self.speed = speed

    def __lt__(self, other):
        if other.speed > self.speed:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.speed < self.speed:
            return True
        else:
            return False

car1 = Car(12)
car2 = Car(48)

print(car1 > car2)

car1 > car2

car1.__gt__(car2)