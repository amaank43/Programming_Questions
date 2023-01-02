'''
https://devsnest.in/algo-challenges/construct-tree-from-inorder-and-postorder-traversal?tab=question
'''

def solve(n1, inorder, n2, postorder):
    # CODE HERE
    def construct(temp,inorder,start, end, postorder):
            if start > end:
                return None
            
            root = postorder.pop()
            node = TreeNode(root)
            index = temp[root]
            
            node.right = construct(temp, inorder, index+1, end, postorder)
            node.left = construct(temp, inorder, start, index-1, postorder)
            return node   
    temp = dict()
    for i,v in enumerate(inorder):
        temp[v] = i
    if len(postorder) == 1:
            return TreeNode(postorder.pop())
    else:
        return construct(temp, inorder,0, len(inorder)-1, postorder)
