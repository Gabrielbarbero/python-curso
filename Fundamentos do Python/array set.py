'''
from array import array

number = array("i",[12,3,4,5,6,7,8,9,10])

print(number)

numberf = array("f",[1.1,1.2,1.3,1.4,1.5])
print(numberf)


list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [5,6,7,8,9,10]

n1 = set(list1)
n2 = set(list2)
print(n1 | n2)
print(n1 - n2)
print(n1 ^ n2)
print(n1 & n2)


set1 = {"a","b","c"}
set2 = {"b","c","d"}
set3 = {"c","d","e"}

set4 =set1.union(set2,set3)
print(set4)
set5 = set1.intersection(set2,set3)
print(set5)
set6 = set1.symmetric_difference(set2)
print(set6)
'''
dicionario = {"nome": "cleber", "idade": "35","altura": "1,95"}
print(dicionario)
dicionario.update({"nota": "A"})
print(dicionario.get("carro","não existe"))
dicionario.update({"carro": "uno"})
print(dicionario.get("carro","não existe"))
for keys , values in dicionario.items():
    print(keys, values)