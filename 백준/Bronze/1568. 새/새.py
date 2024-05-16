M = int(input()) 
B = 1 
time = 0

while M > 0: 
    if M >= B:
        M -= B  
        B += 1 
        time += 1  
    else:
        B = 1  

print(time) 