import reflex as rx

import didacdev.utils as utils
from didacdev.styles.styles import Size
from didacdev.views.navbar import navbar
from didacdev.views.projects_header import projects_header
from didacdev.views.all_projects import all_projects
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
                projects_header(),
                all_projects(),
                footer(),
                width="100%",
                spacing=Size.DEFAULT.value,
            ),
            width="100%",
        ),
        min_height="100vh"
    )
