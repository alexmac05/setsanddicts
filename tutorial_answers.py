# Question 1: Make sure python is loaded and working
# Uncomment the below code and run it
# print("Hello world!")
# TODO: BETHANY - HAVE PEOPLE PRINT OUT THEIR VERSION

#TODO: ALEX - have some memory sticks of tutorial

# Question 2: Get rid of all of the duplicates in this list.
# Think about the complexity of your solution.
# Complexity cheetsheet http://bigocheatsheet.com/
# You will find it is O(n^2), please make sure you can explain why as an exercise
# Cool link https://www.peterbe.com/plog/uniqifiers-benchmark
# https://wiki.python.org/moin/TimeComplexity

# myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
#TODO: ALEX - just fix this up

# ANWSER
# newList = []
# for i in myList:
#    if i not in newList:
#        newList.append(i)

# print(newList)


#TODO: BETHANY - write 4 LIST comphrenehsions to teach comphrenehsnions here! PYTHONIC

# TO DO; BETHANY TO DO - fix this one up - what is pythonic and not pythonic
# Reduce lines of code is comprehensions - there is debate on this topic (doesn't make it faster)
#JUst a nice way of writing
# INTRODUCE COMPREHENSIONS RIGHT THERE - a loop flatended to one line
# LIST COMPHRENSION
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = [x for x in some_list if some_list.count(x) > 1]
# print(duplicates)




#TODO: ALEX - clean up, Alex to talk about tuples introduce that and lists of tuples why it is helpful
#TUPLES - unique and difference between tuples and lists
#TUPLES ARE HASHABLE - gotcha
# Exercise 3: Build an address book only using lists (the lists can be lists of tuples of objects)

# Answer
# Lists of tuples
# phonebook = [
#    ("John Doe", "555-555-5555"),
#    ("Albert Einstein", "212-555-5555"),
# ]
# print(phonebook)

# phonebookNames = ['John Doe', 'Albert Einstein']
# phonebookNumbers = ['555-555-5555', '212-555-5555']
# print(phonebookNames[0])
# print(phonebookNumbers[0])

#todo alex
# Exercise 4 : Build a look up function for your address book

# Answer
# phonebook = [
#    ("John Doe", "555-555-5555"),
#    ("Albert Einstein", "212-555-5555"),
# ]
# print(phonebook)

# def find_phonenumber(phonebook, name):
#    for n, p in phonebook:
#        if n == name:
#            return p
#        return None

# print "John Doe's phone number is", find_phonenumber(phonebook, "John Doe")

# TODO ALEX: CLEAN THIS UP
# Exercise 5 : Build a phone book using dictionary

# answer
# phonebook = {
#    "John Doe": "555-555-5555",
#    "Albert Einstein" : "212-555-5555",
# }
# print "John Doe's phone number is", phonebook["John Doe"]


# SECTION ON BEGINNING DICTIONARY STUFF - Python Pocket reference section
# Fluent python here the beginning section
#TODO ALEX _ THIS ENDS THE ALEX SESSION


# TO DO : BETHANY - WRITE exercises on this
#BETHNAY - WORK IN SETTING DEFAULT FOR DICTIONARY
# Dictionary comphensions
#END BETHANY SECTION


# TODO BETHANY - Why is it that the dictionary works better
# Discussion  :
# Create a function that times the performance of the list-bisect method
# versus a dictionary for finding a number in a phone book.
# How does the timing scale as the size of the phone book grows?
# https://docs.python.org/3.5/library/timeit.html
# SECTION FOR TIMEIT - BETHANY
#BETHANY  - finding stuff in a list, finding stuff in a dictionary, adding stuff to a list and adding stuff to a dict
# using timeit.

#TODO ALEX
# Concept of a hash table
# Concept of open addressing (one object per bucket) and chaining (linked list in each bucket)

# Lookup for a dictionary is constant because O(n) lookup and O(1) for insertion

# A unique object that can
# https://wiki.python.org/moin/TimeComplexity



#TODO ALEX
# Excercise 7 - very simple hash table for illustration
# KEY AND VALUE
# SIMPLE HASH TABLE HERE

# Example of something that is unhashable - another list. lists are mutable. if a datatype is mutable it is not hashable
# Because you can't reduce it to a unique value because it might change and the hash funciton would change.

#TODO ALEX  - fluent python book
# Exercise 8 - Illustrate the difference between a hash table and a set. (review dictionary )
# Sets are just hashtables without values or dictionaries without values. Lists are resizable arrays that track
# What can go in a list can be unhashable

# excecise X - Dedup the list from the beginning using a set

# myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
# mySet = set(myList) #Because it is using a hash funciton, this is O(n)
# print(mySet)


# Excercise X
# myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
# myOtherList = ['c', 'c', 'a', 'z', 'p', 'q', ]
# myListIsNowASet = set(myList)
# myOtherListIsNowASet = set(myOtherList)
# intersaction = myListIsNowASet&myOtherListIsNowASet
# print(intersaction)
# https://docs.python.org/2/library/stdtypes.html#set

#TODO BETHANY - SET COMPREHENSIONS
# Set Comprehensions - fluent programming book
# Comphrehension of a set
#some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#duplicates = set(x for x in some_list if some_list.count(x) > 1)
#print(duplicates)

# SECOND COMPHREHENSION EXAMPLE - TODO: BETHANY Super fast example dedupping with list and a set

#TODO BETHANY - set logical examples


#TODO ALEX
# ABUSES

#Adding items to a dict may change the order of existing keys


#AFTER
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
deduped = []

for value in some_list:
    if value not in deduped:
        deduped.append(some_list.pop(some_list.index(value)))

print(deduped)
print(some_list)

#read the dict from start to finish and collect the needed additions in a second dict. Then update the first one with it.
#Exercise to


#A list of hashable items the keys are a list of hashable items. (LIST OR SET)




# - DICS ARE NOT SPACE EFFECIENT - A dictionary is in memory
# For example, if you are handling a large quantity of records,
# it makes sense to store them in a list of tuples or named tuples instead of using a list of dictionaries i
# n JSON style, with one dict per record. Replacing dicts with tuples reduces the memory usage in two ways:
# by removing the overhead of one hash table per record and by not storing the field names again with each record.


# Adding items to a dict may change the order of existing keys

# Set elements must be hashable objects.
#

#TO DO ALEX
# USES
# PYTHON COOKBOOK




#TODO BETHANY - Peppering stuff there
# Counter, and default dict #DEQUE - double ended queue - as a stack or a queue (append to either end in constant time)
# Ordered dictionaries
# Fluent python here Variations of dict - COLLECTIONS stuff


#END EXAMPLES - for people finished 
#FIND THE MOST Efficient solution for debbing a large list. I want a list of the duplicates and a debbed list and i don't
#want duplicates in the dubbed list

#MARKOV CHAINS and dictionaries
#http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
