## Disponibilidad del servicio de carga de fotos 📷

🚀 Para levantar los servicios es necesario tener docker-compose descargado y ejecutar los siguientes comandos:

> docker-compose build

> docker-compose up -d



✉️ Para enviar peticiones de carga de imágenes, se debe enviar peticiones POST a la siguiente dirección:

> http://localhost/

El Body de la petición debe ser el siguiente, donde <ruta_imagen> es la ruta donde se encuentra la imagen a subir:

```json
{
  "path": <ruta_imagen>
}
```

La imagen debe de encontrarse en la carpeta photos, por ejemplo:
```json 
{
  "path": "/photos/cabra.jpg"
}
```

🔍 Para monitorear el estado de la cola de mensajería en el ambiente local, puede acceder a la siguiente dirección:

> http://localhost:15672

Y acceder con las siguientes credenciales 🔑:

> default_user: guest

> default_pass: guest


✒️ Experimento realizado por Grupo 6 - Arquitecturas Ágiles🍻



