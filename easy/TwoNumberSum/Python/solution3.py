# Time O(n) | Space: O(1)

def getNthFib(n):
    # Write your code here.
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        fibnum = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = fibnum
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
