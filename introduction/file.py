
num1 = 42 #variable declaration, initialize int
num2 = 2.3 #variable declaration, initialize float
boolean = True #variable declaration, initialize Boolean
string = 'Hello World'  #variable declaration, initialize Strings

# #--------------------------------------------------------------------------#
# A list is a collection which is ordered and changable. Allows duplicate members.
#variable declaration, initialize List of strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 

print(f'print list pizza: {pizza_toppings}')
print(pizza_toppings[1]) #log statement, access value of List

pizza_toppings.append('Mushrooms') #List, add value
print(f'print list pizza after add Mushroom: {pizza_toppings}')

pizza_toppings.remove('Cheese') #List, delete value
print(f'print list pizza after emove Cheese: {pizza_toppings}')

pizza_toppings.insert(2,'Mushroom') #List, add value in specific position
print(f'print list pizza after insert Mushroom at postion 2: {pizza_toppings}')

value = pizza_toppings.pop(2) #List, delete value at specific position
print(f'{value} :value and print list pizza after pop at postion 2: {pizza_toppings}')

pizza_toppings.reverse() #List, reverse
print(f'print list reverse: {pizza_toppings}')

pizza_toppings[0] = 'Ham' #List, change value at position zero

#--------------------------------------------------------------------------#

# A Tuple is a correction which is ordered and unchangeable. Allows duplicate members.
# variable declaration, initialize Tuples
fruit = ('blueberry', 'strawberry', 'banana') 

# !note that if you put only one value into tuple without , at the end it will 
# convert to that type of value you put in ex fruit('blueberry') type = string
# so if we should do this friuts('bluberry',)
print(type(fruit))  #log statement, expected type Tuple
print(fruit[2]) #log statement, Tuple, access value

del friut #Tuple, delete Tuple

#--------------------------------------------------------------------------#
# A Set is a collection which is unordered and unindexed. No duplicate members.

animals={'Dog', 'Cat', 'Pig'}

# check if in set will print true or false
print('Dog' in animals)

# add to set
animals.add('Bunny')
print(animals)

#clear Set, Set still exist but empty
animals.clear()

# Delete Set, Set will no more exist
del animals
#--------------------------------------------------------------------------#

# variable declaration, initialize Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 

# log statement, Dictionary, access value
print(person['name']) # equivalent to  person.get('name')
person['name'] = 'George' # Dictionary, change value
person['eye_color'] = 'blue' # Dictionary, add value

print(person)

#Get Dictionary key
print(person.keys())

# Get Dictionary items
print(person.items())

# Copy dictionary
person = person.copy()

# Remove Items
del(person['age'])  # or person.pop('age')

#clear dictionary, will empty Dict
person.clear()


# Get Length
print(len(person))
#--------------------------------------------------------------------------#

num1 = 49; # initialize int value
if num1 > 45:    #conditional, if else
    print("It's greater")
else:
    print("It's lower")

string = 'hello World!' # initialize string value
print(string)
if len(string) < 5: # condition, if else if else
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


for x in range(5): # for loop, start at 0 stop at 4
    print(x)
for x in range(2,5): # for loop, start at 2 stop at 4
    print(x)

#pass the step value to range
# first params is start
# second params is stop(exclusive)
# third params is how many step
# in this case x start at 2 and increse 3 -> 5 -> 8 ->11(will not print because out range)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): # while loop, start at 0 stop when x equal 5
    print(x)
    x += 1  #increase x by one

#--------------------------------------------------------------------------#

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
pizza_toppings.pop() # remove value at last index
pizza_toppings.pop(1) # delete value at index 1
print(pizza_toppings)

# person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
# print(person)
# person.pop('eye_color')
# print(person)

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni':  # condition to check if statement true
        continue # skip to next loop
    print('After 1st if statement') 
    if topping == 'Olives':
        break #break out of loop


--------------------------------------------------------------------------#

def print_hello_ten_times(): #function, no parameter
    for num in range(10): # for loop start 0 stop at 9
        print('Hello') # will print hello 10 times

print_hello_ten_times()

def print_hello_x_times(x): #function, with parameter
    for num in range(x): # for loop start 0 stop at x
        print('Hello') # will print hello 4 times

print_hello_x_times(4)


# function, if no parameter it will initial parameter to 10
# if paramenter provide it will set to x
def print_hello_x_or_ten_times(x = 10): 
    for num in range(x):
        print('Hello')

# print_hello_x_or_ten_times() # will print hello 10 times
print_hello_x_or_ten_times(4) # will print hello  4 times

# lambda function
printHello = lambda: print('Hello World')
printHello()

plusNum = lambda num1, num2: num1+ num2
print(plusNum(1,2))

"""
Bonus section
"""

# print(num3)  # NameError: name num3 is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#    print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'