
print(" pick a number in  your  mind from 0 to 9")
number =  int(input("Enter your number  :"))

if number > 9 :
    print ("the value is greater than 9 ")
    print(" Choose a number below 9")
    number =  int(input("Enter your number  :"))

elif number < 0:
    print("the value is lesser that 0 ")
    print(" choose a number above 0 ")
    number =  int(input("Enter your number  :"))
else:
    print ("the given value comes in the category between 0 and 9 you can countinue " )
    

print ("double the number.")
print (" add five to the new number. ")
print ("multiply the answer by five.")



a =  ( number * 2 )
b = ( a + 5 ) 
c = ( b * 5)
 
print("your answer should be " , c)

print ("pick another number from 0 to 9.")
print("add the value to the original value ")
number2 =  int(input("Enter the number you have recieved  :"))

print("answer  to the this is the the first and the last digit to this number  " , c -25  )
