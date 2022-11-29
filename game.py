import random

# global variables sector

MENU = True
NEW_GAME = False
CREDITS = False
IS_DEAD = False
WAS_DEAD = False

# global player variables sector

HP = 100
ATTACK = 20
DEFENCE = 10

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

# new game sector

while NEW_GAME == True:
    if IS_DEAD == False:
        NEW_GAME = False
        coins = 0
        score = 0
        to_menu = 0 # variable to break from while loops
        potions = 0
        HP = 100
        print('Welcome to RPG Game...')
        player_name = input('Please enter your name here: ')
        print(f'[❓] Hi, {player_name} nice to see you, we got a big problem.')
        print('[❓] Firstable, my name is Sam.')
        print('[🕵️‍♂️] Im here to kill the dragon at the on of this place...')
        print('[🕵️‍♂️] Come here with me!')
        print('[📑] To move forward simply write ("forward")')
        print('[📑] To move towards shop simply write ("shop")')
        while HP > 0:
            have_won = 0
            if WAS_DEAD == 1:
                print('You respawned... start again!')
                score = 0
                coins = 0
                WAS_DEAD = 0
                potions = 0
            print('[✅]Current position: Outside')    
            player_choice = input('[🤴]>> ')
            random_enemy = random.choice(enemy_list)
            
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
                score += 1
                print('You went forward...')
                print(f'Suddenly - {random_enemy} approach you!')
                print('To attack him, simply write "attack".')

                while HP > 0 or ENEMY_HP > 0:
                    if have_won == 1:
                        break
                    player_attack = input('[🪓]>> ')
                    if player_attack == 'attack':
                        print(f'[💥]You have attacked {random_enemy} for {ATTACK-(ENEMY_DEFENCE/2)} health points.')
                        ENEMY_HP = ENEMY_HP - (ATTACK-(ENEMY_DEFENCE/2))
                        print(f'[💥]{random_enemy} attacked you for {ENEMY_ATTACK-(DEFENCE/2)} health points.')
                        HP = HP - (ENEMY_ATTACK-(DEFENCE/2))
                        print(f'[STATS] HP = {HP}❤ | ENEMY_HP = {ENEMY_HP}❤')
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
                                print(f'You have killed 💀{random_enemy}💀')
                                print(f'You earned 💸{MONEY_EARN} coins.💸')
                                coins += MONEY_EARN
                                score += 1
                                have_won = 1
                                break
                    # potions system        
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
                                                                                         
                    else:
                        print(f'[💥]You missed the attack!')
                        print(f'[💥]{random_enemy} attacked you for {ENEMY_ATTACK-(DEFENCE/2)}')
                        HP = HP - (ENEMY_ATTACK-(DEFENCE/2))
                        print(f'[STATS] HP = ❤ {HP} | ENEMY_HP = ❤ {ENEMY_HP}')
                        if HP <= 0 or ENEMY_HP <= 0:
                            if HP <= 0:
                                print('💀You are dead💀')
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
            # shop sector  
            elif player_choice.lower() == 'shop':
                print('[✅]Current position: Shop')
                print('[🧙‍♂️] Welcome to my shop!')
                print('[📑] To buy simply write index of item: Potion[price] - [index]')
                print('[📑] To exit simply press enter.')
                print('[ITEMS]: Potion[10] - [1]')
                while(True):
                    shop_buy = input('[💎SHOP💎]>> ')
                    if shop_buy.lower() == '1':
                        if coins >= 10:
                            coins -= 10
                            potions += 1
                            print('[✅] You have bought a one potion!')
                            print(f'Current balance is: {coins}')
                        else:
                            print('[🧙‍♂️] You dont have enough coins.')
                            print(f'Current balance is: {coins}')
                    elif shop_buy == '':
                        print('[✅] You have left the shop.')
                        break
            # block potion usage
            elif player_choice.lower() == 'potion':
                print('[❌] You only can use potion while you are fighting!')
            else:
                print('[❌] Please write correct command.')
# # # # # # #
            
