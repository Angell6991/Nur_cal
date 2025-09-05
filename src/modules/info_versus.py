import  modules.probability   as  prob

import  flet    as  ft
import  matplotlib
import  matplotlib.pyplot   as  plt

from    flet.matplotlib_chart   import  MatplotlibChart

matplotlib.use("svg")

######################################################################
###---------------------Groups_menu_flet---------------------------###
######################################################################
class   info_versus:

    def __init__(self, color, font, direct_groups, direct_img):
        self.page   =   None
        self.color  =   color
        self.font   =   font
        self.direct_img =   direct_img
        self.direct_groups  =   direct_groups

    ######################################################################
    ###-------------------Definitions_functions------------------------###
    ######################################################################

    ###---------------------------Graph--------------------------------###
    def graph(self, name_group, name_player, die_list, probability_list):
        fig, ax = plt.subplots()

        x_label = die_list
        y_label = probability_list

        ax.barh(x_label, y_label, color=self.color[4], height=0.4)

        fig.patch.set_facecolor(self.color[1])
        ax.set_axisbelow(True)
        ax.grid(axis="x", linestyle="--", color=self.color[3], alpha=0.7)
        ax.set_xlabel("Probability %", color=self.color[3], size=15)
        ax.set_xticks(y_label)
        ax.set_ylabel("Number of blows to die", color=self.color[3], size=15)
        ax.set_title(f"{name_group}: {name_player}", color=self.color[3], size=25)
        ax.tick_params(axis="x", colors=self.color[3], labelsize=12, rotation=45)
        ax.tick_params(axis="y", colors=self.color[3], labelsize=12, rotation=45)
        ax.set_facecolor(self.color[0])

        fig.tight_layout()
        
        return  MatplotlibChart(fig, expand=True)



# import flet as ft


# def main(page: ft.Page):
#     def button_clicked(e):
#         t.value = f"Dropdown value is:  {dd.value}"
#         page.update()

#     t = ft.Text()
#     b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
#     dd = ft.DropdownM2(
#         width=100,
#         options=[
#             ft.dropdownm2.Option("Red"),
#             ft.dropdownm2.Option("Green"),
#             ft.dropdownm2.Option("Blue"),
#         ],
#     )
#     page.add(dd, b, t)


# ft.app(main)


