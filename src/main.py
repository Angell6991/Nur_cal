import  modules.info_menu   as  menu
import  modules.info_groups as  group
import  modules.info_versus as  versus

import  flet    as  ft
import  os

from    flet    import  Icons

########################################################
###-------------------Color_palette------------------###
########################################################
color   =   [
    "#045060", "#033742", "#0790AD", "#6DDEF7",
    "#FF9442", "#DD6C86", "#e2e2e2", "#2e2e2e",
    "#9FDFED"
]

font_dir    =   [
    "assets/fonts/NotoSerifDisplay-BoldItalic.ttf",
    "assets/fonts/Ubuntu-R.ttf",
    "assets/fonts/3270NerdFont-SemiCondensed.ttf"
]

direct_imagen   =   "storage/data"
# direct_list     =   "storage/data/list"

dest    =   os.path.join(os.getcwd(), ".Nur_data_list")
os.makedirs(dest, exist_ok=True)
direct_list = dest


########################################################
###------------------Main_menu_flet------------------###
########################################################
def main_menu(page: ft.Page):

    ###------------------fonts---------------------------###
    page.fonts  =   {
        "title":  font_dir[0],
        "text":   font_dir[1],
        "icons":  font_dir[2],
    }
    font    =   ["title", "text", "icons"]
   
    ###----------acciones_para_la_barra_de_menu----------###
    def action_menu(e):
        
        selected_index  =   e.control.selected_index
        page.controls.clear()

        if  selected_index  ==  0:
            gp  =   group.info_groups(
                color, 
                font, 
                direct_list, 
                f"{direct_imagen}/nur_black.png",
                f"{direct_imagen}/nur_blue.png",
                f"{direct_imagen}/logo_03.png",
            )
            gp.page =   page
            gp.init_menu(menu_navegation)

        elif    selected_index  ==  1:
            mn  =   menu.info_menu(color[4], color[6], color[8], color[4], font, f"{direct_imagen}/logo.png")
            mn.page =   page
            mn.main_menu(menu_navegation)

        elif    selected_index  ==  2:
            vs  =   versus.info_versus(color, font, direct_list, f"{direct_imagen}/logo_02.png")
            vs.page =   page
            vs.main_menu(menu_navegation)
        
        return  page.update()
   

    ###-------------import_module_info_menu--------------###
    mn  =   menu.info_menu(color[4], color[6], color[8], color[4], font, f"{direct_imagen}/logo.png")
    mn.page =   page
    
    ###---------construyendo_menu_de_navegacion----------###
    menu_navegation     =   ft.NavigationBar(
        
        selected_index  =   1,
        on_change       =   action_menu,
        bgcolor         =   color[8],
        indicator_color =   color[6],
        overlay_color   =   color[2],
        shadow_color    =   "#ffffff",
        surface_tint_color  =   "#000000",
        indicator_shape =   ft.RoundedRectangleBorder(radius=10),

        destinations    =   [
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.EDIT_DOCUMENT, color=color[0]), 
                label="GROUPS"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.HOME_FILLED, color=color[0]), 
                label="MENU"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(name=ft.Icons.ANALYTICS, color=color[0]), 
                # selected_icon=ft.Icon(name=Icons.ANALYTICS_OUTLINED, color=color[0]), 
                label="1 VS 1"
            )
        ]
    )
    
    ###----------------construct_page_main---------------###
    page.padding    =   20
    page.bgcolor    =   color[0]
    page.theme_mode =   "LIGHT"
    # page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment     =   ft.MainAxisAlignment.CENTER   
    return  mn.main_menu(menu_navegation)

###-----------------Start_app_in_FLET----------------###
ft.app(target=main_menu)


