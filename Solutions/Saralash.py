"""Bir o’lchamli sonli massiv berilgan. Massiv elementlarini kamaymaslik
tartibida saralovchi dastur tuzing.
 """
n=int(input())
s=input().split(" ")
for i in range(n):
    s[i]=int(s[i])
s.sort()
ss=""
for i in range(n):
    ss+=str(s[i])+" "
print(ss)
#masala ishlandi