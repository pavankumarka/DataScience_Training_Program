#List
num = 10008
print([int(100), float(100 / 2.23), bool(100), str(num % 23)], type([100]))
print("-"*20*2)
#Tuple
print(((int(100), float(100), bool(100), str(100))), type((100,)))
print("-"*20*2)
#set
print("set")
print({int(100), float(100), bool(100), str(100)}, type({str(100)}))
my_set = {int(100), float(100), bool(100), str(100)}
print(my_set)
#del my_set{bool(100)}
my_set.remove(bool(100))
print(my_set)
print("-"*20*2)

#dictionary
my_dict = { "name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
my_dict = dict(name="Alice", age=30, city="New York", email="")
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
my_dict["age"] = 31  # Update existing key
my_dict["email"] = "alice@example.com"  # Add new key
# Removing a key-value pair
del my_dict["city"]
# Iterating over the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("-"*20*2)
