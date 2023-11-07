x,y=map(int,input("Enter the numbers").split())
print("You entered numbers",x,y)
temp = x
x = y
y = temp
print("Swapped numbers are","x = ",x,"y = ",y)
