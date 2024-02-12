import reflex as rx

import didacdev.utils as utils
from didacdev.styles.styles import Size
from didacdev.views.navbar import navbar
from didacdev.views.footer import footer


@rx.page(
    title=utils.title_projects,
    description=utils.description_projects,
    meta=utils.meta_projects
)
def projects() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("Proyectos"),
                footer(),
                width="100%",
                spacing=Size.VERY_BIG.value,
            ),
            width="100%",
        ),
    )
