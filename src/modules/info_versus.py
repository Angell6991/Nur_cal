import  modules.probability   as  prob

import  pandas  as  pd
import  numpy   as  np
import  flet    as  ft
import  os


######################################################################
###---------------------Groups_menu_flet---------------------------###
######################################################################
class   info_versus:

    def __init__(self, color, font, dimentions, direct_groups, direct_img):
        self.page   =   None
        self.color  =   color
        self.font   =   font
        self.dimentions  =   dimentions
        self.direct_img =   direct_img
        self.direct_groups  =   direct_groups

    ######################################################################
    ###-------------------Definitions_functions------------------------###
    ######################################################################

    ###---------------------------Graph--------------------------------###
    def graph(self, name_group, name_player, die_list, probability_list):
       
        title   =   ft.Container(
            ft.Row(
                [ft.Text(f"{name_group}: {name_player}", color=self.color[6], font_family=self.font[1], size=18)],
                alignment   =   ft.MainAxisAlignment.CENTER
            )
        )

        lista   =   probability_list
        n_y     =   len(lista)

        name_list   =   die_list
        n_x     =   len(name_list)

        chart   =   ft.BarChart(
            
            bar_groups  =   [ 
                ft.BarChartGroup(
                    x=i, 
                    bar_rods=[ft.BarChartRod(from_y=0, to_y=lista[i], width=20, color=self.color[4], border_radius=20)]
                ) for i in range(n_y)
            ],

            bottom_axis =   ft.ChartAxis(
                labels  =   [ 
                    ft.ChartAxisLabel(
                        value=i, 
                        label=ft.Container(ft.Text(f"{name_list[i]}", color=self.color[6], font_family=self.font[1]), padding=10)
                        ) for i in range(n_x) 
                ],
                title=ft.Text("Number of blows to die", color=self.color[6], font_family=self.font[1]), 
                labels_size=40,
            ),

            left_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=lista[i],
                        label=ft.Container(
                            ft.Text(f"{round(lista[i], 1)}", color=self.color[6], font_family=self.font[1]), 
                            padding=0
                        )
                    ) for i in range(n_y)
                ],
                title=ft.Text("Probability %", color=self.color[6], font_family=self.font[1]), 
                title_size=20,
                labels_size=40,
            ),

            # border=ft.border.all(1, color=self.color[6]),
            horizontal_grid_lines=ft.ChartGridLines(color=self.color[6], width=1, dash_pattern=[3, 3]),
            tooltip_bgcolor=ft.Colors.with_opacity(0.9, color=self.color[0]),
            # max_y=round(max(lista) + 5, 0),
            interactive=True,
            expand=True,
        )
        
        cont    =   ft.Container(ft.Column([title, chart], alignment=ft.CrossAxisAlignment.CENTER), padding=20)

        return  cont

    ###------------------------input_group-----------------------------###
    def input_group(self, label):
        
        lista   =   os.listdir(self.direct_groups)
        lista   =   [filename.replace(".dat", "") for filename in lista]    

        intro   =   ft.DropdownM2(
            bgcolor=self.color[1],
            border_color=self.color[3],
            border_radius=15,
            color=self.color[6],
            label=str(label),
            label_style=ft.TextStyle(color=self.color[3], font_family=self.font[1], size=18),
            text_style=ft.TextStyle(color=self.color[6], font_family=self.font[1]),
            text_size=18,
            width=120,
            select_icon_enabled_color=self.color[6],
            options=[ ft.dropdownm2.Option( str(i) ) for i in lista ],
        )

        return  intro

    ###------------------------input_player----------------------------###
    def input_player(self, label, group):

        if  group   ==  None:

            intro   =   ft.DropdownM2(
                bgcolor=self.color[1],
                border_color=self.color[3],
                border_radius=15,
                color=self.color[6],
                label=str(label),
                label_style=ft.TextStyle(color=self.color[3], font_family=self.font[1], size=18),
                text_style=ft.TextStyle(color=self.color[6], font_family=self.font[1]),
                text_size=18,
                width=120,
                select_icon_enabled_color=self.color[6],
                disabled=True,
                options=[ ft.dropdownm2.Option("None") ],
            )
            return  intro

        elif    group   !=  None:

            tabla   =   pd.read_csv(f"{self.direct_groups}/{group}.dat", sep=r"\s+")
            lista   =   tabla.columns.tolist()
            lista   =   lista[1:]

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
                disabled=True,
                options=[ ft.dropdownm2.Option( str(i) ) for i in lista ],
            )
            return  intro

    ###------------------------button_icon-----------------------------###
    def button_icon(self, action, label, icono):
        
        boton   =   ft.FilledButton(
            content =   ft.Row([
                ft.Icon(icono, size=20, color=self.color[0]),
                ft.Text(str(label), size=17, text_align=ft.TextAlign.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=8
            ),
            on_click=   action,
            color   =   self.color[0],
            bgcolor =   self.color[6],
            style   =   ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=28)),
            # disabled=   True,
        )
        return  boton

    ###------------------------view_result-----------------------------###
    def view_result(self, group_01, group_02, player_01, player_02, menu_navegation):
        
        ###--------------------------top_baner-----------------------------###
        boton_back  =   ft.IconButton(
            ft.Icons.ARROW_BACK_IOS_OUTLINED, 
            bgcolor =   self.color[6],
            icon_size   =   40,
            on_click    =    lambda e:   self.main_menu(menu_navegation) 
        )
        texto_title =   ft.Text(
            "Result probability",
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   30,
            font_family =   self.font[0],
            text_align  =   ft.TextAlign.START,
        )
        top_baner   =   ft.Container(ft.Row([boton_back, texto_title], spacing=20))

        ###---------------------import_data_player-------------------------###
        tabla_01    =   pd.read_csv(f"{self.direct_groups}/{group_01}.dat", sep=r"\s+")
        tabla_02    =   pd.read_csv(f"{self.direct_groups}/{group_02}.dat", sep=r"\s+")

        data_player_01  =   np.array(tabla_01[f"{player_01}"])
        data_player_02  =   np.array(tabla_02[f"{player_02}"])

        pb  =   prob.probability(data_player_01, data_player_02)
        
        ###-------------craeted_graph_die_blows_probability----------------###
        list_die_01 =   pb.list_probability_die_1
        list_die_01 =   [round(list_die_01[i]*100, 1) for i in range(len(list_die_01))]

        list_die_02 =   pb.list_probability_die_2
        list_die_02 =   [round(list_die_02[i]*100, 1) for i in range(len(list_die_02))]

        graph_01    =   self.graph(group_01, player_01, pb.list_unique_1, list_die_01)
        graph_02    =   self.graph(group_02, player_02, pb.list_unique_2, list_die_02)

        ###---------------------container_view_result----------------------###
        dat_01  =   ft.Container(ft.Column([graph_01]), border_radius=15, bgcolor=self.color[1])
        dat_02  =   ft.Container(ft.Column([graph_02]), border_radius=15, bgcolor=self.color[1])


        texto_01_r   =   [
            ft.Text(
                f"Probability attack true: {round(pb.probability_attack_1_true*100 ,1)}%",
                font_family=self.font[1],
                size=12,
                color=self.color[6]
            ),
            ft.Text(
                f"Probability relaunch: {round(pb.probability_attack_1_relaunch*100 ,1)}%",
                font_family=self.font[1],
                size=12,
                color=self.color[6]
            ),
            ft.Text(
                f"Probability win: {round((1-pb.probability_kill_1)*100 ,1)}%",
                font_family=self.font[1],
                size=12,
                color=self.color[6]
            ),
        ]
        texto_01_l   =   [
            ft.Text(f"Life: {data_player_01[0]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Damage: {data_player_01[1]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Dodge: {data_player_01[2]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Attack: {data_player_01[3]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Dices: {data_player_01[4]}", font_family=self.font[1], size=12, color=self.color[6]),
        ]
        info_dat_01 =   ft.Container(
            ft.Row(
                [
                    ft.Container(ft.Column(texto_01_l), border_radius=15, bgcolor=self.color[1], padding=10), 
                    ft.Container(ft.Column(texto_01_r), border_radius=15, bgcolor=self.color[1], padding=10, expand=True)
                ]
            )
        )


        texto_02_r   =   [
            ft.Text(
                f"Probability attack true: {round(pb.probability_attack_2_true*100 ,1)}%",
                font_family=self.font[1],
                size=12,
                color=self.color[6]
            ),
            ft.Text(
                f"Probability relaunch: {round(pb.probability_attack_2_relaunch*100 ,1)}%",
                font_family=self.font[1],
                size=12,
                color=self.color[6]
            ),
            ft.Text(
                f"Probability win: {round((1-pb.probability_kill_2)*100 ,1)}%",
                font_family=self.font[1],
                size=12,
                color=self.color[6]
            ),
        ]
        texto_02_l   =   [
            ft.Text(f"Life: {data_player_02[0]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Damage: {data_player_02[1]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Dodge: {data_player_02[2]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Attack: {data_player_02[3]}", font_family=self.font[1], size=12, color=self.color[6]),
            ft.Text(f"Dices: {data_player_02[4]}", font_family=self.font[1], size=12, color=self.color[6]),
        ]
        info_dat_02 =   ft.Container(
            ft.Row(
                [
                    ft.Container(ft.Column(texto_02_l), border_radius=15, bgcolor=self.color[1], padding=10), 
                    ft.Container(ft.Column(texto_02_r), border_radius=15, bgcolor=self.color[1], padding=10, expand=True)
                ]
            )
        )


        conte_infer =   ft.Container(
            ft.Column(
                [dat_01, info_dat_01, ft.Divider(color=self.color[0]), dat_02, info_dat_02], 
                scroll=ft.ScrollMode.HIDDEN,
                spacing=10,
            ), 
            height=self.dimentions[0]
        )

        ###------------------------main_container--------------------------###
        cont    =   ft.Container(ft.Column([top_baner, ft.Divider(color=self.color[6]), conte_infer], spacing=10), padding=10)

        self.page.controls.clear()
        self.page.add(cont)
        # self.page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment     =   ft.MainAxisAlignment.START   
        return  self.page.update()

    ######################################################################
    ###-------------------Functions_graph_in_flet----------------------###
    ######################################################################

    ###-------------------------main_menu------------------------------###
    def main_menu(self, menu_navegation):

        ###---------------variables_del_baner_superio----------------------###
        imagen  =   ft.Image(src=str(self.direct_img), width=self.dimentions[0]*0.25)
        
        group_01    =   self.input_group("group")
        group_02    =   self.input_group("group")
        
        player_01   =   self.input_player("player", group_01.value)
        player_02   =   self.input_player("player", group_02.value)

        boton   =   self.button_icon(
            lambda e: self.view_result(group_01.value, group_02.value, player_01.value, player_02.value, menu_navegation),
            "calculated", 
            ft.Icons.LOCAL_FIRE_DEPARTMENT
        )
        
        ###------------funciones_para_actualizar_player_list---------------###
        def change_01(e):
            value = (group_01.value or "")
            
            if value.strip() == "":
                # No hay grupo seleccionado: deshabilitar y mostrar "None"
                player_01.disabled = True
                player_01.options = [ ft.dropdownm2.Option("None") ]
            
            else:
                try:
                  tabla = pd.read_csv(f"{self.direct_groups}/{value}.dat", sep=r"\s+")
                  lista = tabla.columns.tolist()
                  lista = lista[1:] 
                  player_01.disabled = False
                  player_01.options = [ ft.dropdownm2.Option(str(i)) for i in lista ]
                except Exception as ex:
                  # En caso de fallo, dejarlo deshabilitado
                  player_01.disabled = True
                  player_01.options = [ ft.dropdownm2.Option("None") ]
            
            return  self.page.update()
        group_01.on_change = change_01


        def change_02(e):
            value = (group_02.value or "")
            
            if value.strip() == "":
                # No hay grupo seleccionado: deshabilitar y mostrar "None"
                player_02.disabled = True
                player_02.options = [ ft.dropdownm2.Option("None") ]
            
            else:
                try:
                  tabla = pd.read_csv(f"{self.direct_groups}/{value}.dat", sep=r"\s+")
                  lista = tabla.columns.tolist()
                  lista = lista[1:]  
                  player_02.disabled = False
                  player_02.options = [ ft.dropdownm2.Option(str(i)) for i in lista ]
                except Exception as ex:
                  # En caso de fallo, dejarlo deshabilitado
                  player_02.disabled = True
                  player_02.options = [ ft.dropdownm2.Option("None") ]
            
            return  self.page.update()
        group_02.on_change  =   change_02

        ###----------------------------Super-------------------------------###
        texto    =   ft.Text(
            "Battle 1 vs 1", 
            size    =   self.dimentions[0]*0.13, 
            color   =   self.color[4], 
            weight  =   ft.FontWeight.BOLD,
            italic  =   True,
            font_family =   self.font[0] 
        )
        super   =   ft.Container(ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER))

        ###---------------------------Center-------------------------------###
        center_l =   ft.Container(ft.Column([group_01, player_01]))
        center_c =   ft.Container(ft.Column([imagen]), padding=5, bgcolor=self.color[1], border_radius=15)
        center_r =   ft.Container(ft.Column([group_02, player_02]))

        center   =   ft.Container(ft.Row([center_l, center_c, center_r], alignment=ft.MainAxisAlignment.CENTER))
       
        ###---------------------------Inferior-----------------------------###
        infer   =   ft.Container(ft.Row([boton], alignment=ft.MainAxisAlignment.CENTER))

        ###--------------------------Contenedor----------------------------###
        cont    =   ft.Container(ft.Column([super, center, infer], spacing=30))

        self.page.controls.clear()
        self.page.add(cont, menu_navegation)
        self.page.floating_action_button =   None
        self.page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment     =   ft.MainAxisAlignment.CENTER   
        return  self.page.update()


