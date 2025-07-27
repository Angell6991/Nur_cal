import  pandas  as  pd
import  numpy   as  np

name_player_01     =   "Andres"
name_player_02     =   "Carmen"


######################################################################
###----------------------Import_data_list--------------------------###
######################################################################
tabla       =   pd.read_csv(str("list_players.dat"), sep=r"\s+")
player_01   =   np.array(tabla[f"{name_player_01}"])
player_02   =   np.array(tabla[f"{name_player_02}"])


###------------------------Number_dices----------------------------###
number_dices_player_1          =  player_01[4] 
# number_dices_player_2          =  player_02[4]

Dices_3D6   =   list( range(3, 19) )
Dices_N1D6  =   list( range(number_dices_player_1, 6*number_dices_player_1 + 1) )
# Dices_N2D6  =   list( range(number_dices_player_2, 6*number_dices_player_2 + 1) )


###----------------------Player_01_attack--------------------------###
net_attack_1    =   player_01[3]    +   Dices_3D6
net_dodge_2     =   player_02[2]    +   Dices_3D6

attack_1_true       =   0
attack_1_false      =   0
attack_1_relaunch   =   0

for i   in  range(len(net_attack_1)):
    for j   in  range(len(net_dodge_2)):
        
        if  net_attack_1[i]     >   net_dodge_2[j]:
            attack_1_true       =   attack_1_true       +   1

        elif net_attack_1[i]    <   net_dodge_2[j]:
            attack_1_false      =   attack_1_false      +   1

        elif net_attack_1[i]    ==  net_dodge_2[j]:
            attack_1_relaunch   =   attack_1_relaunch   +   1

posibilitys_of_the_attack_1     =   attack_1_true       +   attack_1_false    +   attack_1_relaunch


###-----------------Probaility_player_01_attack--------------------###
probability_attack_1_true        =   round(attack_1_true/posibilitys_of_the_attack_1, 4)
probability_attack_1_false       =   round(attack_1_false/posibilitys_of_the_attack_1, 4)
probability_attack_1_relaunch    =   round(attack_1_relaunch/posibilitys_of_the_attack_1, 4)


###------------------------Player_01_win---------------------------###
net_damge_1     =   player_01[1]    +   Dices_N1D6

rounds_kill_player_2    =   np.array([ player_02[0]/net_damge_1[i] for i in range(len(net_damge_1))])

life_2_kill         =   len(rounds_kill_player_2)*attack_1_true
life_2_no_kill      =   attack_1_false  +   attack_1_relaunch
posibilitys_life    =   life_2_kill     +   life_2_no_kill

###------------------Probaility_player_01_win----------------------###
probability_win_1   =   round(life_2_kill/posibilitys_life, 4)



######################################################################
###------------------------Texting_program-------------------------###
######################################################################
print(tabla)
print(probability_attack_1_true)
print(probability_win_1)

