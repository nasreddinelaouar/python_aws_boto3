#Variables in Strings
firstname = "Nasreddine"
surname = "LAOUAR"

print(f"My first name is {firstname}. My family name is {surname}")

#Using Number Varaibles in strings
my_int = 48
sentence = "The total comes to: "

print(sentence + str(my_int))

#Creating, Reading, Updating and Deleting values in Dictionary

#Create
user = {"first_name":"Ada"}
print(user)

#Read
user = {"first_name":"Ada"}
print(user["first_name"])

#Update
user["family_name"] = "Byron"
print(user)


#Modify a value
user["family_name"] = "Lovelace"
print(user)


#Delete a Key-Value Pair
del user["family_name"]
print(user)


#Creating, Reading, Updating and Deleting elements in a list

#Create
fruit = ["apples","oranges","bananas"]

#list by assigning [] to a variable
fruit = []

#by using the list() constructor
fruit = list()

#Read
fruit = ["apples","oranges","bananas"]
print(fruit[1])

#Find the length of a list
len(fruit)

#You can return the last value in a list or work backwards from the last item using a negative index value
print(fruit[-1])

print(fruit[-2])

#Update
fruit.append("kiwi")
print(fruit)

#if you want add an element at a specific point in the list you can use the index value with the insert() method.
fruit.insert(2, "passion fruit")
print(fruit)

#Organizing a List

#Return information which is sorted, but retain the original order of the list, you can use the sorted() function
print(sorted(fruit))

print(fruit)

#Permanently sort the list using the sort() method
fruit.sort()
print(fruit)

#Reverse the order of a list with the reverse() method
fruit.reverse()
print(fruit)

#Delete
del fruit[1]
print(fruit)

#If you want to use the value after removing it from a list you use the pop() method
favorite_fruit = fruit.pop()
print(favorite_fruit)

#In this example, pop() has returned the last element in the list, which is the default for pop()
fresh_fruit = fruit.pop(1)
print(fresh_fruit)

#If you don't know the index position, or you don't want to remove the last item in the list, 
#you can use the remove() method to specify the value of the element you want to remove.
fruit.remove('bananas')
print(fruit)

#Determining Type

#The way to find out what type of data python has stored in a variable is to use the type() method.
my_variable = "A string"
print(type(my_variable))

#Fix the TypeError by telling python to convert my_number to a string
my_number = 48
some_string = "The number is "
print(some_string + str(my_number))
