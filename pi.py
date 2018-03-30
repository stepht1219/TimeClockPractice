# Pi
# Author: Stephanie Tattrie
# Create Date: 9/20/15

import math
pi = math.pi
r = 0
def main():
    newterm = 0
    number = int(input("Enter number of terms to sum"))
    for r in range(number):
        term =4 / (2 * r + 1)
        if (r % 2 == 0): 
            newterm = term + newterm
        elif (r  % 2 == 1):
            newterm = newterm - term
        else:
            print("invalid")

    print("estimation of pi = ", newterm)
    calcdiff = newterm - pi
    print("calcdiff =", calcdiff)

main()
