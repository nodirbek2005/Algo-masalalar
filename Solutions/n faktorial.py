import math
n=int(input())
k=math.factorial(n)
s=str(k)
t=0
for i in range(len(s)):
    if s[i]=='1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9':
        if str(s[i][i+1])=='0':
            t+=1
print(t)
