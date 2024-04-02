import vertexai
from vertexai.preview.language_models import TextGenerationModel

import sys
sys.path.append('../')

from credentials.ids import PROJECT
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


def summarize_text(text):
    model_name = "text-bison@001"
    temperature = 0.2
    max_decode_steps = 1024
    top_p = 0.8
    top_k = 40

    prompt = 'Resume el siguiente texto en menos palabras de las dadas:'
    content = f"{prompt}\n{text}"

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
