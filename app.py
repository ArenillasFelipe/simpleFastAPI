from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/')
def defaultString():
    return "BircleAI"

@app.post('/')
def callExternAPI():

    external_api_url = "https://api.publicapis.org/"
    
    response = requests.post(external_api_url)

    print(response)
    
    return response.json()


@app.put("/{number}")
def elevateNumber(number: int):
    return (number * number)