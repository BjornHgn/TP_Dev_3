import os

def ping(address):
    response = os.system(f'ping {address}')

if __name__ == "__main__":
    ping('8.8.8.8')