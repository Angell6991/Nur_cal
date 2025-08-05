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
           
            print("")
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
        
        print("hola")


os.system("clear")





