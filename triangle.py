# Triangle
# Author: Stephanie Tattrie
# Create Date: 9/9/2015
r = 0
def main():
    number = int(input("Enter number"))
    for r in range(number):
        print(" " * (number - r - 1) + "*" * (2 * r + 1))
        
main()

