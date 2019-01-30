'''#program to check the armstrong numbers or not armstrong:
num=int(input("enter the numbers:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"is a armstrong numbers.")
else:
    print(num,"is not armstrong numbers.")
'''

#function to check the number is inverse of the numbers:
n=int(input("enter the numbers:"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number is:",rev)






