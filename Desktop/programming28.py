# def outer():
#     x=10
#     def inner():
#         print(x)
#         x=20
#         return x
#     res=inner()
#     return res
# result=outer()
# print(result)    

# OUTPUT:
# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming28.py", line 9, in <module>
#     result=outer()
#   File "c:\Users\parth\Desktop\programming28.py", line 7, in outer
#     res=inner()
#   File "c:\Users\parth\Desktop\programming28.py", line 4, in inner
#     print(x)
#           ^
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value



# def outer():
#     x=10
#     def inner():
#         nonlocal x
#         print(x)
#         x=20
#         return x
#     res=inner()
#     return res
# result=outer()
# print(result)   


# OUTPUT:
# 10
# 20

# x=range(2)
# print(x)