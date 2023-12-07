import reflex as rx

import didacdev.constants as const
from didacdev.components.header_text import header_text
from didacdev.components.item import item
from didacdev.styles.styles import max_width_style, Color


def work() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text("Work Experience", False),
            rx.vstack(
                item(const.MBL_URL, "Project Coordinator", "MBL.S.L",
                     "06-2022", "07-2022."),
                item(const.TEMPO_URL, "Director of programmes and equipment", "Tempo Musical",
                     "06-2022", "07-2022."),
                item(const.MBL_URL, "Music teacher", "MBL.S.L",
                     "09-2018", "act."),

            ),
            style=max_width_style,
        ),
        bg=Color.ACCENT.value,
        width="100%"
    )
