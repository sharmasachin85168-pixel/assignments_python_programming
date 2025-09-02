#task_1
n=int(input("enter the number which you want factorial :"))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
fact=factorial(n)
print("the factorial of ",n,"is :",fact)


#task_2
import math
n=int(input(" 1.Square root of the numbee\n 2.Natural logarithm (log base e) of the number\n 3.Sine of the number (in radians)"))
p=int(input("enter the number :"))
if n==1:
    square_root=math.sqrt(p)
    print("the squareroot is :",square_root)
elif n==2:
    log=math.log(p)
    print("the natural logarithm is :",log)
elif n==3:
    sine=math.sin(p)
    print("the sie is :",sine)
else:
    print("enter the valid choice")