'''
list1 = [1,2,3,4,5,6,7,8,9,10]

def multi(x):
    return x * 2

list2 = map(multi,list1)
print(list(list2))


list1 = [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: x * 2, list1)))

number = [1,17,75,4,3,22,35,31,99,103,234]
def remove(x):
    return x > 50
print(list(filter(remove, number)))

print(list(filter(lambda a: a > 50,number)))


list1 =["12","23","24","54","35","3","4"]
   

#list2 =[number  for number in list1 if "2" in number]

#print(list2)
list3 = [x * 10 for x in range(6)]
print(list3)
'''
from sys import getsizeof

list3 = [x * 10 for x in range(100)]
print(list3)
print(type(list3))
print(getsizeof(list3))

list3 = (x * 10 for x in range(100))
print(type(list3))
print(list(list3))
print(getsizeof(list3))