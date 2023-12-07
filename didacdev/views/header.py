import reflex as rx

from didacdev.styles.styles import Size, max_width_style


def header() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="didacdev.png",
            atl="Imagen de DidacDev.",
            width="20em",
            margin_top=Size.VERY_BIG.value
        ),
        rx.vstack(
            rx.heading(
                "Diego Sánchez Escribano",
                size="lg",
                padding_bottom=Size.DEFAULT.value,
            ),
            rx.box(
                rx.text(
                    "Computer Engineer",
                    class_name="title",
                ),
                rx.progress(
                    value=50,
                    width="100%",
                    height=Size.DEFAULT.value,
                    margin_bottom=Size.MEDIUM.value
                ),
                padding_y=Size.MEDIUM.value,
                class_name="nes-container is-rounded is-dark with-title",
            ),
            margin=Size.ZERO.value,
            class_name="nes-balloon from-left is-dark"
        ),
        padding_top=Size.VERY_BIG.value,
        style=max_width_style
    )
