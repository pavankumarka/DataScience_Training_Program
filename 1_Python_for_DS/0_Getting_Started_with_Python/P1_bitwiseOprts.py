def bitwiseOpteration(a, b, c):
    d = a ^ a

    e = c ^ b

    f = a & b

    g = c | (a ^ a)

    h = ~e

    print(d, e, f, g, h, sep = "\n")


if __name__ == "__main__":
#{
    a = int(input())
    b = int(input())
    c = int(input())

    bitwiseOpteration(a, b, c)
#}
