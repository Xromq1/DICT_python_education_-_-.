
def buy_coffee(water, milk, beans, cups, money):
    coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    water_espresso = 250
    coffee_beans_espresso = 16
    money_espresso = 4
    water_latte = 350
    milk_latte = 75
    coffee_beans_latte = 20
    money_latte = 7
    water_cappuccino = 200
    milk_cappuccino = 100
    coffee_beans_cappuccino = 12
    money_cappuccino = 6
    if coffee == '1':
        water -= water_espresso
        beans -= coffee_beans_espresso
        cups -= 1
        money += money_espresso
    elif coffee == '2':
        water -= water_latte
        milk -= milk_latte
        beans -= coffee_beans_latte
        cups -= 1
        money += money_latte
    else:
        water -= water_cappuccino
        milk -= milk_cappuccino
        beans -= coffee_beans_cappuccino
        cups -= 1
        money += money_cappuccino
    print('The coffee machine has:')
    print(water, ' of water')
    print(milk, ' of milk' )
    print(beans, ' of coffee_beans')
    print(cups, ' of disposable cups')
    print(money,' of money')


def fill_coffee(water, milk, beans, cups):
    water_fill = int(input('Write how many ml of water do you want to add: '))
    milk_fill = int(input('Write how many ml of milk do you want to add: '))
    coffee_beans_fill = int(input('Write how many grams of coffee beans do you want to add: '))
    disposable_cups_fill = int(input('Write how many disposable cups of coffee do you want to add: '))
    water += water_fill
    milk += milk_fill
    beans += coffee_beans_fill
    cups += disposable_cups_fill
    print('The coffee machine has:')
    print(water,' of water')
    print(milk, ' of milk')
    print(beans, ' of coffee_beans')
    print(cups, ' of disposable cups')
    print(money, ' of money')


def money_coffee(money):
    print('I gave you $', money)
    money = 0
    print()
    print('The coffee machine has:')
    print(water, ' of water')
    print(milk, ' of milk')
    print(beans, ' of coffee_beans')
    print(cups, ' of disposable cups')
    print(money, ' of money')

water = 400
milk = 540
beans = 120
cups = 9
money = 550
print('The coffee machine has:')
print(water, ' of water')
print(milk, ' of milk')
print(beans, ' of coffee_beans')
print(cups, ' of disposable cups')
print(money, ' of money')
action = input('Write action (buy, fill, take): ')
if action == 'buy':
    buy_coffee(water, milk, beans, cups, money)
elif action == 'fill':
    fill_coffee(water, milk, beans, cups)
else:
    money_coffee(money)
