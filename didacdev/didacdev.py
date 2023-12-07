import reflex as rx

import didacdev.styles.styles as styles
from didacdev.components.github import github
from didacdev.styles.styles import Size
from didacdev.views.header import header
from didacdev.views.navbar import navbar
from didacdev.views.studies import studies
from didacdev.views.work import work


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                work(),
                studies(),
                github(),
                width="100%",
                spacing=Size.VERY_BIG.value,
            ),
        ),

    )


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="DidacDev",
    description="Curriculum online de Diego Sánchez Escribano"
)
app.compile()
