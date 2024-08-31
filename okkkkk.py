name = input("enter ur name:")

print(f"assalam o alaikum!{name}, nice to meet you , lets have some fun with numbers")

numbers = []
for i in range(1, 4):
    num = int(input(f"Please enter your favorite number {i}: "))
    numbers.append(num)  
total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {total_sum}")
for num in numbers:
   square = num**2
print (f"\n the square of your number is :" ,{square})
if total_sum % 2 == 0:
    print(f"{total_sum} is an even number.")
else:
    print(f"{total_sum} is an odd number.")



    
print(f"\nThanks for exploring numbers with me, {name}! I hope you had fun.")
