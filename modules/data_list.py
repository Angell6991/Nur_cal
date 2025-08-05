import  pandas  as  pd
import  os

############################################################
###-------------------New_list_data----------------------###
############################################################
def new_list(dir, name_list, name_players, data_list):
    
    ###----------Created_directory_and_add_data--------------###
    directory   =   {}
    
    directory["Player"]     =   ["Life", "Damage", "Dodge", "Attack", "Dices"]
    
    for i   in  range(len(name_players)):
        directory[name_players[i]]  =   data_list[i]  

    ###--------Creando_tabla_atravez_del_derectorio----------###
    tabla   =   pd.DataFrame(directory)

    ###-------------------Cal_promedio-----------------------###
    tabla["Promedio"] = tabla.iloc[:, 1:].mean(axis=1)  # evita la columna "Player"
    tabla["Promedio"]   =   tabla['Promedio'].round().astype(int)

    ###-------------------Guardar_tabla----------------------###
    tabla.to_csv(f"{dir}/{name_list}.dat", sep=' ', index=True)

    return  tabla


############################################################
###-----------------Remove_list_data---------------------###
############################################################
def remove_list(dir, name_list):
    return  os.remove(f"{dir}/{name_list}.dat")


############################################################
###-----------------Edit_one_atribut---------------------###
############################################################
def edit_player(dir, name_list, name_player, atribut, value):

    ###------------------Import_data_list--------------------###
    tabla   =   pd.read_csv(f"{dir}/{name_list}.dat", sep=r"\s+").set_index("Player")
    
    ###---------------Eliminar_colum_promedio----------------###
    tabla.drop(columns=["Promedio"], inplace=True)

    ###-------------------Edit_atribut-----------------------###
    tabla.loc[f"{atribut}", f"{name_player}"]   =   value

    ###-------------------Cal_promedio-----------------------###
    tabla["Promedio"]   =   tabla.mean(axis=1)
    tabla["Promedio"]   =   tabla['Promedio'].round().astype(int)

    ###-------------------Guardar_tabla----------------------###
    tabla.to_csv(f"{dir}/{name_list}.dat", sep=' ', index=True)

    return  tabla


############################################################
###-------------------Agregar_player---------------------###
############################################################
def add_player(dir, name_list, name_player, list_data):

    ###------------------Import_data_list--------------------###
    tabla   =   pd.read_csv(f"{dir}/{name_list}.dat", sep=r"\s+").set_index("Player")
    
    ###---------------Eliminar_colum_promedio----------------###
    tabla.drop(columns=["Promedio"], inplace=True)

    ###------------------Add_new_player----------------------###
    tabla[f"{name_player}"]   =  list_data
    
    ###-------------------Cal_promedio-----------------------###
    tabla["Promedio"]   =   tabla.mean(axis=1)
    tabla["Promedio"]   =   tabla['Promedio'].round().astype(int)

    ###-------------------Guardar_tabla----------------------###
    tabla.to_csv(f"{dir}/{name_list}.dat", sep=' ', index=True)
    
    return  tabla


############################################################
###-------------------Eliminar_player--------------------###
############################################################
def remove_player(dir, name_list, name_player):

    ###------------------Import_data_list--------------------###
    tabla   =   pd.read_csv(f"{dir}/{name_list}.dat", sep=r"\s+").set_index("Player")
    
    ###----------Eliminar_colum_promedio_and_player----------###
    tabla.drop(columns=["Promedio"], inplace=True)
    tabla.drop(columns=[f"{name_player}"], inplace=True)

    ###-------------------Cal_promedio-----------------------###
    tabla["Promedio"]   =   tabla.mean(axis=1)
    tabla["Promedio"]   =   tabla['Promedio'].round().astype(int)

    ###-------------------Guardar_tabla----------------------###
    tabla.to_csv(f"{dir}/{name_list}.dat", sep=' ', index=True)
    
    return  tabla


############################################################
###-------------------Texting_pogram---------------------###
############################################################
# directory =   "list"
# new_list(directory, "prueva", ["carlos", "sandra"], [[1,2,3,4,5], [5,4,3,2,1]])
# add_player(directory, "grup_02", "sara", [2,2,2,2,2])
# edit_player(directory, "grup_02", "sara", "Life", 200)
# remove_player(directory, "grup_02", "luis")
# remove_list(directory, "grup_02")


