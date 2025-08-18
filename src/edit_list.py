import  modules.data_list   as  data

import  InquirerPy.inquirer as  inp
import  pandas  as  pd
import  os 


os.system("clear")

direct  =   "modules/list"

######################################################################
###---------------------Init_loop_while----------------------------###
######################################################################

list_option =   ["View grup", "New group", "Delete group", "Edit player", "Add player", "Remove player", "Back"]
selection   =   "empty"

while   selection   !=  "Back":

    ###------------Selection_for_init_actions_grups--------------------###
    selection   =   inp.select(
                            message="select option: ",
                            choices=list_option
                    ).execute()

    ###--------------------View_list_grup------------------------------###
    if  selection   ==  "View grup":
        
        list_directoriy =   os.listdir(direct)
        list_directoriy =   [filename.replace(".dat", "") for filename in list_directoriy]

        view_grup       =   inp.select(
                                message="Select the group to see: ",
                                instruction="Press to Enter view grup",
                                choices=list_directoriy
                            ).execute()
        
        print(
            str("\n")    +
            str(pd.read_csv(f"{direct}/{view_grup}.dat", sep=r"\s+").to_markdown(index=False))  +
            str("\n")
        )

    ###----------------------Add_new_grup------------------------------###
    elif  selection   ==  "New group":

        question        =   inp.confirm(
                                message="Do you want to continue?",
                                default=True  
                            ).execute()

        if  question:
            name_new_grup   =   str(input("Enter the name of the new group: "))
            number_players  =   int(input("Number of players in the group: "))
            
            name_list   =   []
            data_list   =   []
            
            for i   in  range(number_players):
                
                print(str("\n") + str("----------------------"))
                name_list.append(str(input(f"Intro name player {i+1}: ")))
                
                atribut_list    =   ["Life", "Damage", "Dodge", "Attack", "Dices"]
                atribut_list[0] =   int(input(" ** Life: "))
                atribut_list[1] =   int(input(" ** Damege: "))
                atribut_list[2] =   int(input(" ** Dodge: "))
                atribut_list[3] =   int(input(" ** Attack: "))
                atribut_list[4] =   int(input(" ** Dices: "))
                data_list.append(atribut_list)
           
            data.new_list(direct, name_new_grup, name_list, data_list)
        
        os.system("clear")

    ###-----------------------Delete_grup------------------------------###
    elif  selection   ==  "Delete group":

        list_directoriy =   os.listdir(direct)
        list_directoriy =   [filename.replace(".dat", "") for filename in list_directoriy]

        view_grup       =   inp.checkbox(
                                message="Select the groups you want to eliminate: ",
                                choices=list_directoriy,
                                instruction=" To select click space and to continue press Enter",
                            ).execute()

        question        =   inp.confirm(
                                message="Do you want to continue delete grups?",
                                default=True  
                            ).execute()

        if  question:
            for i   in  range(len(view_grup)):
                data.remove_list(direct, view_grup[i])

        os.system("clear")

    ###-----------------------Edit_player------------------------------###
    elif  selection   ==  "Edit player":
       
        os.system("clear")
        list_directoriy =   os.listdir(direct)
        list_directoriy =   [filename.replace(".dat", "") for filename in list_directoriy]

        view_grup       =   inp.select(
                                message="Select the group to edit: ",
                                instruction="Press to Enter for select",
                                choices=list_directoriy
                            ).execute()
        
        edit_grup       =   pd.read_csv(f"{direct}/{view_grup}.dat", sep=r"\s+")
        print(str("\n") + str(edit_grup.to_markdown(index=False))  + str("\n"))

        select_player   =   inp.select(
                                message="Select the player to edit: ",
                                instruction="Press to Enter for select",
                                choices=edit_grup.set_index("Player")
                            ).execute()

        select_atribut  =   inp.select(
                                message="Select the player to edit: ",
                                instruction="Press to Enter for select",
                                choices=["Life", "Damage", "Dodge", "Attack", "Dices"]
                                ).execute()

        new_value       =   int(input(f"Introduc new {select_atribut}: "))

        question        =   inp.confirm(
                                message="Save changes?",
                                default=True  
                            ).execute()

        if  question:
            data.edit_player(direct, view_grup, select_player, select_atribut, new_value)

            print(
                str("\n") + 
                str(pd.read_csv(f"{direct}/{view_grup}.dat", sep=r"\s+").to_markdown(index=False))  + 
                str("\n")
            )

    ###---------------Add_new_player_in_grups--------------------------###
    elif  selection   ==  "Add player":
        
        question        =   inp.confirm(
                                message="Do you want to continue?",
                                default=True  
                            ).execute()

        if  question:
            
            list_directoriy =   os.listdir(direct)
            list_directoriy =   [filename.replace(".dat", "") for filename in list_directoriy]

            view_grup       =   inp.select(
                                    message="Select the group to edit: ",
                                    instruction="Press to Enter for select",
                                    choices=list_directoriy
                                ).execute()

            name_new_player     =   str(input("Enter the name of the new player: "))
            atribut_list        =   []
            list_name_atribut   =   ["Life", "Damage", "Dodge", "Attack", "Dices"]
            
            for i   in range(len(list_name_atribut)):
                atribut_list.append(int(input(f" ** {list_name_atribut[i]}: ")))
            
            data.add_player(direct, view_grup, name_new_player, atribut_list)

            print(
                str("\n") + 
                str(pd.read_csv(f"{direct}/{view_grup}.dat", sep=r"\s+").to_markdown(index=False))  + 
                str("\n")
            )

    ###---------------Remove_players_in_grup---------------------------###
    elif  selection   ==  "Remove player":

        list_directoriy =   os.listdir(direct)
        list_directoriy =   [filename.replace(".dat", "") for filename in list_directoriy]

        view_grup       =   inp.select(
                                    message="Select the group to edit: ",
                                    instruction="Press to Enter for select",
                                    choices=list_directoriy
                                ).execute()

        edit_grup       =   pd.read_csv(f"{direct}/{view_grup}.dat", sep=r"\s+")

        player_delete   =   inp.checkbox(
                                message="Select the group to edit: ",
                                choices=edit_grup.set_index("Player"),
                                instruction=" To select click space and to continue press Enter",
                            ).execute()

        question        =   inp.confirm(
                                message="Do you want to continue delete players?",
                                default=True  
                            ).execute()

        if  question:
            for i   in  range(len(player_delete)):
                data.remove_player(direct, view_grup, player_delete[i])

            print(
                str("\n") + 
                str(pd.read_csv(f"{direct}/{view_grup}.dat", sep=r"\s+").to_markdown(index=False))  + 
                str("\n")
            )

os.system("clear")


