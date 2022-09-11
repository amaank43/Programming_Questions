'''
https://devsnest.in/algo-challenges/path-sum?tab=question
'''

def solve(root, targetSum):
    # CODE HERE
    if root is None:
        return 0
    if not(root.left or root.right):
        return 1 if root.val  == targetSum else 0
    targetSum-=root.val    
    return solve(root.left,targetSum) or solve(root.right,targetSum)
