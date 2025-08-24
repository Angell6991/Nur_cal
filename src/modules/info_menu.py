import  flet    as  ft

########################################################
###------------------Main_menu_flet------------------###
########################################################
class   info_menu:

    def __init__ (self, color_title, color_text, color_git, color_blog, font, dir_imagen):

        ###-------------------contenido_del_tab--------------###
        self.name_app    =   ft.Text(
            "Nur Calculator", 
            size    =   "50", 
            color   =   color_title, 
            weight  =   ft.FontWeight.BOLD,
            italic  =   True,
            font_family =   font[0] 
        )

        self.imagen      =   ft.Image(src=str(dir_imagen), width=200) 

        self.texto   =   ft.Text(
                f"Group management and \n probabilities calculation in battle", 
                size    =   "18", 
                color   =   color_text, 
                text_align  =   ft.TextAlign.CENTER,
                # weight  =   ft.FontWeight.BOLD,
                # italic  =   True,
                font_family =   font[1]
        )
       
        self.git_hut =   ft.IconButton(
            url     =   "https://github.com/Angell6991/Nur_cal",
            icon    =   ft.Icons.INFO, 
            tooltip =   "Project in Github",
            icon_size   =   30,
            icon_color  =   color_git,
        )

        self.nur_web =   ft.IconButton(
            url     =   "https://stivenreyesdesign.wixsite.com/nur-juego-de-rol",                  
            icon    =   ft.Icons.CONTENT_PASTE_SEARCH, 
            tooltip =   "Blog NUR",
            icon_size   =   30,  
            icon_color  =   color_blog,
        )

        self.botones_en_fila =   ft.Row(
            controls    =   [self.git_hut, self.nur_web],
            spacing     =   5,  
            alignment   =   ft.MainAxisAlignment.CENTER,  
        )


