target = int(input("Enter the no =  "))
even_sum = 0
for number in range(2 ,target + 1 , 2):
    even_sum += number
print(even_sum)