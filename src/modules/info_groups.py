import  modules.data_list   as  data

import  pandas  as  pd
import  flet    as  ft
import  os 

os.system("clear")

######################################################################
###--------------------export_contet_texting-----------------------###
######################################################################
direct_texting  =   os.path.join("..", "storage/data/list")
contenido       =   os.listdir(direct_texting)

color   =   [
    "#123E39", "#3E3912", "#6CDD8B", "#DD6C86",
    "#C0CD9E", "#A8CD9E", "#9ECDAB", "#e2e2e2",   
    "#2e2e2e", "#2f4f4f"
]

######################################################################
###-------------------definition_functions-------------------------###
######################################################################

###------------------------view_data_grups-------------------------###
def view_table(direct, name):
    
    table   =   pd.read_csv(f"{direct}/{name}.dat", sep=r"\s+")
    columns =   table.columns.tolist()

    view    =   ft.DataTable(
        
        heading_row_color   =   color[5],
        sort_ascending      =   True,
        bgcolor             =   color[4],
        border              =   ft.border.all(2, color[1]),
        border_radius       =   10,
        vertical_lines      =   ft.border.BorderSide(1, color[1]),
        horizontal_lines    =   ft.border.BorderSide(1, color[1]),
        heading_row_height  =   35,
        divider_thickness   =   0,
        column_spacing      =   22,

        columns =   [ft.DataColumn(ft.Text(str(col), color=color[0]))  for col in  columns],
        rows    =   [ft.DataRow(
            [ft.DataCell(ft.Text(str(table.iloc[j,i]), color=color[8]))    for i   in  range(len(columns))]
        )   for j   in  range(5)]
    )
    return  view

###-------------------------bar_intro_data-------------------------###
def input_box(intro):
    
    intro_text  =   ft.TextField(
        label   =   str(intro), 
        color   =   color[7], 
        bgcolor =   color[9], 
        label_style =   ft.TextStyle(color=color[6]),
        border_color    =   color[6], 
        border_radius   =   10,
        border_width    =   1,
        cursor_color    =   color[6],
        cursor_height   =   20,
        cursor_radius   =   10,
        cursor_width    =   1,
        selection_color =   color[0],
    )
    return  intro_text

###----------------------button_crated_group-----------------------###
def button_new_group(action):
    
    boton   =   ft.FloatingActionButton(
        on_click    =   action, 
        icon        =   ft.Icons.ADD,
        bgcolor     =   color[5],
        foreground_color    =   color[0],
    )
    return  boton

###-------------------------button_icon-------------------------###
def button_icon(action, label, icono):
    
    boton   =   ft.FilledButton(
        content =   ft.Row([
            ft.Icon(icono, color=0, size=20),
            ft.Text(str(label), size=15, text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=8
        ),
        on_click=   action,
        color   =   color[0],
        bgcolor =   color[5],
        style   =   ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=28)),
    )
    return  boton

###-------------------------button_generic-------------------------###
def button_generic(action, label, icono):
    
    boton   =   ft.FilledButton(
        content =   ft.Text(str(label), size=15, text_align=ft.TextAlign.CENTER),
        on_click=   action,
        color   =   color[0],
        bgcolor =   color[5],
        style   =   ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=28)),
    )
    return  boton


######################################################################
###-------------------------graph_in_flet--------------------------###
######################################################################
def edit_list(page: ft.Page):

    ###---------funcion_para_guardar_name_goups_y_number_players-------###
    def new_list(e):
        
        names   =   []
        atribut =   []
        
        def save_and_exit(e):

            page.controls.clear()
            page.floating_action_button     =   button_new_group(new_list)
            page.add(graph)
            data.new_list(direct_texting, str(name_group.value), names, atribut)
            return  page.update()

        def save_players(e):
            
            def save_data(e):
                nonlocal names, atribut
                names.append(name.value)
                atribut.append([int(life.value), int(damage.value), int(dodge.value), int(attack.value), int(dices.value)])
                save_players(e)

            name    =   input_box("Name player")
            life    =   input_box("Life")
            damage  =   input_box("Damage")
            dodge   =   input_box("Dodge")
            attack  =   input_box("Attack")
            dices   =   input_box("Dices")
            button_save     =   ft.Row(
                controls    =   [button_icon(save_and_exit, "Save group exit", ft.Icons.SAVE), 
                                 button_icon(save_data, "Save player", ft.Icons.GROUP_ADD)],
                alignment   =   ft.MainAxisAlignment.CENTER,  
            )

            ###------------------------Dibujando_en_flet-----------------------###
            page.controls.clear()
            page.add(name, life, damage, dodge, attack, dices, button_save)
            return  page.update()

        name_group      =   input_box("Name group")
        button_next     =   ft.Row(
            controls    =   [button_icon(save_players, "Save and intro players", ft.Icons.SAVE_ALT)],
            alignment   =   ft.MainAxisAlignment.CENTER,  
        )

        ###------------------------Dibujando_en_flet-----------------------###
        page.floating_action_button =   None
        page.controls.clear()
        page.add(name_group, button_next)
        return page.update()

    ###------------------------Dibujando_en_flet-----------------------###
    graph   =   view_table(direct_texting, "group texting")
    page.bgcolor    =   color[0]
    page.padding    =   20
    page.scroll     =   ft.ScrollMode.HIDDEN
    page.floating_action_button     =   button_new_group(new_list)
    return  page.add(graph) 

###------------------------Texting_pogram--------------------------###
ft.app(target=edit_list)


