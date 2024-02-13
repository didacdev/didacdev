from enum import Enum

import reflex as rx

from .colors import TextColor, Color
from .fonts import Font

MAX_WIDTH = "850px"


class Size(Enum):
    ZERO = "0px !important"
    XSMALL = "0.5em !important"
    SMALL = "0.8em !important"
    DEFAULT = "1em !important"
    MEDIUM = "1.5em !important"
    BIG = "2em !important"
    VERY_BIG = "4em !important"


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Fira+Mono&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.BACKGROUND.value,
    rx.Heading: {
        "color": TextColor.SECONDARY.value,
        "font_family": Font.DEFAULT.value,
        "text_align": "center",
        "size": "xl",
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",
            "color": f"{TextColor.SECONDARY.value} !important",
        }
    }
}

max_width_style = dict(
    padding=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)

title_style = dict(
    font_weight="bold",
    font_size=Size.BIG.value,
    color=TextColor.SECONDARY.value,
)
