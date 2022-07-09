""" Bir o`lchamli sonli massiv M dan katta elеmеntlari
yigindisi хisоblansin"""
n=int(input())
s=input().split(" ")
m=int(input())
sum=0
for i in range(n):
    s[i]=int(s[i])
    if s[i]>m:
        sum+=s[i]
print(sum)
#masala ishlandi