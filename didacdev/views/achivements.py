import reflex as rx

from didacdev.styles.styles import Size, max_width_style, Color
from didacdev.components.badge import badge
from didacdev.components.header_text import header_text


def achivements() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.responsive_grid(
                badge("Python", "success", "languages/python.png"),
                badge("Django", "success", "languages/django.png"),
                badge("Swift", "primary", "languages/swift.png"),
                badge("SwiftUI", "primary", "languages/swiftUI.png"),
                badge("HTML", "warning", "languages/html.png"),
                badge("CSS", "warning", "languages/css.png"),
                badge("Java", "warning", "languages/java.png"),
                badge("SQL", "warning", "languages/sql.png"),
                badge("Reflex", "warning", "languages/reflex.png"),
                columns=[2, 2, 2, 3, 3],
                width="100%",
                spacing=Size.DEFAULT.value,
                class_name="nes-container is-dark"
            ),
            style=max_width_style,
        ),
        bg=Color.ACCENT.value,
        width="100%"
    )
