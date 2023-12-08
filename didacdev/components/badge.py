import reflex as rx
from didacdev.styles.styles import Size, Color


def badge(title: str, name: str, image: str) -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Didacdev",
            src=image,
            size="lg",
            bg=Color.PRIMARY.value,
            padding="2px",
            border="2px",
            border_color=Color.SECONDARY.value,
            margin_bottom=Size.SMALL.value,
        ),
        rx.box(
            rx.span(
                title,
                class_name=f"is-{name}"
            ),
            class_name="nes-badge",
        ),
        align_items="center",
    )
