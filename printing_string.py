print("this is a sample string")

#print function with comma
name = "Zen"
print("My name is", name)  

#print function using concatenation
name = "Zen"
print("My name is "+name)

#String Interpolation

##F-Strings

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

##string.format()

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

##-formatting

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

##built-in string methods

x = "hello world"
print(x.title())
# output:
"Hello World"


#string.upper(): returns a copy of the string with all the characters in uppercase.
#string.lower(): returns a copy of the string with all the characters in lowercase.
#string.count(substring): returns number of occurrences of substring in string.
#string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
#string.find(substring): returns the index of the start of the first occurrence of substring within string.
#string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
#string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
#string.endswith(substring)