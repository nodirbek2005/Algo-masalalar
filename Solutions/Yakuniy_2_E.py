n1,a1,b1=map(int,input().split(" "))
n=int(n1)
a=int(a1)
b=int(b1)
S=0
for x in range(1,n+1):
    S+=(a*x+b)**2
print(S)