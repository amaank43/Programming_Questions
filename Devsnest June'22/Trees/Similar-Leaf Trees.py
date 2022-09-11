'''
https://devsnest.in/algo-challenges/similar-leaf-trees?tab=question
'''

def solve(root1, root2):
    # CODE HERE
        tree=[]
        def inorder(root):
            nonlocal tree
            if root is None:
                return
            if root.left is None and root.right is None:
                tree.append(root.val)
            
            inorder(root.left)
            inorder(root.right)
        
        inorder(root1)
        inorder(root2)
        tree1=tree[:len(tree)//2]
        tree2=tree[len(tree)//2:]
        if tree1==tree2:
            return 1
        else:
            return 0
