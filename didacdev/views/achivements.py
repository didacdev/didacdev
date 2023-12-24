import reflex as rx

from didacdev.components.badge import badge
from didacdev.styles.styles import Size, max_width_style, Color
import didacdev.constants as const


def achivements() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.responsive_grid(
                badge("Python", "success", "languages/python.png", const.PYTHON_PROJECTS),
                badge("Django", "success", "languages/django.png", const.DJANGO_PROJECTS),
                badge("Swift", "primary", "languages/swift.png", const.SWIFT_PROJECTS),
                badge("SwiftUI", "primary", "languages/swiftUI.png", const.SWIFT_PROJECTS),
                badge("Reflex", "warning", "languages/reflex.png", const.PYTHON_PROJECTS),
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
