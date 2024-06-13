#!/usr/bin/python
import sys
import os

# Add a new product file in 'product/' directory
def add_product(name):
    try:
        file = open('product/' + name, 'x')
    except FileExistsError:
        print('error: Product \'' + name + '\' already exist')
        sys.exit(-1)

    print('new product: ' + name)

    file.write('explain: ' + input('explain: ') + '\n')
    file.write('amount: ' + input('amount: ') + '\n')
    file.write('price: ' + input('price: ') + '\n')

    file.close()

# Delete product from 'product/' directory
def del_product(name):
    try:
        os.remove('product/' + name)
    except FileNotFoundError:
        print('error: No such product \'' + name + '\'')
        sys.exit(-1)

# Print usage and exit with error
def usage():
    print('usage: product ' + 'add|del FILE...')
    sys.exit(-1)

# main
if len(sys.argv) < 3:
    usage()

option = sys.argv[1]
files = sys.argv[2:]

match (option):
    case 'add':
    	for file in files:
    		add_product(file)
    case 'del':
    	for file in files:
    		del_product(file)
    case _:
        usage()
