N = 7789 
c = 0
while(N>0):
    L_d = N%10 
    c=c+1
    N = N//10
    print(L_d)
print(c)