import  modules.data_list   as  data

import  pandas  as  pd
import  flet    as  ft
import  os 

os.system("clear")

direct_texting  =   os.path.join("..", "storage/data/list")
contenido       =   os.listdir(direct_texting)

######################################################################
###----------------------------------------------------------------###
######################################################################

def edit_list(page: ft.Page):
      
    def action_boton(e):
        return  page.add(ft.Text(str(contenido), size=30))

    texto   =   ft.Text("hola mundo")

    boton   =   ft.FloatingActionButton(
        on_click    =   action_boton, 
        icon        =   ft.Icons.ADD,
        bgcolor     =   "#2e2e2e",
        foreground_color    =   "#e2e2e2",
    )
   
    page.padding = 20
    page.scroll = ft.ScrollMode.HIDDEN
    page.floating_action_button     =   boton

    return  page.add(texto)

######################################################################
###------------------------Texting_pogram--------------------------###
######################################################################
ft.app(target=edit_list)



# import flet as ft


# def main(page: ft.Page):
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.padding = 20
#     page.scroll = ft.ScrollMode.HIDDEN

#     # keeps track of the number of tiles already added
#     count = 1

#     def fab_pressed(e):
#         nonlocal count  # to modify the count variable found in the outer scope
#         page.add(
#             ft.ListTile(
#                 title=ft.Text(f"Tile {count}"),
#                 bgcolor=ft.Colors.TEAL_300,
#                 leading=ft.Icon(
#                     ft.Icons.CIRCLE_OUTLINED, color=ft.Colors.DEEP_ORANGE_300
#                 ),
#                 on_click=lambda x: print(x.control.title.value + " was clicked!"),
#             )
#         )
#         count += 1

#     page.floating_action_button = ft.FloatingActionButton(
#         icon=ft.Icons.ADD, on_click=fab_pressed, bgcolor=ft.Colors.LIME_300
#     )

#     page.add(
#         ft.Container(
#             ft.Row(
#                 [
#                     ft.Text(
#                         "Floating Action Button Example",
#                         style=ft.TextStyle(size=20, weight=ft.FontWeight.W_500),
#                     )
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#             ),
#             bgcolor=ft.Colors.BLUE,
#             padding=ft.padding.all(20),
#         ),
#     )


# ft.app(main)

