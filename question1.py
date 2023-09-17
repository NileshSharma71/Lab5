N=int(input("Enter value between 1 to 20: "))
o=1
if N>=1 and N<=20:
    while True: 
        i=1       
        while True:            
            print(f"{o} x {i} = {o*i}")           
            i=i+1        
            if i==21:
                break
        o+=1
        if o==(N+1):
            break
else:
    print("Enter value between 1 and 20!!!")