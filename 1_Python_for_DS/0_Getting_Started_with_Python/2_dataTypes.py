#strings
String1 = 'Geeks'
print("String with the use of Single Quotes: ", String1)
String2 = "I'm a Geek"
print("String with the use of Double Quotes including single quotes: ", String2, type(String2))
String3 = '''I'm a Geek and I live in a world of "Geeks"'''
print("String with the use of Triple Quotes: ", String3, type(String3))
String4 = '''Geeks
			For
			Life'''
print("Creating a multiline String: ", String4)

#LISTS
lst1=[] #empty list
print(type(lst1))
lst2=[1.0, 2, 'GFG', "Geeks"]
print(type(lst2))
lst3 = [lst1, lst2] #this is allowe, as list is mutable
print(lst3)
print(type(lst3))
lst2[0] = 44
print(lst2)

#TUPLE
tup1=('x', 'y')
tup2=(1, 'hi', 3.0)
print(tup1)
print(type(tup1))
print(type(tup2))
tup3 = (tup1, tup2)
print(tup3)
#tup1[1] = ('z') #this is error as tuple is immutable
print(tup1)

#Bool
#is_selected=true  #invalid inbuild keyword true,TRUE
#print((is_selected))
is_selected=True
print((is_selected))
print(type(is_selected))

#set
c = set()
c = {1, 4, 5, "Geeks", 6.0}
print(type(c))
print(c)
#c = {c,c} #unhashable
print(c)

Dict1 = {}
print("Empty Dictionary: ", Dict1, type(Dict1))
Dict2 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Dictionary with the use of Integer Keys: ", Dict2, type(Dict2))
Dict3 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Dictionary with the use of Mixed Keys: ", Dict3, type(Dict3))
Dict4 = dict([(1, 'Geeks'), (2, 'For')])
print("Dictionary with each item as a pair: ", Dict4, type(Dict4))

#seperator
a = "Course Data Science with Python"
b = "GeeksforGeeks"
print(a, end=' at ')
print(b)
print(a, end=' @ ')
print(b)

a = "Course Data Science with Python"
b = "GeeksforGeeks"
print("Course", "Data", "Science", "with", "Python", sep='-', end=' at ' )
print(b)
print(a, b, sep='\n')
