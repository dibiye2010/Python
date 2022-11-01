# This program will compute the grades on 5 differents Subjects and will give the average grade score
Mathematics = int(input("Enter your grade in Mathematics: \n"))
Science = int(input("Enter your grade in Science: \n"))
Literature = int(input("Enter your grade in Literature: \n"))
Psychology = int(input("Enter your grade in Psychology: \n"))
History = int(input("Enter your grade in History: \n"))
Average_Grade = int((Mathematics + Science + Literature + Psychology + History) / 5)
if Average_Grade > 90 or Average_Grade == 90:
    print("GREAT Job!!! you pass the Semester with A ")
elif Average_Grade > 80 or Average_Grade == 80:
    print("GOOD Job!!! you Pass the Semester with B ")
elif Average_Grade > 70 or Average_Grade == 70:
    print("Nice! you pass the Semester with C ")
elif Average_Grade > 60 or Average_Grade == 60:
    print(" Alright you Pass the Semester with D, but you need to put more effort.")

else:
    print("Sorry, but you Failed the Semester with E, you need to work harder.")
    

