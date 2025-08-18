import  flet    as  ft


color_bg    =   "#bdb76b"
color_fg    =   "#3e3e3e"
# color_fg    =   "#fff0f5"


def funcion(page: ft.Page):
    
    page.bgcolor    =   color_bg
    page.horizontal_alignment   =   ft.CrossAxisAlignment.CENTER

    def cambio_texto(e):

        if  texto.value ==  "hola mundo":
            texto.value =   "mi primera app en flet"

        elif    texto.value ==  "mi primera app en flet":
            texto.value =   "hola mundo"

        return  page.update()


    texto   =   ft.Text("hola mundo", color=color_fg, size="15")
    boton   =   ft.FilledButton(
                    text="boton",
                    color=color_bg, 
                    bgcolor=color_fg, 
                    on_click=cambio_texto, 
                    style=ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=30))
                )

    return  page.add(texto, boton)

ft.app(target=funcion)


