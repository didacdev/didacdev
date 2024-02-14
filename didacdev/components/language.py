import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, TextColor, title_style, max_width_style
from datetime import datetime


def language(title: str, date: str) -> rx.Component:
    return rx.vstack(
        rx.heading(
            title,
            size="md",
            color=TextColor.PRIMARY.value
        ),
        rx.hstack(
            rx.text(date),
            width="100%",
            font_size=Size.SMALL.value,
            justify_content="space-between"
        ),
        align_items="start",
        spacing=Size.DEFAULT.value,
        border_bottom=f"1px inset {TextColor.PRIMARY.value}",
        padding_y=Size.XSMALL.value,
        width="30em"
    )
