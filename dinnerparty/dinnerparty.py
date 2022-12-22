import random
import sys

print("Enter the number of friends joining (including you):")
int_personas: int = int(input("; "))

if int_personas <= 0:
    print("No one is joining for the party."); exit(0)

print("Enter the total amount")
total_price=int(input())

individual_price = total_price/int_personas

print("Enter the name of every friend (including you), each on a new line: ")
friend_names = {}

for i in range(int_personas):
  friend_names[input()] = round(individual_price, 2)

print(friend_names)

lucky_man = input("Do you want to use the ""Who is lucky?"" feature? Write y/n:" "\n: ")
choice_lucky = random.choice([key for key in friend_names.keys()])

if lucky_man.lower() == "y":
    int_personas -= 1
    print(f"{choice_lucky} is the lucky one!")
else:
    print("No one is going to be lucky" "\n")

amount_person = round((total_price / int_personas), 2)
for key in friend_names.keys():
    if key == choice_lucky and lucky_man.lower() == 'y':
        friend_names[key] = 'is the lucky one!'
    else:
        friend_names[key] = amount_person

print(friend_names)


