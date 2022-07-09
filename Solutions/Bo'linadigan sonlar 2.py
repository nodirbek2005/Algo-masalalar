a1,b1,l1,r1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
l=int(l1)
r=int(r1)
k=0
for i in range(l,r+1):
    if i%a==0 or i%b==0:
        k+=1
print(k)
#time limit berdi