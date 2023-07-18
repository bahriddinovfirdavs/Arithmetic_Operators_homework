#Create a variable called 'number' and assign it the two-digit number
a=int(input())
#Find the reverse of the number and assign it to a variable called 'answer'.
Q=a%10
P=a//10
A=(Q*10)+P
#Print the answer variable
print(A)