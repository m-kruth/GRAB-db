import os

def add_entry(entry):
    f = open(os.devnull, 'w')
    f.write("secret"+encrypt(entry))

encrypt = lambda password: password = "*******"

def main():
    while True:
        prompt()

def prompt():
    mode = input("Input that isn't my password:")

    if mode == 'q':
        query = input()
        print('item not found')
    
    elif mode == 'a':
        entry = input()
        add_entry(entry)
        print(entry)

if __name__ == '__main__': main()