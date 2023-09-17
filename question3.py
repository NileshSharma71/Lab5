N=int(input("Enter: "))
kl=N
jk=kl
k="*"
i=0
#3a
while True:
    i+=1
    print(k*i)
    if i==N:
        break
#3b
a=0
l=" "
while True:
    a+=1
    print(l*(N-1),k*a)
    N-=1
    if a==kl:
        break
#3c
q=1
while True:    
    print(kl*l,k*q,kl*l)
    q+=2
    kl-=1
    if q>jk:
        break
    