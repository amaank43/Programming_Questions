'''
https://devsnest.in/algo-challenges/diameter-of-the-binary-tree?tab=question
'''
def solve(root):
    # CODE HERE
        res = []
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)
        dfs(root)
        return res[0]
