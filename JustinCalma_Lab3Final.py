#How many ticks to turn
lock_Open = True
have_Combo = False
while lock_Open == True:

    if have_Combo == False:
        #Get the 3 numbers of the combination
        num_1 = int(input("What is the first number in the combination? "))
        num_2 = int(input("What is the second number in the combination? "))
        num_3 = int(input("What is the third number in the combination? "))

    #Determining how much to move
    ticks_1 = int(input("Turn the lock clockwise by how much? "))
    ticks_1 = 40 - ticks_1
    if ticks_1 == 40:
        ticks_1 = 0
    print(ticks_1)
    
    ticks_2 = int(input("Turn the lock counterclockwise by how much? "))
    ticks_2 = ticks_1 + ticks_2
    if ticks_2 > 40:
        ticks_2 -= 40
    if ticks_2 == 40:
        ticks_2 = 0
    print(ticks_2)

    ticks_3 = int(input("Turn the lock clockwise by how much? "))
    ticks_3 = abs(ticks_2 - ticks_3)
    
    if ticks_3 > 2:
        ticks_3 = abs(ticks_3 - 40)
    print(ticks_3)
    if ticks_3 == 40:
        ticks_3 = 0
    

    #Determine if lock opens or does not
    if (num_1 == ticks_1) and (num_2 == ticks_2) and (num_3 == ticks_3):
       print("Correct! You have earned an A in CECS 174.")
       lock_Open = False

    else:
        print("Sorry, that sequence was incorrect :( .")
        have_Combo = True

#The number of possible combinations is 64,000.
#It would take around 53 hours to try to solve every possible combination.
#The tamper-resistant lock would take longer on average to solve by trying
#random combinations
