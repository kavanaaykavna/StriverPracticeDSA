def f(i,Sum):
    if(i<1):
        print(Sum)
        return 
   
    f(i-1 , Sum+i)

f(5, 0)