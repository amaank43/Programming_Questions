'''
https://devsnest.in/algo-challenges/longest-zigzag-path-in-a-binary-tree?tab=question
'''

def solve(root):
    # CODE HERE
     def f(root, k, isleft): 
        if root: 
          if isleft: 
               return max(f(root.left,1,True), f(root.right, k+1, False)) 
          else: 
               return max(f(root.left, k+1, True), f(root.right, 1, False)) 
        return k-1
     return f(root,0,True)
