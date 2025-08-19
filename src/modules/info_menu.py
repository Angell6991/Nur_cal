import  flet    as  ft
import  webbrowser  as  wb

########################################################
###------------------Main_menu_flet------------------###
########################################################
def info_menu():
    
    # ###-------------------color_de_fondo-----------------###
    color_01    =   "#123E39"
    color_02    =   "#3E3912"
    color_03    =   "#6CDD8B"
    color_04    =   "#DD6C86"
    color_05    =   "#C0CD9E"
    color_06    =   "#A8CD9E"
    color_07    =   "#9ECDAB"
    color_08    =   "#e2e2e2"   
   
    ###------------funciones_para_eventos_clik-----------###
    def open_git(e):
        return  wb.open("https://github.com/Angell6991/Nur_cal")

    def open_blog(e):
        return  wb.open("https://stivenreyesdesign.wixsite.com/nur-juego-de-rol")
   
    def open_help(e):
        pass
        # return  

    ###-------------------contenido_del_tab--------------###
    name_app    =   ft.Text("NUR CALCULATOR", size="40", color=color_06, font_family="FreeSerif")
    img     =   ft.Text("Espacio reservado para la Imágen", size="10", color=color_05)
    
    texto   =   ft.Text(
            f"Group management and \n probabilities calculation in battle", 
            size="15", 
            color=color_08, 
            text_align=ft.TextAlign.CENTER
    )
   
    git_hut =   ft.IconButton(
        icon    =   ft.Icons.INFO, 
        tooltip =   "Project in Github",
        icon_size   =   30,
        icon_color  =   color_04,
        on_click    =   open_git,
    )

    nur_web =   ft.IconButton(
        icon    =   ft.Icons.CONTENT_PASTE_SEARCH, 
        tooltip =   "Blog NUR",
        icon_size   =   30,  
        icon_color  =   color_05,
        on_click    =   open_blog                  
    )

    help    =   ft.IconButton(
        icon    =   ft.Icons.HELP, 
        tooltip =   "Use of app",
        icon_size   =   30,  
        icon_color  =   color_05,
        on_click    =   open_help                  
    )

    botones_en_fila =   ft.Row(
        controls    =   [git_hut, nur_web, help],
        spacing     =   5,  
        alignment   =   ft.MainAxisAlignment.CENTER,  
    )

    return  [name_app, img, texto, botones_en_fila]

