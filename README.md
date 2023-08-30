# Workshop: OpenID Connect
I denne workshopen vil dere få en innføring i å gjøre en innlogging mot en OpenID Connect (OIDC) service,
i dette tilfellet Vipps logg inn.
Workshopen er bygd opp av en rekke oppgaver hvor dere må finne ut hvilken informasjon dere må
sende inn til Vipps, og hva dere kan bruke i svaret som kommer tilbake.

## Kort om OpenID Connect
OpenID Connect er den mest brukte standarden for identifisering av brukere på
internett. Den gir oss muligheten til å sende brukeren videre til en tredjepart
som utfører autentiseringen, og som så returnerer brukeren til oss med informasjonen
vi trenger.

## Installasjon av det du trenger til workshopen
Sjekk om du har Python 3 installert, dette kan gjøres med følgende kommando:
```
python --version
```
For å kjøre denne workshopen så er Python 3.10 anbefalt, men en eldre versjon av Python 3 skal i teorien fungere.
Dersom du får Python 2.X.X av å kjøre kommando-en over så kan det være at du har Python 3 under ```python3```.
I dette tilfellet så kan du kjøre følgende kommando for å sjekke versjon:
```
python3 --version
```
Dersom dette gjelder deg, så må du også kjøre ```pip3``` istedenfor ```pip```, for å installere alle nødvendige pakker i punkt 3 under "Hvordan kjøre opp appen".

Dersom du ikke har Python 3 installert så kan du følge denne guiden, [Python 3 Installasjon og Setup Guide](https://realpython.com/installing-python/).
Nyeste Python 3 versjon kan du finne [her](https://www.python.org/downloads/).

## Hvordan kjøre opp appen
1. Hent ned repo-et fra git
    ```
    git clone git@github.com:kantega/oidc-workshop-public.git
    ```
2. Start en terminal og gå inn i oidc workshop mappen
    ```
    cd oidc-workshop-public/oidc-client/
    ```
   
3. Installer alle nødvendige pakker for workshopen
    ```
    pip install -r requirements.txt
    ```
   
4. Start applikasjonen
    ```
    python manage.py runserver
    ```

## Hvordan gjøre endringer i koden
Gjennom denne workshopen så skal dere gjøre endringer i filen [oidc_service.py](oidc-client/core/oidc_service.py) 
og dere vil finne nyttige verdier i filen [variables.py](oidc-client/core/variables.py).

For å gjøre kode endringer kan dere bruke en valgfri tekst-editor, men om dere vil prøve noe nytt så kan vi anbefale:
* [PyCharm Community](https://www.jetbrains.com/pycharm)
* [VS Code](https://code.visualstudio.com/)

Begge disse tekst-editorene har mulighet for å kjøre koden, 
debugge koden og kan gi dere hjelp med tilgjengelige metoder underveis.

## Oppgaver
Oppgavene finner dere ved å starte opp applikasjonen.

## Bonus-oppgaver
Hvis dere blir fort ferdig har vi et forslag til noe dere kan bryne dere på, men
dere må gjerne finne på noe selv også.

Forslag til utvidelse:
På en ekte nettside kan det komme mange brukere på en gang. Slik tjenesten vår
er nå har den kun støtte for at en bruker autentiserer seg om gangen.
Hvordan kan vi utvide tjenesten for å støtte at flere brukere logger seg på
samtidig?

Hint:
Hvordan kan dere gjenkjenne brukerne nå de kommer tilbake fra Vipps?

## Innlogging
Appen logger inn med Vipps Logg inn som er registrert på Kantega AS med Org.nr. 985815534