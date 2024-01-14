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
from utils.vistaMaquinaria import TabContentVistaMaquinaria
from utils.vistaTrabajadores import TabContentVistaTrabajadores
from utils.vistaFaenas import TabContentVistaFaenas
from utils.vistaHome import TabcontentVistaHome

def main(page: ft.Page):
    page.title = "SISTEMA DE CONTROL Y SEGUIMIENTO DE MAQUINAS VEHICULOS Y EQUIPOS(SCS)"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
   
    # create application instance
    #todo = TodoApp()

    #icon_content = TabContentIcon()
    maquinariavista = TabContentVistaMaquinaria()
    maquinariatrabajador = TabContentVistaTrabajadores()
    maquinariafaena = TabContentVistaFaenas()
    maquinariahome = TabcontentVistaHome()
    # tooltip_content = TabContentTooltip()
    # progress_ring_content = TabContentProgressRing()
    # progress_bar_content = TabContentProgressBar()
    # divider_content = TabContentDivider()
    # vertical_divider_content = TabContentVerticalDivider()
    # circle_avatar_content = TabContentCircleAvatar()
    # border_radius_content = TabContentBorderRadius()
    # padding_content = TabContentPadding()
    # icons_browser_content = TabContentIconsBrowser()
    # colors1_content = TabContentColors1()
    # colors2_content = TabContentColors2(page)
    # alignment_content = TabContentAlignment()
    # shape_content = TabContentShape()
    # shadow_content = TabContentShadow()
    # blur_content = TabContentBlur()
    # border_content = TabContentBorder()
    # linear_gradient_content = TabContentLinearGradient()
    # radial_gradient_content = TabContentRadialGradient()
    # sweep_gradient_content = TabContentSweepGradient()
    # shader_mask_content = TabContentShaderMask()
    # Estrucutura principal del proyecto
    page.add(

        ft.Tabs(
            expand=True,
            selected_index=0,
            tabs=[
                ft.Tab(
                    icon=ft.icons.HOME,
                    text="Home",
                    content=maquinariahome
                ),
                ft.Tab(
                    icon=ft.icons.DIRECTIONS_CAR_FILLED,
                    text="Maquinaria",
                    content=maquinariavista
                ),
                ft.Tab(
                    icon=ft.icons.PERSON,
                    text="Trabajadores",
                    content=maquinariatrabajador
                ),
                ft.Tab(
                    icon=ft.icons.BOOK,
                    text="Faenas",
                    content=maquinariafaena
                )
            ]
        ),
        ft.Text(
            "Hecho con amor ❤ por El Olimpus!",
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