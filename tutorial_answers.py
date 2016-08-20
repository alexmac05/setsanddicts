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

#STEP 1 - Create a list




