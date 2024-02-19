import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, max_width_style, title_style
from didacdev.components.main_project import main_projects


def projects() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Proyectos",
            style=title_style,
        ),
        rx.text("Aplicaciones que he desarrollado",
                font_size=Size.DEFAULT.value),
        main_projects(
            "Star Wars Encyclopedia",
            "#",
            const.STAR_WARS_GITHUB_URL,
            const.STAR_WARS_TEXT,
            "Swift, SwiftUI, Alamofire",
            "/projects/main_projects/star_wars.jpg"
        ),
        main_projects(
            "Connect Four",
            "#",
            const.CONNECT_FOUR_GITHUB_URL,
            const.CONNECT_FOUR_TEXT,
            "Swift, SwiftUI",
            "/projects/main_projects/connect_four.jpg"
        ),
        style=max_width_style
    )
