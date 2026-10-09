list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]


common_elements = [x for x in list1 if x in list2]


only_in_list1 = [x for x in list1 if x not in list2]

print("Values present in both lists:", common_elements)
print("Values present only in list1:", only_in_list1)