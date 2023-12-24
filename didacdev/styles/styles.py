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
    BIG = "2em !important"
    BUTTON = "2.75em !important"
    VERY_BIG = "4em !important"


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
    rx.Link: {
        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",
            "color": f"{TextColor.ACCENT.value} !important",
        }
    },
    rx.Span: {
        "font_size": Size.MEDIUM.value,
    },
}

max_width_style = dict(
    align_items="start",
    padding=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH,
)
