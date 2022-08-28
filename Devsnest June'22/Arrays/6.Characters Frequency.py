# https://devsnest.in/algo-challenges/characters-frequency?tab=question

def solve(str1):
   # CODE HERE
    li = []
    j = []
    

    for i in str1:
        if i not in j:
            li.append(str1.count(i)) 
            j.append(i)
    return li
