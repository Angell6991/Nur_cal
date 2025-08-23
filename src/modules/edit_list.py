from numpy import size
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

color_01    =   "#123E39"
color_02    =   "#3E3912"
color_03    =   "#6CDD8B"
color_04    =   "#DD6C86"
color_05    =   "#C0CD9E"
color_06    =   "#A8CD9E"
color_07    =   "#9ECDAB"
color_08    =   "#e2e2e2" 
color_09    =   "#2e2e2e"

######################################################################
###-------------------definition_functions-------------------------###
######################################################################

###------------------------view_data_grups-------------------------###
def view_table(direct, name):

    table   =   pd.read_csv(f"{direct}/{name}.dat", sep=r"\s+")
    columns =   table.columns.tolist()

    view    =   ft.DataTable(
        
        heading_row_color   =   color_06,
        sort_ascending      =   True,
        bgcolor             =   color_05,
        border              =   ft.border.all(2, color_02),
        border_radius       =   10,
        vertical_lines      =   ft.border.BorderSide(1, color_02),
        horizontal_lines    =   ft.border.BorderSide(1, color_02),
        heading_row_height  =   35,
        divider_thickness   =   0,
        column_spacing      =   22,

        columns =   [ft.DataColumn(ft.Text(str(col), color=color_01))  for col in  columns],
        rows    =   [ft.DataRow(
            [ft.DataCell(ft.Text(str(table.iloc[j,i]), color=color_09))    for i   in  range(len(columns))]
        )   for j   in  range(5)]
    )

    return  view

###----------------------button_crated_group-----------------------###
def button_new_group(action):

    boton   =   ft.FloatingActionButton(
        on_click    =   action, 
        icon        =   ft.Icons.ADD,
        bgcolor     =   color_06,
        foreground_color    =   color_01,
    )

    return  boton

###-------------------------bar_intro_data-------------------------###
def intro_bar(intro):
    intro_text  =   ft.TextField(
        label   =   str(intro), 
        color   =   color_01, 
        bgcolor =   color_07, 
        label_style =   ft.TextStyle(color=color_09),
        border_color    =   color_09, 
        border_radius   =   10,
        border_width    =   1,
        cursor_color    =   color_09,
        cursor_height   =   20,
        cursor_radius   =   10,
        cursor_width    =   1,
        selection_color =   color_08,
    )

    return  intro_text

###-------------------------generit_button-------------------------###
def generit_button(action, label):
    boton   =   ft.FilledButton(
        str(label),
        on_click=   action,
        color   =   color_01,
        bgcolor =   color_06,
        style   =   ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )
    return  boton


######################################################################
###-------------------------graph_in_flet--------------------------###
######################################################################
def edit_list(page: ft.Page):

    ###--------funcion_para_guardar_name_goups _y_number_players-------###
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

            name    =   intro_bar("Name player")
            life    =   intro_bar("Life")
            damage  =   intro_bar("Damage")
            dodge   =   intro_bar("Dodge")
            attack  =   intro_bar("Attack")
            dices   =   intro_bar("Dices")
            button_save     =   ft.Row(
                controls    =   [generit_button(save_and_exit, "Save list and exit"), 
                                 generit_button(save_data, "Save data and next player")],
                alignment   =   ft.MainAxisAlignment.CENTER,  
            )

            ###------------------------Dibujando_en_flet-----------------------###
            page.controls.clear()
            page.add(name, life, damage, dodge, attack, dices, button_save)
            return  page.update()

        name_group      =   intro_bar("Name group")
        button_next     =   ft.Row(
            controls    =   [generit_button(save_players, "Save name and intro players")],
            alignment   =   ft.MainAxisAlignment.CENTER,  
        )

        ###------------------------Dibujando_en_flet-----------------------###
        page.floating_action_button =   None
        page.controls.clear()
        page.add(name_group, button_next)
        return page.update()

    ###------------------------Dibujando_en_flet-----------------------###
    graph   =   view_table(direct_texting, "group texting")
    page.bgcolor    =   color_01
    page.padding    =   20
    page.scroll     =   ft.ScrollMode.HIDDEN
    page.floating_action_button     =   button_new_group(new_list)
    
    return  page.add(graph) 

###------------------------Texting_pogram--------------------------###
ft.app(target=edit_list)


