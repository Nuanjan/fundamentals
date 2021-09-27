# def countDown (num):
#     countDownNum = []
#     for i in range(num,-1, -1):
#         countDownNum.append(i)
#     return countDownNum

# print(countDown(5))
# print(countDown(10))

# def printAndReturn(numList):
#     print(numList[0])
#     return numList[1]
# print(printAndReturn([1,2])) 

# def firstPlusLength(numList):
#     return numList[0] + len(numList)
# print(firstPlusLength([1,2,3,4,5]))


# def valueGreaterThanSecond(numList):
#     newList = []
#     if len(numList) < 2:
#         return False
#     else:
#         secondValue = numList[1]
#         for i in range(0, len(numList)):
#             if numList[i] > secondValue:
#                 newList.append(numList[i])
#         return newList
# print(valueGreaterThanSecond([5,2,3,2,1,4]))
# print(valueGreaterThanSecond([3]))

def thisLengthThatValue(size, value):
    numList = []
    for i in range(0, size):
        numList.append(value)
    return numList
print(thisLengthThatValue(4, 7))
print(thisLengthThatValue(6, 2))
