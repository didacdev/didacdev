import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color, title_style, max_width_style
from didacdev.components.about_item import about_item


def job() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Experiencia",
            style=title_style,
        ),
        rx.vstack(
            about_item("Coordinador de proyectos",
                       "Music Box Learning S.L", "Madrid", "Sep 2019 - Presente"),
            align_items="start",
            spacing=Size.BIG.value,
            width="100%"
        ),
        align_items="start",
        spacing=Size.BIG.value,
        style=max_width_style
    )
