#boolean
print(True) # true, TRUE is not inbuild bool values
print(False) # false, FALSE, FAlse is not inbuild bool values
print(type(True))
numBool = False
print(numBool)
print(type(numBool))

#integer
print(10)
print(99999)
print(type(10))
numInt = 100
print(numInt)
print(type(numInt))
#print(100 200) // error:cannot print 2 integer in same print function

#float
print(10.0)
print(99999.2335)
print(type(10.678))
numFloat = 100.1
print(numFloat)
print(type(numFloat))
#print(100.0 200.0) // error:cannot print 2 floats in same print function

#string
print('A')
print("A")
print('ABCD')
print("Hi Hello World!")
print(type("A"))
print(type('ABCD'))
#print(type("ABCD'))
#print(type('ABCD"))
print('True') # is a string
print('100') # is a string
print("100.0123") # is a string
print("This is Pavan's world")

#functionalities of print function and its combination
print(True, False)
print(True, numBool)
print(numBool, numBool)
print(numBool, numBool, False)
print(1, 2, 3)
print(1, numInt, numInt, 2, 3)
print(100, True)
print(100, 200, False, 10.5)
print(1000.555, True, False, 999)
print('A','B','C')
print('Hi',"HELLO"," ", "WORLD","   ", 100)
print('A', end = ' ')
print('B', end = ' ')
print('C', end = ' ')
seperator = " " #manual seperator for next line to include in same line
print('E', end = seperator)
print('F', end = seperator)
seperator = '$'
print('G', end = seperator)
newSeperator = "****"
#print("H", end = newSeperator, "I",'J') #error: no new characters after end keyword
print("H", "I",'J', end = newSeperator)
print('A','B','C', sep = " ")
print('A','B','C', sep = "-")
print('A','B','C', sep = "#######")
