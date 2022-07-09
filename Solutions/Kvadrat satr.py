s=input()
n=len(s)
k=int(n/2)
for i in range(0,k+1):
    for j in range(k,n+1):
        if str(s[i])==str(s[j]):
            print(s[i],s[j])
            print("YES")
        else:
            print("NO")
#misol to'liq yechilmadi