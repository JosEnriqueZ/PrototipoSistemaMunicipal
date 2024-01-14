#importaciones
import flet as ft
from random import choice
from utils.padding_utils import TabContentPadding
from utils.alignment_utils import TabContentAlignment
from utils.border_utils import TabContentBorder
from utils.border_radius_utils import TabContentBorderRadius
from utils.colors_utils import TabContentColors1, TabContentColors2
from utils.icons_browser_utils import TabContentIconsBrowser
from utils.gradient_utils import TabContentLinearGradient, TabContentSweepGradient, TabContentRadialGradient
from utils.shadermask_utils import TabContentShaderMask
from utils.shape_utils import TabContentShape
from utils.tooltip_utils import TabContentTooltip
from utils.icon_utils import TabContentIcon
from utils.progress_ring_utils import TabContentProgressRing
from utils.progress_bar_utils import TabContentProgressBar
from utils.divider_utils import TabContentDivider
from utils.vertical_divider_utils import TabContentVerticalDivider
from utils.circle_avatar_utils import TabContentCircleAvatar
from utils.shadow_utils import TabContentShadow
from utils.blur_utils import TabContentBlur


def pruebas( numero ):
    print(numero+1)
    variable=numero
    return numero

# class Task(ft.UserControl):
#     def __init__(self):
#         super().__init__()
#     def build(self):
#         self.display_task = ft.Checkbox(value=False, label=self.task_name)
#         self.edit_name = ft.TextField(expand=1)

#         self.display_view = ft.Row(
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[
#                 self.display_task,
#                 ft.Row(
#                     spacing=0,
#                     controls=[
#                         ft.IconButton(
#                             icon=ft.icons.CREATE_OUTLINED,
#                             tooltip="Edit To-Do",
#                             on_click=self.edit_clicked,
#                         ),
#                         ft.IconButton(
#                             ft.icons.DELETE_OUTLINE,
#                             tooltip="Delete To-Do",
#                             on_click=self.delete_clicked,
#                         ),
#                     ],
#                 ),
#             ],
#         )

#         self.edit_view = ft.Row(
#             visible=False,
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#             vertical_alignment=ft.CrossAxisAlignment.CENTER,
#             controls=[
#                 self.edit_name,
#                 ft.IconButton(
#                     icon=ft.icons.DONE_OUTLINE_OUTLINED,
#                     icon_color=ft.colors.GREEN,
#                     tooltip="Update To-Do",
#                     on_click=self.save_clicked,
#                 ),
#             ],
#         )
#         return ft.Column(controls=[self.display_view, self.edit_view])

#     def edit_clicked(self, e):
#         self.edit_name.value = self.display_task.label
#         self.display_view.visible = False
#         self.edit_view.visible = True
#         self.update()

#     def save_clicked(self, e):
#         self.display_task.label = self.edit_name.value
#         self.display_view.visible = True
#         self.edit_view.visible = False
#         self.update()

#     def delete_clicked(self, e):
#         self.task_delete(self)

# class TodoApp(ft.UserControl):
#     def build(self):
#         self.new_task = ft.TextField(hint_text="Que necesitas agregar", expand=True)
#         self.tasks = ft.Column()

#         # application's root control (i.e. "view") containing all other controls
#         return ft.Column(
#             width=800,
#             controls=[
#                 ft.Row(
#                     controls=[
#                         self.new_task,
#                         ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
#                     ],
#                 ),
#                 self.tasks,
#             ],
#         )

#     def add_clicked(self, e):
#         task = Task(self.new_task.value, self.task_delete)
#         self.tasks.controls.append(task)
#         self.new_task.value = ""
#         self.update()
    
#     def task_delete(self, task):
#         self.tasks.controls.remove(task)
#         self.update()

# class App(ft.UserControl):
#   def __init__(self,pg):
#     super().__init__()
#     # pg.bgcolor = colors.TRANSPARENT
#     # pg.window_bgcolor = colors.TRANSPARENT
#     # pg.window_title_bar_hidden =True
#     # pg.window_frameless = True
#     self.pg = pg
#     self.animation_style = ft.animation.Animation(500,ft.AnimationCurve.DECELERATE)       
#     self.init_helper()
#   def init_helper(self):
#     self.side_bar_column = ft.Column(
#         spacing=0,
#         controls=[
#           ft.Row(
#             controls=[
#               ft.Container(
#                 data = 0,
#                 on_click=lambda e: self.switch_page(e,'page1'),
#                 expand=True,
#                 height=40,
#                 content=ft.Icon(
#                   ft.icons.CHAT_BUBBLE,
#                   color='blue'
#                 ),
#               ),
#             ]
#           ),        
#           ft.Row(
#             controls=[
#               ft.Container(
#                 on_click=lambda e: self.switch_page(e,'page2'),
#                 data = 1,
#                 expand=True,
#                 height=40,
#                 content=ft.Icon(
#                   ft.icons.BADGE,
#                   color='blue'
#                 ),
#               ),
#             ]
#           ),
#           ft.Row(
#             controls=[
#               ft.Container(
#                 expand=True,
#                 height=40,
#                 data = 2,
#                 on_click=lambda e: self.switch_page(e,'page3'),
#                 content=ft.Icon(
#                   ft.icons.AUDIO_FILE,
#                   color='blue'
#                 ),
#               ),
#             ]
#           ),
#         ]
#       )
#     self.indicator =ft.container(
#       height=40,
#       bgcolor='red',
#       offset=ft.transform.Offset(0,0),
#       animate_offset=ft.animation.Animation(500,ft.AnimationCurve.DECELERATE)
#     )
#     self.page1 = ft.Container(
#       alignment=ft.alignment.center,
#       offset=ft.transform.Offset(0,0),
#       animate_offset=self.animation_style,
#       bgcolor='blue',
#       content=ft.Text('Hola mundo 1',size=50)
#     )
#     self.page2 = ft.Container(
#       alignment=ft.alignment.center,
#       offset=ft.transform.Offset(0,0),
#       animate_offset=self.animation_style,
#       bgcolor='green',
#       content=ft.Text('Hola mundo 1 2',size=50)
#     )
#     self.page3 = ft.Container(
#       alignment=ft.alignment.center,
#       offset=ft.transform.Offset(0,0),
#       animate_offset=self.animation_style,
#       bgcolor='orange',
#       content=ft.Text('Hola mundo 1 3',size=50),
#     )
#     self.switch_control = {
#       'page1':self.page1,
#       'page2':self.page2,
#       'page3':self.page3,
#     }
#     self.pg.add(
#       ft.Container(
#         bgcolor='white',
#         expand=True,
#         content=ft.Row(
#           spacing=0,
#           controls=[
#             ft.Container(
#               width=80,
#               # bgcolor='green',
#               border=ft.border.only(right=ft.border.BorderSide(width=1,color='#22888888'),),
#               content=ft.Column(
#                 alignment='spaceBetween',
#                 controls=[              
#                   ft.Container(
#                     height=100,
#                     # bgcolor='blue'
#                   ),
#                   ft.Container(
#                     height=500,
#                     content=ft.Row(
#                       spacing=0,
#                       controls=[
#                         ft.Container(
#                           expand=True,
#                           content=self.side_bar_column,
#                         ),
#                         ft.Container(
#                           width=3,
#                           content=ft.Column(
#                             controls=[
#                               self.indicator,
#                             ]
#                           ),
#                         ),
#                       ]
#                     )
#                   ),
#                   ft.Container(
#                     height=50,
#                   ),
#                 ]
#               )
#             ),
#             ft.Container(
#               expand=True,
#               content=ft.Stack(
#                 controls=[
#                   self.page1,
#                   self.page2,
#                   self.page3,

#                 ]
#               )
#             ),
#           ]
#         )
#       )
#     )
#   def switch_page(self,e,point):
#     print(point)
#     for page in self.switch_control:
#       self.switch_control[page].offset.x = 2
#       self.switch_control[page].update()
#     self.switch_control[point].offset.x = 0
#     self.switch_control[point].update()  
#     self.indicator.offset.y = e.control.data
#     self.indicator.update()



def main(page: ft.Page):
    page.title = "SISTEMA DE CONTROL Y SEGUIMIENTO DE MAQUINAS VEHICULOS Y EQUIPOS(SCS)"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    variable=0
    #Navegador
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        #leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.DIRECTIONS_CAR_FILLED, 
                selected_icon=ft.icons.DIRECTIONS_CAR_FILLED, 
                label="Maquinarias",
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.PERSON),
                selected_icon_content=ft.Icon(ft.icons.PERSON),
                label="Trabajadores",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOK,
                selected_icon_content=ft.Icon(ft.icons.BOOK),
                label_content=ft.Text("Faenas"),
            ),
        ],
        # on_change=lambda e: print("Hiciste click en:", e.control.selected_index)
        on_change=lambda e: pruebas(e.control.selected_index)
                            if e.control.selected_index == 0 
                            else pruebas(e.control.selected_index) if e.control.selected_index == 1 
                            else pruebas(e.control.selected_index) if e.control.selected_index == 2 
                            else page.update()
        
    )
    #imagen
    # img = ft.Image(
    #     src=f"img/camion.png",
    #     width=1080,
    #     height=600,
    #     fit=ft.ImageFit.CONTAIN,
    # )

   
    # create application instance
    #todo = TodoApp()

    icon_content = TabContentIcon()
    tooltip_content = TabContentTooltip()
    progress_ring_content = TabContentProgressRing()
    progress_bar_content = TabContentProgressBar()
    divider_content = TabContentDivider()
    vertical_divider_content = TabContentVerticalDivider()
    circle_avatar_content = TabContentCircleAvatar()
    border_radius_content = TabContentBorderRadius()
    padding_content = TabContentPadding()
    icons_browser_content = TabContentIconsBrowser()
    colors1_content = TabContentColors1()
    colors2_content = TabContentColors2(page)
    alignment_content = TabContentAlignment()
    shape_content = TabContentShape()
    shadow_content = TabContentShadow()
    blur_content = TabContentBlur()
    border_content = TabContentBorder()
    linear_gradient_content = TabContentLinearGradient()
    radial_gradient_content = TabContentRadialGradient()
    sweep_gradient_content = TabContentSweepGradient()
    shader_mask_content = TabContentShaderMask()
    # Estrucutura principal del proyecto
    page.add(

        ft.Tabs(
            expand=True,
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="Icon",
                    content=icon_content
                ),
                ft.Tab(
                    text="Tooltip",
                    content=tooltip_content
                ),
                ft.Tab(
                    text="ProgressRing",
                    content=progress_ring_content
                ),
                ft.Tab(
                    text="ProgressBar",
                    content=progress_bar_content
                ),
                ft.Tab(
                    text="Divider",
                    content=divider_content
                ),
                ft.Tab(
                    text="VerticalDivider",
                    content=vertical_divider_content
                ),
                ft.Tab(
                    text="CircleAvatar",
                    content=circle_avatar_content
                ),
                ft.Tab(
                    text="Shadow",
                    content=shadow_content
                ),
                ft.Tab(
                    text="Blur",
                    content=blur_content
                ),
                ft.Tab(
                    text="BorderRadius",
                    content=border_radius_content
                ),
                ft.Tab(
                    text="Padding",
                    content=padding_content
                ),
                ft.Tab(
                    text="Icons Browser",
                    content=icons_browser_content
                ),
                ft.Tab(
                    text="Colors V1",
                    content=colors1_content
                ),
                ft.Tab(
                    text="Colors V2",
                    content=colors2_content
                ),
                ft.Tab(
                    text="Alignment",
                    content=alignment_content
                ),
                ft.Tab(
                    text="Shape",
                    content=shape_content
                ),
                ft.Tab(
                    text="Border",
                    content=border_content
                ),
                ft.Tab(
                    text="Linear Gradient",
                    content=linear_gradient_content
                ),
                ft.Tab(
                    text="Radial Gradient",
                    content=radial_gradient_content
                ),
                ft.Tab(
                    text="Sweep Gradient",
                    content=sweep_gradient_content
                ),
                ft.Tab(
                    text="Shader Mask",
                    content=shader_mask_content
                ),
            ]
        ),
        ft.Text(
            "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
            style=ft.TextThemeStyle.LABEL_SMALL,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color=ft.colors.BLUE_900,
        )

        
        # ft.Row(
        #     [
        #         todo,ft.VerticalDivider(width=1)
        #         #ft.Column([ todo], alignment=ft.MainAxisAlignment.START, expand=True)
        #     ],
        #     expand=True,
        # )
    )



    # page.add(todo)

ft.app(target=main)