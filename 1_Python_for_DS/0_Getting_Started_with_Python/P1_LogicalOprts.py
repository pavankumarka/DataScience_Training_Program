def utility():
    a = int(input())
    b = int(input())

    c = a and b

    d = a or b

    e = not a

    print(c,d,e, sep=" ")

    if( a == 2 and b == 3):
        print(True)

def main():
    utility()

if __name__ == "__main__":
    main()
