import reflex as rx

from didacdev.styles.styles import Size, max_width_style
from didacdev.components.header_text import header_text
from didacdev.components.item import item
import didacdev.constants as const


def studies() -> rx.Component:
    return rx.vstack(
        header_text("Educational Background"),
        rx.vstack(
            item(const.UNED_URL, "Grado en Ingeniería Informática", "Universidad Nacional de Educación a Distancia", "09-2020", "act."),
            item(const.UAM_URL, "Máster en Formación del Profesorado", "Universidad Autónoma de Madrid", "09-2018", "06-2019"),
            item(const.CSKG_URL, "Título Superior de Música", "Centro Superior Katarina Gurska", "09-2017", "06-2018"),
            item(const.RCSMM_URL, "Título Superior de Música", "Real Conservatorio Superior de Música de Madrid", "09-2014", "06-2017"),
        ),
        style=max_width_style
    )