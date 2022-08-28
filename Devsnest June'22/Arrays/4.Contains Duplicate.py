# https://devsnest.in/algo-challenges/contains-duplicate?tab=question

def solve(n, arr):
    # CODE HERE 
     if len(set(arr))==len(arr): 
         return 0 
     else: 
         return 1
