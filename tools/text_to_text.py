import vertexai
from vertexai.preview.language_models import TextGenerationModel
import os, sys
sys.path.append('../')

PROJECT = os.environ.get('PROJECT')
# Verifica si la variable de entorno existe
if PROJECT is None:
    from credentials.ids import PROJECT

REGION = os.environ.get('REGION')
if PROJECT is None:
    from credentials.ids import REGION

def predict_large_language_model(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    location: str = REGION,
    tuned_model_name: str = "",
) -> str:
    """Predict using a Large Language Model.

    Args:
      project_id (str): the Google Cloud project ID
      model_name (str): the name of the LLM model to use
      temperature (float): controls the randomness of predictions
      max_decode_steps (int): the maximum number of decode steps
      top_p (float): cumulative probability of parameter highest vocabulary tokens
      top_k (int): number of highest propbability vocabulary tokens to keep for top-k-filtering
      content (str): the text to summarize
      location (str): the Google Cloud region to run in
      tuned_model_name (str): a tuned LLM model to use; default is none

    Returns:
      The summarization of the content
    """
    vertexai.init(
        project=project_id,
        location=location,
    )

    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
        model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,
    )
    return response.text


def summarize_text(text, words=100, mood="normal", max_words='20000'):
    model_name = "text-bison@001"
    temperature = 0.2
    max_decode_steps = 1024
    top_p = 0.8
    top_k = 40
    if text.lenght() > max_words:
        return "El archivo multimedia elegido es demasiado grande para procesarlo."
    if text.lenght() < words:
        content = f"""Te voy a pasar un pequeño texto o una serie de caracteres, tienes que resumirlo de una manera {mood}:
    
        {text}
        
        Con esto, genetra una descripcion o resumen de unas {words} palabras.
        """
    else:
        content = f"""Te voy a pasar un texto o una serie de caracteres, tienes que resumirlo de una manera {mood}:
    
        {text}
        
        Con esto, genetra una descripcion o resumen de mas o menos {words} palabras.
        """

    summary = predict_large_language_model(
        project_id=PROJECT,
        model_name=model_name,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        max_decode_steps=max_decode_steps,
        content=content)

    print("summary: " + summary)

    return summary
