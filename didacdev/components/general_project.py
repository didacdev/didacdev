import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color


def general_project(header: str, link: str, github_link: str, body: str, stack: str, front: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=front,
            border_radius="10px 10px 0 0",
            width="100%"
        ),
        rx.vstack(
            rx.heading(
                header,
                size="sm",
            ),
            rx.text(
                body,
                text_align="center",
                margin_top=Size.MEDIUM.value,
                font_size=Size.SMALL.value,
                height="44%"
            ),
            rx.box(
                rx.span(
                    "Tech Stack: ",
                    font_weight="bold",
                ),
                stack,
                font_size=Size.SMALL.value,
                margin_top=Size.MEDIUM.value,
            ),
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.icon(tag="link"),
                        rx.text("View app"),
                        font_size=Size.SMALL.value
                    ),
                    # href=link,
                    is_external=True
                ),
                rx.link(
                    rx.hstack(
                        rx.icon(tag="chevron_left"),
                        rx.icon(tag="chevron_right", margin=Size.ZERO.value),
                        rx.text("View Code"),
                        font_size=Size.SMALL.value
                    ),
                    href=github_link,
                    is_external=True,
                    margin_x=Size.MEDIUM.value,
                ),
                margin_top=Size.MEDIUM.value,
                width="100%",
            ),
            padding=Size.MEDIUM.value,
            justify_content="space-between"
        ),
        border_radius="10px",
        margin_top=Size.VERY_BIG.value,
        bg=Color.CARD.value,
    )
