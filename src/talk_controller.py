from action import action
import global_game_states 
from add_clue import add_clue

def set_left_right(left, right):
    action('SetLeft('+left+')')
    action('SetRight('+right+')')

def set_dialog(dialog, responses=['Next'], show=False):
    action('ClearDialog()')
    action('SetDialog(\"'+dialog+'\")')
    if show:
        action('ShowDialog()')
    return wait_for_response(responses)

def wait_for_response(responses):
    response_list = []
    for response in responses:
        response_list.append('input Selected ' + response)
    received = input().strip()
    while not received in response_list:
        received = input().strip()
    return received

def castle_predeath(person):
    if person == 'Maester Purcell':
        set_dialog('Oh, who do we have here? The Queen\'s assistant you say? Well, the Queen and I may not agree on everything' +
        ' but you seem like a fine young gentleman. [Next| Thanks who are you again?]')
        set_dialog('I\'m not that important. I\'m just the Kingdom\'s Grand Maester. Mainly just an advisory role, but' +
        ' I plan on retiring at the end of the year...err...who are you again? [Next| ...The Queen\'s Assistant]')
        set_dialog('Right the castle chef. *The maester gets a glassy look and stares off in the distance* [Next| Goodbye]')
    elif person == 'Guard Gallant':
        set_dialog('Grrr... [Next| I\'ll be on my way.]')
    elif person == 'Queen Margerie':
        set_dialog('Isn\'t my husband so sweet! He did all of this for me! [Next| He sure is]')
    elif person == 'Witch Carlita':
        set_dialog('How can I help you? [Next| Can you teach me how to cast spells?]')
        set_dialog("Unfortunately, that takes year of training. Maybe some other time [Next| Darn]")
    elif person == 'Tiana':
        received = set_dialog('I don\'t know why King Phillip went through all this trouble for Margerie. She\'s hardly' + 
        ' worth it [One| Why are you so upset?] [Two| You should appreciate Margerie more]', ['One', 'Two'])
        if received == 'input Selected One':
            set_dialog('You would understand if you grew up with her[Next| I\'m sure]')
        else:
            set_dialog('I\'m sure she\'ll she appreciate what she\'s got coming to her [Next| ...okay]')
    elif person == 'King Phillip':
        set_dialog('Isn\'t Margerie lovely. I would be devastated if anything were to happen to her [Next| You really out did yourself]')

def castle_postdeath(person):
    if person == 'King Phillip':
        set_dialog('My Margerie...what has happened to you! Please find out what has happened. [Next| I\'m so sorry Phillip, let me look around]')
    if person == 'Tiana':
        set_dialog('I mean I never preferred my sister, but I would never have wished this upon her. [Next| Why exactly did you two not get along?]')
        set_dialog('Father always favored her since she was in line for the throne. But again, I would never kill her because of it. [Next| I think the whole kingdom will feel the gravity of this loss]')
    if person == 'Maester Purcell':
        set_dialog('Margerie was never supposed to go before this old coot. Whoever did this has pure malice in their heart. [Next| We will bring them to justice]')
    if person == 'Noble Jeremy' or person == 'Noble Cecilia' or person == 'Merchant Bert':
        set_dialog('Oh how horrible! [Next| Did you see anything?]')
        set_dialog('I\'m sorry I didn\'t see anything. [Next| Okay let me know if you think of anything]')
    if person == 'Chamber Maid Scarlet':
        set_dialog('How can I help? [Next| You served the drink did you notice anything unusual?]')
        set_dialog('No, I poured the wine straight out of the bottle when I was setting up earlier. Everyone\'s cups were filled from the same bottle. [Next| Where did you get the wine?]')
        set_dialog('Where we always get it, the local tavern. [Next| Where was the taste tester?]')
        set_dialog('Errrm....I think he was off today because of the Queen\'s birthday [Next| Thanks for your time]')

def dungeon_convo(person):
    if person == 'Guard Lyra':
        received = set_dialog('Wait, how did you open the cell... [Attack | I need to escape, for the King! (Attack)] [Talk | Listen, the King told me to escape. (Persuade)', ['Attack', 'Talk'], True)
        if received == 'input Selected Talk':
            received = set_dialog('You expect me to believe that? I\'m calling the other guards. [Attack | I can\'t let you do that! (Attack)] [Show | I have a letter from the King! (Persuade)]', ['Attack', 'Show'])
            if received == 'input Selected Show':
                set_dialog('That has the King\'s official seal on it... Fine, I\'ll let you go, but get out of here before I change my mind. [Next | Next]')
                global_game_states.dungeon_guard_lives = True
        action('HideDialog()')
        
def city_convo(person):
    if person == 'Beggar Adeline':
        set_dialog('I\'m not sad about the Queen\'s death. She\'s been rolling in wealth while decent folks can\'t even find a job to support their families. [Next| ... okay?]')
    elif person == 'Beggar Miles':
        set_dialog('Spare some change for an old man? [Next| Sorry, I\'m broke]')
    elif person == 'Scout Joanna':
        set_dialog('You don\'t want to go this way. Once outside the town, you\'re on your own. [Next| Thanks!]')
    elif person == 'Alchemist Jeremy':
        set_dialog('Step inside for all your alchemy needs. Whether it\'s a nice polish for your shoes or a draught for your pain, we\'ve got it here! [Next| I\'ll keep that in mind]')
    elif person == 'Scout Tom':
        set_dialog('You don\'t want to go this way. Once outside the town, you\'re on your own. [Next| Thanks!]')
    elif person == 'Drunk Devon':
        set_dialog('My name is Devon. This here is the Tavern, a good place to hear the comings and goings of the town. [Next | Thanks!]')
    elif person == 'Priestess Esmerelda':
        set_dialog('The witches must burn! It is no surprise the Queen is dead given the monarchy\'s flagrant disrespect of the sacred texts and ancient traditions. [Next | err... ok]')
        if global_game_states.priestess_false_trail == False:
            global_game_states.priestess_false_trail = True
            global_game_states.current_clues.append('The Priestess seems to have strong feelings about killing the Queen.')
    elif person == 'Blind Bandit':
        set_dialog('I heard a rumour last fortnight about a contract killing of the Queen, but I didn\'t believe it until now. [Next | ... Interesting]')
        if global_game_states.blind_bandit_clue == False:
            global_game_states.blind_bandit_clue = True
            global_game_states.current_clues.append('The Blind Bandid mentions there may be more than one person involved.')
    elif person == 'Gossiping Gail':
        set_dialog('I know everything going on in this town. Go ahead, ask me. [Next| I\'d rather not.')

def alchemist_shop_convo(person):
    player_response = 'input Selected Menu'
    if person == 'Alchemist Henry':
        if player_response == 'input Selected Menu':
            if global_game_states.found_poison_purchase == True:
                if global_game_states.found_poison == False:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Find anything you like? [Purchase | Who is Tianna?] [Next | Still looking around]', ['Purchase', 'Next'])
                    else:
                        player_response = set_dialog('Find anything you like? [Purchase | Who is Tianna?] [About | About that rat poison...] [Next | Still looking around]', ['Purchase', 'About', 'Next'])
                else:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Need help with anything else? [Purchase | Who is Tianna?] [Free | Are you sure I can have this?] [Next | No, thanks]', ['Purchase', 'Free', 'Next'])
                    else:
                        player_response = set_dialog('Need help with anything else? [Purchase | Who is Tianna?] [Free | Are you sure I can have this?] [About | About that rat poison...] [Next | No, thanks]', ['Purchase', 'Free', 'About', 'Next'])
            else:
                if global_game_states.found_poison == False:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Welcome! Feel free to look around. [Next | Thanks]')
                    else:
                        player_response = set_dialog('Find anything you like? [About | About that rat poison...] [Next | Still looking around]', ['About', 'Next'])
                else:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Need help with anything else? [Free | Are you sure I can have this?] [Next | No, thanks]', ['Free', 'Next'])
                    else:
                        player_response = set_dialog('Need help with anything else? [Free | Are you sure I can have this?] [About | About that rat poison...] [Next| No, thanks]', ['About','Next'])
        if player_response == 'input Selected Purchase':
            player_response = set_dialog('Oh, Tianna? She\'s the Queen\'s sister. She recently bought some giant rat poison to help clear the sewers. [Menu| Thanks]', ['Menu'])
        elif player_response == 'input Selected Free':
            player_response = set_dialog('If you\'re investigating for the king, take it! Quickly now! [Menu| Okay...]', ['Menu'])
        elif player_response == 'input Selected About' and global_game_states.found_poison == False:
            player_response = set_dialog('Oh, the giant rat poison? I usually don\'t sell it to civilians. [About2 | The king asked me]', ['About2'])
            if player_response == 'input Selected About2':
                player_response = set_dialog('You\'re investigating for the king? Take the display bottle. It\'s one of the purple ones, with a skull and crossbones. [Menu | Thanks]', ['Menu'])
                action('EnableIcon(TakeLeft, hand, Poison, Take Giant Rat Poison, false)')
                if 'Found Poison' not in global_game_states.current_clues:
                    global_game_states.current_clues.append('Found Poison')
                    add_clue('Found Poison')
                    global_game_states.found_poison = True
        elif player_response == 'input Selected About' and global_game_states.found_poison == True:
            player_response = set_dialog('The giant rat poison? Didn\'t you already grab it? [Menu | Yeah...]', ['Menu'])
        action('HideDialog()')
        
def tavern_convo(person):
    if person == 'Maester Purcell':
        set_dialog('Oh! Where am I? Oh that\'s right, the tavern. I really should be going. Who are you again? *The maester gets a glassy look and stares off in the distance* [Next| erm... ok?]')
    elif person == 'Witch Carlita':
        set_dialog('That Maester Purcell sure acts like a fool, but he\'s sharp as a tack. Don\'t let him fool you [Next | Thanks for the heads up]')
        if global_game_states.maester_purcell_senile == False:
            global_game_states.maester_purcell_senile = True
            global_game_states.current_clues.append('Witch Carlita informs you that Maester Purcell may be more than he seems.')        
    elif person == 'Noble Jeremy':
        set_dialog('This murder is the most interesting thing to happen in years. Remember back when the Queen\'s Uncle got his leg eaten by that shark? Now that was a story. [Next| ...Fascinating.]')
    elif person == 'Noble Cecilia':
        set_dialog('Tiana has always been jealous of her sister, I just can\'t imagine she would poison her. [Next | ...]')
        if global_game_states.cecilia_accusations == False:
            global_game_states.cecilia_accusations = True
            global_game_states.current_clues.append('Cecilia accused the Queen\'s Sister of murder')
    elif person == 'Merchant Bert':
        set_dialog('I sold the Alchemist a whole cart-load of ingredients last week, some of them were poisons. If you want to look for clues, I\'d start with the Alchemist shop [Next| Thanks, I\'ll take a look around.]')
    elif person == 'Chamber Maid Scarlet':
        set_dialog('*Scarlet sits silently trembling, fumbling for words* [Next | Next]')
        if global_game_states.chamber_maid_odd_behaviours == False:
            global_game_states.chamber_maid_odd_behaviours = True
            global_game_states.current_clues.append('Chamber Maid Scarlet wasn\'t able to speak afterwords')
    elif person == 'Tiana':
        set_dialog('Why do you speak to me?! Can\'t you see I\'m distraught?! [Next | ...]')
