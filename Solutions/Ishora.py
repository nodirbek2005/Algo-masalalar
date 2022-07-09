a,b=map(int,input().split(" "))
A=int(a)
B=int(b)
if A>0 and B>0:
    print("+")
elif A>0 and B<0:
    print("+")
elif A<0 and B%2==0:
    print("+")
else:
    print("-")
#masala ishlandi