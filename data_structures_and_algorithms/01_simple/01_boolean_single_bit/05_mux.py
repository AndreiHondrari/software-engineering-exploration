
def mux(
    x: bool,
    y: bool,
    a: bool
) -> bool:
    return (x & (not a)) | (y & a)


def mux_with_if(x: bool, y: bool, a: bool) -> bool:
    if a:
        return y
    else:
        return x


if __name__ == '__main__':

    print("mux v1 F T F: ", mux(False, True, False))
    print("mux v1 F T T: ", mux(False, True, True))
    print("mux v1 T F F: ", mux(True, False, False))
    print("mux v1 T F T: ", mux(True, False, True))

    print("mux v2 F T F: ", mux_with_if(False, True, False))
    print("mux v2 F T T: ", mux_with_if(False, True, True))
    print("mux v2 T F F: ", mux_with_if(True, False, False))
    print("mux v2 T F T: ", mux_with_if(True, False, True))
