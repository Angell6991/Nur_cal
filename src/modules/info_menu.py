import  flet    as  ft
import  webbrowser  as  wb


########################################################
###------------------Main_menu_flet------------------###
########################################################
def info_menu(color_title, color_text, color_git, color_blog, dir_imagen):
    
    ###-------------------contenido_del_tab--------------###
    name_app    =   ft.Text("NUR CALCULATOR", size="40", color=color_title, font_family="FreeSerif")
    imagen      =   ft.Image(src=str(dir_imagen), width=200) 

    texto   =   ft.Text(
            f"Group management and \n probabilities calculation in battle", 
            size    =   "15", 
            color   =   color_text, 
            text_align  =   ft.TextAlign.CENTER
    )
   
    git_hut =   ft.IconButton(
        url     =   "https://github.com/Angell6991/Nur_cal",
        icon    =   ft.Icons.INFO, 
        tooltip =   "Project in Github",
        icon_size   =   30,
        icon_color  =   color_git,
    )

    nur_web =   ft.IconButton(
        url     =   "https://stivenreyesdesign.wixsite.com/nur-juego-de-rol",                  
        icon    =   ft.Icons.CONTENT_PASTE_SEARCH, 
        tooltip =   "Blog NUR",
        icon_size   =   30,  
        icon_color  =   color_blog,
    )

    botones_en_fila =   ft.Row(
        controls    =   [git_hut, nur_web],
        spacing     =   5,  
        alignment   =   ft.MainAxisAlignment.CENTER,  
    )

    menu    =   [name_app, imagen, texto, botones_en_fila]
    return  menu


