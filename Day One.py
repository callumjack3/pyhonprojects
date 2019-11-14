"""

print ("hello")
print ("how are you")
print (len('hello'))
print ('hello'.upper())
print('hello'[2])
import random
print(random.randint(1,10))
print ("seni seviyorum")

print ("   |   |")
print ("   |   |")
print ("   |   |")
print ("-----------")
print ("   |   |")
print ("   |   |")
print ("   |   |")
print ("-----------")
print ("   |   |")
print ("   |   |")
print ("   |   |")


favourite_drink = 'Ayran'
print (favourite_drink)
print ('My favourite drink is ' + favourite_drink)
favourite_food = "Tavuk Doner"
print('My favourite food is {}'.format(favourite_food))
print ('My favourite food is {} and my favourite drink is {}' .format(favourite_food, favourite_drink))
i = 10
print(i)
i += 2
print(i)

i = 6
i * 6
print (i*6)

sevcalcim =20
sevcalcim +18
print (sevcalcim+18)

age = 16
if age > 17:
    print ("Yes, I can serve you")
else: print ("No sorry, I can't serve you")

day = "Wednesday"
if day == "Saturday" or day == "Sunday":
    print ("It's weekend!")
else:
    print ("It is a weekday.")
"""

password = 'hellohowareyoutoday'

if len(password) < 8:
    print("Your password is too short!")
else:
    print("Password meets requirements!")

num = 7
if num % 3 ==0:
 print ('number is divisible by 3')
else:
    print ("Number is not divisible by 3")

time = 9
town_of_home = "Stockport"
place_of_work = "Altrincham"

if time > 7:
    print("It's {} o'clock. I'm at home in {}.".format(time, town_of_home))
elif time == 8:
    print("I am commuting from {} to {}.".format(town_of_home, place_of_work))
elif time == 9:
    print("I am at work in {}.".format(place_of_work))

num1 = 5
num2 = 4

if (num1 + num2) % 2 == 0:
    print("it is even.")
else:

    print("it is odd.")

space1 = 'x'
space2 = 'x'
space3 = 'x'

print (" {} |{} |   {}".format(space1, space2, space3))
print ("   |   |")
print ("   |   |")
print ("-----------")
print ("   |   |")
print ("   |   |")
print ("   |   |")
print ("-----------")
print ("   |   |")
print ("   |   |")
print ("   |   |")


space_1 = "X"
space_2 = "X"
space_3 = "O"
space_4 = "X"
space_5 = "X"
space_6 = " "
space_7 = "O"
space_8 = " "
space_9 = " "


print("   |   |   ")
print(" {} | {} | {} ".format(space_1, space_2 , space_3 ))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space_4, space_5 , space_6 ))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} | {} ".format(space_7, space_8 , space_9 ))
print("   |   |   ")

if space_1 == space_2 and space_2 == space_3:
    print("You win")
else:
    print("You have not won yet.")


age = 62

if age < 18:
    print("Child ticket for £8.00.")
    
elif age > 59:
    print("Senior ticket for £7.50.")

else:
    print("Adult ticket for £10.95.")

fav_songs = [
    'A',
    'B',
    'C'
    ]
print (fav_songs)
fav_songs.append('D')
fav_songs.pop()
print (fav_songs)


fav_websites = [
    'Twitter',
    'YouTube',
    'Instagram'
    ]
fav_websites.append ('Facebook')
fav_websites.append ('Myspace')
fav_websites.pop ()
fav_websites.remove ('Twitter')
print (fav_websites)

import random
for i in range (50):
    print (random.randint(1,50))

cars = ["Ford"]
    print(cars)
