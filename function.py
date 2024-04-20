import os
import requests

from google.cloud import aiplatform
from vertexai.generative_models import (
    Content, 
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool)

aiplatform.init(project=os.environ["PROJECT_ID"])

model = GenerativeModel("gemini-1.0-pro")

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

prompt = """What's the exchange rate for Euro to South Africa Rand today?
How much is 1000 Euros worth in South Africa Rand?"""

response = model.generate_content(
    prompt,
    tools=[exchange_rate_tool],
)

print(response.candidates[0].content)

params = {}
for key, value in response.candidates[0].content.parts[0].function_call.args.items():
    params[key[9:]] = value
print(params)

url = f"https://api.frankfurter.app/{params['date']}"
api_response = requests.get(url, params=params)
print(api_response.text)

response = model.generate_content(
    [
    Content(role="user", parts=[
        Part.from_text(prompt + """Give your answer in steps with lots of detail
            and context, including the exchange rate and date."""),
    ]),
    Content(role="function", parts=[
        Part.from_dict({
            "function_call": {
                "name": "get_exchange_rate",
            }
        })
    ]),
    Content(role="function", parts=[
        Part.from_function_response(
            name="get_exchange_rate",
            response={
                "content": api_response.text,
            }
        )
    ]),
    ],
    tools=[exchange_rate_tool],
)


print(response.candidates[0].content.parts[0].text)