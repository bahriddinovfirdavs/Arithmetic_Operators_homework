#Create a variable called 'number' and assign it the three-digit number.
a=int(input())
#Find the 'number' first digit and assign to x1.
x1=a//100
#Find the 'number' second digit and assign to x2.
x2=(a//10)%10
#Find the 'number' third digit and assign to x3.
x3=a%10
#Create a variable called 'answer' and assign it the sum of the three digits.
O=x1+x2+x3
#print the sum of the three digits.
print(O)