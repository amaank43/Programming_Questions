'''
https://devsnest.in/algo-challenges/same-tree?tab=question
'''

def solve(p, q):
    # CODE HERE
    if (p is None and q is None): 
        return 1
    if (q is None or p is None) :
        return 0
    if (p.val != q.val): 
        return 0
    if(solve(p.right, q.right) != 1):
        return 0
    if(solve(p.left, q.left) !=1):
        return 0
    return 1
