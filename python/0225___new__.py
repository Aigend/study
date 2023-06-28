from ast import arg


class father:

    def __new__(cls,*args):
        print("**",args)
        return super(father, cls).__new__(cls)
    
    def __init__(self, name) -> None:
        print("******")
        

class son(father):

    def __new__(cls,*args):
        print("##", args)
        return super(son, cls).__new__(cls)


    def __init__(self, name) -> None:
        print("####")
        super().__init__(name)


p = son("zhans")

for i in range(3):
    print(i, "**")

print(i)

class MyNumber:

    def __iter__(self):
        print("##")
        self.a = 1
        return self

    
    def __next__(self):
        if self.a <= 10:
            x= self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
obj = MyNumber()
for x in obj:
    print(x)
