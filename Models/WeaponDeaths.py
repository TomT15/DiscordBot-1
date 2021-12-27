class Weapons:
    def __init__(self, name, bornheim, caldwell_Conversion, caldwell_Pax, calvery_Saber, doltch, hand_Crossbow, leMatt, machete, nagant):
        #Small Weapon Slots
        self.name = name
        self.Bornheim = bornheim
        self.Caldwell_Conversion = caldwell_Conversion
        self.Caldwell_Pax = caldwell_Pax
        self.Calvery_Saber = calvery_Saber
        self.Doltch = doltch
        self.Hand_Crossbow = hand_Crossbow
        self.LeMatt = leMatt
        self.Machete = machete
        self.Nagant = nagant
        #TODO: finish this model stuff
        #Medium Weapon Slots
        self.Bornheim_Match
        self.Bow
        self.Caldwell_Rival_Handcannon
        self.Combat_Axe
        self.Doltch_Precision
        self.Mosin_Obrez
        self.Nagant_Deadeye
        self.Romero_Handcannon
        self.Specter_Compact
        self.Springfield_Compact
        self.Terminus_handcannon
        self.Vandal
        #large Weapon Slots
        self.Bomb_Lance
        self.Caldwell_Rival
        self.Crossbow
        self.Crown_and_King
        self.Lebel
        self.Martini
        self.Mosin
        self.Nagant_Officer_Carbine
        self.Nitro
        self.Romero
        self.Sparks
        self.Specter
        self.Springfield
        self.Vetterli
        self.Terminus
        self.Winfield
        self.Centennial

class WeaponCounter(Weapons):
    def _init_(self, name, bornheim, caldwell_Conversion, caldwell_Pax):        
        super().__init__(self, name)
        self.Bornheim = bornheim
        self.Caldwell_Conversion = caldwell_Conversion
        self.Caldwell_Pax = caldwell_Pax

