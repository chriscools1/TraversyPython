# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Chris'
age = 39

# concatenate
print ('Hallo, mijn naam is ' + name + ' en ik ben ' + str(age))

# String Formatting

# argumenten door positie
print('Hallo, mijn naam is {name} en ik ben {age}'.format(name=name, age=age))

# F-strings pas vanaf python 3.6
print (f'Hallo, mijn naam is {name} en ik ben {age}')

# String Methods
s = 'hello world'

# string hoofdletters geven met methodes

print(s.capitalize())
print (s.swapcase())
print (len(s))
print (s.isnumeric())
