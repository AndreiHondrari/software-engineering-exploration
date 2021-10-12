"""
You would expect that 0.1 + 0.2 == 0.3
But:

0.3 is represented as: 0.2999999999999999888977697537
0.1 + 0.2 results in : 0.3000000000000000444089209850
"""

if __name__ == '__main__':
    x = 0.1 + 0.2
    if (x == 0.3):
        print("detected")
    else:
        print("ANTI-detected")
