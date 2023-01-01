'''
https://devsnest.in/algo-challenges/common-parent?tab=question
'''

def solve(root, p, q):
    # CODE HERE
    if root is None or root.val in {p,q}:

        return root
    
    left = solve(root.left,p,q) 

    right = solve(root.right,p,q)
    
    return root if left and right else left or right
