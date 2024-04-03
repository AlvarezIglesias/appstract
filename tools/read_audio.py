import os
from google.cloud import speech
from google.auth.exceptions import DefaultCredentialsError


def transcribe_file(speech_file: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file."""
    try:
        client = speech.SpeechClient()

        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=16000,
            language_code="es",
        )
        print("Reconociendo audio...")
        request = speech.LongRunningRecognizeRequest(
            config=config,
            audio=audio,
        )

        # Make the request
        operation = client.long_running_recognize(request=request)

        print("Waiting for operation to complete...")

        response = operation.result()
        print("Done audio!")
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.

        # for result in response.results: # Solo para comprobar
        #     # The first alternative is the most likely one for this portion.
        #     print(f"Transcript: {result.alternatives[0].transcript}")

        return response
    except DefaultCredentialsError as cred:
        print(f"Bad credentials at read_audio: {cred} \n \n please, run: gcloud auth application-default login")
        return None
    except Exception as e:
        print(f"something was wrong: {e}")
        return None

# audio = "tigres.mp3"
# transcribe_file(os.path.join("tmp", audio))

