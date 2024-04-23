number = 0 
for i in range(1 , 101):
    if i%3 and i%5 == 0:
        print("FizzBUzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    
    else:
        print(i)