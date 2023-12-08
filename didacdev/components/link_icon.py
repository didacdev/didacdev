import reflex as rx
from didacdev.styles.styles import Size

def link(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icon} is-medium",
        href=url,
        is_external=True,
        margin_x="0.25em",
    )
