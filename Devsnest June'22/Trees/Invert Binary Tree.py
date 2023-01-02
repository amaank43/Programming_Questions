'''
https://devsnest.in/algo-challenges/invert-binary-tree?tab=question

'''

def solve(root):
    # CODE HERE
    if root is None:
            return None 
        
    def invert(root):
            
        if not root.left and not root.right:
            return root
        left = root.left
        right = root.right
        root.left = invert(right) if right else None
        root.right = invert(left) if left else None
            
        return root
        
    return invert(root)
