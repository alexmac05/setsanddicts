# Question 1: Make sure python is loaded and working
# Uncomment the below code and run it
# print("Hello world!")
# TODO: BETHANY - HAVE PEOPLE PRINT OUT THEIR VERSION

#TODO: ALEX - have some memory sticks of tutorial

#ALEX
# Question 2: Get rid of all of the duplicates in this list.
# Think about the complexity of your solution.
# Complexity cheetsheet http://bigocheatsheet.com/
# You will find it is O(n^2), please make sure you can explain why as an exercise
# Cool link https://www.peterbe.com/plog/uniqifiers-benchmark
# https://wiki.python.org/moin/TimeComplexity

#myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']


# Answer Question 2
#newList = []
#for i in myList:
#    if i not in newList:
#        newList.append(i)

#print(newList)
#---------------------------------------------------------------------------------------------------------------------



#TODO: BETHANY - write 4 LIST comphrenehsions to teach comphrenehsnions here! PYTHONIC

# TO DO; BETHANY TO DO - fix this one up - what is pythonic and not pythonic
# Reduce lines of code is comprehensions - there is debate on this topic (doesn't make it faster)
#JUst a nice way of writing
# INTRODUCE COMPREHENSIONS RIGHT THERE - a loop flatended to one line
# LIST COMPHRENSION
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = [x for x in some_list if some_list.count(x) > 1]
# print(duplicates)


#15 to 20 mins
#TODO : Jouella - PYTHON 3 FUNCTION CALLS ON STACK MEMORY  WRITING EFFECITENT LIST COMPREHENSIONS
# def add_two(n):
#   return n + 2
# x = [add_two(i) for i in range(10)]
# vs. 
# y = [i + 2 for i in range(10)]

#EXERCISES - here
#TODO: Show how tuple is immutable
# tup1 = ('PyLadies', 'Oakland', 1, 2)
# tup2 = tup1

# tup1 is tup2 # True, look at id(tup1) & id(tup2)
# tup1 == tup2 # True

# tup1 = ('PyLadies', 'Oakland', 1, 3)
# id(tup1) # different
# tup1[0] = 'Hello' # will have a type error saying that it won't support item assignment


#ALEX
#Question 3 - Create a list of the months of a year 'jan', 'feb', .... ' dec'
# and use the tuple(myList) function to create a tuple of the list
# Mess around with the list methods, count, index, insert, pop, remove, reverse, append and sort
# Notice any differences between tuples and lists

# Background: You can change a list. You cannot change a tuple.
# Another way to say that is lists are mutable and tuples are immutable.
#
# Create a list and create a tuple both that represent the months of a year

#Answer 3
#myListMonths = ['January', 'Feb', 'march', 'april', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec', 'January']
#myTupleMonths = tuple(myListMonths)

#count
# lists
#count = myListMonths.count('January')
#print(count)
#Tuples
#count = myTupleMonths.count('January')
#print(count)

#index








#TODO: ALEX - clean up, Alex to talk about tuples introduce that and lists of tuples why it is helpful
#TUPLES - unique and difference between tuples and lists
#Exercise - Unpacking a sequence into separate variables
# This section is from the python cookbook, 3rd edition
# You can unpack any sequence into variables using a simple assignment operation. The only requirement is that
# the number of variables and structure match the sequence.
# Example
#p = (4,5) # a tuple
#x, y = p
#print(x)
#print(y)

#data = ['ACME', 50, 91.1, (2012, 12, 21)]
#names, shares, price, date = data
#print(date)



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

# USES

#a = { 'x':1, 'y':2, 'z':3 }
#b = { 'w': 10, 'x': 11, 'y': 12 }


# answer
# phonebook = {
#    "John Doe": "555-555-5555",
#    "Albert Einstein" : "212-555-5555",
# }
# print "John Doe's phone number is", phonebook["John Doe"]

#Vitamins and minerals that go with vegtables
# Shoes and sizes of shoes but you want to track the type of shoe



#ALEX SECTION
# SECTION ON BEGINNING DICTIONARY STUFF - Python Pocket reference section
# Fluent python here the beginning section

#Section that plays with Dictionaries

#Section on initialization - take from O'Reilly Python Pocket Reference by Mark Lutz

#Any immutable object can be a dictionary key (string, number, tuple)
#Class instances can be keys if they inherit hashing methods

# A two item dictionary: keys 'spam' and 'eggs'
#A = {'spam': 2, 'eggs':3}

#Nested dictionaries
#B = { 'info': {42: 1, type(''):2, 'spam':[]}}

#Creates a dictionary by passing keyword arguments to the type constructor
#C = dict(name='Bob', age=45, job=('mgr', 'dev'))

#Dictionary comprehension expression
#D = {c.upper(): ord(c) for c in 'spam'}
#print(D)
#print(ord('s'))

#E = {} # an empty dictionary

#Exercises for this section
#STEP 1 - Print out all of the keys for dictionary A
#print(A.keys())

#STEP 2 - Print out all of the values for dictionary D
#print(D.values())

#STEP 3 - play with the C.items() function.
#print(C.items())

#Step 4 - How would you clear all of the items from dictionary A?
#A.clear()
#print(A)

#Step 5 - Put the values back in A and do a copy (shallow copy) then change a value and print out both
#F = A.copy()
#print(F)
#F['spam'] = 4
#print(A)
#print(F)

#Step 6 - iterate through the dictionary D
#http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python
#for key, value in D.items():
#    print key, 'corresponds to', D[key]

#--------------------------------------------------------------------------------------------------------------------
# TO DO : BETHANY - WRITE exercises on this
#BETHNAY - WORK IN SETTING DEFAULT FOR DICTIONARY
# DICTIONARY COMPHREHENSIONS
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
#---------------------------------------------------------------------------------------------------------------------




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
#---------------------------------------------------------------------------------------------------------------------

#TODO BETHANY - SET COMPREHENSIONS
# Set Comprehensions - fluent programming book
# Comphrehension of a set
#some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#duplicates = set(x for x in some_list if some_list.count(x) > 1)
#print(duplicates)

# SECOND COMPHREHENSION EXAMPLE - TODO: BETHANY Super fast example dedupping with list and a set

#TODO BETHANY - set logical examples
#1.9 Finding Commonalities in Two Dictionaries chapter 1 Data Structures and Algorithms 3rd edition Python cookbook

#____________________________________________________________________________________________________________________

#TODO ALEX
# ABUSES Of Dictionaries

#Adding items to a dict may change the order of existing keys

#MEMORY - don't put too much in memory

#AFTER
#some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#deduped = []jojofabe@gmail.com

#for value in some_list:
#    if value not in deduped:
#        deduped.append(some_list.pop(some_list.index(value)))

#print(deduped)
#print(some_list)

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
#



#---------------------------------------------------------------------------------------------------------------------

#TODO - JOUELLA PEP8 WHAT IS PYTHONIC
# from http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#list-comprehensions
# exercise: try to convert this 
# new_list = []
# for item in a_list:
#    if condition(item):
#       new_list.append(fn(item)) 
# to pythonic 




#--------------------------------------------------------------------------------------------------------------------
#TODO BETHANY - Peppering stuff there
# Counter, and default dict #DEQUE - double ended queue - as a stack or a queue (append to either end in constant time)
# Ordered dictionaries
# Fluent python here Variations of dict - COLLECTIONS stuff


#-------------------------------------------------------------------------------------------------------------------
#TODO - JOUELLA - NAMED TUPLES
# from collections import namedtuple
# Person = namedtuple('Person', 'name age height')
# Person = namedtuple('Person', 'name age height', verbose=True), will print out the class definition
# mara = Person(name='Rooney Mara', 'age=26, height=5.2)
#________________________________________________________________________________________________________________

#TODO BETHANY - END SECTION 
#END EXAMPLES - for people finished
#FIND THE MOST Efficient solution for debbing a large list. I want a list of the duplicates and a debbed list and i don't
#want duplicates in the dubbed list

#MARKOV CHAINS and dictionaries
#http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
