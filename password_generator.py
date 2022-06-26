# basic password gen v0.0.1

# last edited by baburinho; june 25 2022

# i put this together in like 15 minutes, its not the most complex thing but i am proud of it :)

import random
import string

#defining function to generate password string

def random_str_gen(str_length, char_allowed):
    return ''.join(random.SystemRandom().choice(char_allowed)
    for x in range (str_length))

chars = string.printable
length = int(input("How long do you want your password to be? "))

paswrd = random_str_gen(length, chars)
print(paswrd)

#asks user if they would like to print output into a text file as well

p = input("Would you like to export this to a .txt file? y/n ")

if p == 'y':
    file = open("password.txt", "wt")
    file.write(paswrd)
    file.close()
    print("Check password.txt")
else:
    print("Alright! Have a good day:)")