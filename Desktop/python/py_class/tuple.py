t1=(2,4,6,8)
t2=(2,4,6,'python')
print(t1,type(t1))
print(t2,type(t2))
d1={'X':10,'Y':20,'Z':30}
d2={'X':10,'Y':10,'Z':30}
print(d1,d2,type(d1),type(d2))
s = {10,20,30,10,20,30,"python"}
print(s , type(s))
fs = frozenset({10,20,30,10,20,30,"python"})
print(fs,type(fs))

fs = frozenset([10,20,30,10,20,30,"python"])
print(fs,type(fs))

fs = frozenset((10,20,30,10,20,30,"python"))
print(fs,type(fs))

fs = frozenset("python")
print(fs,type(fs))
x=True
print(x,type(x))
print(x=10)

x=None
print(x,type(x))
x=10
y=10
print(id(x),id(y))
t1=(2,4,6,8)
t2=(2,4,6,8)
print(id(t1))
print(id(t2))
d1={'X':10,'Y':20,'Z':30}
d2={'X':10,'Y':20,'Z':30}
print(id(d1),id(d2))
s1 = {10,20,30,10,20,30,"python"}
s2 = {10,20,30,10,20,30,"python"}
print(id(s2) , id(s1))
f1 = frozenset({10,20,30,10,20,30,"python"})
f2 = frozenset({10,20,30,10,20,30,"python"})
print(id(f1),id(f2))

fs = frozenset([10,20,30,10,20,30,"python"])
print(fs,type(fs))

fs = frozenset((10,20,30,10,20,30,"python"))
print(fs,type(fs))

fs = frozenset("python")
print(fs,type(fs))
x=True
print(x,type(x))
x=None
print(x,type(x))
x=10
y=10
print(id(x),id(y))
print(x:=10)
