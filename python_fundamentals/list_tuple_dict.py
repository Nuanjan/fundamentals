import copy
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]

# # this concat will create new copy list
# # this will not change original list

# combinedlist = list1+list2

# combinedlist[5] = 7
# print(combinedlist)
# print(list1,  'list 1')
# print(list2, 'list 2')



# Note that the concat list it a shallow copy
# we need to be aware of concat List in List
list1Nested = [1, [2,3,4], 5]
list2Nested = [6, 7,[8,9,10], 11]

# combinedlistNested = list1Nested+ list2Nested
# combinedlistNested[1][2] = 'hello'
# print(combinedlistNested)
# print(list1Nested, " nested list 1")
# print(list2Nested, " nested list 2")


# to fixed the issue we need to import the copy libralies to be able to use deepcopy method.
combinedlistNested =  copy.deepcopy(list1Nested)+ copy.deepcopy(list2Nested)

combinedlistNested[1][2] = 'hello'
print(combinedlistNested)
print(list1Nested, " nested list 1")
print(list2Nested, " nested list 2")