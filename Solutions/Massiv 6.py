""" Bir o`lchamli sonli massiv elеmеntlarini kvadratlarini
yigindisi хisоblansin"""
n=int(input())
s=input().split(" ")
sum=0
for i in range(n):
    s[i]=int(s[i])
    sum+=(s[i]*s[i])
print(sum)
#masala ishlandi