# Import libraries

# Used for shuffling
import random
# Used to count seconds before updating the board
import time
# Used to clear the console
import os
# Used to check which OS the user is on
import platform

# Here, all string variables containing the card drawings are initialized.
# splitlines is used to also initialize the lists for each one.

c1=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |    ww_          ___.///   |
     |   o__ `._.-'''''    //    |
     |   |/  \   ,     /   //    |
     |        \  ``,,,' _//      |
     |         `-.  \--'         |
     |           \_/_/           |
     |            |||            |
     |                           |
     |                           |
     =============================
 """
lc1 = c1.splitlines()
c2=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |                           |
     |     |\_/|,,_____,~~`      |
     |     (.".)~~     )`~|}     |
     |      \o/\ /---~|\ ~|}     |
     |        _//    _// ~}      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc2 = c2.splitlines()
c3=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |                           |
     |        .|||||||||.        |
     |       |||||||||||||       |
     |      |||||||||||' .\      |
     |      `||||||||||_,__o     |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc3 = c3.splitlines()
c4=""" 
     =============================
     |                           |
     |                           |
     |      c~~p ,---------.     |
     |  ,---'oo  )           \   |
     | ( O O                  )  |
     |  `=^='                 /  |
     |       \    ,      .   /   |
     |        \_  |-----'|  /    |
     |        ||__|    |_|__|    |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc4 = c4.splitlines()
c5=""" 
     =============================
     |                           |
     |                           |
     |     (\__/)  .~    ~. ))   |
     |     /O O `./      .'      |
     |    {O__,   \    {         |
     |      / .  . )    \        |
     |      |-| '-' \    } ))    |
     |     .(   _(   )_.'        |
     |    '---.~_ _ _&           |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc5 = c5.splitlines()
c6=""" 
     =============================
     |                           |
     |                           |
     |       .-:'  `; `-._       |
     |      (_,           )      |
     |    ,'o"(            )>    |
     |   (__,-'            )     |
     |      (             )      |
     |       `-'._.--._.-'       |
     |          |||  |||         |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc6 = c6.splitlines()
c7=""" 
     =============================
     |                           |
     |                           |
     |                  _        |
     |      __   ___.--'_`.      |
     |     ( _`.'. -   'o` )     |
     |     _\.'_'      _.-'      |
     |    ( \`. )    //\`        |
     |     \_`-'`---'|\__,       |
     |      \`_-       `-\       |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc7 = c7.splitlines()
c8=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |                  __       |
     |      _.,-;-;-,. /'_\      |
     |     /_/_/_/_|_\_\) /      |
     |    '-<_><_><_><_>=/\      |
     |      `/_/====/_/-'\_\     |
     |       ""     ""    ""     |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc8 = c8.splitlines()
c9=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |      ___                  |
     |   __/_  `.  .-"'"-.       |
     |   \_,` | \-'  /   )`-')   |
     |    "") `"`    \  ((`"`    |
     |    ___Y  ,    .'7 /|      |
     |   (_,___/...-` (_/_/      |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc9 = c9.splitlines()
c10=""" 
     =============================
     |                           |
     |          z                |
     |        Z                  |
     |      z                    |
     |   |\      _,,,---,,_      |
     |   /,`.-'`'    -.  ;-;;,_  |
     |  |,4-  ) )-,_. ,\ (  `'-' |
     | '---''(_/--'  `-'\_)      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc10 = c10.splitlines()
c11=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |            ((`\           |
     |         ___ \ '--._       |
     |      .'`   `'    o  )     |
     |     /    \   '. __.'      |
     |    _|    /_  \ \_\_       |
     |   {_\______\-'\__\_\      |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc11 = c11.splitlines()
c12=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |                           |
     |        ,::////;::-.       |
     |       /:'///// ``::>/|/   |
     |     .',  ||||    `/( e\   |
     | -==~-'`-Xm````-mm-' `-_\  |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
lc12 = c12.splitlines()

# Here, the designs for all the card backs are also initialized in string variables.

n1=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |           1111            |
     |             11            |
     |             11            |
     |             11            |
     |           111111          |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n2=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |            2222           |
     |           22  22          |
     |              22           |
     |             22            |
     |           222222          |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n3=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |            3333           |
     |           33  33          |
     |              333          |
     |           33  33          |
     |            3333           |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n4=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |           44  44          |
     |           44  44          |
     |           444444          |
     |               44          |
     |               44          |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n5=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |           555555          |
     |           55              |
     |           55555           |
     |               55          |
     |           55555           |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n6=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |            6666           |
     |           66              |
     |           66666           |
     |           66  66          |
     |            6666           |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n7=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |           7777777         |
     |               77          |
     |              77           |
     |             77            |
     |            77             |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n8=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |            8888           |
     |           88  88          |
     |            8888           |
     |           88  88          |
     |            8888           |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n9=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |            9999           |
     |           99  99          |
     |            99999          |
     |               99          |
     |            9999           |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n10=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111     0000       |
     |         11    00  00      |
     |         11    00  00      |
     |         11    00  00      |
     |       111111   0000       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n11=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111    1111        |
     |         11      11        |
     |         11      11        |
     |         11      11        |
     |       111111  111111      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n12=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111     2222       |
     |         11    22  22      |
     |         11       22       |
     |         11      22        |
     |       111111  222222      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n13=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111     3333       |
     |         11    33  33      |
     |         11       333      |
     |         11    33  33      |
     |       111111   3333       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n14=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111    44  44      |
     |         11    44  44      |
     |         11    444444      |
     |         11        44      |
     |       111111      44      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n15=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111    555555      |
     |         11    55          |
     |         11    55555       |
     |         11        55      |
     |       111111  55555       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n16=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111     6666       |
     |         11    66          |
     |         11    66666       |
     |         11    66  66      |
     |       111111   6666       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n17=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111   7777777      |
     |         11       77       |
     |         11      77        |
     |         11     77         |
     |       111111  77          |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n18=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111     8888       |
     |         11    88  88      |
     |         11     8888       |
     |         11    88  88      |
     |       111111   8888       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n19=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |       1111    9999        |
     |         11   99  99       |
     |         11    99999       |
     |         11       99       |
     |       111111  9999        |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """ 
n20=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |        2222    0000       |
     |       22  22  00  00      |
     |          22   00  00      |
     |         22    00  00      |
     |       222222   0000       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n21=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |        2222   1111        |
     |       22  22    11        |
     |          22     11        |
     |         22      11        |
     |       222222  111111      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n22=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |        2222    2222       |
     |       22  22  22  22      |
     |          22      22       |
     |         22      22        |
     |       222222  222222      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n23=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |        2222    3333       |
     |       22  22  33  33      |
     |          22      333      |
     |         22    33  33      |
     |       222222   3333       |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """
n24=""" 
     =============================
     |                           |
     |                           |
     |                           |
     |        2222   44  44      |
     |       22  22  44  44      |
     |          22   444444      |
     |         22        44      |
     |       222222      44      |
     |                           |
     |                           |
     |                           |
     |                           |
     =============================
 """


# Used to track when the player completes the game, 
points = 0

# Used to count the number of turns taken.
counter = 0

# Here, we initialize our three lists used to display and change the board.

# These are our animal cards which we need to shuffle with shuffle().
cards = [c1,c1,c2,c2,c3,c3,c4,c4,c5,c5,c6,c6,c7,c7,c8,c8,c9,c9,c10,c10,c11,c11,c12,c12]

# This is the board that gets updated every time the player flips a card to display it.
initialBoard = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24]

# This order variable is used solely to always know how the completely flipped board looks.
order = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24]


# Here we initialize our lists of card lines when they are not flipped.
ln1 = initialBoard[0].splitlines()
ln2 = initialBoard[1].splitlines()
ln3 = initialBoard[2].splitlines()
ln4 = initialBoard[3].splitlines()
ln5 = initialBoard[4].splitlines()
ln6 = initialBoard[5].splitlines()
ln7 = initialBoard[6].splitlines()
ln8 = initialBoard[7].splitlines()
ln9 = initialBoard[8].splitlines()
ln10 = initialBoard[8].splitlines()
ln11 = initialBoard[10].splitlines()
ln12 = initialBoard[11].splitlines()
ln13 = initialBoard[12].splitlines()
ln14 = initialBoard[13].splitlines()
ln15 = initialBoard[14].splitlines()
ln16 = initialBoard[15].splitlines()
ln17 = initialBoard[16].splitlines()
ln18 = initialBoard[17].splitlines()
ln19 = initialBoard[18].splitlines()
ln20 = initialBoard[19].splitlines()
ln21 = initialBoard[20].splitlines()
ln22 = initialBoard[21].splitlines()
ln23 = initialBoard[22].splitlines()
ln24 = initialBoard[23].splitlines()


# Functions

# This function is called whenever we need to display our board.
def graphBoard():

    # We update our splitlines lists as the cards may have changed.
    ln1 = initialBoard[0].splitlines()
    ln2 = initialBoard[1].splitlines()
    ln3 = initialBoard[2].splitlines()
    ln4 = initialBoard[3].splitlines()
    ln5 = initialBoard[4].splitlines()
    ln6 = initialBoard[5].splitlines()
    ln7 = initialBoard[6].splitlines()
    ln8 = initialBoard[7].splitlines()
    ln9 = initialBoard[8].splitlines()
    ln10 = initialBoard[9].splitlines()
    ln11 = initialBoard[10].splitlines()
    ln12 = initialBoard[11].splitlines()
    ln13 = initialBoard[12].splitlines()
    ln14 = initialBoard[13].splitlines()
    ln15 = initialBoard[14].splitlines()
    ln16 = initialBoard[15].splitlines()
    ln17 = initialBoard[16].splitlines()
    ln18 = initialBoard[17].splitlines()
    ln19 = initialBoard[18].splitlines()
    ln20 = initialBoard[19].splitlines()
    ln21 = initialBoard[20].splitlines()
    ln22 = initialBoard[21].splitlines()
    ln23 = initialBoard[22].splitlines()
    ln24 = initialBoard[23].splitlines()


    # The following loops concatenate the lines of the necessary cards and print them out gradually like a printer.
    # The reason there are four different loops is that 6 cards are printed 4 times.
    for i in range(16):
        print(ln1[i]+ln2[i]+ln3[i]+ln4[i]+ln5[i]+ln6[i])
        
    for i in range(16):   
        print(ln7[i]+ln8[i]+ln9[i]+ln10[i]+ln11[i]+ln12[i])

    for i in range(16):
        print(ln13[i]+ln14[i]+ln15[i]+ln16[i]+ln17[i]+ln18[i])

    for i in range(16):
        print(ln19[i]+ln20[i]+ln21[i]+ln22[i]+ln23[i]+ln24[i])


# This function is used to clear the console before updating the board.
def clear():
    if platform.system() == "Windows":    
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Darwin":
        os.system('clear')


# Start
# This is where the program begins to execute

print("""



    
                                                                            
                                                                                    _      _____ _     ____  ____  _      _____
                                                                                    / \  /|/  __// \   /   _\/  _ \/ \__/|/  __/
                                                                                    | |  |||  \  | |   |  /  | / \|| |\/|||  \  
                                                                                    | |/\|||  /_ | |_/\|  \_ | \_/|| |  |||  /_ 
                                                                                    \_/  \|\____\\\\____/\____/\____/\_/  \|\____\\
                                            
                        
                                                                                                       _____  ____ 
                                                                                                      /__ __\/  _ \\
                                                                                                        / \  | / \|
                                                                                                        | |  | \_/|
                                                                                                        \_/  \____/
                                                                                                                    

    
              _____                    _____                    _____                   _______                   _____                    _____                    _____                    _____          
             /\    \                  /\    \                  /\    \                 /::\    \                 /\    \                  /\    \                  /\    \                  /\    \         
            /::\____\                /::\    \                /::\____\               /::::\    \               /::\    \                /::\    \                /::\____\                /::\    \        
           /::::|   |               /::::\    \              /::::|   |              /::::::\    \             /::::\    \              /::::\    \              /::::|   |               /::::\    \       
          /:::::|   |              /::::::\    \            /:::::|   |             /::::::::\    \           /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
         /::::::|   |             /:::/\:::\    \          /::::::|   |            /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
        /:::/|::|   |            /:::/__\:::\    \        /:::/|::|   |           /:::/    \:::\    \       /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \    
       /:::/ |::|   |           /::::\   \:::\    \      /:::/ |::|   |          /:::/    / \:::\    \     /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \   
      /:::/  |::|___|______    /::::::\   \:::\    \    /:::/  |::|___|______   /:::/____/   \:::\____\   /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \  
     /:::/   |::::::::\    \  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \ 
    /:::/    |:::::::::\____\/:::/__\:::\   \:::\____\/:::/    |:::::::::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/  \:::\   \:::\____
    \::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /\::/    / ~~~~~/:::/    / \:::\    \   /:::/    / \::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\::/    \:::\  /:::/    /
     \/____/      /:::/    /  \:::\   \:::\   \/____/  \/____/      /:::/    /   \:::\    \ /:::/    /   \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /  \/____/ \:::\/:::/    / 
                 /:::/    /    \:::\   \:::\    \                  /:::/    /     \:::\    /:::/    /          |:::::::::/    /            \::::::/    /               /:::/    /            \::::::/    /  
                /:::/    /      \:::\   \:::\____\                /:::/    /       \:::\__/:::/    /           |::|\::::/    /              \::::/    /               /:::/    /              \::::/    /   
               /:::/    /        \:::\   \::/    /               /:::/    /         \::::::::/    /            |::| \::/____/               /:::/    /               /:::/    /               /:::/    /    
              /:::/    /          \:::\   \/____/               /:::/    /           \::::::/    /             |::|  ~|                    /:::/    /               /:::/    /               /:::/    /     
             /:::/    /            \:::\    \                  /:::/    /             \::::/    /              |::|   |                   /:::/    /               /:::/    /               /:::/    /      
            /:::/    /              \:::\____\                /:::/    /               \::/____/               \::|   |                  /:::/    /               /:::/    /               /:::/    /       
            \::/    /                \::/    /                \::/    /                 ~~                      \:|   |                  \::/    /                \::/    /                \::/    /        
             \/____/                  \/____/                  \/____/                                           \|___|                   \/____/                  \/____/                  \/____/         
""")

print("""


""")

# This input is just to show the initial image until the player presses any key.

start = input("                                                                                       Press any key to continue:  ")
clear()


# Shuffle cards
# This is where a new deck is created each time.
random.shuffle(cards)


# Logic

# This loop checks if all 24 cards have been flipped.
# Each pair of matching cards found by the player increases the score by 1.
while points != 12:

    clear()
    
    # Start by displaying the board and asking the user to choose a card.
    graphBoard()

    print("Current turn:  " + str(counter))
    print("")
    numCard1 = input("Choose a card:   ")
    try:

        # Convert the input variable to an integer.
        numCard1 = int(numCard1)
    
        # Check if the chosen card is within the valid list of cards.
        if numCard1 >=1 and numCard1 <= 24:
            clear()
            if cards[numCard1-1] != initialBoard[numCard1-1]:
                
                # Update the chosen card to the shuffled card in our list.
                initialBoard[numCard1-1] = cards[numCard1-1]

                # Update the board display and ask for another card.
                graphBoard()
                numCard2 = input("Choose another card:   ")

                try:
                    # Convert the input variable to an integer.
                    numCard2 = int(numCard2)

                    # Check if the player did not choose the same card again.
                    if numCard1 != numCard2:

                        # Check if the second card is valid.
                        if numCard2 >=1 and numCard2 <= 24:
                            
                            # Check if the second card has not been flipped before.
                            if cards[numCard2-1] != initialBoard[numCard2-1]:

                                clear()

                                # If everything is fine, update the board with the second chosen card.
                                initialBoard[numCard2-1] = cards[numCard2-1]
                                
                                graphBoard()

                                # Check if both cards match.
                                if initialBoard[numCard1-1] == initialBoard[numCard2-1]:
                                    
                                    # If they match, add a point and increment the counter.
                                    points += 1
                                    counter += 1

                                    print("")
                                    print("Loading...")

                                    # Wait two seconds before clearing the board and starting again.
                                    time.sleep(2)
                                    clear()

                                else:
                                    # If they don't match, just increment the counter and flip the cards back.
                                    counter+=1
                                    initialBoard[numCard1-1] = order[numCard1-1]
                                    initialBoard[numCard2-1] = order[numCard2-1]
                                    

                                    print("")
                                    print("Loading...")

                                    # Wait three seconds before updating the program so the player can see the cards.
                                    time.sleep(3)
                                    clear()

                            else:
                                # Flip the first card back and clear the board if the second card was already flipped.
                                initialBoard[numCard1-1] = order[numCard1-1]
                                clear()
                                print("Please choose a card you haven't selected yet <3")    
                               
                        else:
                            # Flip the first card back and clear the board if the second card is invalid.
                            initialBoard[numCard1-1] = order[numCard1-1]
                            clear()
                            print("Choose a valid card")
                            print("")

                    else:
                        # Flip the first card back and clear the board.
                        initialBoard[numCard1-1] = order[numCard1-1]
                        clear()
                        print("Please choose two different cards <3")

                # Use this except block to ensure the player chooses a number.
                except:
                    initialBoard[numCard1-1] = order[numCard1-1]
                    clear()
                    print("Letters are not numbers <3")

            else:
                print("Please choose a card you haven't flipped yet <3")

        # If the card is not valid.
        else: 
            clear()
            print("Choose a valid card")
            print("")
    
    # Use this except block to ensure the player chooses a number.
    except:
        clear()
        print("Letters are not numbers <3")
        
            
# Print final message with the number of turns

if(counter >17):
    print("""







                                                                           
                                                                                 ____  ____  _      _____ ____  ____  _____  _     _     ____  _____  _  ____  _      ____ 
                                                                                /   _\/  _ \/ \  /|/  __//  __\/  _ \/__ __\/ \ /\/ \   /  _ \/__ __\/ \/  _ \/ \  /|/ ___\\
                                                                                |  /  | / \|| |\ ||| |  _|  \/|| / \|  / \  | | ||| |   | / \|  / \  | || / \|| |\ |||    \\
                                                                                |  \_ | \_/|| | \||| |_//|    /| |-||  | |  | \_/|| |_/\| |-||  | |  | || \_/|| | \||\___ |
                                                                                \____/\____/\_/  \|\____\\\\_/\_\\\\_/ \|  \_/  \____/\____/\_/ \|  \_/  \_/\____/\_/  \|\____/
                                                                                                                                                                        



                                                                            








                                
    """)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                                                                            Game completed in "+str(counter)+ " turns.")
    print("")
    print("")
    print("")
    print("                                                                                        Try to complete it in less turns!")
    print("")
    print("")
    print("")
    print("")
    print("")
    time.sleep(20)
            

else:
    print("""







                                                                                                                                                        
                                                                             ____  ____  _      _____ ____  ____  _____  _     _     ____  _____  _  ____  _      ____ 
                                                                            /   _\/  _ \/ \  /|/  __//  __\/  _ \/__ __\/ \ /\/ \   /  _ \/__ __\/ \/  _ \/ \  /|/ __\\
                                                                            |  /  | / \|| |\ ||| |  _|  \/|| / \|  / \  | | ||| |   | / \|  / \  | || / \|| |\ |||    \\
                                                                            |  \_ | \_/|| | \||| |_//|    /| |-||  | |  | \_/|| |_/\| |-||  | |  | || \_/|| | \||\___ |
                                                                            \____/\____/\_/  \|\____\\\\_/\_\\\\_/ \|  \_/  \____/\____/\_/ \|  \_/  \_/\____/\_/  \|\____/
                                                                                                                                                                    



                                                                            








                                
    """)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                                                                            Game completed in "+str(counter)+ " turns.")
    print("")
    print("")
    print("")
    print("                                                                                            But I'm sure you cheated")
    print("")
    print("")
    print("")
    print("")
    time.sleep(20)






