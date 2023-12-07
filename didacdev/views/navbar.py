import reflex as rx

import didacdev.constants as const
from didacdev.components.link_icon import link
from didacdev.styles.styles import Size, Color


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Didacdev",
                src="logo.png",
                size="lg",
                bg=Color.PRIMARY.value,
                padding="2px",
                border="2px",
                border_color=Color.SECONDARY.value,
                margin_right=Size.DEFAULT.value,
            ),
            rx.text("DidacDev"),
            rx.spacer(),
            link("github", const.GITHUB_URL),
            link("linkedin", const.LINKEDIN_URL),
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )
