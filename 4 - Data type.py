# Data Types in Python

age = 21 # <class 'int'>
height = 1.85 # <class 'float'>  . => float point
complexNumber = 5j # <class 'complex'>

# type( variable )

print(type(age))
print(type(height))
print(type(complexNumber))

print('----------------------')

name = 'Mohammad'
family = "Hossein"

print(type(name))
print(type(family))

print('----------------------')

partOfCourse = ['intro' , 'Install' , 'Variable' , 'Data Type' , 'intro' , 2002]
print(partOfCourse)
print(type(partOfCourse))

print('----------------------')

partOfCourse = ('intro' , 'Install' , 'Variable' , 'Data Type' , 'intro' , 2002)
print(partOfCourse)
print(type(partOfCourse))

print('----------------------')

partOfCourse = {'intro' , 'Install' , 'Variable' , 'Data Type' , 'intro' , 2002}
print(partOfCourse)
print(type(partOfCourse))

print('-------------------------')

CountryCode = {
    "Iran" : 98 , 
    'USA' : 1
}

print(CountryCode)
print(type(CountryCode))

print('-----------------------')

# Boolian

print(20 > 30)
print(2 < 10)
print('Mohammad' > 'Ali')

print('-----------------------')

#myNumber = range(10)
#for i in myNumber:
#    print(i)

numberOfChild = None
print(numberOfChild)
print(type(numberOfChild))

print('-----------------------')

# Dynamic Type Like python

x = 1000
x = 'Mohammad'
print(x) # Mohammad

# Static Type Like C#

# int x = 1000
# x = 'Mohammad'
# print(x) # Syntax Error