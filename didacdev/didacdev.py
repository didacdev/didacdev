import reflex as rx

import didacdev.styles.styles as styles
from didacdev.pages.index import index
from didacdev.pages.about import about
from didacdev.pages.projects import projects


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
