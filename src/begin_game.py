from action import action

#Setup beginning of the game
def begin_game_setup():
    #Create Queens Castle
    action('CreatePlace(QueensCastle, DiningRoom)')
    
    #Set at Night
    action('SetNight()')
    #Create Characters
    #Main Character(John)
    action('CreateCharacter(John, B)')
    action('SetClothing(John, Noble)')
    action('SetHairStyle(John, Long)')
    action('SetPosition(John, QueensCastle.BackRightChair)')
    #action('Sit(John, QueensCastle.BackRightChair)')
    #Queen Margerie
    action('CreateCharacter(Queen Margerie, A)')
    action('SetClothing(Queen Margerie, Queen)')
    action('SetHairStyle(Queen Margerie, Long)')
    action('SetPosition(Queen Margerie, QueensCastle.RightChair)')
    action('Sit(Queen Margerie, QueensCastle.RightChair)')
    #Guard Gallant
    action('CreateCharacter(Guard Gallant, F)')
    action('SetClothing(Guard Gallant, HeavyArmour)')
    action('SetPosition(Guard Gallant, QueensCastle.Door)')
    action('CreateItem(GallantSword, Sword)')
    action('SetPosition(GallantSword, Guard Gallant)')
    #King Phillip
    action('CreateCharacter(King Phillip, H)')
    action('SetClothing(King Phillip, King)')
    action('SetPosition(King Phillip, QueensCastle.LeftChair)')
    action('Sit(King Phillip, QueensCastle.LeftChair)')
    action('SetHairStyle(King Phillip, Short_Full)')
    #Witch Carlita
    action('CreateCharacter(Witch Carlita, C)')
    action('SetClothing(Witch Carlita, Witch)')
    action('SetPosition(Witch Carlita, QueensCastle.LeftWindow)')
    action('SetHairStyle(Witch Carlita, Long)')
    action('SetHairColor(Witch Carlita, Gray)')
    action('Face(Witch Carlita, QueensCastle.BackRightChair)')
    action('CreateItem(CarlitaBook, BlueBook)')
    action('SetPosition(CarlitaBook, Witch Carlita)')
    #Noble Jeremy
    action('CreateCharacter(Noble Jeremy, F)')
    action('SetClothing(Noble Jeremy, Noble)')
    action('SetPosition(Noble Jeremy, QueensCastle.LeftWindow)')
    action('Sit(Noble Jeremy, QueensCastle.FrontRightChair)')
    action('SetHairStyle(Noble Jeremy, Spiky)')
    #Noble Cecilia
    action('CreateCharacter(Noble Cecilia, C)')
    action('SetClothing(Noble Cecilia, Noble)')
    action('SetPosition(Noble Cecilia, QueensCastle.LeftWindow)')
    action('SetHairStyle(Noble Cecilia, Short)')
    action('Sit(Noble Cecilia, QueensCastle.FrontLeftChair)')
    #Merchant Bert
    action('CreateCharacter(Merchant Bert, H)')
    action('SetClothing(Merchant Bert, Merchant)')
    action('SetPosition(Merchant Bert, QueensCastle.LeftWindow)')
    action('SetHairColor(Merchant Bert, Blonde)')
    action('Sit(Merchant Bert, QueensCastle.BackLeftChair)')
    #Chamber Maid Scarlet
    action('CreateCharacter(Chamber Maid Scarlet, E)')
    action('SetClothing(Chamber Maid Scarlet, Peasant)')
    action('SetPosition(Chamber Maid Scarlet, QueensCastle.BackDoor)')
    action('SetHairStyle(Chamber Maid Scarlet, Ponytail)')
    action('SetHairColor(Chamber Maid Scarlet, Brown)')
    action('Face(Chamber Maid Scarlet, QueensCastle.DiningTable)')
    #Create Items and position them
    action('CreateItem(QueensCup, GoldCup)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)')
    action('CreateItem(JohnsCup, GoldCup)')
    action('SetPosition(JohnsCup, QueensCastle.DiningTable.BackRight)')
    action('CreateItem(BertsCup, GoldCup)')
    action('SetPosition(BertsCup, QueensCastle.DiningTable.BackLeft)')
    action('CreateItem(JeremysCup, GoldCup)')
    action('SetPosition(JeremysCup, QueensCastle.DiningTable.FrontRight)')
    action('CreateItem(KingsCup, GoldCup)')
    action('SetPosition(KingsCup, QueensCastle.DiningTable.Left)')
    action('CreateItem(CeciliasCup, GoldCup)')
    action('SetPosition(CeciliasCup, QueensCastle.DiningTable.FrontLeft)')
    action('CreateItem(PythonBox, BlueBook)')
    action('SetPosition(PythonBox, QueensCastle.Table)')
    action('CreateItem(GuestLedger, GreenBook)')
    action('SetPosition(GuestLedger, QueensCastle.Shelf)')
    
    #Enable Icons
    action('EnableIcon(Sit, Chair, QueensCastle.BackRightChair, Sit, true)')
    action('EnableIcon(Python, Drink, PythonBox, Command Camelot, true)')
    action('EnableIcon(Talk, Talk, Queen Margerie, Talk to the Queen, true)')
    action('EnableIcon(ReadLedger, Research, GuestLedger, Read, true)')

    # #EnableEffects
    action('EnableEffect(QueensCastle.Fireplace, Campfire)')

    
    action('ShowMenu()')