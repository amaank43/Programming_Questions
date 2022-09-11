'''
https://devsnest.in/algo-challenges/even-odd-tree?tab=question
'''
def solve(root):
    # CODE HERE
        hash={} 
        q=[]
        q.append([root,0])
        while(len(q)>0):
            rem=q.pop(0)
            node=rem[0]
            if rem[1] not in hash:
                hash[rem[1]]=[]
                if rem[1]&1==0 and node.val&1==0:
                    return 0
                elif rem[1]&1!=0 and node.val&1!=0:
                    return 0
                hash[rem[1]].append(node.val)
            else:
                if rem[1]&1==0:
                    if hash[rem[1]][-1]>=node.val or node.val&1==0:
                        return 0
                    else:
                        hash[rem[1]].append(node.val)
                else:
                    if hash[rem[1]][-1]<=node.val or node.val&1!=0:
                        return 0
                    else:
                        hash[rem[1]].append(node.val)
            
            
            
            if node.left:
                q.append([node.left,rem[1]+1])
            if node.right:
                q.append([node.right,rem[1]+1])
        return 1
