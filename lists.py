the_count = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner",
                 1/2, ["Oh no", "A list inside a list"]]

for number in the_count:
    print("This is count", number)

for stock in stocks:
    print("Stock ticker: ", stock)

for i in random_things:
    print("Stock ticker: ", i)

people = []

people.append("Andre")
people.append("Andrew")
people.append("Andrea")

# Print all the people
print(people)

# Remove an item from a list
people.remove("Andre")
print(people)

for person in people:
    print(f"Person is {person}")

for number in range(1, 101):
    print(f"{number} squared is {number**2}")

# here's how you acces elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print(f"There are {len(random_things)} elements in random_things")
print("thing is a:", type(random_things))

another_list = random_things[-1]
print(another_list)
print(type(another_list))
