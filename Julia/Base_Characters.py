#Starting equiptment Characters
import Armory as Ar

# this is just a place to house the Charcters for character selection

SniperBS = {"HP":120,"AP":8, "EqutWepSkil":4, "Number": 0, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
SniperEQ = {"Weapon": Ar.Hunting_Rifle,"Ammo in Gun" :5, "Armor": Ar.No_Armor, "Armor Durability": 100}
SniperINV = {"32Cal Ammo": 15, "Bandage" : 1}
BaseSniper = {"BS": SniperBS ,"EQ": SniperEQ,"INV":SniperINV}

PistolireBS = {"HP":120,"AP":8, "EqutWepSkil":7, "Number": 1, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
PistolireEQ = {"Weapon": Ar.MK4_Ruger,"Ammo in Gun" :24, "Armor": Ar.Gecko_Reinforced_Leather_Armor, "Armor Durability": 100}
PistolireINV = {"22lr Ammo": 24, "Bandage" : 1, "Stimpak" :1}
BasePistolire =  {"BS": PistolireBS ,"EQ": PistolireEQ,"INV": PistolireINV}

CowboyBS = {"HP":120,"AP":8, "EqutWepSkil":6, "Number": 0, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
CowboyEQ = {"Weapon": Ar.SaW_MaP,"Ammo in Gun" :7, "Armor": Ar.Armored_Duster, "Armor Durability": 100}
CowboyINV = {"32Cal Ammo": 14, "Bandage" : 1}
BaseCowboy = {"BS": CowboyBS ,"EQ": CowboyEQ,"INV":CowboyINV}

GruntBS = {"HP":120,"AP":8, "EqutWepSkil":7, "Number": 0, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
GruntEQ = {"Weapon": Ar.PQ_PPSH,"Ammo in Gun" :20, "Armor": Ar.No_Armor, "Armor Durability": 100}
GruntINV = {"32Cal Ammo": 10, "Bandage" : 1}
BaseGrunt = {"BS": GruntBS ,"EQ": GruntEQ,"INV": GruntINV}

HeavyBS = {"HP":120,"AP":8, "EqutWepSkil":7, "Number": 0, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
HeavyEQ = {"Weapon": Ar.Lawbringer_Special,"Ammo in Gun" :6, "Armor": Ar.No_Armor, "Armor Durability": 100}
HeavyINV = {"32Cal Ammo": 6,}
BaseHeavy = {"BS": HeavyBS ,"EQ": HeavyEQ,"INV": HeavyINV}

NerdBS = {"HP":120,"AP":8, "EqutWepSkil":8, "Number": 0, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
NerdEQ = {"Weapon": Ar.Recharger_Pistol,"Ammo in Gun" :"Infinite", "Armor": Ar.No_Armor, "Armor Durability": 100}
NerdINV = {"Bandage" : 1, "Jet":1}
BaseNerd = {"BS": NerdBS ,"EQ": NerdEQ,"INV": NerdINV}

TesterBS = {"HP":120,"AP":8, "EqutWepSkil":11, "Number": 1, "MaxHP" : 120, "MaxAP" : 8, "MovementModifier": 0}
TesterEQ = {"Weapon": Ar.Colt_6520,"Ammo in Gun" :12, "Armor": Ar.Gecko_Reinforced_Leather_Armor, "Armor Durability": 100}
TesterINV = {"10mm Ammo": 35, "Stimpak" : 1, "Jet" :1}
Tester = {"BS": TesterBS ,"EQ": TesterEQ,"INV": TesterINV}

AvailableCharacters = {"Sniper":BaseSniper,"Pistolire":BasePistolire, "Cowboy": BaseCowboy, "Grunt": BaseGrunt,"Heavy":BaseHeavy,"Nerd":BaseNerd}
def CharacterSlection (AvailableCharacters):# this is hoow characters are selected
    for keys in AvailableCharacters:
        print(keys)

    Player1 = input("Please enter character title from list for Player 1: ")
    Player2 = input("Please enter character title from list for Player 2: ")
    Player1 = AvailableCharacters[Player1]
    Player2 = AvailableCharacters[Player2]
    return Player1,Player2
