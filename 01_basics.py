## Hello word program
print("hello world")

# Check version
# import sys
# print(sys.version)
# print(sys.version_info)

# -------Python Variables and commits------
my_variable = 10 # int 
y ="jonh"   # string
float_number = 10.5 # float
complex_number = 3 + 5j # complex
boolean_value = True # boolean

# print(my_variable)
# print(y)
# print(type(my_variable))
# print(float_number)
# print(complex_number)
# print(boolean_value)

#--------multiple words variable names--------
#Camel Case 
myVariableName = "rohan"
#Pascal Case 
MyVariableName ="rohan"
#Snake Case
my_variable_name ="rohan"

# print(myVariableName)


#-----Comments in Pythoon-------
# this is a single line commment
"""
this is a multi line comment
line  2 commit """

'''this is another multi line comment
line 2 of another multi line comment  '''

#-----------Casting in python------------
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
print(type(x), type(y), type(z))

a = float(1)    # a will be 1.0
b = float(2.8)  # b will be 2.8
c = float("3")  # c will be 3.0
d = float("4.2") # d will be 4.2
print(type(a), type(b), type(c), type(d))

e = str("s1") # e will be 's1'
f = str(2)   # f will be '2'
g = str(3.0) # g will be '3.0'
print(type(e), type(f), type(g))



#--------Python--Data---Types-------------
x = "Hello world"  # string
y = 20            # int
z = 20.5          # float
a = 1j            # complex     
b = ["apple", "banana", "cherry"] # list
c = ("apple", "banana", "cherry") # tuple
d = range(6)                     # range
e = {"name" : "John", "age":36}  # dict
f = {"apple", "banana", "cherry"} # set
g = frozenset({"apple", "banana", "cherry"}) # frozenset
h = True                        # bool
i = b"Hello"                   # bytes
j = bytearray(5)               # bytearray
k = memoryview(bytes(5))       # memoryview
# print(type(x), type(y), type(z), type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k))
# print(x, y, z, a, b, c, d, e, f, g, h, i, j, k)


#-------------------------Python---Operator-------------------------------------------------

#01 -Arithmetic operator
x = 15
y = 7
''' 
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)   #floor division
'''

#02--Assignment Operator
x = 5
x += 3 
x -= 2
x *= 5
x /= 2
# print(x)

#03--LOgical operator--
y = 5
print(y > 2 and y < 10) #and oper
print(y > 3 or y < 4)  # one conditions is true
print(not(y > 2 and y < 10))




