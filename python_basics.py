print("print function can take many arguments", "different types too", 12)
print("""
It can even take paragraphs using multi-line
strings written with triple quotes \"\"\" \"\"\".
""")


# Create a variable
# Variables take space in memory
# They are defined with a name and a value
# Values can be of different types, such as:
#   - integers
#   - floats
#   - strings
#   - booleans

integer = 42  # assigning the value 42 to the variable named 'integer'
print(type(integer))

print(integer + 5)  # integers and floats support operators: +, -, *, /, %, **, //
print(integer)  # original value does not change


float1 = 3.14  # float value (decimal number)
print(type(float1))

print("Integer added to float result type is:", type(integer + float1))  # result is float

# Variables can be reassigned and even change type in Python
float1 = 12.0
float1 = 10  # now it's an integer again
print("Variable type can be changed:", type(float1))


bool1 = True
bool2 = False

print(type(bool1))
print("bool1:", bool1)  # printed as True or False (not 1 or 0)
print("bool2:", bool2)


# Comparison operators: ==, >, <, >=, <=, !=
print()
print("Comparison operators:")
print("10 == 10:", 10 == 10) 
print("10 != 5:", 10 != 5)    
print("10 > 5:", 10 > 5)    
print("5 <= 4:", 5 <= 4)      

print()
# Type of comparison results
print("Types of comparison results:")
print("Type of (10 == 10):", type(10 == 10))  # All comparisons return boolean
print("Type of (10 > 5):", type(10 > 5))


print("\n--- Strings ---")
string1 = "Hello, World!"  # strings use quotes
string2 = 'Single quotes work too'
print(string1)
print(string2)

# String methods
print("Uppercase:", string1.upper())
print("Lowercase:", string1.lower())
print("Replace:", string1.replace("Hello", "Hi"))
print("Split:", string1.split(","))
print("Length:", len(string1))


print("\n--- Lists ---")
my_list = [1, 2, 3, 4, 5]  # lists are ordered collections
print("Original list:", my_list)
my_list.append(6)
print("After append:", my_list)
my_list.insert(4, 0)
print("After insert:", my_list)
my_list.remove(3)
print("After remove:", my_list)
print("List item at index 2:", my_list[2])
print("List slice:", my_list[1:4])


print("\n--- String indexing ---")
string_example = "Python Programming"
print("Original string:", string_example)
print("Character at index 0:", string_example[0])
print("Character at index 7:", string_example[7])
print("String slice:", string_example[0:6])
print("Reverse string:", string_example[::-1])


print("\n--- Tuples ---")
my_tuple = (1, 2, 3, 4, 5)  # tuples are immutable (cannot be changed)
print("Tuple:", my_tuple)
print("Tuple item at index 0:", my_tuple[0])
# my_tuple[0] = 10  # This would cause an error
print("Tuple length:", len(my_tuple))


print("\n--- Dictionaries ---")
my_dict = {"name": "John", "age": 30, "city": "New York"}  # key-value pairs
print("Dictionary:", my_dict)
print("Value for 'name':", my_dict["name"])
my_dict["email"] = "john@example.com"
print("After adding email:", my_dict)
del my_dict["age"]
print("After removing age:", my_dict)
print("Dictionary keys:", list(my_dict.keys()))
print("Dictionary values:", list(my_dict.values()))


print("\n--- Console Input ---")
name = input("Enter your name: ")
print("Hello,", name)

num_input = input("Enter a number: ")

# Converting input to integer
num_int = int(num_input)
print("Converted to integer:", num_int, "Type:", type(num_int))

# Converting input to float
num_float = float(num_input)
print("Converted to float:", num_float, "Type:", type(num_float))

# Converting integer back to string
num_str = str(num_int)
print("Converted back to string:", num_str, "Type:", type(num_str))


# File Operations
print("\n--- File Operations ---")
# Traditional file opening and closing
file = open("example.txt", "w")
file.write("Hello, this is a test file.\n")
file.write("This is another line of text.")
file.close()
print("File written successfully")


file = open("example.txt", "r")
content = file.read()
file.close()
print("\nFile content:")
print(content)

# Reading line by line - traditional way
file = open("example.txt", "r")
print("\nReading line by line:")
print(file.readline())
print(file.readline())
file.close()

# Recommended way: using 'with' statement
# The 'with' statement automatically closes the file,
# even if errors occur inside the block.
with open("example.txt", "r") as file:
    print("\nReading with 'with' statement (recommended):")
    print(file.read())
