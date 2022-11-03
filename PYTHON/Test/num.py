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

# x=input('enter an integer:') 
# y=input('enter an integer:') 
# z=input('enter an integer:') 
# if x==y and y==z: print('all the same') 
# if not x==y and not y==z: print('all different') 
# if x==y or y==z or z==x: print('neither')

