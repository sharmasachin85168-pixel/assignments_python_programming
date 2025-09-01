# task_1
a=int(input("enter the first number"))
b=int(input("enter the second number"))
s=int(input(" 1.add\n 2.sub\n 3.mul\n 4.div"))
if s==1:
    print(a+b)
elif s==2:
    print(a-b)
elif s==3:
    print(a*b)
elif s==4:
    print(a/b)
else:
    print("enter the valid choice")

#task_2
f_n=input("enter the first name :")
l_n=input("enter the last name:")
full_name=f_n + " "+ l_n

print("hello ",full_name," ! welcome to python programming")
