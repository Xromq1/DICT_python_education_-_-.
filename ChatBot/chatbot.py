print("Hello! My name is Friday. I was created in 2022.")
print("Please, remind me your name.")
name = input()
print("What a great name you have,"+ name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is" , age , "that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
c = 0
while (c:= c+1)<=number: print(c, "!")