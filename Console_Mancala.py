print("****************************************")
print("      WELCOME TO MANCALA GAME")
print("****************************************")

"""
Rules

you must start dropping one by one ---> clockwise

if last stone drops into its own treasure --> it can play one more round

if last stone drops into enemy side --> check if that container has odd or even amount of stones --> if even you can play one more round

Last stone most important

if your last stone made enemy container even number of stones --> you can pick all of them to your treasure

main purpose --> you must play until game finishes and collect most treasure

if your last stone drops into empty container (your side) --> you can take exact opposite containers stones to your treasure
"""
#---------------------------- Global Variables ----------------------------
game_running = True
mancala_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

#indicating which players turn it is
playerOne = True

message_code = 0

#init
distributed_stones = -1
last_receiver = -1
selected_pit = -1
#--------------------------------------------------------------------------

while(game_running):

    #---------------------------- Error Handling ----------------------------
    #specifying which player is on
    if playerOne and message_code == 0:
        message = "Player One's turn..."
    elif not(playerOne) == 0 and message_code == 0:
        message = "Player Two's turn..."
    elif playerOne and message_code == -2:
        message = "Invalid input. Try again Player 1."
    elif not(playerOne) and message_code == -2:
        message = "Invalid input. Try again Player 2."
    elif playerOne and message_code == -1:
        message = "You must chose a non-empty pit, Player 1"
    elif not(playerOne) and message_code == -1:
        message = "You must chose a non-empty pit, Player 2"
    
    print("")
    print(message)
    print("")
    message_code = 0 # default value
    #------------------------------------------------------------------------
    
    #for adjusting inside of the grid
    i = 0
    for elements in mancala_board:
        #if there are any extra spaces in that value they get removed
        mancala_board[i] = int(mancala_board[i])
        if(int(mancala_board[i] < 10)):
            mancala_board[i] = " " + str(mancala_board[i])
        else:
            mancala_board[i] = str(mancala_board[i])
        i += 1
    
    #-------------- board --------------
    
    print("")
    #pit mapping
    if(not(playerOne)):
        print("        a    b    c    d    e    f")
    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ mancala_board[12] +" | "+ mancala_board[11] +" | "+ mancala_board[10] 
          +" | "+ mancala_board[9] +" | "+ mancala_board[8] +" | "+ mancala_board[7] +" |    |")
    print("| "+ mancala_board[13] +" |----+----+----+----+----+----| "+ mancala_board[6] +" |")
    print("|    | "+ mancala_board[0] +" | "+ mancala_board[1] +" | "+ mancala_board[2] 
          +" | "+ mancala_board[3] +" | "+ mancala_board[4] +" | "+ mancala_board[5] +" |    |")
    print("+----+----+----+----+----+----+----+----+")
    
    #pit mapping
    if(playerOne):
        print("        f    e    d    c    b    a")
    print("")
    
    
    # terminal condition
    user_input = input("Enter a letter to choose a pit or enter 'q' to QUIT the game: ")
    
    if user_input == "q":
        game_running = False
        selected_pit = 0    #init
    elif(playerOne and user_input == "a"):  # selecting a specific pit for player 1
        selected_pit = 5
    elif(playerOne and user_input == "b"):
        selected_pit = 4
    elif(playerOne and user_input == "c"):
        selected_pit = 3
    elif(playerOne and user_input == "d"):
        selected_pit = 2
    elif(playerOne and user_input == "e"):
        selected_pit = 1
    elif(playerOne and user_input == "f"):
        selected_pit = 0
    elif(not(playerOne) and user_input == "a"): # p2
        selected_pit = 12
    elif(not(playerOne) and user_input == "b"):
        selected_pit = 11
    elif(not(playerOne) and user_input == "c"):
        selected_pit = 10
    elif(not(playerOne) and user_input == "d"):
        selected_pit = 9
    elif(not(playerOne) and user_input == "e"):
        selected_pit = 8
    elif(not(playerOne) and user_input == "f"):
        selected_pit = 7
    else:
        selected_pit = -2
        message_code = -2   # invalid input
    
    if int(selected_pit) >= 0:
        distributed_stones = mancala_board[selected_pit]
        # we picked stones
        mancala_board[selected_pit] = 0
        if int(distributed_stones) <= 0:
            message_code = -1 # empty pit is chosen
    
    # moving 1 step clockwise
    receiver_pit = selected_pit + 1
    while(int(distributed_stones) > 0):
        if(playerOne and int(receiver_pit) == 13):
            receiver_pit = 0
        if(not(playerOne) and int(receiver_pit) == 6):
            receiver_pit = 7
        
        # add 1 stone clockwise 
        mancala_board[receiver_pit] = int(mancala_board[receiver_pit]) + 1
        # decrease distributed stone amount
        distributed_stones = int(distributed_stones) - 1

        if(int(distributed_stones) == 0):
            last_receiver = receiver_pit
        else:
            receiver_pit = int(receiver_pit) + 1
            #avoiding adding score to enemy pit
            if(int(receiver_pit) > 13):
                receiver_pit = 0
                
    # own treasure ending rule
    if(playerOne and int(last_receiver) == 6):
        playerOne = True
    # if last stone drops into empty pit rule for p1
    elif(playerOne and int(mancala_board[last_receiver]) == 1 and int(last_receiver) < 6):
        mancala_board[6] = int(mancala_board[6]) + int(mancala_board[last_receiver]) + int(mancala_board[12 - int(last_receiver)])
        mancala_board[last_receiver] = 0
        mancala_board[12 - int(last_receiver)] = 0
        playerOne = not(playerOne)  
    elif (not(playerOne) and int(last_receiver) == 13):
        playerOne = False 
    # if last stone drops into empty pit rule for p2
    elif(not(playerOne) and int(mancala_board[last_receiver]) == 1 and int(last_receiver) > 6):
        mancala_board[13] = int(mancala_board[13]) + int(mancala_board[last_receiver]) + int(mancala_board[12 - int(last_receiver)])
        mancala_board[last_receiver] = 0
        mancala_board[12 - int(last_receiver)] = 0
        playerOne = not(playerOne)
    elif(int(message_code) >= 0):
        # switching between players    
        playerOne = not(playerOne)
        
    #checking for the end of the game
    side_one = 0
    side_two = 0
    for j in range(6):  #for player 1's side of the board
        side_one = int(side_one) + int(mancala_board[j])
        side_two = int(side_two) + int(mancala_board[j + 7])
        
    if(int(side_one) == 0 or int(side_two) == 0):
        game_running = False    # end of the game
        mancala_board[6] = int(mancala_board[6]) + int(side_one)
        mancala_board[13] = int(mancala_board[13]) + int(side_one)
        #clearing board
        for k in range(6):
            mancala_board[k] = 0
            mancala_board[k + 7] = 0

# game ending sequence: d - a - a - e - a - d - f - c - f - a - b - f - a
print("")
print("THE GAME IS OVER!")

if int(mancala_board[13]) < int(mancala_board[6]):
    print("Player 1 WON!")
elif int(mancala_board[13]) > int(mancala_board[6]):
    print("Player 2 WON!")
else:
    print("The game ended in a TIE")

#Printing board for the last time
i = 0
for elements in mancala_board:
    #if there are any extra spaces in that value they get removed
    mancala_board[i] = int(mancala_board[i])
    if(int(mancala_board[i] < 10)):
        mancala_board[i] = " " + str(mancala_board[i])
    else:
        mancala_board[i] = str(mancala_board[i])
    i += 1
    
#-------------- board --------------
print("")
print("+----+----+----+----+----+----+----+----+")
print("|    | "+ mancala_board[12] +" | "+ mancala_board[11] +" | "+ mancala_board[10] 
        +" | "+ mancala_board[9] +" | "+ mancala_board[8] +" | "+ mancala_board[7] +" |    |")
print("| "+ mancala_board[13] +" |----+----+----+----+----+----| "+ mancala_board[6] +" |")
print("|    | "+ mancala_board[0] +" | "+ mancala_board[1] +" | "+ mancala_board[2] 
        +" | "+ mancala_board[3] +" | "+ mancala_board[4] +" | "+ mancala_board[5] +" |    |")
print("+----+----+----+----+----+----+----+----+")
print("")