"""https://devsnest.in/algo-challenges/maximum-product-subarray?tab=question"""

def solve(n, arr):
    # CODE HERE
        res = max(arr)
        curMin, curMax = 1, 1 
        for n in arr:
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin * n, n)
            res = max(res, curMax)
        return res
