
# i = 0
# while i < 10:
#     if i < 10:
#         i = i +1 
#     print('Hello World '+str(i))





while True:
    # print('1. Settings')
    # print('2. Home')
    # print('3. Profile')
    # print('4. Exit')
    menu = ('1. Settings',
            '2. Home', 
            '3. Profile', 
            '4. Exit' )
    
    print(menu)
    print('Enter Menu ID ')
 
    command = input()

    if int(command) == 1:
        print('Go Settings')

    elif int(command) == 2:
        print('Home Page')

    elif int(command) == 3:
        print('Profiel page')

    elif int(command) == 4:
        print('Exit Application')
        
    else:
        print('Wrong Menu ID')
        break
        # continue
