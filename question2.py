N=int(input("Enter: "))
count=0
i=0
while True:
    i+=1
    if i==1001:
        break
    if i%N==0:
        continue
    count+=1
    
print("Total number that are not divisible by",N,"and lie between 1 and 1000\
 are",count)