#task_1
dict = {'sachin': 80, 'sumit': 79, 'rohit': 77, 'sattu': 50}
n = input("enter the student name :")
if n in dict:
    print("student {} has {} marks".format(n, dict[n]))
else:
    print("student {} not found".format(n))
   
#task_2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
list3 = []
for i in range(0, 5):
    list2.append(list1[i])
n = len(list2)-1
for i in range(n, -1, -1):
    list3.append(list2[i])
print("orginal list : ", list1)
print("extracted first five elements : ", list2)
print("reversed extracted five elements : ", list3)


