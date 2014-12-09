class Test:
    def __init__(self,type):
        self.type = type
    def __len__(self):
        return 150
a = Test("ass")
print(len(a))