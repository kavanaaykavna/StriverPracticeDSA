N = 11111
o=N
r = 0
while(N>0):
    ld = N%10 
    N = N//10
    r = (r*10)+ld
print(r)
if r==o:
    print("true")
else:
    print("false")


