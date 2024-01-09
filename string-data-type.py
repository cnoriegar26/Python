print("Cadena")
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print("\n")

print("Concatenación de cadenas")
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("\n")

print("Cadenas de entradas")
name = input("What is your name?:")
print(name)
print("\n")

print("Dar formato a las cadenas de entradas")
color = input("What is your favorite color?: ")
animal = input("What is your favorite animal?:  ")
print("{}, you like a {} {}!".format(name,color,animal))