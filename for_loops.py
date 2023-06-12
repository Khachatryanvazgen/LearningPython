names = ['Vazgen', 'Karen', 'Artash', 'Armena', 'Garo']
'''
for name in names:
    if name == 'Vazgen':
        continue #Skip e anum elementy ancnum e araj
    print(name)
'''
'''
for name in names:
    if name == 'Artash':
        break #Hasnelov ayd elementin durs e galis 
    print(name)
'''

# total = 0
'''
# for number in range(0, 11):
#     if number % 2 == 0 and number % 4 == 0:
#         print(number)
'''

# people = {
#     'Jule': 24,
#     'Vazgen': 28,
#     'Armen': 30,
#     'Karen': 34
# }

# for key,value in people.items():
#     print(key)
#     print(value)
#     print('--------------')

names1 = ['Vazgen', 'Karen', 'Eprem', 'Jhon']
names1.append('Arstrun')
names1.pop()

for el in names1:
    if el  == 'Karen':
        continue
    print(el)
# print(names1)
