import os
from groq import Groq
from tools import full_finance_data
from dotenv import load_dotenv
load_dotenv()
# create groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_agent(country):

    # ---- tool call ----
    data = full_finance_data(country)

    # ---- send to LLM for formatting ----
    prompt = f"""
    Format the following financial data nicely and clearly for user.

    Data:
    {data}

    Show:
    - Currency
    - Exchange rates
    - Stock indices with values
    - Stock exchange HQ
    - Google maps link
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return completion.choices[0].message.content