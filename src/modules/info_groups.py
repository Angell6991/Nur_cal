import  modules.data_list   as  data

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

######################################################################
###-------------------Definitions_functions------------------------###
######################################################################

    ###------------------------view_data_grups-------------------------###
    def view_table(self, direct, name):
        
        table   =   pd.read_csv(f"{direct}/{name}.dat", sep=r"\s+")
        columns =   table.columns.tolist()

        view    =   ft.DataTable(
            
            heading_row_color   =   self.color[5],
            sort_ascending      =   True,
            bgcolor             =   self.color[4],
            border              =   ft.border.all(2, color[1]),
            border_radius       =   10,
            vertical_lines      =   ft.border.BorderSide(1, color[1]),
            horizontal_lines    =   ft.border.BorderSide(1, color[1]),
            heading_row_height  =   35,
            divider_thickness   =   0,
            column_spacing      =   22,

            columns =   [ft.DataColumn(ft.Text(str(col), color=self.color[0]))  for col in  columns],
            rows    =   [ft.DataRow(
                [ft.DataCell(ft.Text(str(table.iloc[j,i]), color=self.color[8]))    for i   in  range(len(columns))]
            )   for j   in  range(5)]
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
            bgcolor     =   self.color[8],
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
    def button_group_list(self):
        
        def boton(name):
            boton   =   ft.TextButton(
                content =   ft.Row([
                    ft.Icon(ft.Icons.LIST_ROUNDED, size=40, color=color[6]),
                    ft.Text(
                        str(name), size=25, text_align=ft.TextAlign.CENTER, 
                        color=color[6], font_family=self.font[1], weight  =   ft.FontWeight.BOLD
                    ),
                ], alignment=ft.VerticalAlignment.START, spacing=10
                )
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
                height  = 400   
            )

        elif    len(lista)  !=  0:
            lista   =   [filename.replace(".dat", "") for filename in lista]    
            lista   =   [boton(i) for i in lista]
            lista_groups    =   ft.Container(
                content =   ft.Column(lista, scroll=ft.ScrollMode.HIDDEN),
                bgcolor =   self.color[1], 
                border_radius   =   15, 
                padding =   ft.padding.all(20),
                height  = 400   
                # border  =   ft.border.all(2, color[3]),
            )

        return  lista_groups

    ###-------------------------init_menu_grups------------------------###
    def init_menu(self):
        cont    =   ft.Container(
            content =   ft.Column(
                [self.baner_group(), self.button_group_list()], spacing=20)
        )
        return  cont



######################################################################
###-------------------------graph_in_flet--------------------------###
######################################################################
# def edit_list(page: ft.Page):

#     ###---------funcion_para_guardar_name_goups_y_number_players-------###
#     def new_list(e):
        
#         names   =   []
#         atribut =   []
        
#         def save_and_exit(e):

#             page.controls.clear()
#             page.floating_action_button     =   button_new_group(new_list)
#             page.add(graph)
#             data.new_list(direct_texting, str(name_group.value), names, atribut)
#             return  page.update()

#         def save_players(e):
            
#             def save_data(e):
#                 nonlocal names, atribut
#                 names.append(name.value)
#                 atribut.append([int(life.value), int(damage.value), int(dodge.value), int(attack.value), int(dices.value)])
#                 save_players(e)

#             name    =   input_box("Name player")
#             life    =   input_box("Life")
#             damage  =   input_box("Damage")
#             dodge   =   input_box("Dodge")
#             attack  =   input_box("Attack")
#             dices   =   input_box("Dices")
#             button_save     =   ft.Row(
#                 controls    =   [button_icon(save_and_exit, "Save group exit", ft.Icons.SAVE), 
#                                  button_icon(save_data, "Save player", ft.Icons.GROUP_ADD)],
#                 alignment   =   ft.MainAxisAlignment.CENTER,  
#             )

#             ###------------------------Dibujando_en_flet-----------------------###
#             page.controls.clear()
#             page.add(name, life, damage, dodge, attack, dices, button_save)
#             return  page.update()

#         name_group      =   input_box("Name group")
#         button_next     =   ft.Row(
#             controls    =   [button_icon(save_players, "Save and intro players", ft.Icons.SAVE_ALT)],
#             alignment   =   ft.MainAxisAlignment.CENTER,  
#         )

#         ###------------------------Dibujando_en_flet-----------------------###
#         page.floating_action_button =   None
#         page.controls.clear()
#         page.add(name_group, button_next)
#         return page.update()

#     ###------------------------Dibujando_en_flet-----------------------###
#     graph   =   view_table(direct_texting, "group texting")
#     page.bgcolor    =   color[0]
#     page.padding    =   20
#     page.scroll     =   ft.ScrollMode.HIDDEN
#     page.floating_action_button     =   button_new_group(new_list)
#     return  page.add(graph) 

###------------------------Texting_pogram--------------------------###
# ft.app(target=edit_list)



######################################################################
###-------------------------Texting_pogram-------------------------###
######################################################################
os.system("clear")

direct_imagen   =   os.path.join("..", "storage/data")
direct_texting  =   os.path.join("..", "storage/data/list")
contenido       =   os.listdir(direct_texting)
color   =   [
    "#045060", "#033742", "#0790AD", "#6DDEF7",
    "#FF9442", "#DD6C86", "#e2e2e2", "#2e2e2e",
    "#9FDFED"
]
font    =   ["Noto Serif Display", "Noto Sans"]
gp  =   info_groups(color, font, direct_texting, f"{direct_imagen}/nur_black.png")

###--------------------export_contet_texting-----------------------###
def main(page: ft.Page):

    page.bgcolor    =   color[0]
    page.padding    =   20
    page.floating_action_button =   gp.button_new_group(None)
    return  page.add(gp.init_menu())

ft.app(target=main)


