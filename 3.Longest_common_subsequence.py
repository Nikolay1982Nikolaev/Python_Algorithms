"""
3.	Longest Common Subsequence
Considering two sequences S1 and S2, the longest common subsequence is a sequence that is a subsequence of both S1 and S2. For instance, if we have two strings (sequences of characters), "abc" and "adb", the LCS is "ab" – it is a subsequence of both sequences and it is the longest (there are two other subsequences – "a" and "b").
Input
•	On the first line, you will receive a string – str1 – first string.
•	On the second line, you will receive a string – str2 – second string.
Output
•	Print the length of the longest common subsequence.
Examples
Input       	Output
abc
adb
                 2
ink some beer
drink se ber
                10
tree
team
                2

"""



first =  "tree"
second = "team"
#first = input()
#second = input()
rows = len(first) + 1
cols = len(second) + 1

dp = []
[dp.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

print(dp[rows - 1][cols - 1])


"""
row = rows - 1
col = cols - 1
result = []

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        result.append(first[row - 1])
        row -= 1
        col -= 1
    elif dp[row - 1][col] > dp[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(result)
"""