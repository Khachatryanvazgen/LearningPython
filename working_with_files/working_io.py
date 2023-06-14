


# with open("users.txt", "r")as f:
#     for line in f.readlines()[1:]:
#         print(line[:-1].split(",")[3])
    

'''
with open("newFile.txt", "a") as f:
    f.write('New Text')
'''


with open('users.txt', 'r') as f:
    for line in f.readlines()[1:]:
        info = line[:-1].split(",")

        if info[3] == 'male':
            with open("male.txt", "a") as mFile:
                mFile.write(line)
        
        elif info[3] == 'female':
            with open("females.txt", "a") as fFile:
                fFile.write(line)

        else:
            print('Unknown')
