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
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 --preolad main:app 

# Para probar en local:
    # gunicorn -w 2 -b 0.0.0.0:5000 main:app --timeout 0 --log-level debug
# ------- V1
# Exponer el puerto en el que se ejecutará la aplicación este o el 8080 como querais
# EXPOSE 5000

# Comando para ejecutar la aplicación en local cuando se usa docker run
# CMD ["flask", "run", "--host=0.0.0.0"]

# Una vez que se suba a cloud hay que usar otro CMD; y no se si tocar algo mas para instalar gunicorn
# CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 app:main

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
