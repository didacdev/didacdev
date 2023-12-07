import reflex as rx

from didacdev.styles.styles import Size, TextColor


def item(url: str, title: str, institution: str, start_date: str, end_date: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            color=f"{TextColor.TERTIARY.value} !important",
            class_name="title"
        ),
        rx.link(
            institution,
            href=url,
            is_external=True
        ),
        rx.text(f"{start_date} - {end_date}"),
        class_name="nes-container is-dark with-title",
        width="100%",
        margin_y=Size.DEFAULT.value
    )
