![](https://http2.mlstatic.com/static/org-img/homesnw/mercado-libre.png) 
# MercadoLibre Challenge Técnico

[![Python](https://img.shields.io/badge/python-3.8.9-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-389/)

Proyecto solución al Challenge Técnico para la aplicación a MercadoLibre. Este proyecto fue realizado con python en su totalidad.

## Componentes
Se utilizaron los siguientes componentes para la optimización de la ejecución del microservicio 
+  [Redis](https://redis.io/) para realizar el caché de información.
+  [PostgreSQL](https://www.postgresql.org/) para la persistencia relacional de la información.
+  [Adminer](https://www.adminer.org/) un ligero cliente de base de datos, para permitir el acceso a la tabla creada.

## Instalación
***Requieres [docker-compose](https://docs.docker.com/compose/install/) para la instalacion del proyecto.***
Solo necesitas es ejecutar la siguiente línea en esta carpeta y voilà!

```cmd
 docker-compose up
```

## Configuración
La configuración se encuentra en el [archivo de configuracion](config/config.ini), aquí puedes cambiar el nombre del archivo a ser leído, su codificación y parametrizar algunos otros aspectos del proyecto.
_Si deseas cambiar contraseñas, puertos u otra información relevante de la aplicación, debes cerciorarte de hacer dichos cambios en el archivo del [compose](docker-compose.yml)_

## Uso
Por defecto, accediendo al puerto [5051](http://localhost:5051) de tu máquina local, accederás al swagger del proyecto que te permitirá ejecutar (por POST) el llamado al ejercicio propuesto. La solicitud GET te mostrará si se está ejecutándo un procesamiento tras bambalinas.


Además de esto, tendrás acceso a [Adminer](http://localhost:18080) en el que utilizando la siguiente configuración te podrás conectar para navegar las tablas.
