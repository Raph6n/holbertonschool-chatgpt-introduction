#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <number>")
        return

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Erreur: Veuillez fournir un nombre entier.")
        return

    f = factorial(number)
    print(f)

if __name__ == "__main__":
    main()
