import os

from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

aiplatform.init(project=os.environ["PROJECT_ID"])

model = GenerativeModel("gemini-1.0-pro")

response = model.generate_content(
    "What's the exchange rate for euros to dollars today?"
)
print(response.text)