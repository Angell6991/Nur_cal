import  modules.probability as  pb  
import  modules.graph   as  plt
import  pandas  as  pd
import  numpy   as  np


###------------------------Def_name_data---------------------------###

name_player_01  =   "carlos"
name_player_02  =   "amanda"
name_table_data =   "list_grups.xlsx"
name_sheet      =   "grup lunes"    

###----------------------Import_data_list--------------------------###

# name_sheet_list = pd.ExcelFile(str(name_table_data)).sheet_names

tabla       =   pd.read_excel(str(name_table_data), sheet_name=str(name_sheet))
player_01   =   np.array(tabla[f"{name_player_01}"])
player_02   =   np.array(tabla[f"{name_player_02}"])

prob    =   pb.probability(player_01, player_02)

print(tabla)

plt.plot( 
     name_player_01, name_player_02,
     prob.probability_kill_1, prob.probability_kill_2,
     prob.probability_attack_1_true, prob.probability_attack_2_true,
     prob.probability_attack_1_relaunch, prob.probability_attack_2_relaunch,
     prob.list_unique_1, prob.list_unique_2,
     prob.list_probability_die_1, prob.list_probability_die_2
)




