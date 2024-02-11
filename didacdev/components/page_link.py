import reflex as rx
from didacdev.styles.styles import Size


def page_link(text: str, link: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            font_size=Size.DEFAULT.value,
        ),
        href=link,
        margin_x=Size.BIG.value,
    )
