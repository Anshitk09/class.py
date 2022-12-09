class one:
    x=20
    def fun1(self):
        print(self.x)
class two:
    y=200
    def fun2(self):
        print(self.y)
class three(one,two):
    z=150
    def fun3(self):
        print(one.x+two.y+self.z)
t1=three()
t1.fun1()
t1.fun2()
t1.fun3()
