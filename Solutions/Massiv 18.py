n=int(input())
s=input().split(" ")
d=[]
k=0
for i in range(n):
    s[i]=int(s[i])
    if s[i]%2==1:
        d.append(s[i])
for i in range(len(d)):
    d[i]=int(d[i])
    k+=d[i]
print("%.2f"%(k/len(d)))
