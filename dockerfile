# TODO Creo que con la slim sera suficiente, si no instalamos mas cosas luego
FROM python:3.10-slim

# Con esto todo se crea dentro de la carpeta /app en el docker  
WORKDIR /app

# ENV GOOGLE_ENTRYPOINT="python main.py"

#installa dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos
COPY . .

# Expone el puerto en el que se ejecutará la aplicación
ENV PORT=8080
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD exec gunicorn -t 0 -w 1 -b 0.0.0.0:8080 main:app --log-level debug

# Para probar en local:
    # gunicorn -t 0 -w 2 -b 127.0.0.1:8080 main:app --log-level debug
# ------- V1

# Comando para ejecutar la aplicación en local cuando se usa docker run


#! Para ejecutarla en local con docker: 
# sudo docker build -t appstract-image .  #! Te crea una imagen
# sudo docker run -it -e PROJECT=amazing-badge-417017 -e REGION=europe-west1 appstract-image
# Accede a -> http://localhost:5000/

# ! para GCP: 
# EN bash:
#   gcloud auth login
#   gcloud auth configure-docker europe-west1-docker.pkg.dev  #! cambiar la region si es necesario
#   gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://europe-west1-docker.pkg.dev/ #! Para login en docker
#   sudo docker tag nodered/node-red:latest eu.pkg.dev/amazing-badge-417017/tmi-appstract/appstract #! Para renombrar la imagen
#   sudo docker push  europe-west1-docker.pkg.dev/amazing-badge-417017/tmi-appstract/appstract
