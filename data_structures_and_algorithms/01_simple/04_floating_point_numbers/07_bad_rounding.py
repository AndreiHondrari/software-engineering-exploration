"""
You would expect that 2.675 would round to 2.68,
but it is represented binary as 2.6749999999999998223643160600
so the rounding ends up with 2.67 (rounded down)
"""

if __name__ == '__main__':
    x = 2.675
    x_rounded = round(x, 2)

    print(f"x normal : {x}")
    print(f"x rounded: {x_rounded}")
    print(f"x actual : {x:.28f}")
