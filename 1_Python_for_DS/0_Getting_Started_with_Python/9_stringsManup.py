# String Concatenation
print("String1")
str2 = "String2"
print("String1" + str2)
print('' + '  ' + "String1" + '  ' + str2)
print("------------------------------------------")

# String Replication
print("\n#String "*20)
print("-"*40)

# String Length
print("string1", type("string1"), "len =",len('String1'))
print("len =",len('String1   '))
print("-"*40)

# String Slicing
print("String1")
str2 = "In DashBoard"
print("String1" + str2)
print(("String1" + str2)[0])
print(("String1" + str2)[7])
print(("String1" + str2)[-1])
print(("String1" + str2)[-4])
print(("String1" + str2)[0:6])
print(("String1" + str2)[7:19])
print(("String1" + str2)[1:18])
print(("String1" + str2)[1:-1])
print(("String1" + str2)[1:])
print(("String1" + "In DashBoard")[1:-1])
print(("String1" + str2)[-18:-1])
print(("String1" + str2)[-1:-18])
#print(("String1" + str2)[-20])
print("-"*40)

# String Case Conversion
print("String1".lower())
print("String1".upper())
print("-"*40)

# String Replacing
print("String1 string2".replace("string2", "---"))
print("String1 string2".replace("ring", "reem"))
print("-"*40)
# String Count
print("String1".count('S'))
print("String1 string2".replace("ring", "reem").count('e'))
print("String1 string2".replace("ring", "reem").lower().count('s'))
print("-"*40)

# String Find
print("String1 Stttring2".find('ring'))
print("-"*40)

# String check
print("String1".isalpha())
print("123".isdigit())
print("string1".islower())
print("STRING".isupper())
print("-"*40)

# String Capitalization
print('stRing1 String2'.capitalize())
print('stRing1 String2'.title())
print("-"*40)

# String start and end
print('stRing1 String2'.startswith('st'))
print('stRing1 String2'.endswith('ing2'))
print("-"*40)

# String align/adjust
print('stRing1 String2'.center(25, "*"))
print('stRing1 String2'.ljust(25, "*"))
print('stRing1 String2'.rjust(25, "*"))


# String Stripping
print("String1 string2".strip())
print("         String1 string2         ".lstrip())
print("         String1    string2         ".rstrip())
print("-"*40)

# String format
str1 = "{} {} {}".format('Begin', 'mid', 'end')
print("strings format order:", str1)

str1 = "{0} {1} {2}".format('Begin', 'mid', 'end')
print("strings format order:", str1)

str1 = "{2} {0} {1}".format('Begin', 'mid', 'end')
print("strings format order:", str1)

str1 = "{b} {c} {a}".format(a='Begin', b='mid', c='end')
print("strings format order:", str1)
