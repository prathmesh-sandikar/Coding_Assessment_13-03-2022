
'''for i in [1,2,3,4]:
    print('hi')
print('program ends')'''
"""a = ['tom','python', 'sam']
b ={}
for i in a:
    b[i] = len(i)
print(b)"""

"""a = ['tom','python', 'sam']
b = [85,98,91]
c = []
for i in range(len(a)):
    c.append((a[i],b[i]))
print(c)"""

"""a = 33
b = 200
if b > a:
print("b is greater than a")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
"""
"""mySum = 0
num = 1
while num <= 10:
    mySum += num
    num += 1
"""



"""num = 9
count = 0
for i in range(2,num+1):
  if num%i==0:
    count = 1
    break
if count == 1:
  print('No. is not Prime')
else:
  print(" No. is Prime")"""

"""num = 5
flag = 0
for i in range(2,num+1):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")"""

"""num = int(input("enter no."))

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")"""

    """def name_adder(list):
         i = 0
         new_list = []
         while i < len(list):
             if list[i] != "":
                 new_list.append(list[i])
             i = i+1
         return new_list
     lst1=["Tapan", "Prathmesh","Sawant", "Sandy", "johny"]
     i=0
     print(name_adder(lst1))"""

 """def name_adder(list):
     i = 0
     new_list = []
     while i < len(list):
         if list[i] != "":
             new_list.append(list[i])
         i = i+1
     return new_list

 lst1=["Tapan", "Prathmesh","","Sawant", "Sandy", "johny"]
 i=0
print(name_adder(lst1))"""

"""def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list

lst1=["Tapan", "Prathmesh","","Sawant", "Sandy", "johny"]
i=0
print(name_adder(lst1))"""

"""def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list

lst1=["Tapan", "Prathmesh","","Sawant", "Sandy", "johny"]
i=0
print(name_adder(lst1))"""

"""lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
for i in lst1:
    lst2.append("Dr. " + i)
print(lst2)"""

"""lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
for i in lst1:
    lst2.append(type(i))
print(lst2)"""

"""def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list
"""
"""lst1=["rahul", "ashwin","","Sahil", "Sandy", "johny"]
i=0
print(name_adder(lst1))"""


"""def name_adder(list):
    i = 0
    new_list = []
    while i < len(list):
        if list[i] != "":
            new_list.append(list[i])
        i = i+1
    return new_list

lst1=["sahil", "Prathmesh","","rahul", "Sandy", "monty"]
i=0
print(name_adder(lst1))"""


"""def fourDigit():
    num = input("Enter a 4 digit number: ")
    if (len(num) == 4 and string.digits == True):
        some = int(int(val[1]) + int(val[3]))
        print("The sum of the 1st and second term is: ")
    else:
       print("Error!")"""

"""import string
import math
def fourDigit():
    num = raw_input("Enter a 4 digit number: ")
    if (len(num) == 4 and string.digits == True):
        some = int(int(val[1]) + int(val[3]))
        print("The sum of the 1st and second term is: ")
    else:
       print("Error!")
"""

"""a = int(input("Number of classes held:"))
b = int(input("Number of classes attended:"))

per = b/a*100

if per >= 75:
    print("The student is allowed to sit in exam")
else:
    print("The student is not allowed to sit in exam")"""


"""age1=int(input('enter age1: '))
age2=int(input('enter age2: '))
age3=int(input('enter age3: '))
if age1>age2 and age1>age3:
    print('age1 is oldest')
elif age2>age1 and age2>age3:
    print('age2 is oldest')
else:
    print('age3 is oldest')
if age1<age2 and age1<age3:
    print('age1 is youngest')
elif age2<age1 and age2<age3:
    print('age2 is youngest')
else:
     print('age3 is youngest')
"""

"""score = input("Enter your score")
score = int(score)
if score < 25:
    print("F")

elif score >= 25 and score < 45:
    print("E")

elif score >= 45 and score < 50:
    print("D")

elif score >= 50 and score < 60:
    print("C")

elif score >= 60 and score < 80:
    print("B")
else:
    print("A")
"""


"""a = ['tom','jack','john']
b = [85,98,91]
c = []
for i in range(len(a)):
    c.append((a[i],b[i]))
    result = dict(c)
print(result)"""


"""my_func1()
print('-'*50)
for i in range(5):
    my_func1()
print('!'*50)
a = my_func1()
print(id(my_func1))
a()"""

"""freq = {}  # frequency of words in text
line = input("Enter Text:")
for word in line.split():
    freq[word] = freq.get(word, 0) + 1
words = freq.keys()
words.sort()
print
"Frequency chart"
for w in words:
    print
    "%s:%d" % (w, freq[w])
"""


    """def frequency(input):
    freq = {}
    for word in input.split():
        freq[word] = freq.get(word, 0) + 1
    words = list(freq.keys())
    words.sort()
    for w in words:
        print(f'{w}:{freq[w]}')
"""


"""def my_function2():
    X = "LocalVariable"
    print(X)
my_function2()"""

