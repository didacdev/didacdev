import reflex as rx

import didacdev.utils as utils
from didacdev.styles.styles import Size
from didacdev.views.navbar import navbar
from didacdev.views.index.header import header
from didacdev.views.index.stack import stack
from didacdev.views.index.projects import projects
from didacdev.views.footer import footer


@rx.page(
    title=utils.title_index,
    description=utils.description_index,
    meta=utils.meta_index
)
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                stack(),
                projects(),
                footer(),
                width="100%",
                spacing=Size.VERY_BIG.value,
            ),
            width="100%",
        ),
    )
