import reflex as rx

from didacdev.styles.styles import Size, TextColor


def item(url: str, title: str, institution: str, start_date: str, end_date: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            color=f"{TextColor.TERTIARY.value} !important",
            font_size=Size.DEFAULT.value,
            margin_bottom=Size.DEFAULT.value,
            class_name="title"
        ),
        rx.vstack(
            rx.link(
                f"> {institution}",
                href=url,
                is_external=True,
                font_size=Size.MEDIUM.value,
            ),
            rx.text(
                f"{start_date} - {end_date}",
                font_size=Size.MEDIUM.value,
            ),
            spacing=Size.MEDIUM.value,
            align_items="start"
        ),
        class_name="nes-container is-dark with-title",
        width="100%",
        margin_y=Size.DEFAULT.value
    )
