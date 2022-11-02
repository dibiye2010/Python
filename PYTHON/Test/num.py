a = int(input("enter your number: ")) 
b = int(input("enter your number: "))
c = int(input("enter your number: "))

if a == b and b == c or a == c:
    print("Equal")
elif a != b and b != c or a != c:
    print("Not Equal")
elif a == b and b == c or a != c:
    print("Not Equal")

else:
    print("Invalid")

# if a == b == c:
#     print("Equal")
# else:
#     print("Not Equal")

