def solve(n, arr):
  sumNatural=int((n*(n+1)/2))
  sum=0
  for i in range(0,n):
    sum+=arr[i]
  return abs(sumNatural-sum)


##############
def solve(n, arr):
    # CODE HERE
    sumNatural=(n*(n+1))//2
    s=sum(arr)
    return abs(s-sumNatural)
