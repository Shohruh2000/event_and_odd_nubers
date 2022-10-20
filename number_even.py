#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int = 1234
x = ( var_int % 10 ) % 2
y = ( ( var_int // 10 ) % 10 ) % 2
z = ( ( ( var_int // 10 ) // 10 ) % 10 ) % 2
d = ( var_int // 1000 ) % 2 
print(4-(x+y+z+d))
