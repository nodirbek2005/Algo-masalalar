t=int(input())
a=[]
p=0
for i in range(t):
    k=input()
    a.append(k)
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(len(a)):
    print(a[i])