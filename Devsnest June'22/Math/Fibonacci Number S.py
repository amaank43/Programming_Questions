#Recursive solution

def solve(n):
  if n<0:
    return "incorrect input"
  elif n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    return solve(n-1)+solve(n-2)
  
  #Iterative
  
  
