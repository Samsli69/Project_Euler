max = 0

def retournement(n):
    Reverse = 0    
    while(n > 0):    
        Reminder = n %10    
        Reverse = (Reverse *10) + Reminder    
        n = n // 10
    return Reverse


for x in range(100, 1000):
    for k in range(100,1000):
        if retournement(x*k) == x*k and max < x*k:
            max = x*k

print(max)




