class Demo:
    image = None

    def __init__(self):
        print(self.image)
        if not self.image:
            Demo.image = 'picture'

obj1 = Demo()
obj2 = Demo()
obj3 = Demo()



