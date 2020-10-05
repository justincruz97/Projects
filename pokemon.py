# Justin Cruz cssc1832  & Jasmine Camacho cssc1835

# This file will read and extract data from pokemon.csv
# The data used will ask the reader to enter 3 Pokemon of their choice
# and 1 enemy Pokemon of their choice to battle.

import numpy as np
import pandas as pd
from operator import itemgetter, attrgetter
from random import randint
import os, sys, math


class Pokemon:
    def __init__(self, against_type1, against_type2,\
            attack, base_total, capture_rate, defense, hp, name, sp_attack,\
            sp_defense, speed, type1, type2, is_legendary, pokedex_number):
        
        self.against_type1 = against_type1
        self.against_type2 = against_type2
        self.attack = attack
        self.base_total = base_total
        self.capture_rate = capture_rate
        self.defense = defense 
        self.hp = hp
        self.name = name 
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.type1 = type1
        self.type2 = type2
        self.is_legendary = is_legendary
        self.pokedex_number = pokedex_number


class EnemyPokemon:
    def __init__(self, ag_bug, ag_dark, ag_dragon, ag_elec,\
            ag_fairy, ag_fighter, ag_fire, ag_flying, ag_ghost, ag_grass,\
            ag_ground, ag_ice, ag_normal, ag_poison, ag_psychic, ag_rock,\
            ag_steel, ag_water, attack, base_total, capture_rate, defense,\
            hp, name, sp_attack, sp_defense, speed, type1, type2, is_legendary,\
            pokedex_number):

            self.ag_bug = ag_bug 
            self.ag_dark = ag_dark 
            self.ag_dragon = ag_dragon 
            self.ag_elec = ag_elec
            self.ag_fairy = ag_fairy
            self.ag_fighter = ag_fighter 
            self.ag_fire = ag_fire
            self.ag_fling = ag_flying 
            self.ag_ghost = ag_ghost
            self.ag_grass = ag_grass 
            self.ag_ground = ag_ground
            self.ag_ice = ag_ice 
            self.ag_normal = ag_normal
            self.ag_poison = ag_poison 
            self.ag_psychic = ag_psychic
            self.ag_rock = ag_rock 
            self.ag_steel = ag_steel
            self.ag_water = ag_water
            self.attack = attack
            self.base_total = base_total
            self.capture_rate = capture_rate
            self.defense = defense 
            self.hp = hp
            self.name = name
            self.sp_attack = sp_attack
            self.sp_defense = sp_defense
            self.speed = speed
            self.type1 = type1
            self.type2 = type2
            self.is_legendary = is_legendary
            self.pokedex_number = pokedex_number


''' PARTY POKEMON METHODS '''

def getPartyData(select, original, col):
    col_data = []
    for sel in select:
        for name in original:
            if( sel == name ):
                idx = original.index(name)
                col_data.append(col[idx])
    return col_data


def getPartyPokemon(ag_t1, ag_t2, atk, b_tot, cap_rate,\
                dfnd, health, names, sp_atk, sp_def, spd, t1, t2, legend, pokedex):
    if( len(health) != len(pokedex) ):
        print('Must have sufficient amount of Pokemon.')
        exit()
    else:
        pokemon = [Pokemon(ag_t1,ag_t2,atk[i],\
                    b_tot[i],cap_rate[i],dfnd[i],health[i],names[i],sp_atk[i],\
                    sp_def[i],spd[i],t1[i],t2[i],legend[i],pokedex[i]) for i in range( len(pokedex) ) ]
        for poke in pokemon:
            if( pd.isnull(poke.type2) ):
                poke.type2 = 0
        return pokemon




'''     ENEMY   POKEMON   METHODS   '''

def getEnemyData(select, original, col):
    idx = original.index(select)
    return col[idx]





'''
MAIN GET METHODS
'''

def getParty():
    # Reading data from csv file
    csv = os.getcwd() + "/pokemon.csv"
    pokemon = pd.read_csv(csv)

    names = pokemon.loc[:,'name']
    low_names = [name.casefold() for name in names]


    atk = pokemon.loc[:,'attack']
    b_tot = pokemon.loc[:,'base_total']
    cap_rate = pokemon.loc[:,'capture_rate']
    dfnd = pokemon.loc[:,'defense']
    health = pokemon.loc[:,'hp']
    names = pokemon.loc[:,'name']
    sp_atk = pokemon.loc[:,'sp_attack']    
    sp_def = pokemon.loc[:,'sp_defense']
    speed = pokemon.loc[:,'speed']
    t1 = pokemon.loc[:,'type1']
    t2 = pokemon.loc[:,'type2']
    legend = pokemon.loc[:,'is_legendary']
    pokedex = pokemon.loc[:,'pokedex_number']
    

    # Asking user to input 6 Pokemon
    print('LIST OF POKEMON')
    print('- - - - - - - - - - ')
    for pokemon in names:
        print(pokemon)
    print(" ")
    print(" ")

    inp = input("Please type the names of up to 6 Pokemon of your choice: ")
    select = inp.split()

    # Checking if choices are in the csv file
    if( len(select) > 6 ):
        print("Must enter at at most 6 Pokemon, choose again.\n")
        getParty()
    else:
        low_select = [name.casefold() for name in select]
        
        if( set(low_names).intersection(set(low_select)) == set(low_select) ):
           
            # Getting Data 
            
            
            atk_data = getPartyData(low_select,low_names,atk)
            bt_data = getPartyData(low_select,low_names,b_tot)
            cr_data = getPartyData(low_select,low_names,cap_rate)
            df_data = getPartyData(low_select,low_names,dfnd)
            hp_data = getPartyData(low_select,low_names,health)
            user_input = [name.capitalize() for name in low_select]
            sp_a_data = getPartyData(low_select,low_names,sp_atk)
            sp_d_data = getPartyData(low_select,low_names,sp_def)
            speed_data = getPartyData(low_select, low_names,speed)
            t1_data = getPartyData(low_select,low_names,t1)
            t2_data = getPartyData(low_select,low_names,t2)
            lgd_data = getPartyData(low_select,low_names,legend)
            pokedex_data = getPartyData(low_select,low_names,pokedex)
            agt1 = 0
            agt2 = 0
            
            return getPartyPokemon(agt1, agt2, atk_data, bt_data,cr_data,\
                    df_data, hp_data, user_input, sp_a_data, sp_d_data, speed_data,\
                    t1_data,t2_data,lgd_data,pokedex_data)
        else:
            print("One or more Pokemon don't exist. Try Again.\n")
            getParty()


def getEnemy():

    # Reading data from csv file
    csv = os.getcwd() + "/pokemon.csv"
    pokemon = pd.read_csv(csv)

    against_bug = pokemon.loc[:,'against_bug']
    against_dark = pokemon.loc[:,'against_dark']
    against_dragon = pokemon.loc[:,'against_dragon']
    against_electric = pokemon.loc[:,'against_electric']
    against_fairy = pokemon.loc[:,'against_fairy']
    against_fight = pokemon.loc[:,'against_fight']
    against_fire = pokemon.loc[:,'against_fire']
    against_flying = pokemon.loc[:,'against_flying']
    against_ghost = pokemon.loc[:,'against_ghost']
    against_grass = pokemon.loc[:,'against_grass']
    against_ground = pokemon.loc[:,'against_ground']
    against_ice = pokemon.loc[:,'against_ice']
    against_normal = pokemon.loc[:,'against_normal']
    against_poison = pokemon.loc[:,'against_poison']
    against_psychic = pokemon.loc[:,'against_psychic']
    against_rock = pokemon.loc[:,'against_rock']
    against_steel = pokemon.loc[:,'against_steel']
    against_water = pokemon.loc[:,'against_water']
    attack = pokemon.loc[:,'attack']
    base_total = pokemon.loc[:,'base_total']
    capture_rate = pokemon.loc[:,'capture_rate']
    defense = pokemon.loc[:,'defense']
    health = pokemon.loc[:,'hp']
    names = pokemon.loc[:,'name']
    sp_attack = pokemon.loc[:,'sp_attack']
    sp_defense = pokemon.loc[:,'sp_defense']
    speed = pokemon.loc[:,'speed']
    type1 = pokemon.loc[:,'type1']
    type2 = pokemon.loc[:,'type2']
    is_legendary = pokemon.loc[:,'is_legendary']
    pokedex_number = pokemon.loc[:,'pokedex_number']

    # Asking user to input 6 Pokemon
    inp = input("Please select one Pokemon of your choice: ")
    select = inp.split()
    

    # Checking if choices are in the csv file
    if( len(select) > 1 ):
        print("Must enter only 1 enemy Pokemon, choose again.")
        getEnemy()
    else:
        low_select = select[0].casefold()
        low_names = [name.casefold() for name in names]

        if( set(low_names).intersection(set( [low_select] )) == set( [low_select] ) ):
            ag_bug = getEnemyData(low_select, low_names, against_bug)
            ag_dark = getEnemyData(low_select, low_names, against_dark)
            ag_drag = getEnemyData(low_select, low_names, against_dragon)
            ag_elec = getEnemyData(low_select, low_names, against_electric)
            ag_fairy = getEnemyData(low_select, low_names, against_fairy)
            ag_fight = getEnemyData(low_select, low_names, against_fight)
            ag_fire = getEnemyData(low_select, low_names, against_fire)
            ag_flying = getEnemyData(low_select, low_names, against_flying)
            ag_ghost = getEnemyData(low_select, low_names, against_ghost)
            ag_grass = getEnemyData(low_select, low_names, against_grass)
            ag_ground = getEnemyData(low_select, low_select, against_ground)
            ag_ice = getEnemyData(low_select, low_names, against_ice)
            ag_normal = getEnemyData(low_select, low_names, against_normal)
            ag_poison = getEnemyData(low_select, low_names, against_poison)
            ag_psychic = getEnemyData(low_select, low_names, against_psychic)
            ag_rock = getEnemyData(low_select, low_names, against_rock)
            ag_steel = getEnemyData(low_select, low_names, against_steel)
            ag_water = getEnemyData(low_select, low_names, against_water)
            atk = getEnemyData(low_select, low_names, attack)
            bt = getEnemyData(low_select, low_names, base_total)
            cr = getEnemyData(low_select, low_names, capture_rate)
            defend = getEnemyData(low_select, low_names, defense)
            hp = getEnemyData(low_select, low_names, health)
            name = getEnemyData(low_select, low_names, names)
            sp_atk = getEnemyData(low_select, low_names, sp_attack)
            sp_def = getEnemyData(low_select, low_names, sp_defense)
            speed = getEnemyData(low_select, low_names, speed)
            t1 = getEnemyData(low_select, low_names, type1)
            t2 = getEnemyData(low_select, low_names, type2)
            legend = getEnemyData(low_select, low_names, is_legendary)
            pkdx_num = getEnemyData(low_select, low_names, pokedex_number)


            enemy = EnemyPokemon(ag_bug, ag_dark, ag_drag,\
                    ag_elec, ag_fairy, ag_fight, ag_fire,\
                    ag_flying, ag_ghost, ag_grass, ag_ground,\
                    ag_ice, ag_normal, ag_poison, ag_psychic,\
                    ag_rock, ag_steel, ag_water, atk, bt, cr,\
                    defend, hp, name, sp_atk, sp_def, speed, t1, t2,\
                    legend, pkdx_num)

            if( pd.isnull(enemy.type2) ):
                enemy.type2 = '      '

            return enemy

        else:
            print("Your Pokemon doesn't exist. Try Again.")
            getEnemy()

    

def displayParty(party, enemy):
    
    sort = sorted(party, key=attrgetter('sp_attack'), reverse=True)
        
    print('POKEMON  DATA')
    print(' ')    
    print('|-------------------------------------------------------------------------------------------------------------------------------|')
    print('|    POKEMON    |     SP_ATK    |    SP_DEF     |       HP      |     TYPE 1    |     TYPE 2    | VS.ATK TYPE 1 | VS.ATK TYPE 2 |')
    print('|-------------------------------------------------------------------------------------------------------------------------------|')
    for i in sort:
        csv = os.getcwd() + "/pokemon.csv"
        pokemon = pd.read_csv(csv)
        sp_attk = i.sp_attack
        type_1 = i.type1
        type_2 = i.type2
        agt_type1 = "against_" + type_1

        if (type_2 == 0):
            enemyPoke = pd.read_csv(csv)
            en_agst1 = enemyPoke.loc[:,agt_type1]
            idx = enemy.pokedex_number - 1
            enemy.agst_type1 = en_agst1[idx]
            adj_atk1 = i.sp_attack *en_agst1[idx]
            space = '       '
            print(f'| {i.name.ljust(12)}  |  {i.sp_attack:12d} |  {i.sp_defense:12d} |  {i.hp:12d} |  {i.type1.ljust(12)} |  {space}      |  {int(adj_atk1):12d} |  {space}      |')
        else:
            agt_type2 = "against_" + type_2
            enemyPoke = pd.read_csv(csv)
            en_agst1 = enemyPoke.loc[:,agt_type1]
            en_agst2 = enemyPoke.loc[:,agt_type2]
            idx = enemy.pokedex_number - 1
            enemy.agst_type1 = en_agst1[idx]
            enemy.agst_type2 = en_agst2[idx]
            adj_atk1 = i.sp_attack *en_agst1[idx]
            adj_atk2 = i.sp_attack *en_agst2[idx]
            print(f'| {i.name.ljust(12)}  |  {i.sp_attack:12d} |  {i.sp_defense:12d} |  {i.hp:12d} |  {i.type1.ljust(12)} |  {i.type2}       |  {int(adj_atk1):12d} |  {int(adj_atk2):12d} |')

        print('| - - - - - - - | - - - - - - - | - - - - - - - | - - - - - - - | - - - - - - - | - - - - - - - | - - - - - - - | - - - - - - - |')
    print('|-------------------------------------------------------------------------------------------------------------------------------|')
    print('')


def displayEnemy(enemy):
    print('')
    print('|-----------------------------------------------------------------------------------------------|')
    print('| ENEMY POKEMON |     SP_ATK    |    SP_DEF     |       HP      |     TYPE 1    |     TYPE 2    |')
    print('|-----------------------------------------------------------------------------------------------|')
    print(f'| {enemy.name.ljust(12)}  |  {enemy.sp_attack:12d} |  {enemy.sp_defense:12d} |  {enemy.hp:12d} |  {enemy.type1.ljust(12)} |  {enemy.type2}       |')
    print('|-----------------------------------------------------------------------------------------------|')

        

def partyAttack(party,foe):
    if( len(party) == 1 ):

        curr = party[0]
        if(curr.type1 == 'fire'):
            inp = input(f'What will {curr.name} do?\nEmber\nFlamethrower\nFire Punch\n')
            atk = inp.casefold()
            if( atk == 'ember' or atk == 'flamethrower' or atk == 'fire punch' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                return enemyAttack(party,foe)
            else:
                print('Move does not exist. Try again\n')
                return partyAttack(party,foe)
        elif(curr.type1 == 'water'):
            inp = input(f'What will {curr.name} do?\nWatergun\nWhirlpool\nSurf\n')
            move = inp.split()
            if( len([move]) > 1 ):
                print('Choose Only One Move.\n')
                return partyAttack(party,foe)
            else:
                atk = inp.casefold()
                if( atk == 'watergun' or atk == 'whirlpool' or atk == 'surf' ):
                    print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                    foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                    print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                    if( foe.hp <= 10 ):
                        print('It\'s Super Effective!\n')
                        if( foe.hp <= 0 ):
                            print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                    return enemyAttack(party,foe)
                else:
                    print('Move Does Not Exist. Try Again\n')
                    return partyAttack(party,foe)
        elif(curr.type1 == 'grass'):
            inp = input(f'What will {curr.name} do?\nBullet Seed\nRazor Leaf\nBarrack Obama\n')
            atk = inp.casefold()
            if( atk == 'bullet seed' or atk == 'razor leaf' or atk == 'barrack obama' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                return enemyAttack(party,foe)
            else:
                print('Move Does Not Exist. Try Again\n')
                return partyAttack(party,foe)
        elif(curr.type1 == 'electric'):
            if( curr.name == 'Pikachu' ):
                print('Pikachu Is The Most Overrated Pokemon Ever.\n')
            inp = input(f'What will {curr.name} do?\nThunderbolt\nVolt Tackle\nThunder Punch\n')
            atk = inp.casefold()
            if( atk == 'thunderbolt' or atk == 'volt tackle' or atk == 'thunder punch' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                # Enemy's turn
                return enemyAttack(party,foe)
            else:
                print('Move doesn\'t exist. Try again\n')
                return partyAttack(party,foe)
        else:
            inp = input(f'What will {curr.name} do?\nHyperbeam\nSlam\nPound\n')
            atk = inp.casefold()
            if( atk == 'hyperbeam' or atk == 'slam' or atk == 'pound' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                # Enemy's turn
                return enemyAttack(party,foe)
            else:
                print('Move doesn\'t exist. try again\n')
                return partyAttack(party,foe)

    # More than 1 party member
    else:
        curr = party[0]
        if(curr.type1 == 'fire'):
            inp = input(f'What will {curr.name} do?\nEmber\nFlamethrower\nFire Punch\n')
            atk = inp.casefold()
            if( atk == 'ember' or atk == 'flamethrower' or atk == 'fire punch' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                return enemyAttack(party,foe)
            else:
                print('Move does not exist. Try again\n')
                return partyAttack(party,foe)
        elif(curr.type1 == 'water'):
            inp = input(f'What will {curr.name} do?\nWatergun\nWhirlpool\nSurf\n')
            move = inp.split()
            if( len([move]) > 1 ):
                print('Choose Only One Move.\n')
                return partyAttack(party,foe)
            else:
                atk = move.casefold()
                if( atk == 'watergun' or atk == 'whirlpool' or atk == 'surf' ):
                    print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                    foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                    print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                    if( foe.hp <= 10 ):
                        print('It\'s Super Effective!\n')
                        if( foe.hp <= 0 ):
                            print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                    return enemyAttack(party,foe)
                else:
                    print('Move Does Not Exist. Try Again\n')
                    return partyAttack(party,foe)
        elif(curr.type1 == 'grass'):
            inp = input(f'What will {curr.name} do?\nBullet Seed\nRazor Leaf\nBarrack Obama\n')
            atk = inp.casefold()
            if( atk == 'bullet seed' or atk == 'razor leaf' or atk == 'barrack obama' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                return enemyAttack(party,foe)
            else:
                print('Move Does Not Exist. Try Again\n')
                return partyAttack(party,foe)
        elif(curr.type1 == 'electric'):
            if( curr.name == 'Pikachu' ):
                print('Pikachu Is The Most Overrated Pokemon Ever.\n')
            inp = input(f'What will {curr.name} do?\nThunderbolt\nVolt Tackle\nThunder Punch\n')
            atk = inp.casefold()
            if( atk == 'thunderbolt' or atk == 'volt tackle' or atk == 'thunder punch' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                # Enemy's turn
                return enemyAttack(party,foe)
            else:
                print('Move doesn\'t exist. Try again\n')
                return partyAttack(party,foe)
        else:
            inp = input(f'What will {curr.name} do?\n Hyperbeam\n Slam\n Pound\n')
            atk = inp.casefold()
            if( atk == 'hyperbeam' or atk == 'slam' or atk == 'pound' ):
                print(f'{curr.name} used {atk.capitalize()} against {foe.name}!')
                foe.hp = foe.hp - (foe.sp_defense - curr.sp_attack)
                print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
                if( foe.hp <= 10 ):
                    print('It\'s Super Effective!\n')
                    if( foe.hp <= 0 ):
                        print(f'{foe.name} has fainted!\n')
                        print('Congratulations! You won!\n')
                        exit()
                # Enemy's turn
                return enemyAttack(party,foe)
            else:
                print('Move doesn\'t exist. try again\n')
                return partyAttack(party,foe)


def deque(party):
    size = len(party)
    if( size > 1 ):
        party.reverse()
        party.pop(size-1)
        party.reverse()
    else:
        print('You lost!\n')
        exit()


def enemyAttack(party,foe):
    
    # Only one party member
    if( len(party) == 1):
        
        curr = party[0]
        
        if(foe.type1 == 'fire'):
            moves = ['Flamethrower','Fire Punch','Ember']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    print(f'You lost!\n')
                    exit()
            return partyAttack(party,foe)
        elif(foe.type1 == 'water'):
            moves = ['Watergun','Whirlpool','Surf']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    print(f'You lost!\n')
                    exit()
            return partyAttack(party,foe)
        elif(foe.type1 == 'grass'):
            moves = ['Bullet Seed','Razor Leaf','Sword Dance']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    print(f'You lost!\n')
                    exit()
            return partyAttack(party,foe)
        elif(foe.type1 == 'electric'):
            moves = ['Thunderbolt','Volt Tackle','Thunder Punch']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    print(f'You lost!\n')
                    exit()
            return partyAttack(party,foe)
        else:
            moves = ['Hyperbeam','Solar Beam','Shadow Ball']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    print(f'You lost!\n')
                    exit()
            return partyAttack(party,foe)
    
    # More than one party member 
    else:

        curr = party[0]

        if(foe.type1 == 'fire'):
            moves = ['Flamethrower','Fire Punch','Ember']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    deque(party)
            partyAttack(party,foe)
        elif(foe.type1 == 'water'):
            moves = ['Watergun','Whirlpool','Surf']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    deque(party)
            partyAttack(party,foe)
        elif(foe.type1 == 'grass'):
            moves = ['Bullet Seed','Razor Leaf','Sword Dance']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    deque(party)
            partyAttack(party,foe)
        elif(foe.type1 == 'electric'):
            moves = ['Thunderbolt','Volt Tackle','Thunder Punch']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    deque(party)
            partyAttack(party,foe)
        else:
            moves = ['Hyperbeam','Solar Beam','Shadow Ball']
            idx = randint(0,len(moves)-1)
            print(f'{foe.name} attacked {curr.name} with {moves[idx]}!')
            curr.hp = curr.hp - (curr.sp_defense - foe.sp_attack)
            print(f'{curr.name} HP:  {curr.hp}    |    {foe.name} HP:  {foe.hp}\n')
            if( curr.hp <= 10 ):
                print('It\'s super effective!\n')
                if( curr.hp <= 0 ):
                    print(f'{curr.name} has fainted!\n')
                    deque(party)
            partyAttack(party,foe)


def fight(party,foe):
    if(len(party) == 1):
        curr = party[0]
        fast = max(curr.speed, foe.speed)
        chp = curr.hp
        fhp = foe.hp
        if(fast == curr.speed):
            partyAttack(party,foe)
        else:
            enemyAttack(party,foe)
    else:
        curr = party[0]
        fast = max(curr.speed, foe.speed)
        if( fast == curr.speed ):
            partyAttack(party,foe)
        else:
            enemyAttack(party,foe)




def choices(party,foe):
    print(f'Go {party[0].name}!\nWhat will {party[0].name} do?')
    inp = input(' Run\n Fight\n Bag\n ')

    if( len([inp]) > 1 ):
        print('Choose only one choice. Try again.\n')
        return choices(party,foe)
    else:
        choice = inp.casefold()
        # Running
        if(choice == 'run'):
            print(f'{party[0].name} ran away!')
            exit()
        # Bagging
        elif(choice == 'bag'):
            print(f'You threw a Pokeball!\n')
            print(f'You caught a {foe.name}!\n')
            exit()
        # Fighting 
        elif(choice == 'fight'):
            return fight(party,foe)
        else:
            print('Choice doesn\'t exist. Try again')
            return choices(party,foe)

def main():

    currDir = os.getcwd()
    csv = currDir + "/pokemon.csv"

    if( os.path.exists(csv) ):
        
        # Part 1 Select Pokemon
        party = getParty()
        enemy = getEnemy()

        print(len(party))
       
        # Part 2 Display
        displayParty(party,enemy)
        displayEnemy(enemy)

        # # Part 3 Choices
        choices(party,enemy)

    else:
        print("Please add a pokemon.csv file.")
        exit()
    

if __name__ == "__main__":
    main()

