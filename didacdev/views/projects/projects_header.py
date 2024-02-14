import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color, title_style


def projects_header() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Proyectos",
            style=title_style,
        ),
        rx.text(
            "Aplicaciones que he desarrollado",
            font_size=Size.DEFAULT.value
        ),
        margin_top=Size.BIG.value,
    )
