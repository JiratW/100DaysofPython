#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
#random.choice() is use random from list
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for char in range(1, nr_letters + 1):
  password += random.choice(letters)
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
print(f"Your password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
Hard_password = ""
for char in range(1, nr_letters + 1):
  Hard_password += random.choice(letters)
for char in range(1, nr_symbols + 1):
  Hard_password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  Hard_password += random.choice(numbers)
#Concatenate strings in Python (+ operator, join, etc.) 
#See detail more in link https://note.nkmk.me/en/python-random-shuffle/
l = list(Hard_password)
random.shuffle(l)
final_pass = ''.join(l)
print(f"Your password is: {final_pass}")
  
