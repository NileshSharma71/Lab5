N=int(input("Enter the value of divisor: "))
c=0
d=0
while True:
    n=int(input("Enter: "))
    if n==-999:
        break
    if n%N==0:
        c+=1
    if n%N!=0:
        d+=1
print(f"total number of inputs that are divisible by {N} are \
{c}")
print(f"total number of inputs that are not divisible by {N} are \
{d}")
