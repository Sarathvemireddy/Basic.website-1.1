n = int(input("Enter the number of terms: "))
a = 0
b = 1
if n < 0:
   print("Incorrect input")
elif n == 1:
   print("The Fibonacci sequence up to",n,"is: ",a)
else:
   print("The Fibonacci sequence up to",n,"is: ",a,",",b)
   for i in range(2,n):
       c = a + b
       a = b
       b = c
       print(",",c)