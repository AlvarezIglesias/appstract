# TODO Creo que con la slim sera suficiente, si no instalamos mas cosas luego
FROM python:3.8-slim

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
CMD ["gunicorn", "-b", ":8080", "app:main"]

# Para ejecutarla: TODO revisar el sudo, a veces en cloud no iba
# sudo docker build -t appstract-image .  # Te crea una imagen 
# ! para gcp hay que ponerle el gcp delante ! docker build -t gcr.io/PROJECT_ID/appstract .
# sudo docker run -p 5000:5000 appstract-image # te despliega la imagen en local
# ! para gcp hay que hacerlo con botones y levantar a mano (y acordarse de apagarlo para que no cobre)
# Accede a -> http://localhost:5000/




# docker push gcr.io/PROJECT_ID/appstract
# gcloud run deploy appstract --image gcr.io/PROJECT_ID/appstract --platform managed --region REGION --allow-unauthenticated
