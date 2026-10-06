# n=12345
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)    


# OUTPUT:
# 5



# n=12345
# print(len(str(n)))

# OUTPUT:
# 5


# n=int(input ("enter any number:"))
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)  


# enter any number:12345
# 54321  
    
    
    
# n=int(input ("enter any number:"))
# x=n
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if x==rev:
#     print(f' given number {x} is palindrom')
# else:
#      print(f' given number {x} is not palindrom')    
# print(rev)      
# OUTPUT:
# enter any number:1234321
#  given number 1234321 is palindrom
# 1234321

# n=int(input("enter any number:"))
# count=sum=0
# x=y=n
# count=0
# while n>0:
#      count=count+1
#      n=n//10
# while x>0:
#     ld=x%10
#     sum=sum+ld**count
#     x=x//10
# if y==sum:
#     print("Armstrong") 
# else:
#     print("Not a Armstrong")  
    
# enter any number:153
# Armstrong       

# s=input("enter any string:")   
# s1=""
# for i in s:
#     s1 =i+s1
# if  s==s1:
#     print("Palendrom")
# else:
#     print("not a palendrom")     
    
# enter any string:madam
# Palendrom       