"""Sizga butun n soni beriladi, sizning vazifangiz bu son qandaydir butun
sonning kvadrati bo’la oladimi yoki yo’qligini tekshirishdan iborat. """
n=int(input())
k=0
for i in  range(n):
    if i*i==n:
       k+=1
if k==0:
    print("NO")
else:
    print("YES")
#masala ishlandi