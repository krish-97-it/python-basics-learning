# A library is a collection of module.
# EX - 
    # Pandas - This library is used for structured data operations, like import CSV files, create dataframes, and data preparation.
# Numpy - This is a mathematical library. ...
    # Matplotlib - This library is used for visualization of data.
    # SciPy - This library has linear algebra modules.
# A module is a program or set of functions that perform a same category of functionalities. 
# It contains code bundles that can be reused in a variety of programs.


# ** There are two modules one is temp_converter and another is calculator. We import these two modules to use inside code of it.

import temp_converter       # using import keyword we can use a module in another module
import calculator
# from calculator import do_calculation     # we can import specific function or variable from a module 
# from calculator import *      # entire module we can import like that

print("List of operations:-")
print("1 - Temperature Converter")
print("2 - calculator")

n = int(input("Please enter your choice: "))

if n == 1:
    # to call a variable or specific funcgtion of a module - modulename.function/varriable name
    temp_converter.temperature_calculation()

elif n == 2:
    calculator.do_calculation()
    # do_calculation()      # in case we only import do_calculation() particularly then we can call this function directly like that
