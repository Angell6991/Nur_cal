import  modules.info_menu   as  menu

import  flet    as  ft
from    flet    import  Icons

########################################################
###-------------------Color_palette------------------###
########################################################
color   =   [
    "#123E39", "#3E3912", "#6CDD8B", "#DD6C86",
    "#C0CD9E", "#A8CD9E", "#9ECDAB", "#e2e2e2",   
    "#2e2e2e"
]

########################################################
###------------------Main_menu_flet------------------###
########################################################
def main_menu(page: ft.Page):

   
    ###----------acciones_para_la_barra_de_menu----------###
    def action_menu(e):
        
        selected_index  =   e.control.selected_index
        page.controls.clear()

        if  selected_index  ==  0:
            page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
            page.vertical_alignment     =   ft.MainAxisAlignment.CENTER  
            page.add(mn.name_app, mn.imagen, mn.texto, mn.botones_en_fila, menu_navegation)

        elif    selected_index  ==  1:
            page.add(
                ft.Text("mi primera app en flet"), 
                menu_navegation
            )

        elif    selected_index  ==  2:
            page.add(
                ft.Text("Menu de pruevas"), 
                menu_navegation
            )
        
        return  page.update()
   

    ###-------------import_module_info_menu--------------###
    mn  =   menu.info_menu(color[5], color[7], color[3], color[4], "storage/data/logo.png")

    ###---------construyendo_menu_de_navegacion----------###
    menu_navegation     =   ft.NavigationBar(
        
        selected_index  =   0,
        on_change       =   action_menu,
        bgcolor         =   color[6],
        indicator_color =   color[4],
        overlay_color   =   color[5],
        shadow_color    =   "#ffffff",
        surface_tint_color  =   "#000000",
        indicator_shape =   ft.RoundedRectangleBorder(radius=10),

        destinations    =   [
            
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.HOME_FILLED, color=color[0]), 
                label="MENU"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.EDIT_DOCUMENT, color=color[0]), 
                label="GROUPS"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.ANALYTICS_OUTLINED, color=color[0]), 
                selected_icon=ft.Icon(name=Icons.ANALYTICS, color=color[0]), 
                label="1 VS 1"
            )

        ]

    )
    
    ###----------------construct_page_main---------------###
    page.padding    =   20
    page.bgcolor    =   color[0]
    page.theme_mode =   "LIGHT"
    page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
    page.vertical_alignment     =   ft.MainAxisAlignment.CENTER   
    
    return  page.add(mn.name_app, mn.imagen, mn.texto, mn.botones_en_fila, menu_navegation)

###-----------------Start_app_in_FLET----------------###
ft.app(target=main_menu)


