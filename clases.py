
class point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")
point=point()
point.move()
point.draw()



class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hii,I'M {self.name}")
john=Person('renu')
john.talk()
bob=Person('bob')
bob.talk()