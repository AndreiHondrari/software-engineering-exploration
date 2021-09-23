
if __name__ == '__main__':
    # typically you don't assign a lambda to a variable but use 'def'
    anonymous_function = lambda x, y: x + y
    result: int = anonymous_function(11, 22)
    print(result)
