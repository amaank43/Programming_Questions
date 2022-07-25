
def solve(n):
   # CODE HERE
  return [(((10**i)-1)//9)**2 for i in range(1, n+1)]
