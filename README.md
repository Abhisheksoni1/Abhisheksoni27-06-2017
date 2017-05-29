# Abhisheksoni27-06-2017
Python java assignment 

to run and test the cache implementation then simply run this command
assume you are in the project folder like /Documents/alex_israel/projectfolder
python PythonAssignment.py

#.................................................................

pythondataset.txt format
first_name@last_name maths@marks science@marks id@roll_number
#.................................................................

MyCache class have some functions
1 > __init__:  constructor which define a empty dict and max size
2 > __contains__: check weather key is in the cache or not, if yes then return true else false
3 > __getitem__: get the value for the corresponding key
4 > __setitem__: add (key,value) pair in dict if dict is full then use lru to remove element
5 > update: update value for corresponding key
6 > __delitem__: del corresponding (key,value) pair
7 > remove_oldest: remove Least recently used item from dict
8 > size, read: these are define as property for this class to acess directly and return its size and content
respectively.
#................................................................

