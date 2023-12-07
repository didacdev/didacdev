import reflex as rx

import didacdev.styles.styles as styles


def index() -> rx.Component:
    return rx.box(
        rx.text(
            "Hola Mundo"
        )
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
