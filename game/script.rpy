# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ren = Character("Ren")
define Raul = Character("Raul")
define Joh = Character("Johnny")
define Pris = Character("Priscila")
define Ale = Character("Alexandra")

define Tio_Astolfo = Character("Astolfo")
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    call Introducao
