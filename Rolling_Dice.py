import random

a = input("type yes if you wish to roll the dice")
if a == "yes":
    a = random.randrange(1,6)
    if a == 1:
        print(" -----------")
        print( "|           |")
        print( "|           |")
        print( "|     o     |")
        print( "|           |")
        print( "|           |")
        print( " -----------")
    elif a == 2:
        print(" -----------")
        print( "|           |")
        print( "|     o     |")
        print( "|           |")
        print( "|     o     |")
        print( "|           |")
        print( " -----------")
    elif a == 3:
        print(" -----------")
        print( "|     o     |")
        print( "|           |")
        print( "|     o     |")
        print( "|           |")
        print( "|     o     |")
        print( " -----------")
    elif a == 4:
        print(" -----------")
        print( "|           |")
        print( "|  o     o  |")
        print( "|           |")
        print( "|  o     o  |")
        print( "|           |")
        print( " -----------")
    elif a == 5:
        print(" -----------")
        print( "|           |")
        print( "|  o     o  |")
        print( "|     o     |")
        print( "|  o     o  |")
        print( "|           |")
        print( " -----------")
    elif a == 6:
        print(" -----------")
        print( "|  o     o  |")
        print( "|           |")
        print( "|  o     o  |")
        print( "|           |")
        print( "|  o     o  |")
        print( " -----------")
else:
    print("Okay!! next time")

   
