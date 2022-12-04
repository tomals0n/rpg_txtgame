import random

# global variables sector

MENU = True
NEW_GAME = False
CREDITS = False
IS_DEAD = False
WAS_DEAD = False

# global player variables sector

HP = 100
MANA = 10
ATTACK = 20
DEFENCE = 10
SPELL_DMG = 25

# global enemy variables sector

enemy_list = ['Skeleton', 'Rat', 'Zombie', 'Jumbo']
ENEMY_HP = 20
ENEMY_ATTACK = 5
ENEMY_DEFENCE = 6

# # # # # # # 

# menu sector

menu_choices = {
    1: 'New Game',
    2: 'Credits',
    3: 'Exit'
}

while MENU == True:
    for x in menu_choices.keys():
        print(f'{x} -- {menu_choices[x]}')
    MENU = False
    while(True):
        try:
            user_choice = input()
        except ValueError:
            print('[❌] Please write correct number.')
        if user_choice == '1':
            NEW_GAME = True
            break
        elif user_choice == '2':
            CREDITS = True
            break
        elif user_choice == '3':
            exit()
        else:
            print('[❌] Please write correct number.')

# # # # # # #


# credits sector

while CREDITS == True:
    CREDITS = False
    print('[📑] The game have been made by tomals0n')
    print('[📑] Latest update: 5.12.2022 | ver: 0.1a')
    print('[✅] Recent update: New Item - Golden Sword')
    print('[✅] To start new game - write yes, to exit write no.')
    while(True):
        wanna_newgame = input('>> ')
        if wanna_newgame.lower() == 'yes':
            NEW_GAME = True
            break
        elif wanna_newgame.lower() == 'no':
            MENU = True
            break
        else:
            print('[❌] Please write correct command.')

# new game sector

while NEW_GAME == True:
    if IS_DEAD == False:
        NEW_GAME = False
        coins = 0
        score = 0
        potions = 0
        mana_potions = 0
        HP = 100
        fireball_scroll = None
        golden_sword = None
        print('Welcome to RPG Game...')
        player_name = input('Please enter your name here: ')
        print(f'[❓] Hi, {player_name} welcome.')
        print('[📑] To move forward simply write ("forward")')
        print('[📑] To move towards shop simply write ("shop")')
        while HP > 0:
            have_won = 0
            # respawned reset
            if WAS_DEAD == 1:
                print('You respawned... start again!')
                score = 0
                coins = 0
                WAS_DEAD = 0
                potions = 0
                mana_potions = 0
                fireball_scroll = None
                golden_sword = None
            # break loop to menu
            if IS_DEAD == 1:
                MENU = True
                IS_DEAD = 0
                break
            print('') # space
            print('[✅]Current position: Outside')    
            player_choice = input('[🤴]>> ')
            random_enemy = random.choice(enemy_list)
            
            # load default player stats
            ATTACK = 20
            #print(f'[DEBUG] YOU HAVE {ATTACK} ATTACK')
            
            
            
            # enemies stats
            if random_enemy == 'Skeleton':
                ENEMY_HP = 40
                ENEMY_ATTACK = 15
                ENEMY_DEFENCE = 12
                MONEY_EARN = 5
            elif random_enemy == 'Rat':
                ENEMY_HP = 10
                ENEMY_DEFENCE = 6
                MONEY_EARN = 2
            elif random_enemy == 'Zombie':
                ENEMY_HP = 30
                ENEMY_ATTACK = 8
                ENEMY_DEFENCE = 8
                MONEY_EARN = 3
            elif random_enemy == 'Jumbo':
                ENEMY_HP = 50
                ENEMY_ATTACK = 8
                ENEMY_DEFENCE = 8
                MONEY_EARN = 9
               
            
            # # # # # #
            # game            
            if player_choice.lower() == 'forward':
                # check if player have golden sword
                if golden_sword == True:
                    ATTACK += 10
                    #print(f'[DEBUG] YOU HAVE {ATTACK} ATTACK')
                score += 1
                print('') # space
                print('[✅] You went forward...')
                print(f'[🔪] Suddenly - {random_enemy} approach you!')
                print('') # space
                print('[❓] To attack him, simply write "attack".')

                while HP > 0 or ENEMY_HP > 0:
                    if have_won == 1:
                        break
                    player_attack = input('[🪓]>> ')
                    if player_attack == 'attack':
                        print('') # space
                        print(f'[💥]You have attacked {random_enemy} for {ATTACK-(ENEMY_DEFENCE/2)} health points.')
                        ENEMY_HP = ENEMY_HP - (ATTACK-(ENEMY_DEFENCE/2))
                        print(f'[💥]{random_enemy} attacked you for {ENEMY_ATTACK-(DEFENCE/2)} health points.')
                        HP = HP - (ENEMY_ATTACK-(DEFENCE/2))
                        print(f'[STATS] HP = {HP}❤ | ENEMY_HP = {ENEMY_HP}❤')
                        print('') # space
                        if HP <= 0 or ENEMY_HP <= 0:
                            # player dead sector
                            if HP <= 0:
                                print('💀You are dead💀')
                                while(True):
                                    play_again = input('Do you want to play again?(yes/no): ')
                                    if play_again.lower() == 'yes':
                                        HP = 100
                                        WAS_DEAD += 1
                                        have_won += 1
                                        break
                                    elif play_again.lower() == 'no':
                                        HP = 100
                                        to_menu = 1
                                        break
                            elif ENEMY_HP <= 0:
                                print(f'[✅] You have killed 💀{random_enemy}💀')
                                print(f'[✅] You earned 💸{MONEY_EARN} coins💸')
                                coins += MONEY_EARN
                                score += 1
                                have_won = 1
                                break
                    # hp potions system        
                    elif player_attack.lower() == 'potion':
                        if potions > 0:
                            if HP+20 <= 100:
                                print('[✅] You have used a potion!')
                                potions -= 1
                                print('[✅] Potion restored 20HP!')
                                HP += 20
                            elif HP+20 > 100:
                                print('[✅] You have used a potion!')
                                potions -= 1
                                print('[✅] Potion restored HP to maximum.')
                                HP = 100
                            elif HP == 100:
                                print('[❌] You have full HP!')
                        else:
                            print('[❌] You dont have a potion!')
                    # mana potions system
                    elif player_attack.lower() == 'mana':
                        if mana_potions > 0:
                            if MANA+10 <= 0:
                                print('[✅] You have used a potion!')
                                mana_potions -= 1
                                print('[✅] Potion restored 10MP!')
                            elif MANA+10 > 10:
                                print('[✅] You have used a potion!')
                                mana_potions -= 1
                                print('[✅] Potion restored MP to maximum.')
                                MANA = 10
                            elif MANA == 10:
                                print('[❌] You have full MP!')
                        else:
                            print('[❌] You dont have a potion!')
                    elif player_attack.lower() == 'fireball':
                        if fireball_scroll == True:
                            if MANA >= 5:
                                print('') # space
                                print(f'[🔥] You have used fireball spell dealing {SPELL_DMG} HP!')
                                ENEMY_HP -= SPELL_DMG
                                MANA -= 5
                                print(f'[💥]{random_enemy} attacked you for {ENEMY_ATTACK-(DEFENCE/2)} health points.')
                                HP = HP - (ENEMY_ATTACK-(DEFENCE/2))
                                print(f'[STATS] HP = {HP}❤ | ENEMY_HP = {ENEMY_HP}❤')
                                print('') # space                                
                                if HP <= 0 or ENEMY_HP <= 0:
                                    # player dead sector
                                    if HP <= 0:
                                        print('💀You are dead💀')
                                        while(True):
                                            play_again = input('Do you want to play again?(yes/no): ')
                                            if play_again.lower() == 'yes':
                                                HP = 100
                                                WAS_DEAD += 1
                                                have_won += 1
                                                break
                                            elif play_again.lower() == 'no':
                                                HP = 100
                                                to_menu = 1
                                                break
                                    elif ENEMY_HP <= 0:
                                        print(f'[✅] You have killed 💀{random_enemy}💀')
                                        print(f'[✅] You earned 💸{MONEY_EARN} coins💸')               
                                        coins += MONEY_EARN
                                        score += 1
                                        have_won = 1
                                        break
                            else:
                                print(f'[❌] You dont have enough mana!')
                        else:
                             print(f'[❌] You dont know how to use this spell!')                                                                              
                    else:
                        print('') # space
                        print(f'[💥] You missed the attack!')
                        print(f'[💥] {random_enemy} attacked you for {ENEMY_ATTACK-(DEFENCE/2)}')
                        HP = HP - (ENEMY_ATTACK-(DEFENCE/2))
                        print(f'[STATS] HP = ❤ {HP} | ENEMY_HP = ❤ {ENEMY_HP}')
                        print('') # space
                        if HP <= 0 or ENEMY_HP <= 0:
                            if HP <= 0:
                                print('💀You are dead💀')
                                play_again = input('Do you want to play again?(yes/no): ')
                                if play_again.lower() == 'yes':
                                    HP = 100
                                    MANA = 10
                                    WAS_DEAD += 1
                                    have_won += 1
                                    break
                                elif play_again.lower() == 'no':
                                    HP = 100
                                    MANA = 10
                                    IS_DEAD += 1
                                    break
            # shop sector  
            elif player_choice.lower() == 'shop':
                print('') # space
                print('[🧙‍♂️] Welcome to my shop!')
                print('[📑] To buy simply write index of item: Item[price] - [index]')
                print('[📑] To exit simply press enter.')
                print('[ITEMS]: Potion[10] - [1] | Mana Potion[15] - [2] | Fireball Scroll[100] - [3] | Golden Sword[150] - [4]')
                print(f'[💸] Your balance is: {coins} coins.')
                print('') # space
                print('[✅]Current position: Shop')
                while(True):
                    shop_buy = input('[💸]>> ')
                    if shop_buy.lower() == '1':
                        if coins >= 10:
                            coins -= 10
                            potions += 1
                            print('[✅] You have bought a one potion!')
                            print(f'Current balance is: {coins}')
                        else:
                            print('[🧙‍♂️] You dont have enough coins.')
                            print(f'Current balance is: {coins}')
                    elif shop_buy.lower() == '2':
                        if coins >= 15:
                            coins -= 15
                            mana_potions += 1
                            print('[✅] You have bought a one mana potion!')
                            print(f'Current balance is: {coins}')
                        else:
                            print('[🧙‍♂️] You dont have enough coins.')
                            print(f'Current balance is: {coins}')
                    elif shop_buy == '3':
                        if coins >= 100:
                            coins -= 100
                            fireball_scroll = True
                            print('[✅] You have bought a fireball scroll!')
                            print('[📑] You can use this in fight by typing "fireball"')
                            print(f'Current balance is: {coins}')
                        elif fireball_scroll == True:
                            print('[❌] You have already bought fireball scroll!')
                        else:
                            print('[🧙‍♂️] You dont have enough coins.')  
                            print(f'Current balance is: {coins}')
                    elif shop_buy == '4':
                        if coins >= 150:
                            coins -= 150
                            golden_sword = True
                            print('[✅] You have bought a Golden Sword!')
                            print(f'[📑] Your attack raised up by 10 points, now you have {ATTACK+10} attack points.')
                            print(f'Current balance is: {coins}')
                        elif golden_sword == True:
                            print('[❌] You have already bought Golden Sword!')
                        else:
                            print('[🧙‍♂️] You dont have enough coins.')  
                            print(f'Current balance is: {coins}')                                                                                      
                    elif shop_buy == '':
                        print('[✅] You have left the shop.')
                        break
            # block potion usage
            elif player_choice.lower() == 'potion':
                print('[❌] You only can use potion while you are fighting!')
            elif player_choice.lower() == 'mana':
                print('[❌] You only can use mana potion while you are fighting!')
            # player statistics
            elif player_choice.lower() == 'stats':
                print('') # space
                print(f'{player_name} stats:')
                print(f'[❤ ] HP - {HP}')
                print(f'[🪓] ATTACK - {ATTACK}')
                print(f'[🛡 ] DEFENCE - {DEFENCE}')
                print(f'[💸] COINS - {coins}')
                print(f'[💥] KILLED ENEMIES - {score}')
                print('') # space
                print(f'{player_name} backpack:')
                if golden_sword == True:
                    print('[🗡] Golden Sword')
                if potions > 1:
                    print(f'[🧪] Health Potions - {potions}')
                if mana_potions > 1:
                    print(f'[🧪] Mana Potions - {mana_potions}')
                if fireball_scroll == True:
                    print(f'[📜] Fireball Scroll')
                print('') # space
            else:
                print('[❌] Please write correct command.')
# # # # # # #
            
while MENU == True:
    for x in menu_choices.keys():
        print(f'{x} -- {menu_choices[x]}')
    MENU = False
    while(True):
        try:
            user_choice = input()
        except ValueError:
            print('[❌] Please write correct number.')
        if user_choice == '1':
            NEW_GAME = True
            break
        elif user_choice == '2':
            CREDITS = True
            break
        elif user_choice == '3':
            exit()
        else:
            print('[❌] Please write correct number.')
