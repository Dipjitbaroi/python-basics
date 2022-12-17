
list = [23,7,4,73,2,33,66,23,47,88,97]

print(list[2])


list.append(8)
print(list)
list.insert(list[2],5)
print(list)
list.remove(2)
print("2 replaced with 5",list)
list.extend([0,2,9,8,7])
print(list)
list.remove(2)
print(list)
list.insert(13,2)
print("removed number added",list)
list.pop()
print(list)
list.sort()
print(list)

list = list + [[1,2,3,4]]
print(list)
print(list[16][2])