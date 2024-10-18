from sys import argv
import os

def ping(address):
    response = os.system(f'ping {argv[1]}')

if __name__ == "__main__":
    ping(argv[1])
