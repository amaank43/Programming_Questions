'''
https://devsnest.in/algo-challenges/construct-tree-from-inorder-and-preorder-traversal?tab=question
'''
def solve(n1, n2, preorder, inorder):
    # CODE HERE
    if not preorder or not inorder: 
        return None 
    root = TreeNode(val = preorder[0]) 
    mid = inorder.index(preorder[0]) 
    root.left = solve(n1,n2,preorder[1: mid+1], inorder[:mid]) 
    root.right = solve(n1,n2,preorder[mid+1:], inorder[mid+1 :])

    return root
