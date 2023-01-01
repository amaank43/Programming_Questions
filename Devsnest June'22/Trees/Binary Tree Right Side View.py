'''
https://devsnest.in/algo-challenges/binary-tree-right-side-view?tab=question
'''
def solve(root):
    # CODE HERE
        res=[]
        if root==None:
            return res
        q=[]
        q.append(root)
        while(len(q)):
            res.append(q[len(q)-1].val)
            for i in range(len(q)):
                temp=q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return res
