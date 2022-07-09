"""Asosining bir burchagi bo’lgan to’g’ri burchakli uchburchakning gipotenuzasi  ga teng.
 Uchburchakning perimetri va gipotenuzaga tushirilgan balandlikni toping. """
import math
c=float(input())
b=c/2
a="%.2f"%(math.sqrt(c**2-b**2))
S=(1/2)*float(a)*float(b)
p=a+float(b)+c
h=2*S/c
print("%.2f"%p,"%.2f"%S)