# import  modules.data_list   as  data

import  pandas  as  pd
import  flet    as  ft
import  os 

######################################################################
###---------------------Groups_menu_flet---------------------------###
######################################################################
class   info_groups:

    def __init__(self, color, font, direct_groups, direct_imagen_group):
        self.color  =   color
        self.font   =   font
        self.direct_groups  =   direct_groups
        self.direct_imagen_group    =   direct_imagen_group
        self.page   =   None

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
            color   =   self.color[7], 
            bgcolor =   self.color[8], 
            label_style =   ft.TextStyle(color=self.color[6]),
            border_color    =   self.color[6], 
            border_radius   =   10,
            border_width    =   1,
            cursor_color    =   self.color[6],
            cursor_height   =   20,
            cursor_radius   =   10,
            cursor_width    =   1,
            selection_color =   self.color[0],
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
    def button_new_group(self, action):
        
        boton   =   ft.FloatingActionButton(
            on_click    =   action, 
            icon        =   ft.Icons.ADD,
            bgcolor     =   self.color[4],
            foreground_color    =   self.color[0],
        )
        return  boton

    ###-------------------------button_icon-------------------------###
    def button_icon(self, action, label, icono):
        
        boton   =   ft.FilledButton(
            content =   ft.Row([
                ft.Icon(icono, size=20),
                ft.Text(str(label), size=15, text_align=ft.TextAlign.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=8
            ),
            on_click=   action,
            color   =   self.color[0],
            bgcolor =   self.color[5],
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


    ######################################################################
    ###-------------------Functions_graph_in_flet----------------------###
    ######################################################################

    ###-------------------------init_menu_grups------------------------###
    def init_menu(self, menu_navegation):
        cont    =   ft.Container(
            content =   ft.Column(
                [self.baner_group(), self.button_group_list(menu_navegation)], spacing=20
            )
        )

        self.page.controls.clear()
        self.page.vertical_alignment     =   ft.MainAxisAlignment.START  
        self.page.add(cont, menu_navegation)
        self.page.floating_action_button =   self.button_new_group(None)
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
                        # on_click    =   lambda  e:  self.init_menu(menu_navegation)
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

######################################################################
###-------------------------Texting_pogram-------------------------###
######################################################################
# os.system("clear")

# direct_imagen   =   os.path.join("..", "storage/data")
# direct_texting  =   os.path.join("..", "storage/data/list")
# contenido       =   os.listdir(direct_texting)

# color   =   [
#     "#045060", "#033742", "#0790AD", "#6DDEF7",
#     "#FF9442", "#DD6C86", "#e2e2e2", "#2e2e2e",
#     "#9FDFED"
# ]

# font    =   ["Noto Serif Display", "Noto Sans"]

# ###--------------------export_contet_texting-----------------------###
# def main(page: ft.Page):

#     global  gp
#     gp  =   info_groups(color, font, direct_texting, f"{direct_imagen}/nur_black.png")
#     gp.page =   page

#     page.bgcolor    =   color[0]
#     page.padding    =   20
#     return  page.add(ft.Text(" "))

# ft.app(target=main)

