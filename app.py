#x = input ("First variable is : ")
#y = input ("Second variable is : ")

#sum = float(x) + float(y)

#print ("Sum of these two variables is : "+ str(sum))

course = "This is for Beginners"
print ("This" in course)
course.capitalize()
print (course.find("for"))

x = 3
x = x + 2
x += 1
y = (10 + 3) * 2

price = 20
print (price < 10 or price > 15)

temperture = 25

if temperture > 30 :
    print ("The weather is hot")

elif temperture < 25:
    print ("The weather is good")

elif temperture < 10:
    print ("The weather is cold")

else :
    print("Done")


weight = input("Please to insert your weight:  ")
statement = input("Do you need to convert it to kilo k or lbs l: ")
letter = statement.upper()
if letter == "K":
    converted = float(weight) / 0.45
    print("your weight is converted to lbs " + str(converted))

else:
    converted = float(weight) * 0.45
    print("your weight is converted to kilo " + str(converted))

i = 1
while i <= 10:
    print(i * '*')
    i = i+1

names = ["Sarra", "Mohamed", "Mounir"]
names[0] = "Mariem"
print(names)
print(names[0])
print(names[0:1])


numbers = [1,2,3,4,5]

print(len(numbers))
print(1 in numbers)

for item in numbers :
    print(item)



i = 0
while i < len(numbers):
    print(numbers[i])
    i = i+1
