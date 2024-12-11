from pickle import FLOAT

import numpy as nd

import Armory as AR

def MapGen(LocationDic): #start up map print
    MapSize = 10
    for row in range(MapSize):
        for col in range(MapSize):
            if [row,col] == LocationDic["P1"]:
                print("[P1]", end=" ")
            elif [row,col] == LocationDic["P2"]:
                print("[P2]",end=" ")
            else:
                print("[  ]", end=" ")
        print()
    print()

def TurnMoveMap(ActivePlayer,NonActivePlayer):# for printing the map when moving
    MapSize = 10
    for row in range(MapSize):
        for col in range(MapSize):
            if [row,col] == ActivePlayer["Location"]:
                if ActivePlayer["BS"]["Number"]== 1:
                   print("[P1]", end=" ")
                elif ActivePlayer["BS"]["Number"]== 2:
                   print("[P2]", end=" ")
            elif [row,col] == NonActivePlayer["Location"]:
                if NonActivePlayer["BS"]["Number"] == 1:
                    print("[P1]", end=" ")
                elif NonActivePlayer["BS"]["Number"] == 2:
                    print("[P2]", end=" ")
            else:
                print("[  ]", end=" ")
        print()
    print()

def Reload (ActivePlayer) : #WIP
    Ammotype = ActivePlayer["EQ"]["Weapon"]["Ammo"]
    if Ammotype == "None":# needed for recharger Pistol
        print("This weapon cannot be reloaded")
        return ActivePlayer
    AmmoUsed = ActivePlayer["EQ"]["Ammo in Gun"]
    MagSize = ActivePlayer["EQ"]["Weapon"]["MagSize"]
    AvailibleAmmo = ActivePlayer["INV"][Ammotype]#
    Check = input(f"You have {AmmoUsed} bullets available out of {MagSize}, would you still like to reload(Y/N): ").upper()
    if Check == "Y":
        if AvailibleAmmo>=AmmoUsed-MagSize:
            if AmmoUsed < MagSize:
                ActivePlayer["EQ"]["Ammo in Gun"] = MagSize
                ActivePlayer["INV"][Ammotype] = ActivePlayer["INV"][Ammotype] - (MagSize - AmmoUsed)
                ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"]-2
                return ActivePlayer
            else:
                print("Mag is already full")
                return ActivePlayer
        elif AvailibleAmmo> 0:
            ActivePlayer["EQ"]["Ammo in Gun"] = AmmoUsed+AvailibleAmmo
            print("Not enough ammo available to reload completely, mag as filled with available ammo")
            return ActivePlayer
        else:
            print("No ammo available to reload")
            return ActivePlayer

# input #1 Attack
def Attack(ActivePlayer,NonActivePlayer) :
    WM = input("Please select your weapons mode (1,2): ")# This is a feture that is for weapons that didn't get impllmented
    DamageType = ActivePlayer["EQ"]["Weapon"]["DamType"]
    if ActivePlayer["EQ"]["Weapon"][f"WeaponMode{WM}"] == "None" :
        print("Invalid mode, please select another")
        return ActivePlayer,NonActivePlayer
    else:
        WMNumber = ActivePlayer["EQ"]["Weapon"][f"WeaponMode{WM}"]
        WMNumber = int(WMNumber)
    if ActivePlayer["EQ"]["Ammo in Gun"] == "Infinite":# for the recharger pistol
        ActivePlayer["EQ"]["Ammo in Gun"]=100
    #Target = input ("Please select target (P1,P2): ")
    ToHit= ActivePlayer["BS"]["EqutWepSkil"]-NonActivePlayer["BS"]["MovementModifier"]
    ToHitPer = ((1-ToHit/20)*100)
    FireCheck = input(f"Your CTH is {ToHitPer}% would you still like to fire(Y,N): ").upper()
    if FireCheck == "Y":
        if ActivePlayer["EQ"]["Ammo in Gun"]>=WMNumber:
            ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"]-ActivePlayer["EQ"]["Weapon"][f"APCostWM{WM}"]
            AmmoUsed = WMNumber
            ActivePlayer["EQ"]["Ammo in Gun"] = ActivePlayer["EQ"]["Ammo in Gun"] - AmmoUsed
            Chance = nd.random.randint(0,21)
            if WMNumber > 1 :
                NumberHit = nd.random.randint(1,(WMNumber+1))
            else:
                NumberHit = WMNumber
            if Chance >= ToHit:
                if ActivePlayer["EQ"]["Weapon"]["ArmorPen"] > NonActivePlayer["EQ"]["Armor"][DamageType]:
                    NonActivePlayer["BS"]["HP"] = NonActivePlayer["BS"]["HP"] - ActivePlayer["EQ"]["Weapon"]["Damage"] * NumberHit
                    NonActivePlayer["EQ"]["Armor"][DamageType] = NonActivePlayer["EQ"]["Armor"][DamageType] - (NumberHit*5)
                    DamageDone = ActivePlayer["EQ"]["Weapon"]["Damage"] * NumberHit
                    print(f"{DamageDone} Points of damage was done to player {NonActivePlayer["BS"]["Number"]}")
                    if ActivePlayer["EQ"]["Ammo in Gun"] == 99:
                        ActivePlayer["EQ"]["Ammo in Gun"] = "Infinite"
                    return ActivePlayer,NonActivePlayer
                elif ActivePlayer["EQ"]["Weapon"]["ArmorPen"] < NonActivePlayer["EQ"]["Armor"][DamageType]:
                    NonActivePlayer["BS"]["HP"] = NonActivePlayer["BS"]["HP"] - ActivePlayer["EQ"]["Weapon"]["Damage"]*(1-NonActivePlayer["EQ"]["Armor"]["DR"])* NumberHit
                    NonActivePlayer["EQ"]["Armor"][DamageType] = NonActivePlayer["EQ"]["Armor"][DamageType]-NumberHit
                    DamageDone = ActivePlayer["EQ"]["Weapon"]["Damage"]*(1-NonActivePlayer["EQ"]["Armor"]["DR"])* NumberHit
                    print(f"{DamageDone} points of damage was done to player{NonActivePlayer["BS"]["Number"]}")
                    if ActivePlayer["EQ"]["Ammo in Gun"] == 99:
                        ActivePlayer["EQ"]["Ammo in Gun"] = "Infinite"
                    return ActivePlayer,NonActivePlayer
            else:
                print("You have missed")
                return ActivePlayer, NonActivePlayer
        else:
            print("You do not have enough ammo to make the requested shot")
            return ActivePlayer, NonActivePlayer

# input #2 Move
def Move(ActivePlayer,NonActivePlayer):
    MapSize = 10
    while ActivePlayer["BS"]["AP"]>0:
        Move = input("Please select direction or enter stop to end moving (N,E,S,W, stop): ").upper()
        if Move == "STOP":
            break
        HowFar = int(input("Please input distance: "))
        if Move == "N" and ActivePlayer["Location"][0]>= HowFar:
            ActivePlayer["Location"][0] -= HowFar
            TurnMoveMap(ActivePlayer,NonActivePlayer)
            ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"]-HowFar
        elif Move == "S" and ActivePlayer["Location"][0]< MapSize-HowFar:
            ActivePlayer["Location"][0] += HowFar
            TurnMoveMap(ActivePlayer,NonActivePlayer)
            ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"] - HowFar
        elif Move == "W" and ActivePlayer["Location"][1]< MapSize - HowFar:
            ActivePlayer["Location"][1] -= HowFar
            TurnMoveMap(ActivePlayer,NonActivePlayer)
            ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"] - HowFar
        elif Move == "E" and ActivePlayer["Location"][1]>= HowFar:
            ActivePlayer["Location"][1] += HowFar
            TurnMoveMap(ActivePlayer,NonActivePlayer)
            ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"] - HowFar
        else:
            print("Invalid move, please try again.")

    ActivePlayer["BS"]["MovementModifier"] = ActivePlayer["BS"]["MovementModifier"]+int(HowFar)
    return ActivePlayer,NonActivePlayer

# input #3 Open Inventory
def OpenInventory(ActivePlayer):
    for items in ActivePlayer["INV"].items():
     print(items)
    UseItem = input("Do you want to use an item (y/n): ").upper()
    if UseItem == "Y":
        ItemKey = input("please enter item name: ")
        for keys in ActivePlayer["INV"]:#this is to stop their from being errors if you type the key in wrong
            if keys == ItemKey:
                ActivePlayer["INV"][ItemKey] = ActivePlayer["INV"][ItemKey] - 1
                ActivePlayer["BS"]["AP"] = ActivePlayer["BS"]["AP"] - 2
                Effect = AR.ItemEffects[ItemKey]
                for keys in Effect:
                    ActivePlayer["BS"][keys] = ActivePlayer["BS"][keys] + Effect[keys]
                if ActivePlayer["BS"]["HP"] > ActivePlayer["BS"]["MaxHP"]:
                    ActivePlayer["BS"]["HP"] = ActivePlayer["BS"]["MaxHP"]
                return ActivePlayer
        print("Item not used, please enter the Item name directly as displayed")
        return ActivePlayer
    else:
        return ActivePlayer


# input #4 View Character Stats
def ViewCharacterStats(ActivePlayer):
    for items in ActivePlayer["BS"].items():
        if items[0] == "EqutWepSkil":
            print(f"Weapon Skill = {items[1]}")
        else:
            print(f"{items[0]} = {items[1]}")

# input #5 End Turn
def EndTurn(PlayerTurn):
    Check = input("Are you sure you want to end your turn? (y/n): ").upper()
    if Check == "Y":
        if PlayerTurn["Player"] == 1:
            PlayerTurn["Player"] = 2
        elif PlayerTurn["Player"] == 2:
            PlayerTurn["Player"] = 1
            PlayerTurn["Turn"] = PlayerTurn["Turn"] + 1

    return PlayerTurn
# Input #6 End Game
def EndGame():
    Check= input("Are you sure you want to surrender? (y/n): ").upper()
    if Check == "Y":
        End = bool(0)
        return End
#def EndGame
def UnpackPlayer (ActivePlayer,NonActivePlayer):# this is too re-asign the Active and Non player to their original Stats
    if ActivePlayer["BS"]["Number"] == 1:
        Player1 = ActivePlayer
        Player2 = NonActivePlayer
    elif ActivePlayer["BS"]["Number"] == 2:
        Player1 = NonActivePlayer
        Player2 = ActivePlayer
    return Player1,Player2
