
class Parent:
    parentAttr = 100

    def __init__(self):
        print 'a parent object'

    def commonM(self):
        print 'parent method ovveride'

    def getAttr(self):
        print 'parent attribute %d' % Parent.parentAttr

    def setAttr(self, attr):
        Parent.parentAttr = attr


class Parent2:
    parentA = 100

    def __init__(self):
        print 'a parent2 object'

    def getA(self):
        print 'parent2 attribute %d' % Parent2.parentA

    def setA(self, attr):
        Parent2.parentA = attr


class Child(Parent, Parent2):
    __demo = 10
    demo = 100

    def count(self):
        self.__demo += 1
        print self.__demo

    def getP(self):
        return  self.__demo+1

    def __init__(self):
        print 'child object inital'

    def commonM(self):
        print 'child method override'


ch = Child()
ch.setAttr(1000)
ch.getA()
ch.commonM()
ch.count()
ch.demo
#ch._demo
print ch._Child__demo
print ch.getP()

