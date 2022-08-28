# https://devsnest.in/algo-challenges/average-between-indices?tab=question

def solve(n, arr, x, y):
   # CODE HERE
   return (sum(arr[x:y+1]))/(y-x+1)
