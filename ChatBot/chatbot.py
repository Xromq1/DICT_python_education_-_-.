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
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
def test():

 otvet=int(input())

 if otvet == 2:
  print("Completed, have a nice day!");
  print("Congratulations, have a nice day!"); exit(0)
 if otvet!=2:
  print("Please, try again.");
 test()
test()