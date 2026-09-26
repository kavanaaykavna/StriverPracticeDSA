def name(i , n):
    if(i<1):
        return 
    
    name(i-1, n )
    print(i)

name(4,4)