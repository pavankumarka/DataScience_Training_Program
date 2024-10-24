"""
def count_subsequences(S, W):
    count = 0
    len_s = len(S)
    len_w = len(W)

    # List to store the indices of the valid subsequences
    indices_list = []

    def backtrack(s_index, w_index, current_indices):
        nonlocal count

        # If we matched all characters of W
        if w_index == len_w:
            count += 1
            indices_list.append(current_indices[:])  # Store the matching indices
            return

        # If we've gone through all characters in S
        if s_index == len_s:
            return

        # Explore the case where we include the current character if it matches
        if S[s_index] == W[w_index]:
            current_indices.append(s_index)  # Record the index
            backtrack(s_index + 1, w_index + 1, current_indices)  # Move to the next character in W
            current_indices.pop()  # Backtrack

        # Explore the case where we skip the current character in S
        backtrack(s_index + 1, w_index, current_indices)

    # Start the backtracking from the first character of S and W
    backtrack(0, 0, [])

    # Filter out duplicate subsequences by creating a set of tuples
    unique_indices = []
    seen = set()

    for indices in indices_list:
        tuple_indices = tuple(indices)
        if tuple_indices not in seen:
            seen.add(tuple_indices)
            unique_indices.append(indices)

    return len(unique_indices), unique_indices

# Example usage
S = "abcdrtbwerrcokokokd"
W = "bcd"
result, subseq_indices = count_subsequences(S, W)
print(f"The number of times '{W}' appears as a subsequence in '{S}' is: {result}")
print("The indices of the subsequences are:", subseq_indices)
"""


class Solution:
    def numberOfSubsequences (self,S,W):
        # code here
        S = list(S)
        W = list(W)
        ans = 0

        while True:
            i = 0
            j = 0
            flag = 0

            while i < len(S):
                if S[i] == W[j]:
                    j += 1;
                    S[i] = '*' #mark as used
                if j == len(W):
                    ans += 1 #sunseq found
                    flag = 1
                    break
                i += 1
            if flag == 0:
                break #no subseq found

        return ans

def main():
    S = "abcdrtbwerrcokokokd"
    W = "bcd"

    ob = Solution()
    print(ob.numberOfSubsequences (S,W))

if __name__ == "__main__":
    main()


"""
#User function Template for python3
class Solution:
    def numberOfSubsequences (self,S,W):
        # code here
        n = len(S)
        m = len(W)
        count = 0  # To count the number of subsequences

        used = [False] * n  # To mark used characters of S

        for i in range(n):
            if S[i] == W[0] and not used[i]:  # Start searching if it's the first char of W and not used
                k = 0  # Pointer to traverse W
                for j in range(i, n):
                    if S[j] == W[k] and not used[j]:  # Only consider unused characters
                        used[j] = True  # Mark this character as used
                        k += 1  # Move to the next character of W
                    if k == m:  # If we matched the entire W
                        count += 1
                        break  # Stop searching for this subsequence
        return count

"""
