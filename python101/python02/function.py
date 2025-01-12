introduce = "Hello people"
introduce = introduce.upper() #string methods
print(introduce)

def say_hi(first_name, last_name):    #Missing function or method docstring
    name = first_name + " " + last_name
    return f"Hello {name}!"

print(say_hi("Jules","Mokolo")) #Function call 
print(say_hi("Toure".upper(),"Bonaberi".lower()))   #"Toure":Unknow word

def add(a,b):    #Missing function or method Docstring
    return a+b 

x = 12.5 
y = 14.8 
print(f"The sum of{x} and {y} is {add(x,y)}")

def divide(a,b):
    if b>0:
        return a/b 
    else:
        return "Division by zero not allowed"
    
print(divide(45,5))

def divise2(a,b):    #Missing function or method docstring 
    result = a/b if b>0 else "Division by zero is not allowed"
    return result 

print(round(divise2(2,55),3))

def is_float(num, name):
    if type(num)==float or name=="Koli Boy":
        return True
    return False 
print(is_float(23,"Koli Boy"))


students = ["Jules Toure" , "Joel" , "Calvin"]
students_ages = [34, 45, 56]

for index, student in enumerate(students):
    age =students_ages[index]
    print(f"{student} is {age} years old")

cities = [{"Douala":"Littoral","Yaounde":"Centre", "Hemmingen":"Badenwüttenberg"}, {"Wolfsburg": "Niedersachsen", "Nürnberg":"Bayern","Zwickau":"Sachsen"}]
print(cities[0]["Douala"])

for key in cities[0]:
    print(key)
    
for region in cities[0].values():
    print(region)    
    
for city in cities:
    for key in city.values():
        print(key)
    
        