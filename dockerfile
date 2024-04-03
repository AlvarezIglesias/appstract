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

# Exponer el puerto en el que se ejecutará la aplicación este o el 8080 como querais
EXPOSE 5000

# Comando para ejecutar la aplicación en local cuando se usa docker run
# CMD ["flask", "run", "--host=0.0.0.0"]

# Una vez que se suba a cloud hay que usar otro CMD; y no se si tocar algo mas para instalar gunicorn
CMD ["gunicorn", "-b", ":8080", "app:main","--worker-class", "gevent", "--worker-connections", "100", "--timeout", "0", "--graceful_timeout", "2000"]

# Para ejecutarla: 
# sudo docker build -t appstract-image .  # Te crea una imagen
# Accede a -> http://localhost:5000/

# ! para GCP: 
# EN bash:
#   gcloud auth login
#   gcloud auth configure-docker europe-west1-docker.pkg.dev  #! cambiar la region si es necesario
#   gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://europe-west1-docker.pkg.dev/ #! Para login en docker
#   sudo docker tag nodered/node-red:latest eu.pkg.dev/amazing-badge-417017/tmi-appstract/appstract #! Para renombrar la imagen
#   sudo docker push  europe-west1-docker.pkg.dev/amazing-badge-417017/tmi-appstract/appstract
