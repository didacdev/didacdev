import reflex as rx

from didacdev.styles.styles import Size, title_style, max_width_style
from didacdev.components.language import language


def languages() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Idiomas",
            style=title_style,
        ),
        rx.vstack(
            language("Inglés C1 Advanced",
                     "Jul 2019"),
            align_items="start",
            width="100%"
        ),
        align_items="start",
        spacing=Size.BIG.value,
        style=max_width_style
    )
