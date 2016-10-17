from secondclass import Person, Manager
bob = Person("bob Galloway", "Engineer", 3000)
ricky = Person("Ricky Martin", "Singer", 10000)
greg = Person("Greg Oden", "Basketball Player", 6000)
steve = Manager("Steve Jobs", 100000)

import shelve
db = shelve.open('persondb')
for object in (bob, ricky, greg, steve):
    db[object.name] = object
db.close()