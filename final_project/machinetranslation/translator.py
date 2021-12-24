import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2021-12-24',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def english_to_french(request):
    if request is None:
        return None
    response = language_translator.translate(text=request, model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation 

def french_to_english(request):
    if request is None:
        return None
    response = language_translator.translate(text=request, model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation 