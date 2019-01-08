'''
    logging in python
'''
#display in console

import logging
#logging.basicConfig(level=logging.DEBUG)
l = logging
l1 = logging

l1.basicConfig(filename = "test.log",level = logging.CRITICAL,format = "{asctime} : {message}")
l.basicConfig(level = logging.DEBUG)


class Pizza:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        l1.debug("Pizza created : {} ${}".format(self.name,self.price))
        l.debug("Pizza created : {} ${}".format(self.name,self.price))


    def make (self,quantity):
        l1.debug(" Made {} pizza".format(quantity))

    def eat(self,quantity=1):
        l.debug("Ate {} pizza {} ".format(quantity,self.name))

pizza01 = Pizza("italian",100)
pizza01.make(2)
pizza01.eat(2)



pizza01 = Pizza("Indian",100)
pizza01.make(5)
pizza01.eat(3)


#log to file
