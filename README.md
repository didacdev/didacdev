# Curriculum Vitae Didacdev

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.3.6+-5646ED?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://reflex.dev)
[![NES.css](https://img.shields.io/badge/NES.css-2.3.0-007bff?style=for-the-badge&logo=css3&logoColor=white&labelColor=101010)](https://nostalgic-css.github.io/NES.css)
[![Render](https://img.shields.io/badge/Render-static-gray?style=for-the-badge&logo=render&logoColor=white&labelColor=101010&color=green)](https://render.com)

### Visita [https://didacdev.com](https://didacdev.com)

## Proyecto

Esta es la estructura general del proyecto.

* **didacdev**: código fuente principal
	* **didacdev.py**: index del sitio web
	* **constants.py**: constantes utilizadas en el sitio
	* **styles**: directorio de estilos (css, colores y fuentes)
	* **views**: directorio de vistas (secciones gráficas)
	* **components**: directorio de componentes (elementos gráficos con menor entidad que una vista)
* **assets**: recursos gráficos y utilidades JavaScript (nive y cuenta atrás)
* **rxconfig.py**: configuración principal del proyecto (por defecto)
* **requirements.txt**: dependencias del proyecto para su ejecución
* **assets**: recursos gráficos y utilidades JavaScript (nive y cuenta atrás)
* **build.sh**: script de generación estática de la web para producción
* **[generado] public**: empaquetado estático del proyecto que se despliega en producción (HTML, CSS, JS e imágenes)

## Configuración en local

1. Haz un `Fork` del repositorio.

2. Clona ese repositorio en tu máquina local.

    ```bash 
    git clone https://github.com/<USERNAME>/adeviento-web.git
    ```

3. Navega al directorio del proyecto.

    ```bash
    cd adeviento
    ```

4. Crea un entorno virtual.

    ```bash
    python3 -m venv venv
    ```

5. Activa el entorno virtual.

    ```bash
    source venv/bin/activate
    ```

6. Instala las dependencias.

    ```bash
    python -m pip install -r requirements.txt
    ```

7. Inicializa el proyecto de Reflex.

    ```bash
    reflex init
    ```

8. Ejecuta el proyecto en local.

    ```bash
    reflex run
    ```

    *Podrás acceder a él entrando en la url `http://localhost:3000/` desde el navegador.*
    
> Tienes más la información sobre [Reflex](https://reflex.dev/) en su [documentación oficial](https://reflex.dev/docs).

## Recursos utilizados

![Python](https://img.shields.io/github/stars/python/cpython?label=Python&style=social)
![Reflex](https://img.shields.io/github/stars/reflex-dev/reflex?label=Reflex&style=social)
![NES.css](https://img.shields.io/github/stars/nostalgic-css/NES.css?label=NES.css&style=social)

* Lenguaje: [Python](https://www.python.org/)
* Framework: [Reflex](https://reflex.dev/)
* CSS: [NES.css](https://nostalgic-css.github.io/NES.css/)
* Fuente: [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P)
