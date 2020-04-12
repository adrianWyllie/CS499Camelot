'''
Author: Zachary Moore
Purpose: Handles playing of the ending cutscene
'''
# File imports 
from action import action
import global_game_states
from master_action_controller import check_master_actions, scene_start, display_clues_action, midscene_narration
from talk_controller import *
from end_cutscene_setup import end_cutscene_setup


# def present_evidence():
#     for clue in global_game_states.current_clues:
    
'''
Purpose: Creates a modular way to perform the execution of whomever was accused
Inputs: None
Outputs: None
'''
def commence_execution():
    action('DisableInput()')
    action('HideDialog()')
    action('WalkToSpot(' + global_game_states.accused + ', 1185.7, 11.7, 17.2)')
    action('Face(' + global_game_states.accused + ', Guard Gallant)')
    action('SetCameraFocus(Guard Gallant)')
    action('SetCameraMode(follow)')
    action('Attack(Guard Gallant, ' + global_game_states.accused + ', true)')
    action('Die(' + global_game_states.accused + ')')
    action('EnableInput()')

'''
Purpose: Handles the flow of the execution scene
Inputs: None
Outputs: None
'''
def end_cutscene():

    #Setup the scene
    end_cutscene_setup()

    # King's Dialog
    action('FadeIn()')
    set_left_right('King Phillip', 'null')
    action('EnableInput()')
    set_dialog('We are gathered here today to face the person who has killed my dearest Margerie. \\n[Next | Next]', ['Next'], True)
    set_dialog('My trusted advisor, John, has gathered the necessary evidence to bring ' + global_game_states.accused + ' to justice. \\n[Next | Next]')
    #display_clues_action() # implement present_evidence()
    set_dialog('It brings me no joy in sentencing you to death, but you have committed the greatest atrocity to this kingdom. \\n[Next | Next]')
    action('HideDialog()')

    #Set up accused dialogue
    action('SetCameraMode(focus)')
    action('SetCameraFocus(' + global_game_states.accused + ')')
    set_left_right(global_game_states.accused, 'null')

    # Check who the accused is, and display unique dilaogue and end game scores
    if global_game_states.accused == 'Maester Purcell':
        # Purcell's Dialogue
        set_dialog('No...I don\'t even remember who Margerie is. \\n[Next | Next]', ['Next'], True)
        set_dialog('Oh, darn this senile act. It\'s hard to act this stupid anyway. \\n[Next | Next]')
        set_dialog('Margerie was going to be the downfall of the kingdom. Her progressive ideas were tearing the land apart. \\n[Next | Next]')
        set_dialog('I was doing you all a favor. Get on with it. \\n[Next | Next]')
        # Execution
        commence_execution()
        # Score screen
        midscene_narration('Accusation Score: 5/5. Perfect! Clue Score: ')
    elif global_game_states.accused == 'Tiana':
        # Tiana's Dialogue
        set_dialog('I WAS MEANT TO BE THE TRUE QUEEN! \\n[Next | Next]', ['Next'], True)
        set_dialog('This isn\'t fair. I would have ruled the kingdom better. Margerie was just lucky she was born first. \\n[Next | Next]')
        set_dialog('Please it\'s not too late to change your mind! \\n[Next | Next]')
        # Execution
        commence_execution()
        # Score screen
        midscene_narration('Accusation Score: 4/5. Nice job! However, the master perpetrator remained free! Clue Score: ')
    elif global_game_states.accused == 'Chamber Maid Scarlet':
        # Scarlet's Dialogue
        set_dialog('Please sir, I was threatened with my life!  \\n[Next | Next]', ['Next'], True)
        set_dialog('It was me or her! I\'m innocent! \\n[Next | Next]')
        # Execution
        commence_execution()
        # Score screen
        midscene_narration('Accusation Score: 3/5. Decent! However, the master perpetrator remained free! Clue Score: ')
    elif global_game_states.accused == 'Alchemist Henry':
        # Henry's Dialogue
        set_dialog('I was just doing a job! How was I supposed to know what it was going to be used for! \\n[Next | Next]', ['Next'], True)
        set_dialog('The law in this land is straight backwards! \\n[Next | Next]')
        # Execution
        commence_execution()
        # Score screen
        midscene_narration('Accusation Score: 2/5. You can do better! The real masterminds remain free! Clue Score: ')
    else:
        # Random's Dialogue
        set_dialog('What evidence is there against me! \\n[Next | Next]', ['Next'], True)
        set_dialog('You\'re putting blind faith in a madman! \\n[Next | Next]')
        set_dialog('I swear I\'m innocent! \\n[Next | Next]')
        # Execution
        commence_execution()
        # Score screen
        midscene_narration('(Accusation Score: 1/5.  \\nDefinitely room for improvement! The actual perpetrators remain free!\\n\\n Clue Score: ')
    midscene_narration('Thanks for playing!')
    action('ShowMenu()')
        
