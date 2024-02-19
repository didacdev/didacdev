import reflex as rx

from didacdev.styles.styles import Size, Color, title_style, max_width_style
from datetime import datetime


def about_header() -> rx.Component:

    birthday = datetime(year=1996, month=3, day=10)

    return rx.vstack(
        rx.text(
            "Sobre mí",
            style=title_style,
            text_align="start",
        ),
        rx.box(
            f"Me llamo Diego, tengo {age(
                birthday=birthday)} y soy de Madrid. Cursé estudios superiores de música y, tras años ejerciendo como profesor, me decidí por el mundo de la informática. Actualmente, llevo cursado más de ",
            rx.span(
                "la mitad del Grado en Ingeniería Informática.",
                font_weight="bold",
                background_image=f"linear-gradient(to right, {Color.BLUE.value}, " +
                f"{Color.GREEN.value})",
                background_clip="text",
                color="transparent",
            ),
            font_size=Size.DEFAULT.value
        ),
        rx.box(
            "Mientras estudio, he probado y aprendido algunas de las tecnologías más utilizadas en el sector, ",
            rx.span(
                "creando aplicaciones mobile para dispositivos iOS ",
                font_weight="bold",
                background_image=f"linear-gradient(to right, {Color.BLUE.value}, " +
                f"{Color.GREEN.value})",
                background_clip="text",
                color="transparent",
            ),
            "y web. Tengo gran interés en la visión artificial y la parte de la robótica aplicada a la visión espacial.",
            font_size=Size.DEFAULT.value,
        ),
        align_items="start",
        spacing=Size.BIG.value,
        style=max_width_style
    )


def age(birthday: datetime) -> int:

    age = (datetime.now() - birthday) // 365
    return age.days
