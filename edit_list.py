import  modules.data_list   as  data

import  InquirerPy.inquirer as  inp
import  os 


os.system("clear")


######################################################################
###----------------------------------------------------------------###
######################################################################

list_option =   ["hola", "saludo", "back"]
selection   =   "empty"

while   selection   !=  "back":
    selection   =   inp.select(
                            message="select option: ",
                            choices=list_option
                        ).execute()

