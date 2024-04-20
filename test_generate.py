import os

from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

aiplatform.init(project="YOUR_PROJECT_ID")

model = GenerativeModel("gemini-1.0-pro")

response = model.generate_content(
    "What's the exchange rate for Euro to South Africa Rand today?"
)
print(response.text)