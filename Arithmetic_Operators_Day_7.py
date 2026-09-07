x = int(input())
y = int(input())

result=""

p=x+y
result+=str(p)+" "
q=x-y
result+=str(q)+" "
r=x*y
result+=str(r)+" "
s=float(x/y)
result+=format(s,".3f")+" "
t=x//y
result+=str(t)+" "
u=x%y
result+=str(u)+" "



print(p, q, r, f"{s:.3f}", t, u)
