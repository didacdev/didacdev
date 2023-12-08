import reflex as rx

import didacdev.constants as const
from didacdev.components.header_text import header_text
from didacdev.components.item import item
from didacdev.styles.styles import max_width_style


def work() -> rx.Component:
    return rx.vstack(
        header_text("Work Experience"),
        rx.vstack(
            item(const.NUTRICYNN_URL, "Full Stack Developer", "Nutricynn", "06-2022", "act."),
            item(const.MBL_URL, "Project Coordinator", "MBL.S.L", "06-2022", "07-2022."),
            item(const.TEMPO_URL, "Director of programmes and equipment", "Tempo Musical", "06-2022", "07-2022."),
            item(const.MBL_URL, "Music teacher", "MBL.S.L", "09-2018", "act."),
            width="100%",
        ),
        style=max_width_style,
    )
