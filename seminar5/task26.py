"""
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
"""


def degree_of_number(number, degree, result=1.0):
    if degree == 0:
        return result
    elif degree > 0:
        result = result * number
        return degree_of_number(number, degree - 1, result)
    elif degree < 0:
        result = result / number
        return degree_of_number(number, degree + 1, result)


try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("It's not a number!")
else:
    try:
        input_degree = int(input("Enter degree: "))
    except ValueError:
        print("It's not a number!")
    else:
        print("Answer: ", degree_of_number(input_number, input_degree))
