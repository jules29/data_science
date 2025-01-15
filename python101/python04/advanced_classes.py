#Creating a dictionnary 
alien_0 = {'color':'green','points':5 ,'x_position':0 , 'y_position':25 , 'speed':'medium'}
print(alien_0['color'])

#Updating new key-values pairs
alien_0["color"] = "Red"

print(alien_0['color'])

#Removing key-values pairs 
del alien_0['y_position']

print(alien_0)

#Adding a new key-values pair
alien_0['z_position'] = 35 

print(alien_0)


for key in alien_0:
    print(key)
    
for value in alien_0.values():
    print(value)
    
for keys, value in alien_0.items():
    print(f"key: {keys}, Value: {value}")
    
alien_0["points"] -=2
print(alien_0)         


# class House:
#     def _init_(self, owner, location, price, width, length):
#         self.owner = owner
#         self.location = location
#         self.price = price
#         self.width = width
#         self.length = length

#     def floor_area(self):
#         return self.width*self.length

#     def price_per_area(self):
#         return self.price /self.floor_area()
#     def house_info(self):
#         return f"Owner: {self.owner}, Location: {self.location}, Price:{self.price}Euro, Price per area: {self.price_per_area()}"

# Jules_house = House("Jules Kasongo", "Djamena, Tchad, Central African Republic", 100000, 30, 40)

# print(Jules_house.house_info())


# class Jules_Skysraper(House):
#     def __init__(self, owner, location ,price , width , length, floor):
#         super().__init__(owner, location, price, width , length )
#         self.floor = floor 
        
#     def floor_area(self):
#         print(super().floor_area()*self.floor)
#         return super().floor_area()*self.floor

# Jules_House = Jules_Skysraper("Jules Dongmo", "Hemmingen, Germany", 1000000, 30, 40, 20)

# print(Jules_Skysraper.house_info())        