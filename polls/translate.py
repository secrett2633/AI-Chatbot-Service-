import time
import requests
import os
from dotenv import load_dotenv

def get_translate(text, language):
    load_dotenv()
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    if language: a='ko'; b = "en"
    else: a='en'; b = "ko"
    data = {'text' : text,#inputtext
            'source' : a,#input lan
            'target': b}#output lan

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data= data)
    rescode = response.status_code

    if(rescode==200):
        t_data = response.json()
        return response.json()['message']['result']['translatedText']
    else:
        print("Error Code:" , rescode)
        return 0