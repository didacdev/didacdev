import reflex as rx

# Common


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


meta = [
    {"name": "og:type", "content": "website"}
]


# Index

title_index = "Portfolio | by Didacdev"
description_index = "Portafolio de proyectos de Diego Sánchez Escribano."

meta_index = [
    {"name": "og:title", "content": title_index},
    {"name": "og:description", "content": description_index},
]
meta_index.extend(meta)


# About

title_about = "Sobre mí | by Didacdev"
description_about = "Todo sobre Didacdev."

meta_about = [
    {"name": "og:title", "content": title_about},
    {"name": "og:description", "content": description_about},
]
meta_about.extend(meta)


# Projects

title_projects = "Proyectos | by Didacdev"
description_projects = "Todos mis proyectos."

meta_projects = [
    {"name": "og:title", "content": title_projects},
    {"name": "og:description", "content": description_projects},
]
meta_projects.extend(meta)
