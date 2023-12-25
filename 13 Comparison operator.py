# progTed

# Comparison Operators -> == | != | < | > | <= | >=

# Comparison Operators return Blooean Type : True | False

number1 = float(input('Please enter number 1 :'))
number2 = float(input('Please enter number 2 :'))

# == -> return true if the values of number1 and number2 is equal
print(f"{number1} == {number2} : {number1 == number2}")

# != -> return true if the values of number1 and number2 is not equal
print(f"{number1} != {number2} : {number1 != number2}")

# < -> return true if the values of number1 lesster than number2
print(f"{number1} < {number2} : {number1 < number2}")

# > -> return true if the values of number1 lesster than number2
print(f"{number1} > {number2} : {number1 > number2}")

# <= -> return true if < or ==
print(f"{number1} <= {number2} : {number1 <= number2}")

# >= -> return true if > or ==
print(f"{number1} >= {number2} : {number1 >= number2}")


print('------------------------------------')

age = int(input('Please enter your age :'))

if age >= 18:
    print('You can watch this movie')
else:
    print('Boro Bache joon')