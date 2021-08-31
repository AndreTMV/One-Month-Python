# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"{number} is Fizzbuzz")
#     elif number % 3 == 0:
#         print(f"{number} is Fizz")
#     elif number % 5 == 0:
#         print(f"{number} is Buzz")
#     else:
#         print(number)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print(f"{number} is Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print(f"{number} is Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print(f"{number} is FizzBuz")
    else:
        print(number)
