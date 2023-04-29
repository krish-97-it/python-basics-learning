
#* This module consists functions to convert temperature
"""Fahrenheit to Centrigrade"""

def f_to_centrigrade(f):
    return 5*(f-32)/9.0

def c_to_fahrenheit(c):
    return (c*9/5.0)+32

def k_to_fahrenheit(k):
    return ((k-273.15)*9/5) + 32

def f_to_kelvin(f):
    return ((f-32)*5/9) + 273.15

def temperature_calculation():
    print("List of operations:-")
    print("1 - c to f")
    print("2 - f to c")
    print("3 - k to f")
    print("4 - f to k")
    n = int(input("Please enter your choice: "))
    input_temp = float(input("Enter the temperature: "))


    if n == 1:
        result = c_to_fahrenheit(input_temp)
        print("result= ",result)
    elif n == 2:
        result = f_to_centrigrade(input_temp)
        print("result= ",result)
    elif n == 3:
        result = k_to_fahrenheit(input_temp)
        print("result= ",result)
    elif n == 4:
        result = f_to_kelvin(input_temp)
        print("result= ",result)
