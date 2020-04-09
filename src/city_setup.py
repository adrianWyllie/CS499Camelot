from action import action

def city_setup():
    #Create City
    action('CreatePlace("City", City)')
    action('CreatePlace(Gallows, Ruins)')
    #Set Day
    action('SetDay()')
    
    #Create City Characters
    #Beggar Adeline
    action('CreateCharacter(Beggar Adeline, G)')
    action('SetClothing(Beggar Adeline, Beggar)')
    action('SetHairStyle(Beggar Adeline, Long)')
    action('SetPosition(Beggar Adeline, City.Fountain)')
    
    #Beggar Miles
    action('CreateCharacter(Beggar Miles, H)')
    action('SetClothing(Beggar Miles, Beggar)')
    action('SetHairStyle(Beggar Miles, Mage)')
    action('SetPosition(Beggar Miles, City.Bench)')
    action('Sit(Beggar Miles, City.Bench)')
    
    #Alchemist Jeremy
    action('CreateCharacter(Alchemist Jeremy, F)')
    action('SetClothing(Alchemist Jeremy, Merchant)')
    action('SetHairStyle(Alchemist Jeremy, Spiky)')
    action('SetPosition(Alchemist Jeremy, City.BrownHouseDoor)')
    action('WalkToSpot(Alchemist Jeremy, 925.3, 0.3, 5.0)')
    
    #Scout Joanna
    action('CreateCharacter(Scout Joanna, C)')
    action('SetClothing(Scout Joanna, LightArmour)')
    action('SetHairStyle(Scout Joanna, Ponytail)')
    action('SetPosition(Scout Joanna, City.NorthEnd)')
    action('CreateItem(JoannaTorch, Torch)')
    action('SetPosition(JoannaTorch, Scout Joanna)')
    
    #Scout Tom
    action('CreateCharacter(Scout Tom, D)')
    action('SetClothing(Scout Tom, LightArmour)')
    action('SetHairStyle(Scout Tom, Short)')
    action('SetPosition(Scout Tom, City.WestEnd)')
    action('CreateItem(TomTorch, Torch)')
    action('SetPosition(TomTorch, Scout Joanna)')
    action('WalkToSpot(Scout Tom, 916.0, 0.3, -12.6)')
    
    #Drunk Devon
    action('CreateCharacter(Drunk Devon, F)')
    action('SetClothing(Drunk Devon, Peasant)')
    action('SetHairStyle(Drunk Devon, Musketeer)')
    action('SetPosition(Drunk Devon, City.GreenHouseDoor)')
    action('CreateItem(DevonsBottle, Bottle)')
    action('SetPosition(DevonsBottle, Drunk Devon)')
    action('WalkToSpot(Drunk Devon, 906.4, 0.3, -1.2)')
    
    #Priestess Esmerelda
    action('CreateCharacter(Priestess Esmerelda, E)')
    action('SetClothing(Priestess Esmerelda, Priest)')
    action('SetHairStyle(Priestess Esmerelda, Short)')
    action('SetPosition(Priestess Esmerelda, City.RedHouseDoor)')
    action('CreateItem(EsmereldaBook, RedBook)')
    action('SetPosition(EsmereldaBook, Priestess Esmerelda)')
    
    #Blind Bandit
    action('CreateCharacter(Blind Bandit, C)')
    action('SetClothing(Blind Bandit, Bandit)')
    action('SetHairStyle(Blind Bandit, Long)')
    action('SetPosition(Blind Bandit, City.Alley)')
    
    #Gossiping Gail
    action('CreateCharacter(Gossiping Gail, A)')
    action('SetClothing(Gossiping Gail, Peasant)')
    action('SetHairStyle(Gossiping Gail, Spiky)')
    action('SetPosition(Gossiping Gail, City.BlueHouseDoor)')
    
    #Enable Icons
    action('EnableIcon(Talk, Talk, Beggar Adeline, Talk to Beggar Adeline, true)')
    action('EnableIcon(Talk, Talk, Beggar Miles, Talk to Beggar Miles, true)')
    action('EnableIcon(Talk, Talk, Alchemist Jeremy, Talk to Alchemist Jeremy, true)')
    action('EnableIcon(Talk, Talk, Scout Joanna, Talk to Scout Joanna, true)')
    action('EnableIcon(Talk, Talk, Scout Tom, Talk to Scout Tom, true)')
    action('EnableIcon(Talk, Talk, Drunk Devon, Talk to Drunk Devon, true)')
    action('EnableIcon(Talk, Talk, Blind Bandit, Talk to Blind Bandit, true)')
    action('EnableIcon(Talk, Talk, Priestess Esmerelda, Talk to Priestess Esmerelda, true)')
    action('EnableIcon(Talk, Talk, Gossiping Gail, Talk to Gossiping Gail, true)')
    action('EnableIcon(Enter, Exit, City.BrownHouseDoor, Enter the Alchemist Shop, true)')
    action('EnableIcon(Enter, Exit , City.GreenHouseDoor, Enter the Tavern, true)')
    
