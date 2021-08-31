def greet(name):
    return f"Hey {name}!"


print(greet('Andre'))
print(greet('Isis'))


def concatenate(word_one, word_two):
    return word_one + ' ' + word_two


print(concatenate('Andre', 'Isis'))


def age_in_dog_years(age):
    return age * 7


print(age_in_dog_years(17))

print(concatenate(word_two='Andre', word_one='Isis'))


def uppercase_and_reverse(string):
    return string.upper()[::-1]  # string[::-1].upper()


print(uppercase_and_reverse("Hola como estas"))
