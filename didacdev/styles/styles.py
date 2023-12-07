from enum import Enum

import reflex as rx

from .colors import TextColor, Color
from .fonts import Font

MAX_WIDTH = "1000px"

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em !important"
    MEDIUM = "0.8em !important"
    DEFAULT = "1em !important"
    BIG = "2em"
    BUTTON = "2.75em"
    VERY_BIG = "4em"


STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.Heading: {
            "color": TextColor.ACCENT.value,
            "font_family": Font.DEFAULT.value,
            "text_align": "center"
        },
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)

