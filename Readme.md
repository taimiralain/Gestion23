<p align="center">
 <h2 align="center">Proyecto Django de Gestión de Órdenes </h2>
</p>
  <p align="center">
    <a href="https://github.com/taimiralain/Gestion23/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/taimiralain/FrontEnd" />
    </a>
    <a href="https://github.com/taimiralain/Gestion23/network/members">
      <img alt="Fork" src="https://img.shields.io/github/forks/taimiralain/FrontEnd" />
    </a>
    <a href="https://github.com/taimiralain/Gestion23/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/taimiralain/FrontEnd" />
    </a>
 
  </p>

Este proyecto es un sistema de microservicio para gestionar la ubicación de órdenes en un Centro de Distribución (CD).

## Requisitos

- Python 3.10 o superior
- Django 4.1
- Django Rest Framework

## Configuración del entorno

Para configurar el entorno de desarrollo, sigue estos pasos:

1. Clona el repositorio:

git clone url_del_repositorio


2. Crea un entorno virtual:

python -m venv venv


3. Activa el entorno virtual:
- En Windows:
  ```
  venv\Scripts\activate
  ```
- En Unix o MacOS:
  ```
  source venv/bin/activate
  ```

4. Instala las dependencias:

pip install -r requirements.txt


## Configuración de la base de datos

1. Configura tu base de datos en `settings.py`.

2. Realiza las migraciones:

python manage.py makemigrations python manage.py migrate


## Ejecución del servidor

Para ejecutar el servidor de desarrollo, utiliza el siguiente comando:


python manage.py runserver


El servidor estará disponible en `http://127.0.0.1:8000/`.

## Pruebas

Para probar la aplicación, puedes utilizar la interfaz de administración de Django o herramientas como Postman.

1. Crea un superusuario para acceder a la interfaz de administración:

python manage.py createsuperuser


2. Accede a `http://127.0.0.1:8000/admin/` y utiliza las credenciales del superusuario para iniciar sesión.

3. Utiliza Postman para enviar solicitudes HTTP a los endpoints de la API y verificar las respuestas.

## Documentación de la API

La documentación de la API está disponible en `http://127.0.0.1:8000/docs/` donde podrás encontrar información detallada sobre los endpoints, parámetros y formatos de respuesta.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, envía tus pull requests a la rama `develop` para cualquier mejora o corrección.
