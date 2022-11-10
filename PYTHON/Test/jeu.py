
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)

employee_data = {
    "nd": {             #dictionary
     'prenom': 'Dicha',  # key and value
     'nom' : 'Njoh',
     'addresse': ['32 bis bonapriso', '33 bis koumassi']
    },

    "ss": {
      'prenom': 'Charles',
      'nom' : 'Sess',
      'addresse': '228 Tokoin'
    }

}

# print(employee_data["nd"]['prenom'])

# Dicha = employee_data["nd"]

# print(Dicha['addresse'] [1]) #slicing
employee = employee_data.get("ss")

if employee:
    print(f" the value is: {employee} ")

else:
    print("does not exist")