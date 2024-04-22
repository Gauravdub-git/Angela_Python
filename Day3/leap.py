print("Leap Year/Normal Year")
n= int(input("Enter the year = "))
if n%4 == 0:
    if n%400 == 0:
     print("It is not a leap Year")
    else:
       print("It is a leap year")
       
elif n%100 == 0:
    print("It is not a leap year")

else:
    print("IT IS NOT A LEAP YEAR")

