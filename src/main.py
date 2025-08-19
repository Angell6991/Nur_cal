import  modules.info_menu   as  info

import  flet    as  ft
from    flet    import  Icons

########################################################
###-------------------Color_palette------------------###
########################################################
color_01    =   "#123E39"
color_02    =   "#3E3912"
color_03    =   "#6CDD8B"
color_04    =   "#DD6C86"
color_05    =   "#C0CD9E"
color_06    =   "#A8CD9E"
color_07    =   "#9ECDAB"
color_08    =   "#e2e2e2"   
    
########################################################
###------------------Main_menu_flet------------------###
########################################################
def main_menu(page: ft.Page):

    ###-------------------color_de_fondo-----------------###
    page.bgcolor    =   color_01
    page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
    page.vertical_alignment     =   ft.MainAxisAlignment.CENTER   
 
    ###----------acciones_para_la_barra_de_menu----------###
    def action_menu(e):
        
        selected_index  =   e.control.selected_index
        page.controls.clear()

        if  selected_index  ==  0:
            page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
            page.vertical_alignment     =   ft.MainAxisAlignment.CENTER   
            page.add(
                *info.info_menu(color_06, color_08, color_04, color_05, "storage/data/logo.png"),
                menu_navegation
            )

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
    
    ###---------construyendo_menu_de_navegacion----------###
    menu_navegation     =   ft.NavigationBar(
        
        selected_index  =   0,
        on_change       =   action_menu,
        bgcolor         =   color_07,
        indicator_color =   color_05,
        overlay_color   =   color_06,
        shadow_color    =   "#ffffff",
        surface_tint_color  =   "#000000",
        indicator_shape =   ft.RoundedRectangleBorder(radius=10),

        destinations    =   [
            
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.HOME_FILLED, color=color_01), 
                label="MENU"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.EDIT_DOCUMENT, color=color_01), 
                label="GROUPS"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.ANALYTICS_OUTLINED, color=color_01), 
                selected_icon=ft.Icon(name=Icons.ANALYTICS, color=color_01), 
                label="1 VS 1"
            )

        ]

    )
    
    return  page.add(*info.info_menu(color_06, color_08, color_04, color_05, "storage/data/logo.png"), menu_navegation)

###-----------------Start_app_in_FLET----------------###
ft.app(target=main_menu)


