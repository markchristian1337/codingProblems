# print("Hello World")
# Python Strings

# To comment out and uncomment
# multiple lines of code in Pycharm,
# highlight or place cursor anywhere
# on the lines of the text and hit ctrl + /

"""Python

    Strings"""
"""
x = "Hello, World"
y = "    hello world"

print(x[0:3])
print((y.strip()))
print(x.split(','))
print("Hello".upper())
print("shit"*100)

########################

x = -100

if x != 100 and x > 0:
    print("x is = ")
    print(x)

if x > 0:
    print("x is positive")
else:
    print("x is negative")

print("end")

name = input("Enter a name: ")

if name == "Max":
    print("Name entered is : ", name)
elif name == "Leo":
    print("Name entered is : ", name)
elif name == "Roy":
    print("Name entered is : ", name)
else:
    print("Name entered is invalid")
    
##########################################

x = 10
if x < 0:
    print("negative")
else:
    print("positive")
    if (x % 2) == 0:
        print("even")
    else:
        print("odd")

##########################
# Lists

x = [3, 5, 4, 9, 7, 10]
print(x)
print(x[0])
y = ['Max', 1, 15.5, [3, 2]]
print(y[3])
x.insert(2, 'tommy')
print(x)
x.remove('tommy')
print(x)
x.insert(2, 'tommy')
x.insert(2, 'tommy')
print(x)
x.remove('tommy')
print(x)
# remove will only remove one item starting with the one from the left
x.pop()
print(x)
z = [1,2,5,4]
z.sort()
print(z)
# reverse, append, copy, count
print(x)
x.reverse()
print(x)
x.append(3)
x.append(3)
x.remove('tommy')
print(x)
x.sort()
print(x.count(3))

# Tuples
# Tuples are like lists, but they are immutable - cannot be changed

x = (1, 5, 3, 4, 8)
print(x)
y = (1, 'max', 1.6)
# can concatenate tuples
z = x + y
print(z)
# can fill tuple with multiplication
a = ('hi',) * 5
print(a)
print(max(x))

#####################
# Set - unordered collection with no duplicate elements and no indexing

A = {1, 2, 5, 4, 7, 9, 2}
print(A)
print(len(A))
A.add(10)
print(A)
A.update([15, 18, 17, 14])
print(A)
A.discard(17)
print(A)
# discard and remove are similar but discard won't throw error with out of range value
A.pop()
# pop removes random element
print(A)
A.pop()
print(A)
name = {'max', 'tom', 'dan'}
name.clear()
print(name)
# set constructor
name = set(('alice', 'bob', 'eve'))
print(name)
print(name)
# convert list to set
Z = set([5, 3, 1, 2, 2, 3])
print(Z)
print(A)
B = {10, 11, 12, 13, 14, 16, 18}
print(B)
print(A | B)
print(A & B)
print(A.intersection(B))
print(A - B)
print(B - A)
print(A.difference(B))
# Symmetric difference - either in A but not B or vice versa
print(A ^ B)

##############
# Dictionary

# Dictionary - list of pairs

D = {'name': 'max', 'age': 14, 'year': 2004}

print(D)
print(D['name'])
print(D['age'])

E = {'name': 'Tom', 15: 15, 15.1: 15.1, True: True, (2,3): 5}
print(E[(2,3)])
print(E[True])
# print(E[100]) # error
print(len(E))
''' print(D.get('name').upper())
D['name'] = D.get('name').upper()
print((D['name']))
D['name'] = 'max'
print(D['name']) '''
D['Surname'] = 'Smith'
print(D)
D.pop('Surname')
print(D)
print(E)
E.clear()
print(E)
del E
# print(E)
D['name'] = 'Mark'
print(D)
D.update({'name': 'Christian'})
print(D)
print(D.keys())
print(D.values())
# popitem removes last item inserted
# D.popitem()
D.update({'name': 'max'})
D.popitem()
print(D)

#############################
# Slice and negative index

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
c = '0123456789'

x = a[0:5]
print(x)

print(a[:5])
print(a[3:])
print(c[0:5])
print(a[0:10:3])
print(c[-1])
print(a[::-1])
print(c[::-1])
print(a[3:1:-1])
print(a[-1:-4:-1])
print(a[-3::-1])

"""

##############################
# Loops

"""  

num = 1
sum = 0
print("Enter a number. Please enter zero(0) to exit.")
while num != 0:
    num = float(input())
    sum += num
    print("sum = ", sum)
else:
    print("Finished sum")

i = 1
while i <= 5:
    print("The value of i is: ", i)
    i += 1

A = [0,1,2,3,4,5]  # list
B = (0,1,2,3,4,5)  # tuple
C = {0,1,2,3,4,5}  # set
D = '012345'  # string
E = {
    "name": 'max',
    "age": 20
}

for x, y in E.items(): # keys(), values(), items()
    print(x, ' ', y)

for z in range(2,30,3):
    print(z)
else:
    print("Finished")

a = [0,1,2,3,4,5]
for x in a:
    if x == 3:
        break
    print(x)

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

"""

##############################
# Functions

"""
def student(name='unknown', age='unknown', **grades):
    # * for tuple, ** for dictionary
    print("Name: ", name)
    print("Age: ", age)
    # print("Grades: ", grades)
    for x,y in grades.items():
        print(x,y)
    # print("Grades: ",grades)


student()
student('Mark',28, English=90, Math=85,History=99,Science=100)

"""

##############################
# Classes
##############################

# if you pyt multiple init methods in class, it only recognizes last one

# to make data private, use __ in front

# encapsulation
# single _ makes data partially private, and it's only a convention

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
    def public_method(self):
        print(self.a)
        print(self.__c);
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')

hello = Hello('Name')
print(hello.a)
print(hello._b)
hello.public_method()
# print(hello.__c)



######################### Inheritance





















# Reverse and add integer problem. Given integer input, check first and last digits.
# If they are not equal, take reverse of integer and add together e.g. 123 + 321.
# Repeat until you come to a number in which the first and last digits are equal.
# Output the final integer, and the amount of additions needed to get the result.
#
# Examples:
#
# Input: 123
# Output: 444 1
#
# Input: 945
# Output: 11781 3
#
#
#
# def reverse(num):
#     return int(str(num)[::-1])
#
#
# def checkFirstLast(num):
#     return str(num)[0] == str(num)[-1]
#
#
# def reverseAdd(num, count=0  xz):
#     if checkFirstLast(num):
#         print(num, " ", count)
#     else:
#         num += reverse(num)
#         count += 1
#         reverseAdd(num, count)
#
#
# a = int(input("Enter number: "))
#
# reverseAdd(a)



"""

num = input("Enter number: ")
count = 0
def checkFirstLast
def reverseandadd(num):
    if num[0] == num[-1]:
        print(num)
        # print(count)
    elif num[0] != num[-1]:
        print("Not palindrome")
        rev = int(num[::-1])
        num = int(num)
        print(rev)
        print(num)
        sumOf = num + rev
        # count += 1
        print(sumOf)
        print(count)
        num = sumOf
        reverseandadd(num)
"""