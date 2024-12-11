#import
import Turn_Code as TC
import Base_Characters as BC

#Characters selection and start up varibles
print("Welcome to this combat game, available classes are:")
print("Please make sure to type Names directly as displayed")
CharacterDic = BC.AvailableCharacters
Player1,Player2 = BC.CharacterSlection(CharacterDic)

Player1["BS"]["Number"] = 1#set up correct player #
Player2["BS"]["Number"] = 2




Player1Location = [0,4]# Strating Location codes
Player2Location = [9,4]
#PlayerList=[]

#inital startup varibals 
End = 1
PlayerTurn = {"Player":1, "Turn":1,}#turn counter and Player section
Locations = {"P1":Player1Location,"P2": Player2Location}# for Startup Map Generation
Player1['Location'] = Player1Location#Adding location lists to overall player dictionary
Player2['Location'] = Player2Location
ActivePlayer = Player1# inisliation
NonActivePlayer = Player2
print(".....................................................................")

TC.MapGen(Locations)#Starting Map

while End == 1:
#will add while loop
    print(".....................................................................")

    if ActivePlayer["BS"]["AP"] <= 0:  # end of Player turn chech
        PlayerTurn["Player"] = NonActivePlayer["BS"]["Number"]
        Player1, Player2 = TC.UnpackPlayer(ActivePlayer, NonActivePlayer)
        if NonActivePlayer["BS"]["Number"] == 1:  # this is for when the overall turn ends to refill the players AP
            PlayerTurn["Turn"] = PlayerTurn["Turn"] + 1
            Player1["BS"]["AP"] = Player1["BS"]["MaxAP"]
            Player2["BS"]["AP"] = Player2["BS"]["MaxAP"]

    if PlayerTurn["Player"] == 1 :# Makes Player 1 the active player
        print(f"Player 1 Turn {PlayerTurn["Turn"]}, Ap remaining:{Player1["BS"]["AP"]}, HP remaining: {Player1["BS"]["HP"]}, Ammo remaining:{Player1["EQ"]["Ammo in Gun"]}")
        ActivePlayer = Player1
        NonActivePlayer = Player2
        #

    elif PlayerTurn["Player"] == 2:# Makes Player 2 the active player
        print(f"Player 2 Turn {PlayerTurn["Turn"]}, Ap remaining:{Player2["BS"]["AP"]}, HP remaining: {Player2["BS"]["HP"]}, Ammo remaining:{Player2["EQ"]["Ammo in Gun"]}")
        ActivePlayer = Player2
        NonActivePlayer = Player1

        #Active player and nonActive player are use as a way to modif the players without having
        #to write seprate code for each of them

    if Player1["BS"]["HP"]<=0:# End Game Check
        print("Player2 Has Won!")
        break
    if Player2["BS"]["HP"] <= 0:
        print("Player1 Has Won!")
        break


    print(".....................................................................")# Prints
    print("1. Attack")
    print("2. Move")
    print("3. Reload")
    print("4. Open Inventory")
    print("5. View Character Stats")# this could be better but
    print("6. Show Map")
    print("7. End Player Turn")
    print("8. Surrender")
    choice = int(input("Enter your choice: "))
    if PlayerTurn["Turn"] == 1:# this is a balance featur to alow the characters to move befor combat starts to make them harder to hit
        if choice == 1:
            print('Invalid choice, you cannot attack on turn #1.')
            continue

    if choice == 1:#Attack
        if ActivePlayer["BS"]["AP"] >= ActivePlayer["EQ"]["Weapon"]["APCostWM1"]:
            ActivePlayer, NonActivePlayer = TC.Attack(ActivePlayer,NonActivePlayer)
        else:
            print("No enough Ap")
            continue

    elif choice == 2:
        ActivePlayer, NonActivePlayer = TC.Move(ActivePlayer, NonActivePlayer)

    elif choice == 3:
        ActivePlayer = TC.Reload(ActivePlayer)
    elif choice == 4:
        TC.OpenInventory(ActivePlayer)

    elif choice == 5:
            TC.ViewCharacterStats(ActivePlayer)

    elif choice == 6:
        TC.TurnMoveMap(ActivePlayer, NonActivePlayer)

    elif choice == 7:
        EndPlayerTurn = TC.EndTurn(PlayerTurn)
        Player1,Player2 = TC.UnpackPlayer(ActivePlayer,NonActivePlayer)
        PlayerTurn = EndPlayerTurn
        if NonActivePlayer["BS"]["Number"] == 1:# to refill AP even if player 2 Ends turn
            PlayerTurn["Turn"] = PlayerTurn["Turn"] + 1
            Player1["BS"]["AP"] =  Player1["BS"]["MaxAP"]
            Player2["BS"]["AP"] =  Player2["BS"]["MaxAP"]

    elif choice == 8:
        CEnd = TC.EndGame()
        print(f"Player{NonActivePlayer["BS"]["Number"]} Has Won!")
        End = CEnd




