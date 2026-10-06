# def add(x,y):
#     return x+y
# p=int(input("enter any number:"))
# q=int(input("enter any number:"))
# res=add(p,q)
# print(res)


# OUTPUT:
# enter any number:10
# enter any number:20
# 30


# def add(x,y):
#     return x+y
# p=int(input("enter any number:"))
# q=int(input("enter any number:"))
# res=add(p)
# print(res)


# OUTPUT:
# enter any number:10
# enter any number:20
# Traceback (most recent call last):
#   File "C:\Users\parth\Desktop\programming19.py", line 19, in <module>
#     res=add(p)
# TypeError: add() missing 1 required positional argument: 'y'




# def add(x,y):
#     return x+y
# p=int(input("enter any number:"))
# q=int(input("enter any number:"))
# res=add(p,q,r)
# print(res)


# OUTPUT:
# enter any number:10
# enter any number:20
# Traceback (most recent call last):
#   File "C:\Users\parth\Desktop\programming19.py", line 38, in <module>
#     res=add(p,q,r)
#                 ^
# NameError: name 'r' is not defined





# def add(x,y):
#     return x+y
# p=int(input("enter any number:"))
# q=int(input("enter any number:"))
# r=int(input("enter any number:"))
# res=add(p,q,r)
# print(res)

# output:
# enter any number:10
# enter any number:20
# enter any number:30
# Traceback (most recent call last):
#   File "C:\Users\parth\Desktop\programming19.py", line 51, in <module>
#     res=add(p,q,r)
# TypeError: add() takes 2 positional arguments but 3 were given


# def add(x=0,y=0):
#     return x+y
# print(add())

# OUTPUT:
# 0



# def add(x=0,y=0):
#     return x+y
# print(add(10))

# OUTPUT:
# 10



# def add(x=0,y=0):
#     return x+y
# print(add(10,20))


# OUTPUT:
# 30

# def add(x=0,y=0):
#     return x+y
# print(add(10,20,30,40,50))

# OUTPUT:
# Traceback (most recent call last):
#   File "C:\Users\parth\Desktop\programming19.py", line 90, in <module>
#     print(add(10,20,30,40,50))
#           ~~~^^^^^^^^^^^^^^^^
# TypeError: add() takes from 0 to 2 positional arguments but 5 were given


# def add(*args):
#     print(args)
#     print(type(args))
# add()    


# OUTPUT:
# ()
# <class 'tuple'>


# def add(*args):
#     print(args)
#     print(type(args))
# add(10)    

# (10,)
# <class 'tuple'>


# def add(*args):
#     print(args)
#     print(type(args))
# add(10,20,30,40,50)    





# (10, 20, 30, 40, 50)
# <class 'tuple'>