import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color
from didacdev.components.page_link import page_link
from didacdev.components.social_link import social_link


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="logo.png",
                width="8em",
            ),
            rx.spacer(),
            page_link("_home", "#"),
            page_link("_didacdev", "#"),
            page_link("_proyectos", "#"),
            rx.spacer(),
            social_link("github", "#"),
            social_link("linkedin", "#"),
            width="100%"
        ),
        bg=Color.BACKGROUND.value,
        position="sticky",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )
