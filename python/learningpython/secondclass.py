# Second  Python Class
from classtools import AttrDisplay

class Person(AttrDisplay):
    # Initialize the __init__ constructor
    def __init__(self, name, job  = None, pay = 0):
        # this __init__ takes 3 arguements
        self.name = name
        self.job = job
        self.pay = pay
        # These attributes will be initialized when you call on this class to define an instance!
    def GiveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def lastName(self):
        return self.name.split()[-1]
    # Omitted this overloading of string as I've inserted a more general way of implementing the printing
# New SubClass: Manager

class Manager(Person):
    # a Manager is almost like a Person although he customizes some of Person's features/ attributes
    def __init__(self, name, pay):  # Modify the already defined __init_ constructor
        Person.__init__(self, name, "manager", pay)
    def GiveRaise(self, percent, bonus = 0.10): # Modify the inherited function
        # NOT LIKE THIS, increases time mentainance
        #self.pay = int(self.pay * (1 + percent + bonus))
        # DO IT LIKE THIS!!
        Person.GiveRaise(self, percent + bonus)