'''
https://devsnest.in/algo-challenges/flatten-tree-to-linked-list?tab=question

'''


def solve(root):
    # CODE HERE
    curr=root
    while(curr):
        if(curr.left):
            pred=curr.left
            while(pred.right):
                pred=pred.right
            pred.right=curr.right
            curr.right=curr.left
            curr.left=None
        curr=curr.right
    return root
