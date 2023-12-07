import reflex as rx

import didacdev.constants as constants
from didacdev.styles.styles import Size


def github() -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.vstack(
                rx.span(
                    "Proyecto",
                ),
                rx.span(
                    "en GitHub",
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value,
            ),
            rx.box(
                rx.span(
                    "©didacdev",
                    class_name="is-success",
                ),
                class_name="nes-badge",
            ),

        ),
        rx.box(
            class_name="nes-octocat animate"
        ),
        href=constants.GITHUB_REPO_URL,
        is_external=True,
        align_items="end",
        display="flex",
        margin_top=Size.ZERO.value,
    )
