import os

from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

aiplatform.init(project=os.environ["PROJECT_ID"])

model = GenerativeModel("gemini-1.5-flash-001")

response = model.generate_content(
    "What's the exchange rate for US Dollar to Kenya Shilling today?"
)
print(response.text)