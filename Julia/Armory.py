# this is home for all the equiptment stats
#there was suppost to be so much more but I didnt get it added

#Ammo Types [Damage, ArmorPen]
A_10mm = [37, 6]
A_32Cal = [27, 3]
A_22lr = [25, 2]
A_4Ten = [40, 0]

#Wepons
Colt_6520 = {"Name": "Colt 6520", "DamType": "Ballistic","Damage": A_10mm[0] ,"ArmorPen": A_10mm[1], "MagSize" : 12, "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "10mm Ammo", "APCostWM1":3 }
MK4_Ruger = {"Name": "MK4 Ruger", "DamType": "Ballistic","Damage": A_22lr[0] ,"ArmorPen": A_22lr[1], "MagSize" : 24, "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "22lr Ammo", "APCostWM1":3 }
SaW_MaP = {"Name": "S&W M&P", "DamType": "Ballistic","Damage": A_32Cal[0] ,"ArmorPen": A_32Cal[1], "MagSize" : 7, "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "32 Cal Ammo",  "APCostWM1":3 }
PQ_PPSH ={"Name": "Poor Quality PPSH", "DamType": "Ballistic","Damage": A_32Cal[0] ,"ArmorPen": A_32Cal[1], "MagSize" : 20, "WeaponMode1": 2, "WeaponMode2": "None", "Ammo": "32Cal Ammo", "APCostWM1":5 }
Single_Shotgun = {"Name": "Single Shotgun", "DamType": "Ballistic","Damage": A_4Ten[0] ,"ArmorPen": A_4Ten[1], "MagSize" : 1, "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "4-10 Shells", "APCostWM1":3}
Varmit_Rifle ={"Name": "Varmit Rifle", "DamType": "Ballistic","Damage": A_22lr[0] ,"ArmorPen": A_22lr[1], "MagSize" : 10, "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "22lr Ammo", "APCostWM1":5}
Hunting_Rifle = {"Name": "Hunting Rifle", "DamType": "Ballistic","Damage": A_32Cal[0] ,"ArmorPen": A_32Cal[1], "MagSize" : 5, "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "32 Cal Ammo","APCostWM1":5}
Lawbringer_Special ={"Name": "Lawbringer Special", "DamType": "Ballistic","Damage": A_32Cal[0] ,"ArmorPen": A_32Cal[1], "MagSize" : 6, "WeaponMode1": 3, "WeaponMode2": "None", "Ammo": "32 Cal Ammo", "APCostWM1":5}
Recharger_Pistol = {"Name": "Recharger Pistol", "DamType": "Energy","Damage": 20 ,"ArmorPen": 1, "MagSize" : "Infinite", "WeaponMode1": 1, "WeaponMode2": "None", "Ammo": "None", "AmmoCount":0, "APCostWM1":2}

#old ides that got cut
#WeaponDic = {"10mm":Colt_6520,"22lrp":MK4_Ruger,"32pi":SaW_MaP,"32SMG":PQ_PPSH,"4-10":Single_Shotgun,"22rif":Varmit_Rifle,"32rif":Hunting_Rifle,"32HMG":Lawbringer_Special,"REPit":Recharger_Pistol}

#Armor
Gecko_Reinforced_Leather_Armor = {"Name":"Gecko Reinforced Leather Armor","Ballistic":2,"Energy":0,"DR":.75}
Armored_Duster = {"Name":"Armored Duster","Ballistic":5,"Energy":0,"DR":.75}
T51 = {"Name":"T51","Ballistic":45,"Energy":55}
No_Armor = {"Name":"None","Ballistic":0,"Energy":0,"DR":0}

#ArmorDic = {"Gek":Gecko_Reinforced_Leather_Armor,"Duster":Armored_Duster,"T51":T51}

#Items
Stimpak = {"HP": 60, }#these are the character effects of these Items
Jet= {"MaxAP": 2,"AP":4 }
Bandage = {"HP": 20}
ItemEffects = {"Stimpak":Stimpak,"Jet":Jet}