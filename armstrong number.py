# Python Program For Armstrong Number using While Loop

Number = int(input("\nPlease Enter the Number to Check for Armstrong: "))

# Initializing Sum and Number of Digits
Sum = 0
Times = 0
           
# Calculating Number of individual digits
Temp = Number
while Temp > 0:
           Times = Times + 1
           Temp = Temp // 10

# Finding Armstrong Number
Temp = Number
while Temp > 0:
           Reminder = Temp % 10
           Sum = Sum + (Reminder ** Times)
           Temp //= 10
if Number == Sum:
           print("\n %d is Armstrong Number.\n" %Number)
else:
           print("\n %d is Not a Armstrong Number.\n" %Number)
        

#function to check the number is inverse of the numbers:
n=int(input("enter numbers:"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number is:",rev)






