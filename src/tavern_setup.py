from action import action

def tavern_setup():
    
    # Witch Carlita
    action('SetPosition(Witch Carlita, Tavern.BackDoor)')
    action('SetExpression(Witch Carlita, neutral')
    
    # Noble Jeremy
    action('SetPosition(Noble Jeremy, Tavern)')
    action('WalkToSpot(Noble Jeremy, 1802.9, 0.1, -1.9)')
    action('Face(Noble Jeremy, Tavern.Table)')
    #action('Sit(Noble Jeremy, Tavern.StoolFrontRight)')
    action('SetExpression(Merchant Bert, afraid)')
    
    # Noble Cecilia
    action('SetPosition(Noble Cecilia, Tavern)')
    action('WalkToSpot(Noble Cecilia, 1803.6, 0.1, -5.8)')
    action('Face(Noble Cecilia, Tavern.Table)')
    #action('Sit(Noble Cecilia, Tavern.StoolFrontLeft)')
    action('SetExpression(Merchant Bert, afraid)')
    
    # Merchant Bert
    action('SetPosition(Merchant Bert, Tavern)')
    action('WalkToSpot(Merchant Bert, 1800.0, 0.1, -2.0)')
    action('Face(Merchant Bert, Tavern.Table)')
    action('SetExpression(Merchant Bert, afraid)')
    #action('Sit(Merchant Bert, Tavern.StoolBackLeft)')
    
    # Chamber Maid Scarlet
    action('SetPosition(Chamber Maid Scarlet, Tavern.Fireplace)')
    action('Face(Chamber Maid Scarlet, Tavern.Fireplace)')
    action('SetExpression(Chamber Maid Scarlet, afraid)')
    
    # Castle Grand Maester Purcell
    action('SetPosition(Maester Purcell, Tavern.Table)')
    action('Face(Maester Purcell, Tavern.Table)')
    action('SetExpression(Maester Purcell, neutral)')
    
    # Queen's Sister
    action('SetPosition(Tiana, Tavern.Bar)')
    action('Face(Tiana, Tavern.Fireplace)')
    action('SetExpression(Tiana, sad)')
    
    # Enable Icons
    #action('EnableIcon(Sit, Chair, Tavern.StoolBackRight, Sit, true)')
    action('EnableIcon(Enter, Exit , Tavern.Door, Leave the Tavern, true)')
    action('EnableIcon(Talk, Talk , Witch Carlita, Talk to Witch Carlita, true)')
    
    # Enable Effects
    action('EnableEffect(Tavern.Fireplace, Campfire)')
    action('PlaySound(Tavern, Tavern, true)')
    
    # Branching Path Alternative
    #if (not global_game_states.change_clothing):
        #action(SetExpression(Chamber Maid Scarlet, a))
