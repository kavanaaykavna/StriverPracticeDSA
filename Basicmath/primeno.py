import math 

N = 7
l = []
c = 0
i = 1

while i <= int(math.sqrt(N)):
    if N % i == 0:
        l.append(i)
        c=c+1

        if N // i != i:
            l.append(N // i)
            c = c+1

    i += 1 
if(c==2):
    print("yes prime")
else:
    print("no")
