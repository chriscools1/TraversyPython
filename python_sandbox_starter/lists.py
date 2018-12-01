# A List is a collection which is ordered and changeable. Allows duplicate members.

#  lijst maken

numbers = [1,2,3,4,5,6]
fruits = ['appels', 'peren', 'druiven', 'peren','bananen']
# constructor gebruiken
# numbers2 = list((7,8,9,10))


print(numbers)
print(fruits)
print(fruits[1])
print(len(fruits))

# fruit toevoegen aan de lijst
fruits.append('mango')
print(fruits)

# item uit lijst verwijderen
fruits.remove('druiven')
print(fruits)

# item toevoegen op bepaalde positie in lijst
fruits.insert(2, 'pruimen')
print(fruits)

# item delten op bepaalde positie
fruits.pop(2)
print(fruits)

# lijst omdraaien
fruits.reverse()
print(fruits)

# lijst sorteren
fruits.sort()
print(fruits)

# omgekeerd sorteren
fruits.sort(reverse=True)
print(fruits)

# waarde veranderen in de lijst
fruits[0]= 'blauwe bessen'
print(fruits)