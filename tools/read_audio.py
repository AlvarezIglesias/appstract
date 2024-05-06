from  datetime import datetime
import os
from google.cloud import speech
from google.cloud import storage
# from google.auth.exceptions import DefaultCredentialsError

PROJECT = os.environ.get('PROJECT')
# Verifica si la variable de entorno existe
if PROJECT is None:
    from credentials.ids import PROJECT

REGION = os.environ.get('REGION')
if PROJECT is None:
    from credentials.ids import REGION

def convert_file_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension != '.mp3':
        from moviepy import editor

        # Load the audio file
        audio = editor.AudioFileClip(file_path)
        exit_file_name = file_path.replace(file_extension, '') + '.mp3'
        # Convert and save as MP3
        audio.write_audiofile(exit_file_name)
        return exit_file_name

        # # ALternative with other library
        # from pydub import AudioSegment
        # exit_file_name = file_path.replace(file_extension, '') + '.mp3'
        # audio = AudioSegment.from_file(file_path, format=file_extension.replace('.', ''))
        # audio.export(exit_file_name, format="mp3")
    return file_path

def upload_audio_file(source_file_name):
    """Subir un archivo a un bucket de Google Cloud Storage.

    Args:
        source_file_name (str): La ruta del archivo local que se va a subir.
    """
    source_file_name = convert_file_extension(source_file_name)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    bucket_name = 'appstract-data'
    client = storage.Client(project=PROJECT)
    # subir archivo
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f'audio_tmp/audio_{timestamp}.mp3')
    blob.upload_from_filename(source_file_name)

    print(f"Archivo {source_file_name} subido a {blob.public_url}")
    uri = 'gs://' + bucket_name + '/' + blob.name
    return uri

def transcribe_file(speech_file: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file."""
    try:
        uri = upload_audio_file(speech_file)
        client = speech.SpeechClient()

        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(uri=uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code="es",
        )
        request = speech.LongRunningRecognizeRequest(
            config=config,
            audio=audio,
        )
        print(f"Reconociendo audio...")
        # Make the request
        operation = client.long_running_recognize(request=request)

        print(f"Waiting for operation to complete... {operation}")

        response = operation.result()
        print("Done audio!")
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.

        # for result in response.results: # Solo para comprobar
        #     # The first alternative is the most likely one for this portion.
        #     print(f"Transcript: {result.alternatives[0].transcript}")

        return response
    # except DefaultCredentialsError as cred: #TODO esto para ver si es error de credenciales
    #     print(f"Bad credentials at read_audio: {cred} \n \n please, run: gcloud auth application-default login")
    #     return None
    except Exception as e:
        print(f"something was wrong: {e}")
        return 500, f"Ha ocurrido un error interno. Por favor, intenta de nuevo más tarde.{e}"

# audio = "record_out.wav"
# transcribe_file(os.path.join("tmp", audio))
