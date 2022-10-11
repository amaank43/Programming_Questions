"""https://devsnest.in/algo-challenges/two-sum?tab=question"""

def solve(n, nums, target):
    # CODE HERE
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return hashMap[diff], i
            hashMap[n] = i
