#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".

var_int = 2375
x = ( var_int % 10 ) % 2
y = ( ( var_int // 10 ) % 10 ) % 2
z = ( ( ( var_int // 10 ) // 10 ) % 10 ) % 2
d = ( var_int // 1000 ) % 2 
print(x+y+z+d)