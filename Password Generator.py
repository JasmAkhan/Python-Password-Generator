import random
print('Welcome To Your Personal Password Generator')
print('============================================')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
number = input('How Many Passwords Would You Like To Generate?: ')
number = int(number)
length = input('What Is Your Desired Password Length?: ')
length = int(length)
print('Here Are Your Passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    
import random

numbs = '0123456789'

number = input('If you would like a numbers only password press 1: ')
number = int(number)
print('here are your passwords')

