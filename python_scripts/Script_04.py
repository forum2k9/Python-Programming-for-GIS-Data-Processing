# Script_04.py
# Author: UmarYusuf.com
# Date: 25/05/2022
# Topic: Conditional (Control flow) Statements if/for/while
# ------------------------------


# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# See more Boolean, Bitwise operators in the book "A Byte of Python"
# Also see: https://chercher.tech/python-programming/python-operators



#1- if/elif/else
travelling_to_africa = 'Yes' # True
destination = 'Nigeria'

if travelling_to_africa == 'Yes':
    print('Have a safe trip to:', destination)
    # print(f'have a safe trip to: {destination}')


if travelling_to_africa == 'Yes':
	print('Awsome idea')
elif travelling_to_africa == 'No':
	print('Oops, please consider coming to Africa')
else:
	print('Please choose Yes/No')


# More than one condition
if travelling_to_africa == 'Yes' and destination == 'Nigeria':
	print('Welcome to NIGERIA')
else:
	print('Have a safe trip to:', destination)


# Nested if statement
if travelling_to_africa == 'Yes':
	if destination == 'Nigeria':
		print('Welcome to NIGERIA')
	else:
		print('Have a safe trip to:', destination)

elif travelling_to_africa == 'No':
	print("Sorry to hear you don't like Africa")

else:
	print("Your response is not recorgnized!")




# Lets check if lat/long coordinates are to N/S of meridian or E/W equator...
# Line of Graticules - https://www.naturalearthdata.com/downloads/50m-physical-vectors/50m-graticules/
# Geographic lines - https://www.naturalearthdata.com/downloads/10m-physical-vectors/10m-geographic-lines/

latitude = 0.00

if latitude > 0:
	print('This latitude value is in the NORTHERN hemisphere')
elif latitude < 0:
	print('This latitude value is in the SOUTHERN hemisphere')
else latitude == 0:
	print('This latitude value is on the EQUATOR')


# longitude = -17.290


# Handling invalid coordinate
if type(latitude) == float or type(latitude) == int:
	if latitude > 0:
		print('This latitude value is in the NORTHERN hemisphere')
	elif latitude < 0:
		print('This latitude value is in the SOUTHERN hemisphere')
	elif latitude == 0:
		print('This latitude value is on the EQUATOR')
else:
	print('This is not a valid latitude value')



# Use ternary operator for inline conditional expressions
my_time = 7
print("Good Morning") if my_time < 12 else print("Good Day")





# The if __name__ == "__main__"
# This tells Python that you only want to run the following code 
# if this program is executed as a standalone file.




#2- for loop
# Use a loop when you want to iterate over something n number of times
country_name = ['Nigeria', 'Cote d\'Ivoire', 'Germany', 'Japan', None, 'Egypt']
country_code = ['NG', 'CI', 'DE', 'JP', None, 'EG']
area = ['923,768 kmSq', '322,463 kmSq', '357,386 kmSq', '377,973 kmSq', None, '1,010,408 kmSq']
in_africa = [True, True, False, False, None, True]


# Simple for loop
for country in country_name:
	print(country)


# Nested for loop
coord = ["LATITUDE", "LONGITUDE"]
country = ["Nigeria", "Ghana", "Morroco"]

for x in country:
  for y in coord:
    print(x, y)



# Using the 'else' statement in loops
country_name = ['Nigeria', 'Cote d\'Ivoire', 'Germany', 'Japan', None, 'Egypt']

for c in country_name:
    if c == 'Japan':
        print("***Country found!***")
        break
    print(c)
else:
    print("Country not found!")




# Write several repeated text on the console...
for x in range(20):
   print('I love QGIS Python Programing')




# *************** Problem Solving 1 - Mini Project *********************
# Write several text files into a folder...
txtfolder = r"C:\Users\Yusuf_08039508010\Desktop\DeskTop\GIS Data Processing Scripts\I love QGIS Python Programing"

for x in range(20):
    print('Writing file... ', x)

    # Create file obj
    f = open(f'{txtfolder}\\file_' + str(x) + '.txt', mode='x')
    # Write text to the file
    f.write('I love QGIS Python Programing')
    # f.write('I love QGIS Python Programing\n'*x) # with each file containing lines 
    # Close the file
    f.close()


# List of Python special/escape characters:
# \n - Newline
# \t - Horizontal tab
# \r - Carriage return
# \b - Backspace
# \f - Form feed
# \' - Single Quote
# \" - double quote
# \\ - Backslash
# \v - vertical tab
# \N - N is the number for Unicode character
# \NNN - NNN is digits for Octal value
# \xNN - NN is a hex value; \x is used to denote following is a hex value.
# \a - bell sound, actually default chime


# *************** Problem Solving 2 - Mini Project *********************
# Read the text file 'countries_1.txt', then save each country row data into it own text file

txt_file = r"C:\Users\Yusuf_08039508010\Desktop\DeskTop\GIS Data Processing Scripts\data files\countries_1.txt"

# Read content of text file...
f = open(txt_file)
text_content = f.readlines()
f.close()

# Save row contents to individual text files...
txtfolder = r"C:\Users\Yusuf_08039508010\Desktop\DeskTop\GIS Data Processing Scripts\countries_txt_folder"

for row in text_content:
    if row.endswith('%\n'):
        print('Processsing...', row)
        filename = row.split('\t')[0].strip()
        
        f = open(f'{txtfolder}\\{filename}' + '.txt', mode='x')

        f.write(row.strip())
        f.close()






#3- while loop
# loop until a specific condition is met
elev = 1 # initial elevation of a point
while elev < 10:
	print(elev)
	elev += 1



# break, continue, pass statements

# break - is used to break out of a loop statement 
for afri in afri_countries:
	if afri == 'Egypt':
		break
	print(afri)


# continue - is used to skip the current loop item and continue to the next iteration of the loop.
for afri in afri_countries:
	if afri.endswith('a'):
		continue
	print(afri)



# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for cd in country_code:
	pass




# Alternatives to loops...
#~ zip(),
#~ map(),
#~ filter(),
#~ reduce(),
#~ list comprehension,
#~ collections module,
#~ itertools module












# List of Countries by continents 
afri_countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome and Pri­ncipe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'The Gambia', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
euro_countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City']
asia_countries = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China (PRC)', 'East Timor', 'Georgia', 'Hong Kong', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Macau', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'The Philippines', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']
north_america_countries = ['United States of America', 'Mexico', 'Canada', 'Guatemala', 'Cuba', 'Haiti', 'Dominican Republic', 'Honduras', 'Nicaragua', 'El Salvador', 'Costa Rica', 'Panama', 'Jamaica', 'Trinidad and Tobago', 'Belize', 'Bahamas', 'Barbados', 'Saint Lucia', 'Grenada', 'Saint Vincent and the Grenadines', 'Antigua and Barbuda', 'Dominica', 'Saint Kitts and Nevis']
south_america_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
oceania_countries = ['Australia', 'Federated States of Micronesia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']

