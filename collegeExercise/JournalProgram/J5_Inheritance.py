'''
    5.Write a program for Inheritance.(Use __init__)
'''
class Parent:
    parentAttr = 0
    def __index__(self):
        print('Parent Constructor')

    def parentMethod(self):
        print('calling Parent Method')

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent Atribute :',Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print('Calling Child Constructor')

    def childMethod(self):
        print('Calling Child Method')

c1 = Child(Parent)
c1.parentMethod()
