from art import logo

print(logo)
print('Welcome to Treasure Island. \n'
      'Your mission is to find the treasure.')
c1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right": \n ')
c2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type '
           '"swim"'
           'to swim across.\n ')
c3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which "
           "color do you choose?: \n ")

# logic of the game here:
if c1.lower() == 'left':
    if c2.lower() == 'wait':
        if c3.lower() == 'yellow':
            print("You Win!")
        elif c3.lower() == 'red':
            print("Burned by fire. Game Over.")
        elif c3.lower() == 'blue':
            print('Eaten by beats. Game Over.')
        else:
            print('Game Over.')
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall in to a hole. Game Over.")
