"""
1.	Fibonacci
Write a dynamic programming solution for finding nth Fibonacci members.
•	F0 = 0
•	F1 = 1
Examples
Input	Output
20	     6765
50	     12586269025

"""

def calc_fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    memo[n] = result
    return result


n = int(input())
print(calc_fib(n, {}))