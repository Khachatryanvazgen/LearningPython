from random import randint
def autogenerate_number():
    randomNumber = randint(0, 10)
    return randomNumber



def main():
    theNumber = autogenerate_number()
    i = 1
    while True:
        print('Guess the number: ')
        number = input()

        try:
            number = int(number)

        except:
             print('The input should contain only number:\nPlease try again:')
             continue
        
        if number == theNumber:
            print('Congratulations...')
            print("The correct number is {} you've tried {} times ".format (str(number),str(i)))
            break
                  
        elif number > theNumber:
            print('The Chosen number is highest')
        
        elif number < theNumber:
            print('The Chosen number is lower')

        print('=======================')
        i += 1


main()
        
        


