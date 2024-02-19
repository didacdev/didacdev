import reflex as rx
from didacdev.styles.styles import Size, max_width_style, title_style


def stack() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "Tech Stack",
                style=title_style,
            ),
            rx.text(
                "Tecnologías que he utilizado y estudiado",
                font_size=Size.DEFAULT.value
            ),
            text_align="center",
        ),
        rx.tablet_and_desktop(
            rx.flex(
                rx.image(src="tech_stack/swift.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Swift"),
                rx.image(src="tech_stack/swiftUI.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje SwiftUI"),
                rx.image(src="tech_stack/kotlin.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Kotlin"),
                rx.image(src="tech_stack/python.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Python"),
                rx.image(src="tech_stack/django.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Django"),
                rx.image(src="tech_stack/html.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje HTML"),
                rx.image(src="tech_stack/css.png",
                         width="5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje CSS"),
                gap="20",
                align_items="center",
                justify_content="center",
                flex_wrap="wrap",
                margin_y=Size.BIG.value,
                width="100%",

            ),
        ),
        rx.mobile_only(
            rx.flex(
                rx.image(src="tech_stack/swift.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Swift"),
                rx.image(src="tech_stack/swiftUI.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje SwiftUI"),
                rx.image(src="tech_stack/kotlin.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Kotlin"),
                rx.image(src="tech_stack/python.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Python"),
                rx.image(src="tech_stack/django.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje Django"),
                rx.image(src="tech_stack/html.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje HTML"),
                rx.image(src="tech_stack/css.png",
                         width="3.5em", margin=Size.MEDIUM.value, alt="Logotipo del lenguaje CSS"),
                gap="2",
                align_items="center",
                justify_content="center",
                flex_wrap="wrap",
                margin_y=Size.DEFAULT.value,
                width="100%",

            ),
        ),

        align_items="center",
        style=max_width_style
    )
