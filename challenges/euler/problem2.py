"""
Title: Even Fibonacci Numbers
Description:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with  and , the first terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89 [...]

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Link: https://projecteuler.net/problem=2
"""

prev, cur = 0, 1
total = 0
while True:
    prev, cur = cur, prev + cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
        total += cur
    
print(total)