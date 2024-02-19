import reflex as rx

import didacdev.constants as const
from didacdev.styles.styles import Size, TextColor, max_width_style
from didacdev.components.social_link import social_link


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.tablet_and_desktop(
                    rx.image(
                        src="/dark_logo.png",
                        width="7em",
                        alt="Logotipo de Didacdev. Una \"de\" creada con signos de código."
                    ),
                ),
                rx.mobile_only(
                    rx.image(
                        src="/dark_logo.png",
                        width="4em",
                        alt="Logotipo de Didacdev. Una \"de\" creada con signos de código."
                    ),
                ),

                href=const.WEB_GITHUB_URL,
                is_external=True
            ),
            rx.spacer(),
            social_link("github", const.GITHUB_URL),
            social_link("linkedin", const.LINKEDIN_URL),
            width="100%"
        ),
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        border_top=f"1px inset {TextColor.PRIMARY.value}",
        style=max_width_style
    )
