#Given a string, S, of length N that is indexed from 0 to N-1,
#print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

t=input()                      # Input to get number of strings
inputs=[]                      # Creating an empty list
for i in range(int(t)):
    inputs.append(input())     # adding strings in a list from user input
even=''                        # Creating empty string
odd=''
for j in inputs:
    value=j
    for k in range(len(value)):
        if k %2==0:
            even=even+value[k] # Append even indexing characters into a even string
        else:
            odd=odd+value[k]   # Append odd indexing characters into a odd string
    print(even+" "+odd)
    even=''
    odd=''


## Sample Input:
`2
 First
 Second`

## Sample Output:
`Frt is
 Scn eod`
