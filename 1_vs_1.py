import  modules.probability as  pb  
import  modules.graph   as  plt

import  InquirerPy.inquirer as  inp
import  pandas  as  pd
import  numpy   as  np
import  os 

os.system("clear")

name_table_data =   "list_grups.xlsx"
name_sheet_list =   pd.ExcelFile(str(name_table_data)).sheet_names

###-----------------------Select_grup_01---------------------------###
select_grup_01  =   inp.select(
                        message="seletc grup 1: ",
                        choices=name_sheet_list
                    ).execute()

###-----------------------Select_grup_02---------------------------###
select_grup_02  =   inp.select(
                        message="seletc grup 2: ",
                        choices=name_sheet_list
                    ).execute()

###----------------------Import_data_list--------------------------###
tabla_01        =   pd.read_excel(str(name_table_data), sheet_name=str(select_grup_01))
tabla_02        =   pd.read_excel(str(name_table_data), sheet_name=str(select_grup_02))

list_players_01 =   tabla_01.columns.to_numpy()
list_players_01 =   list_players_01[1:]

list_players_02 =   tabla_02.columns.to_numpy()
list_players_02 =   list_players_02[1:]

###----------------------Select_player_01--------------------------###
name_player_01  =   inp.select(
                        message="seletc player 1: ",
                        choices=list_players_01
                    ).execute()

###----------------------Select_player_01--------------------------###
name_player_02  =   inp.select(
                        message="seletc player 2: ",
                        choices=list_players_02
                    ).execute()

###--------------------------Init_cal------------------------------###
player_01   =   np.array(tabla_01[f"{name_player_01}"])
player_02   =   np.array(tabla_02[f"{name_player_02}"])

prob    =   pb.probability(player_01, player_02)

plt.plot( 
     name_player_01, name_player_02,
     prob.probability_kill_1, prob.probability_kill_2,
     prob.probability_attack_1_true, prob.probability_attack_2_true,
     prob.probability_attack_1_relaunch, prob.probability_attack_2_relaunch,
     prob.list_unique_1, prob.list_unique_2,
     prob.list_probability_die_1, prob.list_probability_die_2
)


