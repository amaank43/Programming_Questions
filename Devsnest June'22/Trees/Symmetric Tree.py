'''

https://devsnest.in/algo-challenges/symmetric-tree?tab=question
'''

def symtree(p,q):
    if p is None and q is None:
        return 1
    if not(p) and q or p and not(q):
        return 0
    
    return int(p.val==q.val and symtree(p.left,q.right) and symtree(p.right,q.left))

def solve(root):
    # CODE HERE
    return symtree(root.left,root.right)
