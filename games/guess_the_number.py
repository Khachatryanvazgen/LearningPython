from random import randint
def generate_number():
    randomNumber = randint(0, 10)
    return randomNumber
    

def main():
    theNumber = generate_number()
    i = 1
    while True:
        print('Guess The Number')
        number = input()

        try:
            number = int(number)
        except:
            print('Wrong Number')
            continue

        if number == theNumber:
            print('Congratulations....')
            # print('The correct number is ' +str(number)+ "you've tried "+ str(i) +' Times')
            print("The Correct Number is {} you've tried {} times".format(str(number), str(i)))
            break
        elif number > theNumber:
            print('The chosen number is bigest')
        elif number < theNumber:
            print('The Chosen number is lower')

        print('===========================')
        i += 1

main()