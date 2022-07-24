def solve(s1, s2):
    # CODE HERE
    if sorted(s1)==sorted(s2):
        return 1 #true
    else: #false
        return 0
#calling funtion        
x='dusty'
y='study'
print(solve(x,y))