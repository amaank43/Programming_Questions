'''
https://devsnest.in/algo-challenges/balanced-binary-tree?tab=question
'''

def solve(root):
    # CODE HERE
    def f(root): 
        if not root: 
            return 0 
        return 1 + max(f(root.left),f(root.right))

    r1 = f(root.left)
    r2 = f(root.right)
    if r1 +1 == r2 or r2 +1 == r1 or r1==r2:
        return 1
    else:
        return 0
