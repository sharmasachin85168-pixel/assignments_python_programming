#task_1
try:
    with open ('E:\python-program\sample.txt', 'r') as file:
        data=file.read()
        for line in data.split('\n'):
            print(line)
except FileNotFoundError:
    print("the file sample.txt not found")
finally:
    print("thankyou for using program")


#task_2

with open ('E:\python-program\sample.txt', 'a') as file1:
    appending=input("enter the text which you want to append :")
    file1.write("\n"+appending)
    print("the text is appending successfully")

with open('E:\python-program\sample.txt', 'r')as file3:
    data=file3.read()
    print(data)
    





