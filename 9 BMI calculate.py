# ProgTed

'''
       weight(kg)
BMI =----------------
      height(m) ** 2
'''

name = input('Please enter your name : ')

weight = input('Please enter your weight(kg) : ')  

weight = float(weight)

height = float(input('Please enter your height(m) : '))

BMI = weight / (height ** 2)

print(f"dear {name} ,your BMI is {round(BMI,3)}")


