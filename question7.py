N=int(input("Enter: "))
kl=N
i=0
k="*"
l=" "
while i<=N:    
    j=1
    while j<=N-1:
        print(l,end=" ")
        j+=1
    j=1
    while j<=2*i-1:
        print(k,end=" ")
        j+=1
    j=1
    while j<=N-1:
        print(l,end=" ")
        j+=1
    print()
    i+=1
    N-=1
    if i==kl:
        break