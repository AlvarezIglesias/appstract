# APPSTRACT

This project was created for the TMI course from the Complutens University of Madrid's Master's Degree in Computer Science.

Este proyecto fue creado para la asignatura TMI del Máster en Informática de la Universidad Complutens de Madrid.

## Presentacion:
La productividad está en auge en estos últimos años, y cada vez se publican más archivos en la web, En YouTube se suben más de 300 horas de video por minuto y se ven más de 5 billones de videos al día, y por otro lado, Spotify cuenta con 433 millones de usuarios activos mensuales que pueden acceder a 4,4 millones de podcasts. ¡¡ESTO ES DEMASIADO!! Por ello, queremos realizar una aplicación para resumir archivos multimedia a través de Inteligencia Artificial, APIs y algoritmos, filtrando además el contenido almacenado, para que no contenga elementos inadecuados.

**El objetivo principal será el de hacer una web-app sencilla y funcional donde el usuario pueda subir sus archivos multimedia y estos se procesen, generando un resumen de lo que el usuario está proporcionando.**

## STACK
**Python** como lenguaje principal, desde el que llamaremos a las APIs y se controlará el flujo de la aplicación. El framework para la app será **Flask**.

**HTML, CSS Y JS** para el frontend de la página web.

**Docker** como contenedor para la aplicación, lo que nos permite poder crearla portable entre clouds, lo cual será clave si los créditos de alguna de ellas se nos acaban.

## Instalacion

La aplicacion viene con un dockerfile para que sea mas sencillo desplegarla, para ponerla en marcha en local hay que seguir estos pasos

 1- **sudo docker build -t appstract-image .**  # Te crea una imagen (tambien se puede descargar del repositorio de docker)
 2- **sudo docker run -p 5000:5000 appstract-image** # despliega la imagen en local
 3- **Accede a -> http://localhost:5000/** # Y todo listo!

### Subir contenedor a goolge:
1. gcloud auth login
2. gcloud auth configure-docker europe-west1-docker.pkg.dev
3. gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://europe-west1-docker.pkg.dev/
4. gcloud run deploy  -- (Seguir las instrucciones, region 16, )

## Utilizaremos control de versiones con la siguiente estructura:
- **Rama main:** para los cambios finales antes de un hito.
- **Rama develop** para los cambios en proceso, pero finalizados y para probar.
- **Ramas auxiliares** para desarrollar diferentes funcionalidades, con el siguiente esquema TIPO/USUARIO/NOMBRE, donde nombre será un par de palabras descriptivas de lo que hace esa actualizacion, Usuario será uno de los 3 desarrolladores y tipo puede ser uno de los siguientes:
  - **feature:** característica definida de la aplicación.
  - **hotfix:** corrección de errores urgentes por haberse detectado un defecto crítico (generalmente en producción) que deba resolverse.
  - **Release:** Rama lista para subir a main donde poder depurar el código.
Algunos ejemplos de ramas serian: *Feature/AlvarezIglesias/diseño_web* , *Feature/Corrochano/conexion_BBDD* o *Hotfix/cmolina/google_api_fix*

## Changelog
Cada commit llevara asociado un changelog acumulativo de los cambios realizados (los mas nuevos siempre encima) en el siguiente formato:

 ### YYYY-MM-DD - [BRANCH_NAME]

- changes
- to
- update

## Miembros
Álvaro Corrochano López, 10/10 de implicación. -> Corrochano

Álvaro Álvarez Iglesias, 10/10 de implicación. -> AlvarezIglesias

Cristian Molina Muñoz, 10/10 de implicación. -> crismom / crismo04

