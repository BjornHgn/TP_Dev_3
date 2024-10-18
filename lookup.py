from sys import argv
import socket
import re

def valid_domain(domain):
    pattern = r'^[a-z0-9]+(\.[a-z0-9]+)+$'
    return re.match(pattern,domain) is not None

def lookup(domain):
    response = socket.gethostbyname(domain)
    print(f"{response}")


if __name__ == "__main__":
    domain = argv[1]
    if valid_domain(domain):
        lookup(domain)
    else :
        print(f"{domain} n'est pas un nom de domaine valide")