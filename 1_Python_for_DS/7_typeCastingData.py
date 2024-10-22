#integer
print(100)              # 100
print(type(100))        # <class 'int'>
print(100, type(100))   # 100 <class 'int'>
num = print(100)        # 100
print(num)              # None
num = 1000
print(num)
print("-"*20)

#typecasting INTEGER to FLOAT, BOOL and String
print(int(100), type(int(num)))
print(float(100 + 3.3), type(float(100/2.23)))
print(bool(100), type(bool(100)))
print(str(100), type(str(num % 23 )))
print([int(100), float(100 / 2.23), bool(100), str(num % 23)], type([100]))
print(((int(100), float(100), bool(100), str(100))), type((100,)))
print({int(100), float(100), bool(100), str(100)}, type({str(100)}))
print("-"*20*2)

#typecasting FLOAT to Integer, BOOL and String
print(999.99)
print(999.99, type(999.99))
print(int(999.99/4), type(int(999.99%4)))
print(bool(999.99/4), type(bool(999.99%4)))
print(str(999.99/4), type(str(999.99%4)))
print("-"*20*2)

#typecasting Bool to Integer, float and String
print(True, False, type(True))
print(int(True), type(int(True)))
print(float(False/4), type(float(False)))
print(str(False/5.5), type(str(False)))
print("-"*20*2)

#typecasting FLOAT to Integer, BOOL and String
print("My_string", type("My_string"))
#print(int("M"), type(int("M")))
#print(float("My"), type(float("My")))
print(int("100"), type(int("100")))
print(float("100.3456"), type(float("100.23456")))
print(bool("100.3456"), type(bool("100.23456")))
# special cases
print(int(float("100.3456")), type(int(float("100.23456"))))
print(bool(''), type(bool('')))
print(bool(' '), type(bool(' ')))
print(bool('  mystr '), type(bool(' mystr ')))
print("-"*20*2)
