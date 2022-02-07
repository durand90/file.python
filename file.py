num1 = 42 # varible declaration
num2 = 2.3 # variable declaration
boolean = True # data type(boolean)
string = 'Hello World' #data type(string)
    #data type(list)
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
    #data type(dictionary)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana') # data type string
print(type(fruit)) # log statement
print(pizza_toppings[1]) #log statement w/index location
pizza_toppings.append('Mushrooms') #push() statement
print(person['name']) #log statement w/ bracket notation
person['name'] = 'George' #changing varible of name
person['eye_color'] = 'blue' #changing the varible of 'eye color'
print(fruit[2]) #log statement w/index location

if num1 > 45: #if statement
    print("It's greater") #log statement
else: #else statement
    print("It's lower") #log statement

if len(string) < 5: #if statement
    print("It's a short word!") #log statement
elif len(string) > 15: #else if statement
    print("It's a long word!") #log statement
else: #else statement
    print("Just right!") #log statement

for x in range(5): #for loop
    print(x) #log statement
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): #while loop
    print(x) #log statement 
    x += 1 #increment x++

pizza_toppings.pop() #popped function/method
pizza_toppings.pop(1) #popped method w/index location

print(person) #log statement
person.pop('eye_color') #popped 'eye color'
print(person) #log statement

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if statement
        continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement
        break

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello') #log statement

print_hello_ten_times() #log statement

def print_hello_x_times(x): #function
    for num in range(x): #for loop
        print('Hello') #log statement

print_hello_x_times(4) #calling the function

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x): #for loop
        print('Hello') #log statement

    # calling the function/log statement
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)