import  modules.data_list   as  data

import  pandas  as  pd
import  flet    as  ft
import  os 

######################################################################
###---------------------Groups_menu_flet---------------------------###
######################################################################
class   info_groups:

    def __init__(self, color, font, direct_groups, direct_imagen_group, direct_imagen_player_01, direct_imagen_player_02):
        self.color  =   color
        self.font   =   font
        self.direct_groups  =   direct_groups
        self.direct_imagen_group    =   direct_imagen_group
        self.direct_imagen_player_01    =   direct_imagen_player_01
        self.direct_imagen_player_02    =   direct_imagen_player_02
        self.page   =   None

        ###----------------define_variables_para_crear_listas--------------###
        self.name_player    =   []
        self.data_list      =   []

    ######################################################################
    ###-------------------Definitions_functions------------------------###
    ######################################################################

    ###------------------------view_data_grups-------------------------###
    def view_table(self, direct, name):
        
        table   =   pd.read_csv(f"{direct}/{name}.dat", sep=r"\s+")
        columns =   table.columns.tolist()

        view    =   ft.DataTable(
            
            heading_row_color   =   self.color[2],
            sort_ascending      =   True,
            bgcolor             =   self.color[6],
            border              =   ft.border.all(2, self.color[0]),
            border_radius       =   10,
            vertical_lines      =   ft.border.BorderSide(1, self.color[0]),
            horizontal_lines    =   ft.border.BorderSide(1, self.color[0]),
            heading_row_height  =   35,
            divider_thickness   =   0,
            column_spacing      =   22,
            
            columns =   [
                ft.DataColumn(
                    ft.Text(str(col), color=self.color[7], font_family=self.font[1], weight=ft.FontWeight.BOLD, italic=True)
                )  for col in  columns
            ],

            rows    =   [
                ft.DataRow([
                    ft.DataCell(
                        ft.Text(str(table.iloc[j,i]), color=self.color[7], font_family=self.font[1], weight=ft.FontWeight.BOLD)
                    )    for i   in  range(len(columns))
                ])   for j   in  range(5)
            ],
        )
        return  view

    ###-------------------------bar_intro_data-------------------------###
    def input_box(self, intro):
        
        intro_text  =   ft.TextField(
            label   =   str(intro), 
            color   =   self.color[6], 
            bgcolor =   self.color[0], 
            label_style =   ft.TextStyle(color=self.color[6]),
            border_color    =   self.color[6], 
            border_radius   =   10,
            border_width    =   1,
            cursor_color    =   self.color[6],
            cursor_height   =   20,
            cursor_radius   =   10,
            cursor_width    =   1,
            selection_color =   self.color[1],
        )
        return  intro_text

    ###-------------------------baner_group----------------------------###
    def baner_group(self):
        imagen  =   ft.Image(src=str(self.direct_imagen_group), width=170)
        texto   =   ft.Text(
            "Groups list", 
            size    =   40, 
            color   =   self.color[7],
            font_family =   self.font[0],
            weight  =   ft.FontWeight.BOLD,
            italic  =   True
        )
        box     =   ft.Row(
            controls    =   [imagen, texto],
            spacing     =   40,
            alignment   =   ft.MainAxisAlignment.START,
        )
        cont    =   ft.Container(
            content =   box, 
            bgcolor =   self.color[3], 
            border_radius   =   15,
            padding =   ft.padding.all(20) 
        )
        return  cont

    ###----------------------button_crated_group-----------------------###
    def button_new_group(self, menu_navegation):
        
        boton   =   ft.FloatingActionButton(
            on_click    =   lambda  e: self.intro_new_group(menu_navegation), 
            icon        =   ft.Icons.ADD,
            bgcolor     =   self.color[4],
            foreground_color    =   self.color[0],
        )
        return  boton

    ###-------------------------button_icon-------------------------###
    def button_icon(self, action, label, icono):
        
        boton   =   ft.FilledButton(
            content =   ft.Row([
                ft.Icon(icono, size=20, color=self.color[0]),
                ft.Text(str(label), size=17, text_align=ft.TextAlign.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=8
            ),
            on_click=   action,
            color   =   self.color[0],
            bgcolor =   self.color[3],
            style   =   ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=28)),
        )
        return  boton

    ###-------------------------button_generic-------------------------###
    def button_generic(self, action, label, icono):
        
        boton   =   ft.FilledButton(
            content =   ft.Text(str(label), size=15, text_align=ft.TextAlign.CENTER),
            on_click=   action,
            color   =   self.color[0],
            bgcolor =   self.color[5],
            style   =   ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=28)),
        )
        return  boton

    ###------------------------button_group_list-----------------------###
    def button_group_list(self, menu_navegation):

        def boton(name):
            boton   =   ft.TextButton(
                content =   ft.Row([
                    ft.Icon(ft.Icons.LIST_ROUNDED, size=40, color=self.color[6]),
                    ft.Text(
                        str(name), size=25, text_align=ft.TextAlign.CENTER, 
                        color=self.color[6], font_family=self.font[1], weight=ft.FontWeight.BOLD
                    ),
                ], 
                alignment=ft.VerticalAlignment.START, spacing=10
                ),
                on_click    =   lambda  e:  self.view_list(name, menu_navegation)
            )
            return  boton

        lista   =   os.listdir(self.direct_groups)

        if  len(lista)  ==  0:
            lista   =   ft.Text(
                str("Create your first list"), 
                size    =   25, 
                weight  =   ft.FontWeight.BOLD,
                color   =   self.color[6], 
                text_align  =   ft.TextAlign.CENTER, 
                font_family =   self.font[1], 
            )
            lista_groups    =   ft.Container(
                content =   ft.Column([lista]), 
                bgcolor =   self.color[1], 
                padding =   ft.padding.all(20),
                alignment   =   ft.alignment.center, 
                border_radius   =   15,
                height  = 4000,
            )

        elif    len(lista)  !=  0:
            lista   =   [filename.replace(".dat", "") for filename in lista]    
            lista   =   [boton(i) for i in lista]

            lista_00    =   ft.Container(
                content =   ft.Column(lista, scroll=ft.ScrollMode.HIDDEN),
                height  = 700 
            )

            lista_groups    =   ft.Container(
                content=ft.Column([lista_00]),
                bgcolor =   self.color[1], 
                border_radius   =   15, 
                padding =   ft.padding.all(20),
                height  = 4000 
            )

        return  lista_groups

    ###------------------------intro_data_player-----------------------###
    def intro_data_player(self, name_group, menu_navegation):

        ###---------------------definitions_functions----------------------###
        def save_exit(e):
            data.new_list(self.direct_groups, name_group, self.name_player, self.data_list)
            return  self.init_menu(menu_navegation)

        def save_player(e):
            self.name_player.append(info_player[0].value)
            valores = []
            indices = [2, 3, 4, 5, 6] 
            for i in indices:
                try:
                    valores.append(int(info_player[i].value))
                except (ValueError, TypeError):
                    valores.append(0) 
            
            self.data_list.append(valores)
            return self.intro_data_player(name_group, menu_navegation)

        ###----------------------contenedor_superior-----------------------###
        imag_title  =   ft.Image(src=str(self.direct_imagen_player_01), width=170)
        texto_title =   ft.Text(
            "Enter a player \n to the group", 
            size    =   25,
            color   =   self.color[0],
            weight  =   ft.FontWeight.BOLD,
            italic  =   True,
            font_family =   self.font[0],
            text_align  =   ft.TextAlign.START,
        )
        contenedor_01   =   ft.Container(
            content =   ft.Row(controls=[imag_title, texto_title], alignment=ft.MainAxisAlignment.START, spacing=50),
            bgcolor =   self.color[6],
            border_radius   =   15,
            padding =   ft.padding.all(20) 
        )

        ###------------------------contenedor_medio------------------------###
        imag_player =   ft.Image(src=str(self.direct_imagen_player_02), fit=ft.ImageFit.CONTAIN)
        info_player =   [
            self.input_box("Name"),
            ft.Divider(),
            self.input_box("Life"),
            self.input_box("Damage"),
            self.input_box("Dodge"),
            self.input_box("Attack"),
            self.input_box("Dices"),
        ]
        contenedor_02   =   ft.Container(
            ft.Row(
                [
                    ft.Container(ft.Row([imag_player], alignment=ft.MainAxisAlignment.CENTER), bgcolor=self.color[0], height=400),
                    ft.Container(ft.Column(info_player), bgcolor=self.color[1], padding=ft.padding.all(20), border_radius=15) 
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
       
        ###-----------------------contenedor_inferior----------------------###
        boton_01    =   self.button_icon(save_exit, "Save group and exit", ft.Icons.SAVE)
        boton_02    =   self.button_icon(save_player, "Enter another player", ft.Icons.GROUP_ADD)
        contenedor_03   =   ft.Container(
            ft.Row(
                [boton_01, boton_02], 
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ), 
            padding=20, 
            bgcolor=self.color[1],
            border_radius=15
        )

        ###----------------------contenedor_principal----------------------###
        contenedor_main =   ft.Container(ft.Column([contenedor_01, contenedor_02, contenedor_03], spacing=20))
        
        self.page.controls.clear()
        self.page.add(contenedor_main)
        return  self.page.update()

    ###--------------------------Delete_group--------------------------###
    def delet_group(self, name, menu_navegation):
        data.remove_list(self.direct_groups, name)
        return  self.init_menu(menu_navegation) 
    
    ###---------------------------Copy_group---------------------------###
    def copy_group(self, name, menu_navegation):

        def copy_and_exit(e):
            origin  =   f"{self.direct_groups}/{name}.dat"
            copy    =   f"{self.direct_groups}/{intro_name_copy.value}.dat"
            
            with    open(origin, "rb")  as  f_origen:
                with    open(copy,  "wb")   as  f_copy:
                    f_copy.write(f_origen.read())

            return  self.init_menu(menu_navegation)

        texto   =   ft.Text(
            "Enter the name with which the copy is saved: ", 
            size    =   20,
            color   =   self.color[6],
            font_family =   self.font[1],
        )

        intro_name_copy  =   self.input_box(f"Name copy {name}")   
        boton   =   self.button_icon(copy_and_exit, "Copy", ft.Icons.COPY)

        boton_container =   ft.Container(
            ft.Row(
                [ft.Container(boton, width=100)],
                alignment   =   ft.MainAxisAlignment.CENTER,
            )
        )

        box =   ft.Container(
            ft.Column([texto, intro_name_copy, boton_container]), 
            bgcolor=self.color[1], 
            border_radius=15,
            padding=20
        )

        self.page.controls.clear()
        self.page.add(box)
        return  self.page.update()

    ###-------------------------Delete_players-------------------------###
    def delete_players(self, name_list, menu_navegation):

        def delete(player_name):
            data.remove_player(self.direct_groups, name_list, player_name)
            return  self.delete_players(name_list, menu_navegation)

        def boton(player_name):
            boton   =   ft.TextButton(
                on_click    =   lambda e:   delete(player_name),
                content =   ft.Text(
                    f"{player_name}",
                    color   =   self.color[6], 
                    weight  =   ft.FontWeight.BOLD, 
                    size    =   20,
                    font_family =   self.font[1],
                )
            )
            return  boton

        tabla   =   pd.read_csv(f"{self.direct_groups}/{name_list}.dat", sep=r"\s+")
        name_player =   tabla.columns.tolist()
        name_player =   name_player[1:-1]

        boton_back  =   ft.IconButton(
            ft.Icons.ARROW_BACK_IOS_OUTLINED, 
            bgcolor =   self.color[6],
            icon_size   =   40,
            on_click    =    lambda e:   self.setting_group(name_list, menu_navegation) 
        )
        texto_title =   ft.Text(
            "Select Player to Delete",
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   40,
            font_family =   self.font[0],
        )
        title   =   ft.Container(content=ft.Row([boton_back, texto_title], spacing=30))
        texto_secondary =   ft.Text(
            str(name_list),
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   25,
            font_family =   self.font[1],
        )
        
        box =   ft.Container(
            content =   ft.Column([boton(name)  for name in  name_player], scroll="always"),
            height  =   700
        )

        self.page.controls.clear()
        self.page.horizontal_alignment =   ft.MainAxisAlignment.START  
        self.page.add(title, texto_secondary, ft.Divider(), box)
        return  self.page.update()

    ###---------------------------Add_player---------------------------###
    def add_player(self, name_list, menu_navegation):

        ###---------------------definitions_functions----------------------###
        def save_exit(e):

            name_player = info_player[0].value
            if not name_player: 
                name_player = "non name"

            valores = []
            indices = [2, 3, 4, 5, 6] 
            for i in indices:
                try:
                    valores.append(int(info_player[i].value))
                except (ValueError, TypeError):
                    valores.append(0) 

            data.add_player(self.direct_groups, name_list, name_player, valores)
            return  self.view_list(name_list, menu_navegation)

        ###----------------------contenedor_superior-----------------------###
        imag_title  =   ft.Image(src=str(self.direct_imagen_player_01), width=170)
        texto_title =   ft.Text(
            "Add new player", 
            size    =   40,
            color   =   self.color[0],
            weight  =   ft.FontWeight.BOLD,
            italic  =   True,
            font_family =   self.font[0],
            text_align  =   ft.TextAlign.START,
        )
        contenedor_01   =   ft.Container(
            content =   ft.Row(controls=[imag_title, texto_title], alignment=ft.MainAxisAlignment.START, spacing=50),
            bgcolor =   self.color[6],
            border_radius   =   15,
            padding =   ft.padding.all(20) 
        )

        ###------------------------contenedor_medio------------------------###
        imag_player =   ft.Image(src=str(self.direct_imagen_player_02), fit=ft.ImageFit.CONTAIN)
        info_player =   [
            self.input_box("Name"),
            ft.Divider(),
            self.input_box("Life"),
            self.input_box("Damage"),
            self.input_box("Dodge"),
            self.input_box("Attack"),
            self.input_box("Dices"),
        ]
        contenedor_02   =   ft.Container(
            ft.Row(
                [
                    ft.Container(ft.Row([imag_player], alignment=ft.MainAxisAlignment.CENTER), bgcolor=self.color[0], height=400),
                    ft.Container(ft.Column(info_player), bgcolor=self.color[1], padding=ft.padding.all(20), border_radius=15) 
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
       
        ###-----------------------contenedor_inferior----------------------###
        boton_01    =   self.button_icon(save_exit, "Save player", ft.Icons.SAVE)
        contenedor_03   =   ft.Container(
            ft.Row(
                [boton_01], 
                alignment=ft.MainAxisAlignment.CENTER
            ), 
            padding=20, 
            bgcolor=self.color[1],
            border_radius=15
        )

        ###----------------------contenedor_principal----------------------###
        contenedor_main =   ft.Container(ft.Column([contenedor_01, contenedor_02, contenedor_03], spacing=20))
        
        self.page.controls.clear()
        self.page.add(contenedor_main)
        return  self.page.update()

    ###--------------------------Edit_player---------------------------###
    def edit_player(self, name_list, menu_navegation):

        def boton(player_name):
            boton   =   ft.TextButton(
                # on_click    =   lambda e:   delete(player_name),
                content =   ft.Text(
                    f"{player_name}",
                    color   =   self.color[6], 
                    weight  =   ft.FontWeight.BOLD, 
                    size    =   20,
                    font_family =   self.font[1],
                )
            )
            return  boton

        tabla   =   pd.read_csv(f"{self.direct_groups}/{name_list}.dat", sep=r"\s+")
        name_player =   tabla.columns.tolist()
        name_player =   name_player[1:-1]

        boton_back  =   ft.IconButton(
            ft.Icons.ARROW_BACK_IOS_OUTLINED, 
            bgcolor =   self.color[6],
            icon_size   =   40,
            on_click    =    lambda e:   self.view_list(name_list, menu_navegation) 
        )
        texto_title =   ft.Text(
            "Select Player to Edit",
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   40,
            font_family =   self.font[0],
        )
        title   =   ft.Container(content=ft.Row([boton_back, texto_title], spacing=30))
        texto_secondary =   ft.Text(
            str(name_list),
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   25,
            font_family =   self.font[1],
        )
        
        box =   ft.Container(
            content =   ft.Column([boton(name)  for name in  name_player], scroll="always"),
            height  =   700
        )

        self.page.controls.clear()
        self.page.horizontal_alignment =   ft.MainAxisAlignment.START  
        self.page.add(title, texto_secondary, ft.Divider(), box)
        return  self.page.update()


    ######################################################################
    ###-------------------Functions_graph_in_flet----------------------###
    ######################################################################

    ###-------------------------init_menu_grups------------------------###
    def init_menu(self, menu_navegation):

        ###----------reseteo_de_variables_globales_para_las_listas---------###
        self.name_player    =   []
        self.data_list      =   []

        cont    =   ft.Container(
            content =   ft.Column(
                [self.baner_group(), self.button_group_list(menu_navegation)], spacing=20
            )
        )

        self.page.controls.clear()
        self.page.vertical_alignment     =   ft.MainAxisAlignment.START  
        self.page.add(cont, menu_navegation)
        self.page.floating_action_button =   self.button_new_group(menu_navegation)
        return  self.page.update()

    ###-------------------------View_data_table------------------------###
    def view_list(self, name_table, menu_navegation):
        boton   =   ft.Container(
            content =   ft.Row(
                [
                    ft.IconButton(
                        ft.Icons.ARROW_BACK_IOS_OUTLINED, 
                        bgcolor=self.color[6],
                        on_click    =   lambda  e:  self.init_menu(menu_navegation)
                    ),
                    ft.TextButton(
                        on_long_press   =   lambda  e:   self.edit_player(name_table, menu_navegation),
                        content =   ft.Text(
                            str(name_table), 
                            color   =   self.color[6], 
                            weight  =   ft.FontWeight.BOLD, 
                            italic  =   True,
                            size    =   25,
                            font_family =   self.font[1],
                        ),
                        on_click    =   lambda  e:  self.init_menu(menu_navegation)
                    ),
                    ft.IconButton(
                        ft.Icons.SETTINGS, 
                        bgcolor=self.color[6],
                        on_click    =   lambda  e:  self.setting_group(name_table, menu_navegation)
                    ),
                ],
                alignment   =   ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )
       
        tabla   =   ft.Row([self.view_table(self.direct_groups, name_table)] ,scroll="always")
        
        lista   =   [boton, tabla]
        tabla_inferior  =   ft.Container(
            content =   ft.Column(lista, scroll=ft.ScrollMode.HIDDEN),
            bgcolor =   self.color[1], 
            border_radius   =   15, 
            padding =   ft.padding.all(20),
            height  = 4000   
        )        

        cont    =   ft.Container(
            content =   ft.Column(
                [self.baner_group(), tabla_inferior], spacing=20)
        )
        
        self.page.controls.clear()
        self.page.floating_action_button =   None
        self.page.add(cont, menu_navegation)
        return  self.page.update()

    ###-------------------------intro_new_group------------------------###
    def intro_new_group(self, menu_navegation):
        
        texto   =   ft.Text(
            "Enter the name for the new group: ", 
            size    =   20,
            color   =   self.color[6],
            font_family =   self.font[1],
        )

        intro_name  =   self.input_box("Name")   
        boton   =   self.button_icon(lambda e: self.intro_data_player(intro_name.value, menu_navegation), "Next", ft.Icons.SAVE_AS)

        boton_container =   ft.Container(
            ft.Row(
                [ft.Container(boton, width=100)],
                alignment   =   ft.MainAxisAlignment.CENTER,
            )
        )

        lista   =   [texto, intro_name, boton_container]
        tabla_inferior  =   ft.Container(
            content =   ft.Column(lista, scroll=ft.ScrollMode.HIDDEN, spacing=20),
            bgcolor =   self.color[1], 
            border_radius   =   15, 
            padding =   ft.padding.all(20),
            height  = 4000   
        )        

        cont    =   ft.Container(
            content =   ft.Column(
                [self.baner_group(), tabla_inferior], spacing=20)
        )
        
        self.page.controls.clear()
        self.page.floating_action_button =   None
        self.page.add(cont, menu_navegation)
        return  self.page.update()

    ###-------------------------settings_group-------------------------###
    def setting_group(self, name_group, menu_navegation):
        boton_back  =   ft.IconButton(
            ft.Icons.ARROW_BACK_IOS_OUTLINED, 
            bgcolor =   self.color[6],
            icon_size   =   40,
            on_click    =    lambda e:   self.view_list(name_group, menu_navegation) 
        )
        texto_title =   ft.Text(
            "Group settings",
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   50,
            font_family =   self.font[0],
        )
        title   =   ft.Container(content=ft.Row([boton_back, texto_title], spacing=20))
        texto_secondary =   ft.Text(
            str(name_group),
            color   =   self.color[6], 
            weight  =   ft.FontWeight.BOLD, 
            italic  =   True,
            size    =   25,
            font_family =   self.font[1],
        )
        boton_app_player    =   ft.TextButton(
            on_click    =   lambda  e:  self.add_player(name_group, menu_navegation),
            content =   ft.Text(
                "App player", 
                color   =   self.color[6], 
                weight  =   ft.FontWeight.BOLD, 
                size    =   20,
                font_family =   self.font[1],
            )
        )
        boton_edit_player   =   ft.TextButton(
            on_click    =   lambda  e:  self.edit_player(name_group, menu_navegation),
            content =   ft.Text(        
                "Edit player",
                color   =   self.color[6], 
                weight  =   ft.FontWeight.BOLD, 
                size    =   20,
                font_family =   self.font[1],       
            )
        )
        boton_remove_player =   ft.TextButton(
            on_click    =   lambda e:   self.delete_players(name_group, menu_navegation),
            content =   ft.Text(
                "Remove player",
                color   =   self.color[6], 
                weight  =   ft.FontWeight.BOLD, 
                size    =   20,
                font_family =   self.font[1],
            )
        )
        boton_copy_group    =   ft.TextButton(
            on_click    =   lambda e:   self.copy_group(name_group, menu_navegation),
            content =   ft.Text(
                "Copy group",
                color   =   self.color[6], 
                weight  =   ft.FontWeight.BOLD, 
                size    =   20,
                font_family =   self.font[1],
            )
        )
        boton_delete_group    =   ft.TextButton(
            on_click    =   lambda e:   self.delet_group(name_group, menu_navegation),
            content =   ft.Text(
                "Delete group",
                color   =   self.color[5], 
                weight  =   ft.FontWeight.BOLD, 
                size    =   20,
                font_family =   self.font[1],
            )
        )
        divisor =   ft.Divider()
        box =   ft.Container(
            content =   ft.Column(
                spacing =   15,
                controls    =   [
                    title,
                    texto_secondary,
                    divisor,
                    boton_app_player,
                    boton_edit_player,
                    boton_remove_player,
                    boton_copy_group,
                    divisor,
                    boton_delete_group,
                ]
            )
        )
        self.page.controls.clear()
        self.page.add(box)
        return  self.page.update()


