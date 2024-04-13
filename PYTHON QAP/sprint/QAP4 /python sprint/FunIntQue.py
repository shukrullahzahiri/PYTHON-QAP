
for number in range(1, 101):
    if number % 5 == 0 and number % 8 == 0:
        print("FizzBizz")
    elif number % 5 == 0:
        print("Fizz")
    elif number % 8 == 0:
        print("Buzz")
    else:
        print(number)

print(":")
