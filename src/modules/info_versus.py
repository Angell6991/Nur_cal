from numpy import size
import  modules.probability   as  prob

import  flet    as  ft
import  pandas  as  pd
import  matplotlib
import  matplotlib.pyplot   as  plt
import  os

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

    ###------------------------input_group-----------------------------###
    def input_group(self, label):
        
        lista   =   os.listdir(self.direct_groups)
        lista   =   [filename.replace(".dat", "") for filename in lista]    

        intro   =   ft.DropdownM2(
            bgcolor=self.color[1],
            border_color=self.color[1],
            border_radius=15,
            color=self.color[6],
            label=str(label),
            label_style=ft.TextStyle(color=self.color[4], font_family=self.font[1], size=18),
            text_style=ft.TextStyle(color=self.color[6], font_family=self.font[1]),
            text_size=18,
            width=120,
            select_icon_enabled_color=self.color[4],
            options=[ ft.dropdownm2.Option( str(i) ) for i in lista ],
        )

        return  intro


    ######################################################################
    ###-------------------Functions_graph_in_flet----------------------###
    ######################################################################

    ###-------------------------main_menu------------------------------###
    def main_menu(self, menu_navegation):
       
        imagen  =   ft.Image(src=str(self.direct_img), width=100)
        
        group_01    =   self.input_group("group 1")
        group_02    =   self.input_group("group 2")

        super_l   =   ft.Container(ft.Column([imagen]), padding=5, bgcolor=self.color[1], border_radius=15)
        super_r =   ft.Container(
            ft.Column([
                ft.Container(ft.Row([group_01, group_01])),
                ft.Container(ft.Row([group_02, group_02]))
            ])
        )

        super   =   ft.Container(ft.Row([super_l, super_r], alignment=ft.MainAxisAlignment.CENTER))
        infer   =   ft.Text("mundo")

        cont    =   ft.Container(ft.Column([super,infer], spacing=20, alignment=ft.MainAxisAlignment.START), padding=10)


        self.page.controls.clear()
        self.page.add(cont, menu_navegation)
        self.page.floating_action_button =   None
        self.page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment     =   ft.MainAxisAlignment.START   
        return  self.page.update()

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


