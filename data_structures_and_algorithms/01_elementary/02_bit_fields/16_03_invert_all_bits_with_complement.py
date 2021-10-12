"""
Invert all bits
"""


if __name__ == '__main__':
    a = 0b11001010
    print(f"INITIAL      {a:#0{10}b}")

    # it will display as -(x + 1)
    # the sign bit is stored additionally to the value
    # and you can't manipulate this bit directly
    a_complement = ~a
    print(f"COMPLEMENT  {a_complement:#0{10}b}")

    # the & 0xff is necessary because of the extra sign bit
    # it will simply filter out the sign and just obtain us the
    # one's complement bit sequence
    a = a_complement & 0xff
    print(f"FINAL        {a:#0{10}b}")
