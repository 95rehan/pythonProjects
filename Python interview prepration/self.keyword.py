class B:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name,self.age)


c = B("rehan",25)
c.info()

