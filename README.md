<h1 align="center">
Proyecto Autotest Urban Routes
</h1>
<h1 align="center">
Automatización con Selenium y Python
</h1>


Este proyecto implementa un flujo de interacción automatizado para la aplicación web Urban Routes, utilizando Selenium para la automatización del navegador. 
EL Objetivo es automatizar la interacción que cubra el proceso completo de pedir un taxi:
 
- Se accede a la URL de Urban Routes.
- Se ingresan las direcciones de origen y destino.
- Se espera que se cargue el mapa y se hace clic en "Pedir un taxi".
- Se selecciona la tarifa Comfort.
- Se ingresa el número de telefono y se completa la verificación mediante un código SMS.
- Se accede a la forma de pago, se agrega una tarjeta.
- Se ingresa un mensaje para el conductor y se selecciona requisitos adicionales: manta y pañuelos y pedir 2 helados.
- Mostrar la información del pedido y del conductor en el modal.

## Tecnologías y Técnicas Utilizadas
Para el desarrollo del proyecto se utilizó:

- Python: Lenguaje de programación principal del proyecto.
- Selenium: Herramienta de automatización de pruebas utilizada para interactuar con el navegador y simular las acciones del usuario.
- Pytest: Para la ejecución de los test, se debe instalar en el proyecto.
- Chrome: Versión 118.0.5993.89
- Chrome Driver: se utiliza la version que sea compatible con la version de Chrome. Ejemplo: Version: 118.0.5993.70

## Instrucciones para ejecución de las pruebas

 Módulos Principales
- data.py: Contiene datos de prueba, como la URL de Urban Routes, direcciones de origen y destino, números de teléfono y detalles de tarjetas.
- codigo_sms.py: Proporciona una función para recuperar el código SMS necesario para la verificación.
- locators.py: Define la clase `UrbanRoutesLocators` que almacena los selectores de elementos de la interfaz de usuario.
- interceptor.py: Proporciona una función para recuperar la respuesta de los resultados de la ruta (nombre conductor, tiempo de espera y placa de vehiculo) para la verificación.
#### Clases Principales
- *UrbanRoutesPage*: Implementa métodos para interactuar con la interfaz de Urban Routes, desde el ingreso de direcciones hasta la confirmación del pedido.
- *TestUrbanRoutes*: Contiene los casos de prueba utilizando la biblioteca de pruebas `pytest`. Configura y cierra el navegador, además de realizar las 8 pruebas.

1. Clona el repositorio.
2. Instala las dependencias necesarias (`pip install selenium pytest`).
3. Ejecuta las pruebas de TestUrbanRoutes (archivo main.py).
