def stringReverse(s):

    #method1
    return s[::-1]

    #method2
    #return "".join(reversed(s))

    #method3
    """
    revStr = ''
    for char in s:
        revStr = char + revStr

    return revStr
    """

def main():
    s = str(input())
    print(stringReverse(s))

if __name__ == "__main__":
    main()
