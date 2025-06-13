import copy

#learning about zipping

list1 = []
list2 = []

for i in range(6):
    list1.append(i)
    list2.append(5 - i)

list3 = list(zip(list1, list2))
print("List 1:", list1)
print("List 2:", list2)
print("Zipped List:", list3)

new_set = set(list3)
print("New Set:", new_set)