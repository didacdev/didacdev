import reflex as rx

from didacdev.styles.styles import Size, TextColor


def header_text(text: str, dark=True) -> rx.Component:
    return rx.heading(
            text,
            size="md",
            color=TextColor.ACCENT.value if dark else TextColor.SECONDARY.value,
        )
