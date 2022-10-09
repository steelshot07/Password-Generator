from pickle import TRUE
import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '0123456789'
symbols = '{}[](),.?:;_+/*'

upper, lower, number, symbol = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if number:
    all += digits
if symbol:
    all += symbols

while True:
    length = int(
        input("Enter number of characters you want for your password: "))
    amt = int(input("Enter number of passwords you want: "))

    for i in range(amt):
        password = "".join(random.sample(all, length))
        print(password)

    x = input("Do you want to continue(Y/N)")
    if x in "Nn":
        break
