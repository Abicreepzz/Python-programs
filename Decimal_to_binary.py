def binary(n):
  result=''
  while n>0:
    result=str(n%2)+str(result)
    n//=2
return int(result)

binary(5) ##output= 101
