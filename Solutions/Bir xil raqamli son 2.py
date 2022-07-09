s=1
n=int(input())
d=[]
while s<n:
    s+=1
    if s%n==0:
        for i in range(len(str(s))):
            s[i]=int(s[i])
            if s[i]==s[i+1]:
                d.append(i)
print(d)