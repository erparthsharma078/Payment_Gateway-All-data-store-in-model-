# x=10
# print(type(x))
# x=(10)
# print(type(x))
# x=10,
# print(type(x))
# x=(10,)
# print(type(x))


# <class 'int'>
# <class 'int'>
# <class 'tuple'>
# <class 'tuple'>

# x=10
# print(type(x))
# print(type(x=10))



# OUTPUT:
# <class 'int'>
# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming23.py", line 18, in <module>
#     print(type(x=10))
#           ~~~~^^^^^^
# TypeError: type() takes 1 or 3 arguments




# def   add(*n):
#     print(n)
#     print(type(n))
# add(10,20,30,40)      

# OUTPUT:
# (10, 20, 30, 40)
# <class 'tuple'>




# def add(*n):
#     res=sum(n)
#     return res
# result=add(10,20,30,40)
# print(result)

# `OUTPUT:
# 100`



# s=(10,20,30,40)
# sum=0
# for i in s:
#     sum=sum+i
# print(sum)  


# OUTPUT:
# 100  



# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# result=add(10,20,30,40) 
# print(result)   
    
# OUTPUT: 
# 100


# def add(*n):
#     print(n)
#     print(type(n))
# x=eval(input("enter values:"))
# res=add(x)

# OUTPUT:
# enter values:(10,20,30,40)
# ((10, 20, 30, 40),)
# <class 'tuple'>


# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum    
    
# x=eval(input("enter values:"))
# res=add(x)
# print(res)


# OUTPUT:
# enter values:(10,20,30,40)
# 100


x=eval(input("Enter any value: "))
print(x)
print(*x)