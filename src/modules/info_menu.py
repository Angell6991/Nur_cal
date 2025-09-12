import  flet    as  ft

########################################################
###------------------Main_menu_flet------------------###
########################################################
class   info_menu:

    def __init__ (self, color_title, color_text, color_git, color_blog, font, dir_imagen):

        ###-------------------contenido_del_tab--------------###
        self.page   =   None

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
                size    =   "15", 
                color   =   color_text, 
                text_align  =   ft.TextAlign.CENTER,
                weight  =   ft.FontWeight.BOLD,
                italic  =   True,
                font_family =   font[1]
        )
       
        self.git_hut   =   ft.TextButton(
            content =   ft.Text(" ", size=30, color=color_git, font_family=font[2]),
            url     =   "https://github.com/Angell6991/Nur_cal",
            style   =   ft.ButtonStyle(shape=ft.CircleBorder(), padding=5),
        )

        self.nur_web   =   ft.TextButton(
            content =   ft.Text("󰖟 ", size=30, color=color_blog, font_family=font[2]),
            url     =   "https://stivenreyesdesign.wixsite.com/nur-juego-de-rol",                  
            style   =   ft.ButtonStyle(shape=ft.CircleBorder(), padding=5),
        )

        self.botones_en_fila =   ft.Row(
            controls    =   [self.git_hut, self.nur_web],
            spacing     =   5,  
            alignment   =   ft.MainAxisAlignment.CENTER,  
        )
        
    ########################################################
    ###------------------Main_menu_flet------------------###
    ########################################################
    def main_menu(self, menu_navegation):
        self.page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment     =   ft.MainAxisAlignment.CENTER  
        self.page.floating_action_button =   None
        self.page.add(self.name_app, self.imagen, self.texto, self.botones_en_fila, menu_navegation)
        return  self.page.update()


