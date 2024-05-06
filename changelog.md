## 2024-05-06 - Corrochano

- Final hot fix to little details

## 2024-05-06 - feature/Corrochano/TextToTextUnification

- Update the logo to a cleanest version

## 2024-05-06 - feature/cmolina/main_page

- css in main_page to a new file
- Better text box for summary
- Fix main.py

## 2024-05-06 - feature/cmolina/configure_fields

- Changed the login to no accept duplicate IDs
- Add timestamp field to know the register date
- Add fields to configure the summary (num_words & style)
- New prompt query for summarize text

## 2024-05-05 - feature/cmolina/updateVM2

- Changed the main to fix it so that it can be uploaded to a GCP VM, thats includes:
    - Changes in html to manage better problems whit login
    - Changes in login to include bigquery and users in that mode


## 2024-05-05 - feature/Corrochano/TextToTextUnification

- "TextToText" functional alongside "Audio to Text"
- Restructured the main.py so that both work, and preparation for "VideoToText"

## 2024-05-03 - feature/cmolina/updateVM

- Changed the main to fix it so that it can be uploaded to a GCP VM

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

- Added a loading sequence to make the wait more enjoyable
- New style for main page buttons
- Fixed the logo
- New propts for text creation, and differentiation according to length.
- Added improvements to be implemented in text creation, like length and mood attributes.

## 2024-03-30 - feature/cmolina/videoTest

- Creation of the tools folder where the application's auxiliary python files will be stored.
- Creation of video_to_audio.py using moviepy library

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
