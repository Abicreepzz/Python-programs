def binary(n):
  result=''
  while n>0:
    result=str(n%2)+str(result)
    n//=2
  return int(result)

binary(5) ##output= 101
# Another simple one line code for converting the decimal number to binary is followed:

def f(n): print('{:04b}'.format(n))
  
binary(5) ##output =101

# If we want to print in the 8 bit digit of the binary numbers then we can just specify the 8 bit in function.

def f(n): print('{:08b}'.format(n))
  
binary(5) ##output = 00000101
