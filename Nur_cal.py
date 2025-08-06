import  InquirerPy.inquirer as  inp
import  pyfiglet    as    pf
import  subprocess
import  os

os.system("clear")

list_selection  =   ["edit groups", "1 vs 1","exit"]
selection       =   "empty"

while   selection   !=  "exit":

    print(pf.figlet_format("Nur cal"))

    selection   =   inp.select(
                        message="Select menu: ",
                        instruction="Press enter for contiue",
                        choices=list_selection
                    ).execute()

    if  selection   ==  "edit groups":
        subprocess.run(['python', 'edit_list.py'])

    elif  selection   ==  "1 vs 1":
        subprocess.run(['python', '1_vs_1.py'])


os.system("clear")

