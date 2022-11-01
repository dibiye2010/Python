# This program will ask the users for a number and will check if it is Even or Odd.
number = int(input("enter a number between 1 and 100: \n"))
if (number % 2) == 0:
    print(f"the number you entered {number} is Even")
else:
    print(f"the number you entered {number} is Odd")