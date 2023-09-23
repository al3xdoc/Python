class P1:
    def __init__(self):
        self.legs = 2

    def method1(self):

        print("Parents 1 method")

class P2:
    def method2(self):
        print("Parent's 2 method")

class Child(P1, P2):
    def __init__(self, legs):
        P1.__init__(self.legs)
    def method3(self):
        print("Child's method")

child = Child()

child.method3()
child.method1()
child.legs = 2
print(child.legs)