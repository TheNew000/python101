# print "Danny Arango"
#Arrays are called "Lists" in python
animals = ['wolf', 'giraffe', 'hippo']
# print animals
# print animals[0]
# print animals[-1]

# How do we push to the list?

# animals.push('Dog') In Python:
animals.append('dog')
# print animals

# Instead of delete:
animals.remove('wolf')
# print animals

# animals.prepend('wolf')
# We can insert at any postion with .insert
animals.insert(0, 'zebra')
animals.insert(1, 'dog')
# del animals[0]

# Pop is the same syntax
# print animals

dc_class = ['Summer', 'Jackson', 'Danny', 'Dave', 'JT', 'Eric', 'Paige', 'Brett', 'Danielle', 'Alex', 'Shirlette', 'Dan']
# will sort but not change array
# print sorted(dc_class)
# will sort AND change array
# dc_class.sort()
# will reverse and change the list by index
# dc_class.reverse()
# print dc_class
# len method will work like .length in jS
# print len(dc_class)

# Indentation matters to Python!!!
for student in dc_class:
    print student

for i in range(1, 10):
    print i

for i in range(1, len(dc_class)):
    print i

# in python a function is called def NOT function
def sayHello():
    print "hello, world"

sayHello()

def say_hello_with_name(name):
    print "hello, " + name

say_hello_with_name('Danny')
