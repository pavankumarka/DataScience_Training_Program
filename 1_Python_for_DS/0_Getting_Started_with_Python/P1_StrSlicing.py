def sliceString(s):
    #Write your code below
    return s[1:-1]



#{
 # Driver Code Starts.




def main():
    t=int(input())
    while(t>0):
        s=input()
        print(sliceString(s))
        t-=1

if __name__ == "__main__":
    main()
# } Driver Code Ends
