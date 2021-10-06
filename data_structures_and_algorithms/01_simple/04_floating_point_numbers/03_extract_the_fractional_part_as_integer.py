
PRECISION = 6

if __name__ == '__main__':
    x = 123.456
    y = x % 1
    z = round(y, PRECISION)

    tau = 0
    while z > 0.0:
        shifted_z = z * 10
        digit = int(shifted_z // 1)
        tau *= 10
        tau += digit
        z = round(shifted_z % 1, PRECISION)

    print(f"{x} -> {tau}")
