import os

from google.cloud import aiplatform
from vertexai.generative_models import (
    FunctionDeclaration,
    GenerativeModel,
    Tool)

aiplatform.init(project=os.environ["PROJECT_ID"])

model = GenerativeModel("gemini-1.5-flash-001")

get_exchange_rate_func = FunctionDeclaration(
    name="get_exchange_rate",
    description="Get the exchange rate for currencies between countries",
    parameters={
    "type": "object",
    "properties": {
        "currency_date": {
            "type": "string",
            "description": "A date that must always be in YYYY-MM-DD format or the value 'latest' if a time period is not specified"
        },
        "currency_from": {
            "type": "string",
            "description": "The currency to convert from in ISO 4217 format"
        },
        "currency_to": {
            "type": "string",
            "description": "The currency to convert to in ISO 4217 format"
        }
    },
         "required": [
            "currency_from",
            "currency_date",
      ]
  },
)

exchange_rate_tool = Tool(
    function_declarations=[get_exchange_rate_func],
)

prompt = """What's the exchange rate for US Dollar to Euro today?
How much is 1000 Us Dollars worth in Euros?"""

response = model.generate_content(
    prompt,
    tools=[exchange_rate_tool],
)

print(response.candidates[0].content)

params = {}
for key, value in response.candidates[0].content.parts[0].function_call.args.items():
    params[key[9:]] = value
print(params)