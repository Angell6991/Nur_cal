import  numpy   as  np

######################################################################
###------------------Created_class_probability---------------------###
######################################################################
class   probability:

    def __init__(self, player_01, player_02):

        ###------------------------Number_dices----------------------------###
        self.number_dices_player_1          =  player_01[4] 
        self.number_dices_player_2          =  player_02[4]

        self.Dices_3D6   =   list( range(3, 19) )
        self.Dices_N1D6  =   list( range(self.number_dices_player_1, 6*self.number_dices_player_1 + 1) )
        self.Dices_N2D6  =   list( range(self.number_dices_player_2, 6*self.number_dices_player_2 + 1) )


        ###------------------------Attack_phase----------------------------###
        self.net_attack_1    =   player_01[3]    +   self.Dices_3D6
        self.net_attack_2    =   player_02[3]    +   self.Dices_3D6
        self.net_dodge_1     =   player_01[2]    +   self.Dices_3D6
        self.net_dodge_2     =   player_02[2]    +   self.Dices_3D6

        self.attack_1_true       =   0
        self.attack_1_false      =   0
        self.attack_1_relaunch   =   0

        self.attack_2_true       =   0
        self.attack_2_false      =   0
        self.attack_2_relaunch   =   0

        for i   in  range(len(self.Dices_3D6)):
            for j   in  range(len(self.Dices_3D6)):
                
                ###--------player_01_attack_player_02_dodge---------###
                if  self.net_attack_1[i]     >   self.net_dodge_2[j]:
                    self.attack_1_true       =   self.attack_1_true       +   1

                elif self.net_attack_1[i]    <   self.net_dodge_2[j]:
                    self.attack_1_false      =   self.attack_1_false      +   1

                elif self.net_attack_1[i]    ==  self.net_dodge_2[j]:
                    self.attack_1_relaunch   =   self.attack_1_relaunch   +   1

                ###--------player_02_attack_player_01_dodge---------###
                if  self.net_attack_2[i]     >   self.net_dodge_1[j]:
                    self.attack_2_true       =   self.attack_2_true       +   1

                elif self.net_attack_2[i]    <   self.net_dodge_1[j]:
                    self.attack_2_false      =   self.attack_2_false      +   1

                elif self.net_attack_2[i]    ==  self.net_dodge_1[j]:
                    self.attack_2_relaunch   =   self.attack_2_relaunch   +   1

        self.posibilitys_of_the_attack_1     =   self.attack_1_true       +   self.attack_1_false    +   self.attack_1_relaunch
        self.posibilitys_of_the_attack_2     =   self.attack_2_true       +   self.attack_2_false    +   self.attack_2_relaunch


        ###----------------------Probaility_attack-------------------------###
        self.probability_attack_1_true        =   round(self.attack_1_true/self.posibilitys_of_the_attack_1, 4)
        self.probability_attack_1_relaunch    =   round(self.attack_1_relaunch/self.posibilitys_of_the_attack_1, 4)
        self.probability_attack_2_true        =   round(self.attack_2_true/self.posibilitys_of_the_attack_2, 4)
        self.probability_attack_2_relaunch    =   round(self.attack_2_relaunch/self.posibilitys_of_the_attack_2, 4)


        ###-----------------------Probaility_kill--------------------------###
        self.life_1_kill     =   (5*self.number_dices_player_2 + 1)*self.attack_2_true
        self.life_2_kill     =   (5*self.number_dices_player_1 + 1)*self.attack_1_true   

        self.posibilitys_kill_net    =   self.life_1_kill     +   self.life_2_kill

        self.probability_kill_1      =   round(self.life_1_kill/self.posibilitys_kill_net, 4)
        self.probability_kill_2      =   round(self.life_2_kill/self.posibilitys_kill_net, 4)


        ###------------------number_of_meetings_to_die---------------------###
        self.net_damage_1    =   player_01[1]    +   self.Dices_N1D6
        self.net_damage_2    =   player_02[1]    +   self.Dices_N2D6

        self.life_init_1     =   player_01[0]
        self.life_init_2     =   player_02[0]

        self.list_die_1              =   np.array([
                                        (self.life_init_1 // self.net_damage_2[i] if self.life_init_1 % self.net_damage_2[i] == 0  
                                            else (self.life_init_1 // self.net_damage_2[i] + 1))
                                        for i in range(len(self.net_damage_2))
                                    ])

        self.list_die_2              =   np.array([
                                        (self.life_init_2 // self.net_damage_1[i] if self.life_init_2 % self.net_damage_1[i] == 0  
                                            else (self.life_init_2 // self.net_damage_1[i] + 1))
                                        for i in range(len(self.net_damage_1))
                                    ])

        self.list_unique_1           =   np.unique(self.list_die_1)
        self.list_unique_2           =   np.unique(self.list_die_2)
        self.list_frequency_list_1   =   np.array([ np.count_nonzero(self.list_die_1 == i) for i in self.list_unique_1 ])
        self.list_frequency_list_2   =   np.array([ np.count_nonzero(self.list_die_2 == i) for i in self.list_unique_2 ])

        self.list_probability_die_1  =   np.array([ 
                                        round(self.list_frequency_list_1[i]/len(self.list_die_1) ,4)
                                        for i in range(len(self.list_frequency_list_1)) 
                                    ])

        self.list_probability_die_2  =   np.array([ 
                                        round(self.list_frequency_list_2[i]/len(self.list_die_2), 4) 
                                        for i in range(len(self.list_frequency_list_2)) 
                                    ])



######################################################################
###------------------------Texting_program-------------------------###
######################################################################
# import  pandas  as  pd

# name_player_01     =   "Andres"
# name_player_02     =   "Carmen"

###----------------------Import_data_list--------------------------###
# tabla       =   pd.read_csv(str("list_players.dat"), sep=r"\s+")
# player_01   =   np.array(tabla[f"{name_player_01}"])
# player_02   =   np.array(tabla[f"{name_player_02}"])

###---------------------Instanciando_objeto------------------------###
# pb  =   probability(player_01, player_02)

###------------------------print_result----------------------------###
# print(str(tabla) + "\n")

# print(f"Probability kill {name_player_01}: {pb.probability_kill_1}")
# print(f"Probabilidad attack true: {pb.probability_attack_1_true} y relanzar: {pb.probability_attack_1_relaunch}")
# print(f"Todos los posibles golpes para matar á {name_player_01}: {pb.list_die_1}")
# print(f"Golpes para matar á {name_player_01}: {pb.list_unique_1}")
# print(f"Probabildad de matarlo con esa cantidad de golpes: \n {pb.list_probability_die_1} \n")

# print(f"Probability kill {name_player_02}: {pb.probability_kill_2}")
# print(f"Probabilidad attack true: {pb.probability_attack_2_true} y relanzar: {pb.probability_attack_2_relaunch}")
# print(f"Todos los posibles golpes para matar á {name_player_02}: {pb.list_die_2}")
# print(f"Golpes para matar á {name_player_02}: {pb.list_unique_2}")
# print(f"Probabildad de matarlo con esa cantidad de golpes: \n {pb.list_probability_die_2} \n")

