import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color, title_style, max_width_style
from didacdev.components.about_item import about_item


def studies() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Educación",
            style=title_style,
        ),
        rx.vstack(
            about_item("Grado en Ingeniería Informática",
                       "UNED", "Madrid", "Sep 2020 - Presente"),
            about_item("Máster en Formación del Profesorado",
                       "UAM", "Madrid", "Sep 2018 - Jun 2019"),
            about_item("Título Superior de Música",
                       "CSKG y RCSMM", "Madrid", "Sep 2014 - Jun 2018"),
            align_items="start",
            spacing=Size.BIG.value,
            width="100%"
        ),
        align_items="start",
        spacing=Size.BIG.value,
        style=max_width_style
    )
