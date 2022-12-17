h=int(input("the hight of the diamond:"))
for i in range(h):
    print(" "*(h-i),"*"*(i*2+1))
for j in range(h-2,-1,-1):
    print(" "*(h-j),"*"*(j*2+1))