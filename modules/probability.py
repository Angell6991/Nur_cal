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
number_dices_player_2          =  player_02[4]

Dices_3D6   =   list( range(3, 19) )
Dices_N1D6  =   list( range(number_dices_player_1, 6*number_dices_player_1 + 1) )
Dices_N2D6  =   list( range(number_dices_player_2, 6*number_dices_player_2 + 1) )


###------------------------Attack_phase----------------------------###
net_attack_1    =   player_01[3]    +   Dices_3D6
net_attack_2    =   player_02[3]    +   Dices_3D6
net_dodge_1     =   player_01[2]    +   Dices_3D6
net_dodge_2     =   player_02[2]    +   Dices_3D6

attack_1_true       =   0
attack_1_false      =   0
attack_1_relaunch   =   0

attack_2_true       =   0
attack_2_false      =   0
attack_2_relaunch   =   0

for i   in  range(len(Dices_3D6)):
    for j   in  range(len(Dices_3D6)):
        
        ###--------player_01_attack_player_02_dodge---------###
        if  net_attack_1[i]     >   net_dodge_2[j]:
            attack_1_true       =   attack_1_true       +   1

        elif net_attack_1[i]    <   net_dodge_2[j]:
            attack_1_false      =   attack_1_false      +   1

        elif net_attack_1[i]    ==  net_dodge_2[j]:
            attack_1_relaunch   =   attack_1_relaunch   +   1

        ###--------player_02_attack_player_01_dodge---------###
        if  net_attack_2[i]     >   net_dodge_1[j]:
            attack_2_true       =   attack_2_true       +   1

        elif net_attack_2[i]    <   net_dodge_1[j]:
            attack_2_false      =   attack_2_false      +   1

        elif net_attack_2[i]    ==  net_dodge_1[j]:
            attack_2_relaunch   =   attack_2_relaunch   +   1

posibilitys_of_the_attack_1     =   attack_1_true       +   attack_1_false    +   attack_1_relaunch
posibilitys_of_the_attack_2     =   attack_2_true       +   attack_2_false    +   attack_2_relaunch


###----------------------Probaility_attack-------------------------###
probability_attack_1_true        =   round(attack_1_true/posibilitys_of_the_attack_1, 4)
probability_attack_1_relaunch    =   round(attack_1_relaunch/posibilitys_of_the_attack_1, 4)
probability_attack_2_true        =   round(attack_2_true/posibilitys_of_the_attack_2, 4)
probability_attack_2_relaunch    =   round(attack_2_relaunch/posibilitys_of_the_attack_2, 4)


###-----------------------Probaility_kill--------------------------###
life_1_kill     =   (5*number_dices_player_2 + 1)*attack_2_true
life_2_kill     =   (5*number_dices_player_1 + 1)*attack_1_true   

posibilitys_kill_net    =   life_1_kill     +   life_2_kill

probability_kill_1      =   round(life_1_kill/posibilitys_kill_net, 4)
probability_kill_2      =   round(life_2_kill/posibilitys_kill_net, 4)


###------------------number_of_meetings_to_die---------------------###
net_damage_1    =   player_01[1]    +   Dices_N1D6
net_damage_2    =   player_02[1]    +   Dices_N2D6

life_init_1     =   player_01[0]
life_init_2     =   player_02[0]

list_die_1              =   np.array([
                                (life_init_1 // net_damage_2[i] if life_init_1 % net_damage_2[i] == 0  
                                    else (life_init_1 // net_damage_2[i] + 1))
                                for i in range(len(net_damage_2))
                            ])

list_die_2              =   np.array([
                                (life_init_2 // net_damage_1[i] if life_init_2 % net_damage_1[i] == 0  
                                    else (life_init_2 // net_damage_1[i] + 1))
                                for i in range(len(net_damage_1))
                            ])

list_unique_1           =   np.unique(list_die_1)
list_unique_2           =   np.unique(list_die_2)
list_frequency_list_1   =   np.array([ np.count_nonzero(list_die_1 == i) for i in list_unique_1 ])
list_frequency_list_2   =   np.array([ np.count_nonzero(list_die_2 == i) for i in list_unique_2 ])

list_probability_die_1  =   np.array([ 
                                round(list_frequency_list_1[i]/len(list_die_1) ,4)
                                for i in range(len(list_frequency_list_1)) 
                            ])

list_probability_die_2  =   np.array([ 
                                round(list_frequency_list_2[i]/len(list_die_2), 4) 
                                for i in range(len(list_frequency_list_2)) 
                            ])


######################################################################
###------------------------Texting_program-------------------------###
######################################################################
print(str(tabla) + "\n")

print(f"Probability kill {name_player_01}: {probability_kill_1}")
print(f"Probabilidad attack true: {probability_attack_1_true} y relanzar: {probability_attack_1_relaunch}")
print(f"Todos los posibles golpes para matar á {name_player_01}: {list_die_1}")
print(f"Golpes para matar á {name_player_01}: {list_unique_1}")
print(f"Probabildad de matarlo con esa cantidad de golpes: \n {list_probability_die_1} \n")

print(f"Probability kill {name_player_02}: {probability_kill_2}")
print(f"Probabilidad attack true: {probability_attack_2_true} y relanzar: {probability_attack_2_relaunch}")
print(f"Todos los posibles golpes para matar á {name_player_02}: {list_die_2}")
print(f"Golpes para matar á {name_player_02}: {list_unique_2}")
print(f"Probabildad de matarlo con esa cantidad de golpes: \n {list_probability_die_2} \n")

