class Solution:
    def isPalin(self, N):
        """
        #palStr = str(N)
        if (N == int(str(N)[::-1])):
            return 1
        else:
            return 0
        """
        return N == int(str(N)[::-1])

def main():
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        obj = Solution()
        print(int(obj.isPalin(n)))

if __name__ == "__main__":
    main()
