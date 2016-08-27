# Question 1: Make sure python is loaded and working
# Exercise 1: Make sure python is loaded and working
# Uncomment the below code and run it
#import sys
#print(sys.version_info)
#print(sys.version)
#print("Hello world!")

#######################################################################################################################
# Exercise 2: Get rid of all of the duplicates in this list.
# Think about the complexity of your solution.

#myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']


# Answer Question 2
#newList = []
#for i in myList:
#    if i not in newList:
#        newList.append(i)

#print(newList)

#RESOURCES
# Complexity cheetsheet http://bigocheatsheet.com/
# You will find it is O(n^2), please make sure you can explain why as an exercise
# Cool link https://www.peterbe.com/plog/uniqifiers-benchmark
# https://wiki.python.org/moin/TimeComplexity

#######################################################################################################################
# Exercise 3: Run this timeit example and play with it.

#import timeit

#setup = '''myList = ['c', 'd', 'c', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'f', 'g']
#'''

#statement_A = '''
#newList = []
#for i in myList:
#    if i not in newList:
#        newList.append(i)
#'''

#print(timeit.timeit(stmt=statement_A, setup=setup, number=10000))


#print(timeit.timeit(stmt=statement_B, setup=setup, number=10000))

########################################################################################################################

# Exercise 4: Use the skills you just learned. Create a list with a mix of upper case and lower case letter
# And then use timeit to time your algorithm for filtering out the upper case letters.


########################################################################################################################

#PAUSE HERE FOR A WORD ABOUT PYTHONIC
'''
Thank you Python Foundation & Lea Verou

PEP8 (Code Formatting)            https://www.python.org/dev/peps/pep-0008/
An alternate view on spaces       http://lea.verou.me/2012/01/why-tabs-are-clearly-superior/

PEP202 (list comprehensions)      https://www.python.org/dev/peps/pep-0202/
PEP274(dictionary comprehensions) https://www.python.org/dev/peps/pep-0274/
PEP20 (The Zen of Python)         'import this' in the Python shell

"Programs must be written for people to read,
and only incidentally for machines to execute." -- Harold Abelson (Structure and Interpretation of Computer Programs)

"Code is read much more often than it is written" -- Guido VanRossum
'''

#EXERCISE 5 - to get the zen of python
#UNCOMMENT THIS LINE!
#import this
########################################################################################################################

#PAUSE HERE FOR A WORD ABOUT LIST COMPHREHENSIONS

'''
Quick Examples

this                                                                becomes

#symbols = '$¢£¥€¤'                                                  symbols = '$¢£¥€¤'
codes = []                                                          codes = [ord(caracter) for character in symbols]
for symbol in symbos:
    codes.append(ord(symbol))

this                                                                becomes

results = []                                                        results = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 21)]
for num in range(1, 21):
    if num % 2 == 0:
        results.append(num ** 2)
    else:
        results.append(num ** 3)

#RESOURCES
'''

'''
______________________________________________________
LIST COMPREHENSIONS
________________________________________________________
Thank you
Bruce Eckel  -- Python3 Patterns & Idioms   http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
Mark Pilgrim -- Dive into Python3           www.diveintopython3.net
Obi Ike-Nwosu                               http://intermediatepythonista.com/python-comprehensions
Python Foundation                           https://docs.python.org/3/howto/functional.html.

With exercises help from
Trey Hunner                                 http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
Boston Python                               http://puzzles.bostonpython.com/
github/zhiwehu/Python-programming-exercises
'''



########################################################################################################################
#15 to 20 mins
#TODO : Jouella - PYTHON 3 FUNCTION CALLS ON STACK MEMORY  WRITING EFFECITENT LIST COMPREHENSIONS
#EXERCISES - here
#TODO: Show how tuple is immutable


########################################################################################################################
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


import re

class HashTable:
    myHashTable = []

    def __init__(self):
        self.myHashTable = [None] * 1000

    def addToHash(self, name):
        index = self.hashIt(name)
        self.myHashTable[index] = name


    def printHashTable(self):
        for i, val in enumerate(self.myHashTable):
            if val is not None:
                print(i, val)

    def hashIt(self, value):
        #Take the first three letters of the string
        #Get the ord('f') of each of these first three chars
        #Add these
        #return the hash for hashing
        regExString = r'^[A-Za-z]{3}$'
        m = re.match(regExString,value)
        if m is not None:
           a = ord(value[0])
           b = ord(value[1])
           c = ord(value[2])
           d = a + b + c
           print(str(a) + " " + str(b) + " " + str(c) + " " +  str(d))
        else:
            print(str + " Failed input - this function only takes 3 letters")

        return d


myHash = HashTable()
myHash.addToHash('foo')
myHash.addToHash('boo')
myHash.addToHash(('cry'))
myHash.addToHash('oof')
results = myHash.printHashTable()
print(results)













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

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
deduped = []

for value in some_list:
    if value not in deduped:
        deduped.append(some_list.pop(some_list.index(value)))

print(deduped)
print(some_list)

# Adding a new item to a dictionary can cause the hash table to change. During this process, the keys might
# change their order in the underlying datastructure. You can't reliably predict what or when this will happen.
# If you are iterating over the dictionary keys and changing them at the same time, your loop may
# not scan all of the items as expected.
# Best Practice - If you need to scan and add items to a dictionary, do it in steps
# 1. Read the dict from start to finish and collect the needed additions in a second dict
# 2. Update the first one with the second one in a separate move

#EXERCISE - Take this phonebook dictionary and write a function that find duplicate phone numbers (they must be
# roommates in those cases) and then update the keys to read LastName1 - LastName2 Household
phonebook = {
    "Marie Curie": "555-555-5555",
    "Rosalind Franklin" : "212-555-5555",
    "Lise Meitner" : "212-555-5555",
    "Chien-Shiung Wu" : "555-555-5555",
    "Rita Levi-Montalcini" : "510-908-1234",
    "Barbara McClintock" : "415-987-4313",
    "Gertrude B. Elion" : "757-698-1234",
    "Ada Lovelace" : "614-987-1456"
}
print("Ada's phone number is", phonebook["Marie Curie"])

# So, the result for Marie Curie and Chien-Shiung Wu would be "Curie-Wu Household" : "555-555-5555
# This way we would only have one entry per household. (They share a phone)
#However, make this change following the best practice above and avoiding an abuse of dictionaries, which is changing
#dictionary keys (changing the hashtable) at the same time that you are iterating through it







#Adding items to a dict may change the order of existing keys

#MEMORY - don't put too much in memory

#AFTER


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

#TODO - JOUELLA PEP8 WHAT IS PYTHONIC - reserve indexiging with slicing and performance and other PEP 8 stuff
#TIMEIT WILL HAVE BEEN INTRODUCED






#--------------------------------------------------------------------------------------------------------------------
#TODO BETHANY - Peppering stuff there
# Counter, and default dict #DEQUE - double ended queue - as a stack or a queue (append to either end in constant time)
# Ordered dictionaries
# Fluent python here Variations of dict - COLLECTIONS stuff


#-------------------------------------------------------------------------------------------------------------------
#TODO - JOUELLA - NAMED TUPLES


#________________________________________________________________________________________________________________

#TODO BETHANY - END SECTION 
#END EXAMPLES - for people finished
#FIND THE MOST Efficient solution for debbing a large list. I want a list of the duplicates and a debbed list and i don't
#want duplicates in the dubbed list

#MARKOV CHAINS and dictionaries
#http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
