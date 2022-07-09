s=input().split(":")
for i in range(len(s)):
    s[i]=int(s[i])
s.sort()
ss=""
for i in range(len(s)):
    ss+=str(s[i])+" "
print(ss)
