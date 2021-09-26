"""
Obtain a "negative" mask where one bit is 0
"""

if __name__ == '__main__':
    N = 3

    # 0xff is equivalent with 0b11111111
    x = 0xff ^ (0b1 << N)

    print(f"{x:#0{10}b}")
