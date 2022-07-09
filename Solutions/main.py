n=int(input())
s=input().split(" ")
b=[]
for i in range(len(s)):
    s[i]=int(s[i])
max=s[0]
for i in range(len(s)):
    if s[i]>max:
        max=s[i]
ss=""
for i in range(len(s)):
    b.append("%.2f"%((s[i])/max))
    ss+=str(b[i])+" "
print(ss)

