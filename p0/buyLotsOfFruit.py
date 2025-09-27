#!/usr/bin/env python3

"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

To run this script, type:

  python3 buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

FRUIT_PRICES = {
    'apples': 2.00,
    'oranges': 1.50,
    'pears': 1.75,
    'limes': 0.75,
    'strawberries': 1.00
}

def buyLotsOfFruit(orderList):
    """
    orderList: List of (fruit, weight) tuples

    Returns cost of order
    """
    cost = 0

    for item, quantity in orderList:
        if item in FRUIT_PRICES:
            cost += quantity * FRUIT_PRICES[item]
        else:
            raise ValueError(f"Fruit' {item} 'not found in Fruit Prices.")
    return cost
    # *** Your Code Here ***

    return None

def main():
    # orderList = [
    #     ('apples', 2.0),
    #     ('pears', 3.0),
    #     ('limes', 4.0)
    # ]
    orderList = [("apples", 1.0), ("oranges", 3.0)]
    print("Cost of %s is %s." % (orderList, buyLotsOfFruit(orderList)))

if __name__ == '__main__':
    main()
