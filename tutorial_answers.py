# Question 1: Make sure python is loaded and working
# Uncomment the below code and run it
#print("Hello world!")


# Question 2: Get rid of all of the duplicates in this list.
#Think about the complexity of your solution.
# Complexity cheetsheet http://bigocheatsheet.com/
# You will find it is O(n^2), please make sure you can explain why as an exercise
#Cool link https://www.peterbe.com/plog/uniqifiers-benchmark

#myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']


#ANWSER
#newList = []
#for i in myList:
#    if i not in newList:
#        newList.append(i)

#print(newList)


# Exercise 3: Build an address book only using lists (the lists can be lists of tuples of objects)

#Answer
#Lists of tuples
#phonebook = [
#    ("John Doe", "555-555-5555"),
#    ("Albert Einstein", "212-555-5555"),
#]
#print(phonebook)

#phonebookNames = ['John Doe', 'Albert Einstein']
#phonebookNumbers = ['555-555-5555', '212-555-5555']
#print(phonebookNames[0])
#print(phonebookNumbers[0])


# Exercise 4 : Build a look up function for your address book

#Answer
#phonebook = [
#    ("John Doe", "555-555-5555"),
#    ("Albert Einstein", "212-555-5555"),
#]
#print(phonebook)

#def find_phonenumber(phonebook, name):
#    for n, p in phonebook:
#        if n == name:
#            return p
#        return None

#print "John Doe's phone number is", find_phonenumber(phonebook, "John Doe")

# Exercise 5 : Build a phone book using dictionary

#answer
#phonebook = {
#    "John Doe": "555-555-5555",
#    "Albert Einstein" : "212-555-5555",
#}
#print "John Doe's phone number is", phonebook["John Doe"]


# Discussion 6 :
# Create a function that times the performance of the list-bisect method
# versus a dictionary for finding a number in a phone book.
# How does the timing scale as the size of the phone book grows?
#https://docs.python.org/3.5/library/timeit.html

#Concept of a hash table
#Concept of open addressing (one object per bucket) and chaining (linked list in each bucket)

#Lookup for a dictionary is constant because O(n) lookup and O(1) for insertion

#A unique object that can

# Excercise 7 - very simple hash table for illustration
#KEY AND VALUE

# Exercise 8 - Illustrate the difference between a hash table and a set. (review dictionary )
#Sets are just hashtables without values or dictionaries without values. Lists are resizable arrays that track
#What can go in a list can be unhashable

#Example of something that is unhashable - another list. lists are mutable. if a datatype is mutable it is not hashable
#Because you can't reduce it to a unique value because it might change and the hash funciton would change.


#excecise X - Dedup the list from the beginning using a set

#myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
#mySet = set(myList) #Because it is using a hash funciton, this is O(n)
#print(mySet)


#Excercise X
#myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
#myOtherList = ['c', 'c', 'a', 'z', 'p', 'q', ]
#myListIsNowASet = set(myList)
#myOtherListIsNowASet = set(myOtherList)
#intersaction = myListIsNowASet&myOtherListIsNowASet
#print(intersaction)
#https://docs.python.org/2/library/stdtypes.html#set

