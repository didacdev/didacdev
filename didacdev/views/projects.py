import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color, max_width_style, title_style
from didacdev.components.social_link import social_link


def projects() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Proyectos",
            style=title_style,
        ),
        rx.text("Aplicaciones que he desarrollado",
                font_size=Size.DEFAULT.value),
        style=max_width_style
    )
