'''
https://devsnest.in/algo-challenges/mario-kart?tab=submissions

'''




def solve(mat):
    # CODE HERE
    l=[]
    for i in range(len(mat)):
        l.append(mat[i][1])
    a = list(set(l))
    a.sort()
    temp= a[1]
    res=[]
    for i in range(len(mat)):
        if temp==mat[i][1]:
            res.append(mat[i][0])
    res.sort()
    return res 
