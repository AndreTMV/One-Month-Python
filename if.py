answer = input("Do you want to hear a joke? ")
affirmative_responses = ["yes", "y"]
negative_responses = ["no", "n"]

if "y" in answer.lower():
    print("I'm against picketing, but I don't know how to show it.")
    # if answer.lower() in affirmative_responses:
    #     print("I'm against picketing, but I don't know how to show it.")
    # elif answer == "No" or answer == "no":
    #     print("Fine.")
elif answer.lower() in negative_responses:
    print("Fine.")
else:
    print("I don't understand.")
