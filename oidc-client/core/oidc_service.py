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
##------------ Løsning ------------##
from .variables import CLIENT_ID
from .variables import CLIENT_SECRET
from .variables import GRANT_TYPE
from .variables import REDIRECT_URL
from .variables import RESPONSE_TYPE
from .variables import WELL_KNOWN_URL
##---------------------------------##

##------------ Løsning ------------##
class WellKnown:
    data = dict()
##---------------------------------##

###
# For å starte en pålogging må brukeren sendes til OIDC tjenesten.
# For at OIDC tjenesten skal kunne håndtere forespørselen så må visse parametre legges til en url før brukeren videresendes.
# Det første dere må gjøre er å finne data-en dere trenger for å bygge opp denne url-en.
###
def create_oidc_session(request):

    url = ""
    params = {}

    ##------------ Løsning ------------##
    fetch_well_known()
    url = WellKnown.data['authorization_endpoint']

    params['client_id'] = CLIENT_ID
    params['response_type'] = RESPONSE_TYPE
    params['redirect_uri'] = REDIRECT_URL

    params['state'] = str(uuid.uuid4())
    params['scope'] = 'openid name'
    ##---------------------------------##

    redirect_url = url + '?' + urllib.parse.urlencode(params)

    formatted_params = prettify_data(params)

    return render(request, 'login_redirect.html',
                  {'url': url, 'params': formatted_params, 'redirect_url': redirect_url})


###
# Brukeren har returnert fra OIDC-serveren til Vipps med en autorisasjons kode.
# Neste steg er å finne ut hvordan dere kan bytte denne inn i et access token.
###
def get_access_token(request):
    authorization_code = request.GET['code']

    url = ""
    body = {}
    basic_auth = ""

    ##------------ Løsning ------------##
    url = WellKnown.data['token_endpoint']

    body = dict()
    body['code'] = authorization_code
    body['grant_type'] = GRANT_TYPE
    body['redirect_uri'] = REDIRECT_URL

    basic_auth = (CLIENT_ID, CLIENT_SECRET)
    ##---------------------------------##

    response = requests.post(url, data=body, auth=basic_auth)
    formatted_json = prettify_body_if_json(response)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        return render(request, 'received_access_token.html',
                      {'access_token': access_token, 'json': formatted_json, 'response': response})
    else:
        return render(request, 'received_access_token_error.html',
                      {'reason': response.reason, 'response': response, 'json': formatted_json})


###
# Du har fått byttet autorisasjons koden inn i et access token.
# Nå er spørsmålet hvordan kan du bruke dette til å hente informasjon om brukeren?
###
def get_userinfo(request):
    access_token = request.GET['access_token']

    url = ""
    headers = {}

    ##------------ Løsning ------------##
    url = WellKnown.data['userinfo_endpoint']
    headers = dict()
    headers['authorization'] = 'Bearer ' + access_token
    ##---------------------------------##

    response = requests.get(url, headers=headers)
    formatted_json = prettify_body_if_json(response)

    if response.status_code == 200:
        return render(request, 'received_userinfo.html',
                      {'response': response, 'json': formatted_json})
    else:
        return render(request, 'received_userinfo_error.html',
                      {'reason': response.reason, 'response': response, 'json': formatted_json})


###
# Under her ligger det hjelpe metoder for programmet.
###

# Metode som tar i mot og henter autorisasjons koden når det kommer fra OIDC tjenesten.
def receive_callback(request):
    formatted_params = prettify_data(request.GET)
    if (request.method == 'GET' and 'error' in request.GET):
        return render(request, 'received_callback_error.html',
                      {'error': request.GET['error'], 'error_description': request.GET['error_description']})
    else:
        return render(request, 'received_callback.html',
                      {'code': request.GET['code'], 'formatted_params': formatted_params})


# Leverer startsiden til nettleseren
def index(request):
    return render(request, 'start_login.html')


# Metode for å gjøre en potensiell json i response body meir lesbar i en nettleser
def prettify_body_if_json(response):
    if (has_json_body(response)):
        return prettify_data(response.json())
    else:
        return dict()


# Metode for å sjekke om en respons har en body av type json
def has_json_body(response):
    return 'Content-Type' in response.headers and response.headers.get('Content-Type').startswith('application/json')


# Metode for å gjøre data objekter, json, dict, osv, meir lesbare i en nettleser
def prettify_data(data):
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


##------------ Løsning ------------##
def fetch_well_known():
    if not bool(WellKnown.data):
        WellKnown.data = requests.get(WELL_KNOWN_URL).json()
    return WellKnown.data
##---------------------------------##