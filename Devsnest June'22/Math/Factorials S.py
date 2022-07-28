#Recursive

'''

def solve(n):
    # CODE HERE
    if n==1 or n==0:
      return 1
    else:
     return (n)*(solve(n-1))
     
'''

#Iterative
def solve(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return (fact)
