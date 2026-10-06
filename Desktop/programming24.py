
# x=eval(input("Enter any value: "))
# print(x)
# print(*x)



# OUTPUT:
# PS C:\Users\parth\AppData\Local\Programs\Microsoft VS Code> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming24.
# python
# p y t h o n
# PS C:\Users\parth\AppData\Local\Programs\Microsoft VS Code> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming24.py
# Enter any value: [10,20,30,40]
# [10, 20, 30, 40]
# 10 20 30 40
# PS C:\Users\parth\AppData\Local\Programs\Microsoft VS Code> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming24.py
# Enter any value: (10,20,30,40)
# (10, 20, 30, 40)
# 10 20 30 40


# py
# Enter any value: 10,20,30,40,
# PS C:\Users\parth\AppData\Local\Programs\Microsoft VS Code> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming24.py
# Enter any value: 10,20,30,40
# (10, 20, 30, 40)
# 10 20 30 40


# res=eval(input("Enter any value: "))
# print(res)

# print(*res)
# print(*(*res))


# py
#   File "c:\Users\parth\Desktop\programming24.py", line 23
#     print(*(*res))
#             ^^^^
# SyntaxError: cannot use starred expression here


# def add(x,y):
#     return x+y
# p=10
# q=20
# res=add(x=q,y=p)
# print(res)



 

# def add(x,y):
#     return x+y
# p=10
# q=20
# res=add(x=q,y=p)
# print(res)

# res=add(x=p)



# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming24.py", line 60, in <module>
#     res=add(x=p)
# TypeError: add() missing 1 required positional argument: 'y'


# def add(x,y):
#     return x+y
# p=10
# q=20
# # res=add(x=q,y=p)
# # print(res)


# # res=add(x=p)




# res=add(x=p,y=q,z=r)


# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming24.py", line 79, in <module>
#     res=add(x=p,y=q,z=r)
#                       ^
# NameError: name 'r' is not defined



# def add(x,y):
#     return x+y
# p=10
# q=20
# r=30
# res=add(x=q,y=p)
# print(res)


# res=add(x=p)




# res=add(x=p,y=q,z=r)



# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming24.py", line 107, in <module>
#     res=add(x=p,y=q,z=r)
# TypeError: add() got an unexpected keyword argument 'z'





# def add(x=0,y=0):
#     return x+y
# p=10
# q=20
# # r=30
# res=add(x=q,y=p)
# print(res)


# res=add(x=p)




# res=add(x=p,y=q,z=r)

# OUTPUT:
# py
# 30



# def add(x=0,y=0):
#     return x+y
# p=10
# q=20
# r=30
# res=add()
# res=add(x=p)
# res=add(y=q)
# res=add(x=q,y=p)
# res=add(x=p,y=q,z=r)
# print(res)



# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# add()
# add(x=10)
# add(x=10,y=20,z=30,b=0)


# OUTPUT:
# {}
# <class 'dict'>
# {'x': 10}
# <class 'dict'>
# {'x': 10, 'y': 20, 'z': 30, 'b': 0}
# <class 'dict'>    


# d={'x':10,'y':20,'z':30}
# for i in d:
#     print(f' key is {i} and value is {d[i]}')
#     # print(f' key is {i} and value is {d.get(i)}')
    
    
    
#  key is x and value is 10
#  key is y and value is 20
#  key is z and value is 30    



# d={'x':10,'y':20,'z':30}
# for i in d:
#     # print(f' key is {i} and value is {d[i]}')
#     print(f' key is {i} and value is {d.get(i)}')
    
    
    
#  key is x and value is 10
#  key is y and value is 20
#  key is z and value is 30  




# d={'x':10,'y':20,'z':30}
# for i in d:



# n=int(input("enter any number:"))
# for i in range(1,11):
#     print(f'{n}*{i}= {n*i}')
    
# OUTPUT:    
# 2*1=2
# 2*2=4
# 2*3=6
# 2*4=8
# 2*5=10
# 2*6=12
# 2*7=14
# 2*8=16
# 2*9=18
# 2*10=20    
    