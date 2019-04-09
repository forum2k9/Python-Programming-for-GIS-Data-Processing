# Author: UmarYusuf.com
# Date: 23/10/2018

#print('Hello QGIS') # This print a string

#print('Hello QGIS from SublimeText')

#print('Hello from QGIS')

'''
Type your comments here
Type another here
Type 1234
'''

##=============================
# Variable
##=============================

x = 3
y = 5

print(x*y)

_lat, _long = 9.0004, 10.7701 # Valid
my_lat1, my_long1 = 8.9001, 10.1010 # Valid

print(my_lat1, my_long1)

# Multi variable assigned to one value
a = b = c = "Nigeria"
x, y, z = "Nigeria", "Ghana", "Senegal"
print(x, y, z)

age1 = 23
print('The value of age1 is: ', age1)

age2 = 50
print('The value of age2 is: ', age2)

##=============================
# Interactive Help
##=============================
#help() - calls the built-in Python help or documentation system on an object.
#dir() - return a list of valid attributes of an object or module.
#type() - Returns the type of object.
#__doc__ - Returns the doc-string of object or module.

#============ Print variables to text file =============

myFile = open('C:\\Users\\Yusuf_08039508010\\Desktop\\GIS Data Processing Scripts\\myTextFile.txt', 'a')

print('The value of x is: ', x, file = myFile)
print('The value of y is: ', y, file = myFile)
print('The value of z is: ', z, file = myFile)

print('The value of lat1 is: ', my_lat1, file = myFile)
print('The value of long1 is: ', my_long1, file = myFile)
print('The value of age1 is: ', age1, file = myFile)
print('The value of age2 is: ', age2, file = myFile)

myFile.close()
print("Finished......")
