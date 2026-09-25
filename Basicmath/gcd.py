a = 52 
b = 10
while(a>0 and b>0):
    if(a>b):
        a =a%b
    else:
        b= b%a
if(a==0):
    print("gcd:", b)
elif(b==0):
    print("gcd:", a)

