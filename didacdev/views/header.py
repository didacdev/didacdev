import reflex as rx
from didacdev.styles.styles import Color, Size, max_width_style, title_style
import didacdev.constants as const


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                rx.text("Hola 👋"),
                rx.box(
                    "Mi nombre es ",
                    rx.span(
                        "Diego Sánchez",
                        background_image=f"linear-gradient(to right, {Color.BLUE.value}, " +
                        f"{Color.GREEN.value})",
                        background_clip="text",
                        color="transparent",
                    ),
                ),
                rx.text("Soy desarrollador mobile iOS"),
                style=title_style,
                width="45%",
            ),
            rx.avatar(
                src="didacdev.png",
                width="13em",
                height="13em",
                box_sizing="border-box",
                border="4px solid transparent",
                background_clip="padding-box, border-box",
                background_origin="padding-box, border-box",
                background_image=f"linear-gradient({Color.BACKGROUND.value}, " +
                f"{Color.BACKGROUND.value}), linear-gradient({Color.BLUE.value}, " +
                f"{Color.GREEN.value})",
            ),
            width="100%",
            justify_content="space-between",
            align_items="start",
        ),
        rx.box(
            rx.text(
                const.MAIL,
                font_size=Size.DEFAULT.value,
                font_weight="bold",
            ),
            padding=Size.SMALL.value,
            box_sizing="border-box",
            border="2px solid transparent",
            border_radius="6px",
            background_clip="padding-box, border-box",
            background_origin="padding-box, border-box",
            background_image=f"linear-gradient({Color.BACKGROUND.value}, " +
            f"{Color.BACKGROUND.value}), linear-gradient({Color.BLUE.value}, " +
            f"{Color.GREEN.value})",
        ),
        margin_top=Size.BIG.value,
        align_items="start",
        style=max_width_style,
    )
