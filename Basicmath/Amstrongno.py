N = 371
o = N
s = 0
while(N>0):
    L_d = N%10 
    s = s + (L_d**3)
    N = N//10
if(s==o):
    print("amstrong num")
else:
    print("no")
