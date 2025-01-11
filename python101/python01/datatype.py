print("hello world") # string
print(42) #Integer
print(3.14) #Float
print(True) #Boolean
print(None) #NoneType
print([])
print(())
print({})

ages = [23, 45, 56 , 68]#List
print(ages)
print(f"The type of {ages} is {type(ages)}")
users = {"Name": "Jules le Koli", "age": 18, "Adress": "Hemmingen , Wolfsburg" , "Gender":"Male"} #Dictionary
print(users)


#Reading datatype
print(f"The first person is: {ages[0]} years old")
print(f"The first person is: {ages[1]} years old")

print(users["Name"])
print(users["Adress"])

print(ages[1:4])
print(range(10))

greet = "Hello world!"
introduce = greet + f'\nMy name is {users["Name"]} and I am {users["Gender"]}'
print(introduce)
print(("Jules", 23))
user = (users ["Name"],users["age"]) #Tuple
print(user)
print(user[0]) #Indexing