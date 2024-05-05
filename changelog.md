## 2024-05-05 - feature/Corrochano/TextToTextUnification

- "TextToText" functional alongside "Audio to Text"
- Restructured the main.py so that both work, and preparation for "VideoToText"

## 2024-05-03 - feature/cmolina/videoTest

- Cambiado el main para arreglarlo y poder subirlo a una VM de GCP

## ---- otros cambios pendientes 

## 2024-04-10 - feature/Corrochano/faq

- faq page done
- back buttons were added

## 2024-04-09 - feature/Corrochano/faq
- First html approach to final solution

## 2024-04-02 - feature/Corrochano/TextToText

- Added Text to Text via VertexAI
- You need to configure the GCloud Project Name
- The summarize was called after the audio to text, but works bad if the text it's too short (like two words).
- Find a bug hen the audio to text doesn't recognise any word
- Now the text of the summarized text is displayed well
- Now the icons of audio, text and video aren't links to Google
- Requeriments.txt are updated
- All __pycache__ folders are added to the .gitignore file with **/__pycache__/

## 2024-04-02 - feature/Corrochano/TextToText

- Previously, the text message was all the response, but now it takes only the transcript text.

## 2024-03-30 - feature/cmolina/videoTest

- Añadida una secuencia de carga para hacer la espera mas amena
- Nuevo estilo para los botones de la main page
- Fix del logo
- Nuevos propts para la creacion de texto, y diferenciacion segun la longitud.
- Añadidas mejoras por implementar en la creacion de texto, como atributos de longitud y mood

## 2024-03-30 - feature/cmolina/videoTest

- Creacion de la carpeta de tools donde se guardaran los python auxiliares de la aplicacion
- Creacion de video_to_audio.py usando la libreria moviepy

## ---- otros cambios pendientes 

## 2024-03-29 - feature/Corrochano/AudioToText

- "read_audio.py" was added with the method to invoke the cloud service (Google Cloud Speech) for "AudioToText".
- Requirements for the audio to text library were added.

## 2024-03-29 - feature/Corrochano/MainAppDiseño

- Update main_page.html for the logo path.

## 2024-03-28 - feature/Corrochano/MainAppDiseño

- The images now are buttons to process the file.

## 2024-03-28 - feature/Corrochano/MainAppDiseño

- The page it's practically done. I only want to set the image from a local relative path.
- Rename the main file from app.py to main.py

## 2024-03-19 - feature/Corrochano/MainAppDiseño

- First approach of the final html design that we have on our mind.

## 2024-03-19 - feature/Corrochano/MainAppDiseño

- Adding watchdog dependency.
- Create a copy of the landing page placeholder in order to create there the design of the main page.

## 2024-03-13 - feature/cmolina/docker

- Configure files to update GCP

## 2024-03-13 - feature/cmolina/docker

- Add dockerfile & instructions to install it

## 2024-03-12 - feature/cmolina/changelogMD

- Create changelog to add changes and release.
- Add changelog & gitflow standar names.

## 2024-03-12 - Corrochano

- The names of all the authors were added to the license.

## 2024-03-05 - AlvarezIglesias

- first app body release.
- Create the repository.
