import reflex as rx

import didacdev.styles.styles as styles
from didacdev.styles.styles import Size
from didacdev.views.navbar import navbar
from didacdev.views.header import header


def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                width="100%",
                spacing=Size.VERY_BIG.value,
            ),
            width="100%",
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
    description="Portfolio de proyectos de Diego Sánchez Escribano",
)
