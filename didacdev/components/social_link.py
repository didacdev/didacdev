import reflex as rx
from didacdev.styles.styles import Size


def social_link(icon: str, link: str) -> rx.Component:

    return rx.link(
        rx.image(
            src=f"/icons/{icon}.svg",
            width=Size.MEDIUM.value,
        ),
        href=link,
        is_external=True,
        margin_x=Size.SMALL.value,

    )
