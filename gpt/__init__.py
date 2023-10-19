import openai
import os

os.environ['OPEN_API_KEY'] = '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'

key = os.environ.get("OPEN_API_KEY")

if key:
    openai.api_key = key
    model = openai.ChatCompletion()
    print("Openai API Activated!")
else:
    print("No Key Founded!")