def name(i , n):
    if(i>n):
        return 
    
    name(i+1, n )
    print(i)

name(1,4)