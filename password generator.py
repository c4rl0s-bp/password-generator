import random

minLenght = 8	#Feel free to modify these values
maxLenght = 20

letters = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", 
        "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", 
        "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "@", ".", ":"]

num = int(input("Enter your password's length: "))

while num < minLenght or num > maxLenght:
    print(f"Password's length must be between {minLenght} and {maxLenght}")

    num = int(input("Enter your password's lenght: "))

password = ""

while num != 0:
    randomChar = random.randint(0, len(letters) -1)
    password += str(letters[randomChar])
    num -= 1

print(f"Generated password is: \033[1;33m{password}\033[0m \n Make sure to save it")


