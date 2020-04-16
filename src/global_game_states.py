''' 
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Stores global game variables.
'''

# Castle
queen_death = False
castle_key = False
castle_clues = []

# Dungeon
acquired_CellDoorKey = True
dungeon_guard_lives = False
dirtpile_inventory = [['Note From King', 'Note From King'], ['Cell Door Key', 'Cell Door Key']]
dungeon_chest_inventory = [['Change of Clothes', 'Change of Clothes']]
dungeon_clues = []

# City
first_city_entry = True
blind_bandit_offended = False
blind_bandit_clue_aquired = False
priestess_false_trail = False
scarlet_working_extra_hard = False
city_clues = []

# Alchemy Shop
alchemist_is_paranoid = False
first_alchemist_entry = True
found_poison_purchase = False #Evidence for buyer of poison
found_poison = False #Evidence for alchemist
identified_poison = False #used as a step for found_potion
alchemist_shop_clues = []

# Tavern
staring_contest_with_purcell = 0
first_tavern_entry = True
maester_purcell_senile = False
cecilia_accusations = False
chamber_maid_odd_behaviours = False
tavern_clues = []

# Ending
execution_characters = ['Noble Jeremy', 'Noble Cecilia', 'Tiana']
selected_clues = []

# Global
current_scene = 'castle'
prev_scene = ''
accused = ''
wearing_disguise = False
player_inventory = [['Party Invitation', 'Party Invitation']]
list_of_inventories = [player_inventory, dungeon_chest_inventory, dirtpile_inventory]
current_clues = []
character_list = ['Guard Gallant', 'King Phillip', 'Witch Carlita', 'Noble Jeremy', 'Noble Cecilia','Merchant Bert', 'Chamber Maid Scarlet', 'Tiana', 
    'Maester Purcell', 'Beggar Adeline', 'Beggar Miles', 'Alchemist Jeremy', 'Scout Joanna', 'Scout Tom', 'Drunk Devon', 
    'Priestess Esmerelda', 'Blind Bandit', 'Gossiping Gail', 'Guard', 'Alchemist Henry'
]



