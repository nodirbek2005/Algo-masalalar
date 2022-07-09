"""Bir o`lchamli sonli massivni tоq o`rindagi elеmеntlarini ko`paytmasini
juft o`rindagi elеmntlarini yigindisiga bo`linsin """
n=int(input())
s=input().split(" ")
p=1
sum=0
for i in range(n):
    s[i]=int(s[i])
    if (i-1)%2==1:
        p*=s[i]
    else:
        sum+=s[i]
print("%.2f"%(p/sum))
#masala ishlandi