def utility():
#{
    x = int(input())
    y = int(input())

    # add
    add = x + y

    # sub
    sub = x - y

    # mul
    mul = x * y

    # float div
    div = x / y

    # int div
    iDiv = x //y

    # mod
    mod = x % y

    # pow
    xPowY = x ** y

    print( add, sub, mul, "{:.5f}".format(div), iDiv, mod, xPowY)
#}


def main():
#{
    utility()

if __name__ == "__main__":
    main()
#}
