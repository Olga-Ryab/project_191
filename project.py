import os.path
import random
import string

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()
def generate(n):
    letters = string.ascii_letters
    digits = string.digits
    characters = '!@#$%^&*()_+' 
    alphabet = letters + digits + characters

    password = ''

    for i in range(n):
        password += random.choice(alphabet)

    return password

n = int(input("Enter n: "))
print(generate(n))		
def appendNew():
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
	Password = input("Please enter the Password: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)
