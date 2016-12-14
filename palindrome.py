n =  int( input("Enter Value to be checked: ") )

originalNum = n
revNum = 0

while n > 0 :
    temp = int(n % 10)
    #print("temp is: ",temp)
    n = int(n / 10)
    revNum = (revNum * 10) + temp

print("Original No. is: ",originalNum)
print("Rev No. is: ",revNum)

if originalNum == revNum:
    print("No. is Palindrome.")
else:
    print("No. is not a Palindrome.")
