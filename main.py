import os
import sys


def add_entry(entry):
    f = open(os.devnull, 'w')
    f.write(entry)

def main():
    while True:
        prompt()

def prompt():
    mode = input("input:")

    if mode == 'q':
        query = input()
        print('item not found')
    
    elif mode == 'a':
        entry = input()
        add_entry(entry)
        print(input)

if __name__ == '__main__': main()