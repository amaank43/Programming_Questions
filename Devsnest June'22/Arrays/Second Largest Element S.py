"""https://devsnest.in/algo-challenges/second-largest-element?tab=question"""


def solve(n, arr):
    # CODE HERE
   arr = set(arr)
   arr.remove(max(arr))
   return max(arr)
