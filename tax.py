import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyD4YYmxn5PX43Adjud9PXTyAHFK3jOOmMc")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
def generate_json_response(company_income, sbc_qualified, turnover_tax_exempt, taxable_income=None, estimated_tax=None):
    response = {
        "sbc_qualified": sbc_qualified,
        "turnover_tax_exempt": turnover_tax_exempt,
        "taxable_income": taxable_income,
        "estimated_tax": estimated_tax
    }
    return json.dumps(response, indent=2)
convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Can you act as a tax estimation tool where you calculate taxes for small businesses. And you return the data as a json response.\n\nthese are the questions:\n1. how much income do you make?"]
    },
    {
        "role": "model",
        "parts": ["​"]
    },
    {
        "role": "user",
        "parts": ["can you return the data as a json response.\n\nthe json file should contain a boolean of whether you qualify for sbc. and a boolean for if you are exempt because of turnover tax."]
    },
    {
        "role": "model",
        "parts": [generate_json_response(company_income=None, sbc_qualified=False, turnover_tax_exempt=True)]
    },
    {
        "role": "user",
        "parts": ["if you do qualify for tax it should it should tell you how much of your income is taxable"]
    },
    {
        "role": "model",
        "parts": ["Okay, I can enhance the JSON response to include taxable income calculation if the company qualifies for SBC."]
    },
    {
        "role": "user",
        "parts": ["and the total tax amount"]
    },
    {
        "role": "model",
        "parts": ["Okay, I can enhance the JSON response to include estimated tax amount if the company qualifies for SBC."]
    }
])
print(convo.last.text)









