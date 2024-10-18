from sys import argv
import os

def ping(address):
    response = os.system(f'ping {argv[1]} > nul 2>&1')
    if response == 0:
        print(f"UP !")
    else:
        print(f"DOWN !")

if __name__ == "__main__":
    ping(argv[1])
