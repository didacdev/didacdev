import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, Color
from didacdev.components.page_link import page_link
from didacdev.components.social_link import social_link


def navbar() -> rx.Component:
    return rx.vstack(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    width="8em",
                ),
                rx.spacer(),
                page_link("_home", "/"),
                page_link("_didacdev", "/about"),
                page_link("_proyectos", "/projects"),
                rx.spacer(),
                social_link("cv", "/cv.pdf"),
                social_link("github", const.GITHUB_URL),
                social_link("linkedin", const.LINKEDIN_URL),
                width="100%"
            ),
        ),
        rx.mobile_only(
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    width="5em",
                ),
                rx.spacer(),
                social_link("cv", "/cv.pdf"),
                social_link("github", const.GITHUB_URL),
                social_link("linkedin", const.LINKEDIN_URL),
                rx.spacer(),
                rx.menu(
                    rx.menu_button("Menú"),
                    rx.menu_list(
                        rx.menu_item(
                            page_link("_home", "/"),
                            background=Color.BACKGROUND.value,
                        ),
                        rx.menu_item(
                            page_link("_didacdev", "/about"),
                            background=Color.BACKGROUND.value,
                        ),
                        rx.menu_item(
                            page_link("_proyectos", "/projects"),
                            background=Color.BACKGROUND.value,
                        ),
                        background=Color.BACKGROUND.value,
                    ),
                ),
                width="100%"
            ),

        ),
        bg=Color.BACKGROUND.value,
        position="sticky",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )
