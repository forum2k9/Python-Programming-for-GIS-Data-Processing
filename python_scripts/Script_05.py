# Script_05.py
# Author: UmarYusuf.com
# Date: 30/05/2022
# Topic: Functions
# ------------------------------

# A function is a block of code which only runs when it is called.
# They allow you to give a name to a block of statements, allowing you to run that block using
# the specified name anywhere in your program and any number of times.

# Basically, we can divide functions into the following two types:
#~1. Built-in functions - Functions that are built into Python.

# Built-in functions we have used... type(), dir(), help(), print(), open(), len(), etc
# https://docs.python.org/3/library/functions.html
# Use locals() and globals() functions to see the current local and global data structure created 
# (aka 'Symbol table') your python compiler using. Symbol table is the data structure maintained by the 
# compiler which contains all necessary information about the program. These information include
# variable, methods, classes etc.
local_data = locals()
type(local_data)
local_data.keys()
local_data['__builtins__']
local_data['__builtins__'].keys()




#~2. User-defined functions - Functions defined by the users themselves.

# Defining and calling simple functions
# Syntax of Function
# ----------------------------------
def function_name():
	"""docstring"""
	print ('something...')

function_name()

# Parameter is the variable listed inside the parentheses in the function definition.
# Argument is the value that are sent to the function when it is called.
# Types of arguments:-
    # Default arguments
    # Required arguments
    # Keyword arguments
    # Variable number of arguments
# ----------------------------------


# Parameter and Argument
# Defining a function...
def openGISsoftware(version):
    """
    This function will open
    provided QGIS software version
    """
    print(f"Loading QGIS {str(version)}... please wait!")



# function call
openGISsoftware(2.10)
openGISsoftware(3.00)
openGISsoftware(3.12)
openGISsoftware(3.24)


# To display the DocString...
print(openGISsoftware.__doc__)



# More than one parameter...
def openGISsoftware(name, version):
    """
    This function will open
    provided GIS software version
    """
    print(f"Loading {name} {str(version)}... please wait!")


openGISsoftware('QGIS', 3.16)
openGISsoftware('GRASS', 7.9)
openGISsoftware('SAGA', 2.6)
openGISsoftware('ArcGIS Pro', 2.8)


# ----------------------------------
# Defining a function with an arbitrary number of arguments
def lat_long_ele(lat, long, ele):
    print(lat, long, ele)
    
lat_long_ele(9.90, 10.72, 982.89)


# Lets say it needs to take additional arguments for: day, month, year
# Better way to do it is by use *args which passes it a turple...
def lat_long_ele(*args):
    print(args)
    
lat_long_ele(2.733, 4.536, 278.890)




# Keyword arguments...
def lat_long_ele(lat=0, long=0, ele=0):
    print(lat, long, ele)
    
lat_long_ele(ele=982.89, lat=9.90, long=10.72)


# Arbitrary Keyword Arguments, **kwargs
def lat_long_ele(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

lat_long_ele(ele=982.89, lat=9.90, long=10.72)



coords = {'lat':2.733, 'long':4.536, 'ele':278.890}
def lat_long_ele(**kwargs):
    print(kwargs)
    
lat_long_ele(**coords)


# ----------------------------------
# Returning values from functions
# Functions can return a value that you can use directly.
def add_xy(x, y):
    return x+y

# this allow you to continue to work with the result of your function

def avg_lat(latitudes):
    return sum(latitudes)/len(latitudes)

latitudes = [12.34, 3.02, 4.89, 55.01, 67.55]
print("Average of Latitudes:", avg_lat(latitudes))


# Note return statement should be the last line, any line after it wont be processed
def add_xy(x, y):
    print('BEFORE return')
    return x+y
    print('AFTER return')

# A function with no return statement implicitly returns None.
# Similarly a function with a return statement, but no return value or variable returns None.



# ----------------------------------
# Anonymous Functions in Python
# Anonymous functions are also called lambda functions in Python 
# because instead of declaring them with the standard 'def' keyword, you use the lambda keyword.

# Syntax
# lambda arguments : expression

# Filter elevation greater than 1000m....
elevation_list = [1122.03, 528.89, 4012.22, 560.44, 2228.93, 211.89, 1333, 412.89]
new_elevation_list = list(filter(lambda x: (x >= 1000) , elevation_list))
print(new_elevation_list)


# Above is the same as....
def elevation_above_1k(x):
    return x >= 1000

new_elevation_list = list(filter(elevation_above_1k , elevation_list))
print(new_elevation_list)




# Sum of lat/long squares...
lat_long = [(12, 34), (22, 13), (45, 8)]
new_lat_long = list(map(lambda x : x[0]**2 + x[1]**2, lat_long))
print(new_lat_long)

# Above is the same as....
def sq_lat_long(x):
    ans = x[0]**2 + x[1]**2
    return ans

new_lat_long = list(map(sq_lat_long, lat_long))
print(new_lat_long)






# ----------------------------------
# Nested functions
# Nested functions have direct access to the variables and names that you define in 
# the enclosing function. It provides a mechanism for 
# encapsulating functions, creating helper solutions, and implementing closures and decorators.
# https://www.analyticsvidhya.com/blog/2021/08/how-nested-functions-are-used-in-python/
def outer_func():
    def inner_func():
        print("Hello, World!")
    inner_func()
outer_func()



# ----------------------------------
# Recursion - a function calls itself




# ----------------------------------
# Functions Vs Methods - a function defined in a 'Class' (OOP)
# A method refers to a function which is part of a class. You access it with an instance or object of the class. 
# All methods are functions, but not all functions are methods.

# Lets look at built-ins...
# help(str)

# Method
'Nigeria'.upper()

# Function
len('Nigeria')




