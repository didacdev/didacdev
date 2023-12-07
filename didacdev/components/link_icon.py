import reflex as rx


def link(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name=f"nes-icon {icon} is-large",
        href=url,
        is_external=True,
    )
