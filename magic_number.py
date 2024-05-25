answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


answer = 24
if answer == 24:
    print("That's the correct answer! You won!")


age = 19
print(age < 21 )


age <= 21
print(age < 21)


age < 21
print(age > 21)


age >= 21
print(age > 21)


# check if two people are both over 21 

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# di seguito lo stesso codice ma con le parentesi (facilmente leggibile)

age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))

age_1 = 21
print((age_0 >= 21) and (age_1 >= 21))


#utilizzare or per verificare condizioni multiple

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# utilizzare in per controllare se un valore è in una lista 

requested_toppings =  ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)
