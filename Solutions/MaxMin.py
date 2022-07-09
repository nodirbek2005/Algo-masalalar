n=int(input())
s=input()
for i in range(n):
    max=s[i]
    for j in range(len(s)):
        if s[j]>max:
            max=s[j]
for k in range(n):
    min=s[k]
    for q in range(len(s)):
        if s[q]<min:
            min=s[q]
print(min,max)
#masala oxiriga yetmadi xali