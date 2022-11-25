# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Ren", color="#000000")
define Raul = Character("Raul", color="#00D710")
define Joh = Character("Johnny", color="#B10000")
define Pris = Character("Priscila", color="#FF0097")
define Ale = Character("Alexandra", color="#00BFBF")

define Tio_Astolfo = Character("Astolfo", color="#545454")
define Cida = Character("Cida", color="#663535")

default pointsPriscila = 0
default pointsRaul = 0
default pointsAlexandra = 0
default pointsJohnny = 0

#Day 1 - Check if the player met the characters
default firstTimeInCenter = False
default talkToPriscila1 = False
default talkToRaul1 = False
default talkToAlexandra1 = False
default talkToJohnny1 = False
# The game starts here.

#Day 3 - Check if the player met the characters
default talkToPriscila3 = False

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
#<<<<<<< Updated upstream
    call Dia3_AlexandraPriscila
#=======
    call Dia4_PriscilaJohnny
#>>>>>>> Stashed changes
