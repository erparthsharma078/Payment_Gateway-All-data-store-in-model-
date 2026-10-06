# def add():
#     x=10
#     y=20
#     print(x+y)
#     print(x)
# add()
# print(x)    


# OUTPUT:
# 30
# 10
# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming25.py", line 7, in <module>
#     print(x)
#           ^
# NameError: name 'x' is not defined




# x=10
# y=20
# def add():
#     print(x+y)
# add()
# print(x,y)    


# PS C:\Users\parth> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming25.py
# 30
# 10 20


# x=10
# def display():
#     print(x)
#     x=20
#     print(x)
# display()    


# Traceback (most recent call last):
#   File "c:\Users\parth\Desktop\programming25.py", line 40, in <module>
#     display()
#     ~~~~~~~^^
#   File "c:\Users\parth\Desktop\programming25.py", line 37, in display
#     print(x)
#           ^
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value


# x=10
# def display():
#     print(x)
#     y=20
#     print(x)
# display() 


# PS C:\Users\parth> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming25.py
# 10
# 10



# x=10
# def display():
#     x=20
#     print(x)
# display() 
# print(x)


# PS C:\Users\parth> & C:\Users\parth\AppData\Local\Programs\Python\Python314\python.exe c:/Users/parth/Desktop/programming25.py
# 20
# 10





# x=10
# def display():
#     global x
#     x=20
#     print(x)
# print(x)
# display() 
# print(x)


# 10
# 20
# 20
    
    
# x=10
# def display():
#     x=20
#     print(x)
#     print(globals()['x'])
# display()    

# OUTPUT:
# 20
# 10

    
# x=10
# def display():
#     global x
#     x=20
#     print(x)
#     print(globals()['x'])
# display()    

# OUTPUT:
# 20
# 20