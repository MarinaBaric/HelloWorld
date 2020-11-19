import os
import sys

print('Hola World')

first_number = input('Please provide a number: ')
second_number = input('One more please: ')
product = int(first_number) * int(second_number)
sumsum = int(first_number) + int(second_number)

if product < 1000:
    print(product)
else: 
    print(sumsum)
    print('Do you understand?')
