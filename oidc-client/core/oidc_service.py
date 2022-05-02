import json
import urllib.parse
import uuid

import requests
from django.shortcuts import render

###
# Variabler kan hentes fra variables.py med
# from .variables import VARIABEL_NAVN
# og deretter brukes slik
# variabel = VARIABEL_NAVN
###
from .variables import CLIENT_ID
from .variables import CLIENT_SECRET
from .variables import GRANT_TYPE
from .variables import REDIRECT_URL
from .variables import RESPONSE_TYPE
from .variables import WELL_KNOWN_URL


###
# For å starte en pålogging må brukeren sendes til OIDC tjenesten.
# For at OIDC tjenesten skal kunne håndtere requesten så må visse parametre legges til en url før brukeren vidersendes.
# Det første dere må gjøre er å finne dataen dere trenger for å bygge opp denne url-en.
###
def create_oidc_session(request):
    url = ""
    params = dict()

    redirect_url = url + '?' + urllib.parse.urlencode(params)

    formatted_params = prettify_data(params)
    return render(request, 'login_redirect.html',
                  {'url': url, 'params': formatted_params, 'redirect_url': redirect_url})


###
# Brukeren har returnert fra OIDC-serveren til Vipps med en autorisasjonskode.
# Neste steg er å finne ut hvordan dere kan bytte denne inn i et access token.
###
def get_access_token(request):
    authorization_code = request.GET['code']

    url = ""
    body = dict()
    basic_auth = ""

    response = requests.post(url, data=body, auth=basic_auth)

    if response.status_code == 200:
        formatted_json = prettify_data(response.json())
        access_token = response.json()['access_token']
        return render(request, 'receive_access_token.html',
                      {'access_token': access_token, 'json': formatted_json, 'response': response})
    else:
        formatted_json = dict()
        if has_json_body(response):
            formatted_json = prettify_data(response.json())
        return render(request, 'receive_failed_access_token.html',
                      {'reason': response.reason, 'response': response, 'json': formatted_json})


###
# Du har fått byttet autorisasjonskoden inn i et access token.
# Nå er spørsmålet hvordan kan du bruke dette til å hente informasjon om brukeren?
###
def get_userinfo(request):
    access_token = request.GET['access_token']

    url = ""
    headers = dict()

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        formatted_json = prettify_data(response.json())
        return render(request, 'receive_userinfo.html',
                      {'response': response, 'json': formatted_json})
    else:
        formatted_json = dict()
        if has_json_body(response):
            formatted_json = prettify_data(response.json())
        return render(request, 'receive_failed_userinfo.html',
                      {'reason': response.reason, 'response': response, 'json': formatted_json})


def has_json_body(response):
    return 'Content-Type' in response.headers and response.headers.get('Content-Type').startswith('application/json')


###
# Under her ligger det hjelpemetoder for programmet.
###

# Metode som tar i mot og henter autorisasjonskoden når det kommer fra OIDC tjenesten.
def receive_callback(request):
    formatted_params = prettify_data(request.GET)
    return render(request, 'received_callback.html',
                  {'code': request.GET['code'], 'formatted_params': formatted_params})


# Leverer startsiden til nettleseren
def index(request):
    return render(request, 'start_login.html')


#
def start_login(request):
    create_oidc_session_response = create_oidc_session()
    return render(request, 'login_redirect.html',
                  {'response': create_oidc_session_response})


# Metode for å gjøre data objekter, json, dict, osv, meir lesbare i en nettleser
def prettify_data(data):
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


# Metode for å sjekke om en respons har en body av type json
def has_json_body(response):
    return 'Content-Type' in response.headers and response.headers.get('Content-Type').startswith('application/json')
