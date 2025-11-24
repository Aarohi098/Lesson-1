var1 = 1
var2 = "apple"
var3 = 4.2
var4 = True

print("I have" , var1 , var2)
print("I would like to eat an" , var2, "I would like to eat" , var1 , var2 , "at a time")
print(f"I would like to eat an {var2}. I would like to eat {var1} {var2} at a time")
print("I would like to eat an {}. I would like to eat {} {} at a time".format(var2, var1, var2))

a = 214
b = 527
result = a + b

print("Sum of %d and %d is %d"%(a, b, result))

print("The data type of var1 is" , type(var1))
print("The data type of var2 is" , type(var2))
print("The data type of var3 is" , type(var3))
print("The data type of var4 is" , type(var4))

num1 = var3
print(type(num1), num1)
num1 = int(num1)
print(type(num1), num1)

string = "24"
print(type(string), string)
string = int(string)
print(type(string), string)

variable = 24
variable2 = 6

#4
result = 24/6
#0
result2 = 24%6
#4
result3 = 24//6

print(result , "\n"  , result2  ,"\n" , result3 )

