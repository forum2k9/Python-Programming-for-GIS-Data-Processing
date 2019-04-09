# Script_02.py
# Author: UmarYusuf.com
# Date: 3/01/2019
# Topic: Python Data Types - String, Boolean, Number, List, Tuple, Arrays, Dictionary, Sets and Files
# ------------------------------

#String ' ' or " " or ''' ''' or """ """

#https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)
#country_name, country_code, area, in_africa, latitude, longitude, population

# Primitive or the basic data types (String, Boolean and Number)
#-------Nigeria--------
country_name1 = 'Nigeria'
country_code1 = 'NG'
area1 = '923,768 kmSq'
in_africa1 = True # Boolean
# Numbers - float, integers, complex num, Long
latitude1 = 9.081999
longitude1 = 8.675277
population1 = 164669751

#-----Cote d'Ivoire----------
country_name2 = 'Cote d\'Ivoire' # Ivory Coast
country_code2 = 'CI'
area2 = '322,463 kmSq'
in_africa2 = True
latitude2 = 7.539989
longitude2 = -5.54708
population2 = 23695919

# ------Germany---------
country_name3 = 'Germany'
country_code3 = 'DE'
area3 = '357,386 kmSq'
in_africa3 = False
latitude3 = 51.165691
longitude3 = 10.451526
population3 = 82800000

# -----Japan----------
country_name4 = 'Japan'
country_code4 = 'JP'
area4 = '377,973 kmSq'
in_africa4 = False
latitude4 = 36.204824
longitude4 = 138.252924
population4 = 127748513

#1- None type
# ------ Unknown ---------
country_name5 = None
country_code5 = None
area5 = None
in_africa5 = None
latitude5 = None
longitude5 = None
population5 = None

#------Egypt---------
country_name6 = 'Egypt'
country_code6 = 'EG'
area6 = '1,010,408 kmSq'
in_africa6 = True
latitude6 = 26.820553
longitude6 = 30.802498
population6 = 95688681

#2- Escape character = \n, \t, \\


#3- dir/help(str and num)




# Non-primitive or complex data types that stores a collection of values in various formats (List, Tuple, Arrays, Dictionary, Sets and Files)

# List -  Stacks, Queues, Graphs and Trees

country_name = ['Nigeria', 'Cote d\'Ivoire', 'Germany', 'Japan', None, 'Egypt']
country_code = ['NG', 'CI', 'DE', 'JP', None, 'EG']

area = ['923,768 kmSq', '322,463 kmSq', '357,386 kmSq', '377,973 kmSq', None, '1,010,408 kmSq']
in_africa = [True, True, False, False, None, True]

# latitude = [9.081999, 7.539989, 51.165691, 36.204824, None, 26.820553]
# longitude = [8.675277, -5.54708, 10.451526, 138.252924, None, 30.802498]

lat_long = [(9.081999, 8.675277), (7.539989, -5.54708), (51.165691, 10.451526), (36.204824, 138.252924), (None, None), (26.820553, 30.802498)]

population = [164669751, 23695919, 82800000, 127748513, None, 95688681]

# Length, Sort, Reverse, Append, Delete, Insert, Count, slicing etc

# Accessing Elements (Index Positions Start at 0, Not 1)

# Stacks - container of objects that are inserted and removed according to the Last-In-First-Out (LIFO) concept.
# Queues - container of objects that are inserted and removed according to the First-In-First-Out (FIFO) principle.
# Graphs - networks consisting of nodes, also called vertices which may or may not be connected to each other.
# Trees - Just like a tree in the real world.

population1 = [164669751, 23695919, 82800000, 127748513, None, 95688681] # List
population2 = (164669751, 23695919, 82800000, 127748513, None, 95688681) # Tuple


# Array - is a collection of elements of the same type.
import array as arr
import numpy as np

population_array = arr.array('i', (164669751, 23695919, 82800000, 127748513, 95688681))

population_np_array = np.array([164669751, 23695919, 82800000, 127748513, 95688681])
#population_np_array.reshape(1,5)


# Dictionary and Sets

#{key:value, key:value, key:value} 
population_dic = {'NG':164669751, 
        'CI':23695919, 
        'DE':82800000, 
        'JP':127748513, 
        'Unknown':None, 
        'EG':95688681}


#{item1, item2, item3, item4}
population_set = {164669751, 23695919, 82800000, 127748513, None, 95688681}

set_a = set(population)

in_africa_uniqe = set(in_africa)




#@@@@@@@@@@@@@-------------------------------
import ogr
cnt = ogr.GetDriverCount()
formatsList = []  # Empty List

for i in range(cnt):
    driver = ogr.GetDriver(i)
    driverName = driver.GetName()
    if not driverName in formatsList:
        formatsList.append(driverName)

formatsList.sort() # Sorting the messy list of ogr drivers

for i in formatsList:
    print (i)