n1,l1,r1=map(int,input().split(" "))
n=int(n1)
l=int(l1)
r=int(r1)
s=input().split(" ")
k=0
for i in range(len(s)):
    s[i]=int(s[i])
for i in range(l,r+1):
    #print(i)
    for j in range(len(s)):
        #print(s[j])
        if i%s[j]==0:
           k+=1
print(k-1)
