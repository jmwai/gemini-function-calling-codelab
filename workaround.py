import os

from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

aiplatform.init(project=os.environ["PROJECT_ID"])

model = GenerativeModel("gemini-1.0-pro")

user_prompt = "What's the exchange rate from euros to US dollars today?"

response = model.generate_content("""
Your task is to extract parameters from the user's input and return it as a
structured JSON payload. The user will ask about the exchange rate and which
currency they are converting from and converting to.

User input: {user_prompt}

Please extract the currencies as parameters and put them in a JSON object.
""".format(user_prompt=user_prompt))

print(response.text)