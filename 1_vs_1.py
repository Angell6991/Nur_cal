import  modules.probability as  pb  
import  modules.graph   as  plt

import  InquirerPy.inquirer as  inp
import  pandas  as  pd
import  numpy   as  np
import  os 

os.system("clear")
######################################################################
###---------------------Init_loop_while----------------------------###
######################################################################
list_option =   ["Calculate 1 vs 1", "back"]
selection   =   "empty"

while   selection   !=  "back":
    
    ###---------------Selection_for_back_1_vs_1------------------------###
    selection   =   inp.select(
                            message="Select an action: ",
                            choices=list_option
                        ).execute()
    
    if  selection   !=  "back":
        os.system("clear")

        ######################################################################
        ###---------------------Import_grup_data---------------------------###
        ######################################################################
        list_directoriy = os.listdir("modules/list/")
        list_directoriy = [filename.replace(".dat", "") for filename in list_directoriy]


        ######################################################################
        ###-----------------------Select_grup_01---------------------------###
        ######################################################################
        select_grup_01  =   inp.select(
                                message="select grup 1: ",
                                choices=list_directoriy
                            ).execute()

        tabla_01        =   pd.read_csv(f"modules/list/{select_grup_01}.dat", sep=r"\s+").set_index("Player")

        ###----------------------Select_player_01--------------------------###
        name_player_01  =   inp.select(
                                message="select player: ",
                                choices=tabla_01
                            ).execute()

        print(" ")
        ######################################################################
        ###-----------------------Select_grup_02---------------------------###
        ######################################################################
        select_grup_02  =   inp.select(
                                message="select grup 2: ",
                                choices=list_directoriy
                            ).execute()

        tabla_02        =   pd.read_csv(f"modules/list/{select_grup_02}.dat", sep=r"\s+").set_index("Player")

        ###----------------------Select_player_02--------------------------###
        name_player_02  =   inp.select(
                                message="select player: ",
                                choices=tabla_02
                            ).execute()


        ######################################################################
        ###--------------------------Init_cal------------------------------###
        ######################################################################
        player_01   =   np.array(tabla_01[f"{name_player_01}"])
        player_02   =   np.array(tabla_02[f"{name_player_02}"])

        prob    =   pb.probability(player_01, player_02)


        ######################################################################
        ###-------------------------Viw_result-----------------------------###
        ######################################################################
        os.system("clear")

        plt.plot( 
            name_player_01,
            prob.probability_kill_1,
            prob.probability_attack_1_true,
            prob.probability_attack_1_relaunch,
            prob.list_unique_1,
            prob.list_probability_die_1,
        )
        print(
            "Life "     + str(player_01[0]) + " || "  +
            "Damage "   + str(player_01[1]) + " || "  +
            "Dodge "    + str(player_01[2]) + " || "  +
            "Attack "   + str(player_01[3]) + " || "  +
            "Dices "    + str(player_01[4])
        )


        plt.plot( 
            name_player_02,
            prob.probability_kill_2,
            prob.probability_attack_2_true,
            prob.probability_attack_2_relaunch,
            prob.list_unique_2,
            prob.list_probability_die_2,
        )
        print(
            "Life "     + str(player_02[0]) + " || "  +
            "Damage "   + str(player_02[1]) + " || "  +
            "Dodge "    + str(player_02[2]) + " || "  +
            "Attack "   + str(player_02[3]) + " || "  +
            "Dices "    + str(player_02[4]) + "\n"
        )
        

os.system("clear")


