# stocks.py
# Author: Stephanie Tattrie
# Create Date: 10/17/15


import random 

def main():
    print("\nTotal Stock Portfolio Value =", f_totalPortfolio())
    f_simulateTradingday()

def f_totalPortfolio():
    fb = 100 * 94.01
    orcl = 100 * 37.59
    msft = 200 * 46.63
    total = fb + orcl + msft
    return total


def f_simulateTradingday():
    close_price1 = 94.01
#    print("\n Simulating Trading Day ... \n")
    mylist1 = []
#    print("Facebook: ")
    price1 = close_price1
    for x in range(5):
        tick1 = random.randint(0,1)
        delta1 = float(random.random())
        if tick1 == 1:
            price1 = price1 + delta1
        else:
            price1 = price1 - delta1
#        print("%.2f" % price, "\t", tick)
        mylist1.append(price1)
    high1 = max(mylist1)
    low1 = min(mylist1)
    print("\nsimulating trading day...")
    print("\nSym \t Open  \t High  \t Low \t CLose \t Net Change")
    print("Fb", end = "")
    print("\t %.2f" % close_price1, end = "")
    print("\t  %.2f" % high1, end = "")
    print("\t  %.2f" % low1, end = "")

    net_change1 = price1 - close_price1
    print("\t %.2f" % price1, end = "")
    print("\t %.2f" % net_change1, end = "")
    
    close_price2 = 37.59
    mylist2 = []
#    print("Oracle: ")
    price2 = close_price2
    y = 0 
    for y in range(5):
        tick2 = random.randint(0,1)
        delta2 = float(random.random())
        if tick2 == 1:
            price2 = price2 + delta2
        else:
            price2 = price2 - delta2
#        print("%.2f" % price, "\t", tick)
        mylist2.append(price2)
    high2 = max(mylist2)
    low2 = min(mylist2)
    print("\nOrcl", end = "")
    print("\t %.2f" % close_price2, end= "")
    print("\t %.2f" % high2, end = "")
    print("\t %.2f" % low2, end = "")

    net_change2 = price2 - close_price2
    print("\t %.2f" % price2, end = "")
    print("\t %.2f" % net_change2, end = "")
    

    close_price3 = 46.63
    mylist3 = []
#    print("Microsoft: ")
    price3 = close_price3
    z = 0
    for z in range(5):
        tick3 = random.randint(0,1)
        delta3 = float(random.random())
        if tick3 == 1:
            price3 = price3 + delta3
        else:
            price3 = price3 - delta3
#        print("%.2f" % price, "\t", tick)
        mylist3.append(price3)
    high3 = max(mylist3)
    low3 = min(mylist3)
    print("\nMsft", end = "")
    print("\t %.2f" % close_price3, end= "")
    print("\t  %.2f" % high3, end = "")
    print("\t  %.2f" % low3, end = "")

    net_change3 = price3 - close_price3
    print("\t %.2f" % price3, end = "")
    print("\t %.2f" % net_change3, end = "")
    c = close_price3 * 200
    a = close_price1 * 100
    b = close_price2 * 100
    total = a + b + c
    print("\n\nThe New Total Portfolio = %.2f" % total)
    

main()

