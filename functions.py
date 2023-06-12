# import os
# dirpath = os.getcwd()
# print('Current Directory: ' + dirpath)

# from datetime import datetime
# print(datetime.today ())



'''
def print_hello(fromWho, to):
    print('Hello from '+ fromWho + ' to ' + to)

print_hello('vazgen', 'Nara')

# print_hello('Vazgen', 'Arman')
# print_hello('Vazgen', 'Anna')
''' 
# =================================================

'''
def sum(numberOne, numberTwo):
    print(numberOne + numberTwo)

sum(117,235)
'''
# ==================================================

'''
def doubled(x):
    x *= 2
    return x

finalResult = doubled(10)
# print(finalResult)
'''
# ====================================
# GLOBAL VARIABLE

# myString = 'Hello World '
# def changeString():
#     global myString
#     myString +=  'from Vazgen'

# changeString()
# print(myString)


# =========================================================


'''
# def print_hello(fromWho, to):
#     print('Hello from ' + fromWho + 'to ' + to)


# print_hello('Vazgen ', 'Anna')
# print_hello('Anna')
'''


def sum(number1= 0, number2= 0):
    print(number1 + number2)




# ===================================================
#  CHECK VARIABLE TYPE (STR/INT)

'''
myVar = 12
print(type(myVar))

print(type(str(myVar)))
'''
# ==================================================
# IMPORT FROM LIB


'''
import os 
dirpath = os.getcwd()
print('Current Directory: ' +dirpath)

from datetime import datetime
print(datetime.today())
'''
# =====================================


'''
def doubled(x):
    x *= 2
    return x

finalResult = doubled(10)
# print(finalResult) 
'''
# =============================================
# GLOBAL VARIABLE
'''
myString = 'Hello World'

def changeString():
    # print(myString)
    global myString
    myString += ' From Vazgen'

changeString()

print(myString)
'''


