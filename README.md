# Workshop: OpenID Connect
I denne workshopen vil dere få en innføring i å gjøre en innlogging mot en OpenID Connect (OIDC) service,
i dette tilfellet Vipps logg inn.
Workshopen er bygd opp av en rekke oppgaver hvor dere må finne ut hvilken informasjon dere må
sende inn til Vipps, og hva dere kan bruke i svaret som kommer tilbake.

## Kort om OpenID Connect
OpenID Connect er den mest brukte standarden for identifisering av brukere på
internett. Den gir oss muligheten til å sende brukeren videre til en tredjepart
som utfører autentiseringen, og som så returnerer brukeren til oss med informasjonen
vi trenger. Standarden har også mange andre bruksområder, men disse vil vi ikke
gå inn på i dag.

## Installasjon av det du trenger til workshopen
Sjekk om du har Python 3 installert, kan gjøres med følgende kommando i en kommando linje:
```
python --version
```
For å kjøre denne workshopen så er Python 3.10 anbefalt, men en eldre versjon av Python 3 skal i teorien fungere.
Dersom du får Python 2.X.X av å kjøre kommandoen over så kan det være at du har Python 3 under ```python3```.
I dette tilfellet så kan du kjøre følgende kommando for å sjekke versjon:
```
python3 --version
```
Dersom dette gjelder deg, så må du også kjøre ```pip3``` istedenfor ```pip``` i de kommende kommandoene.

Dersom du ikke har Python 3 installert så kan du følge denne guiden, [Python 3 Installasjon og Setup Guide](https://realpython.com/installing-python/).
Nyeste Python 3 versjon kan du finne [her](https://www.python.org/downloads/).

## Hvordan kjøre opp appen
1. Hent ned repoet fra git

```
git clone "url"
```

2. Start en terminal i oidc client mappa
```
cd oidc-workshop/oidc-client/
```
3. Installer alle pakkene denne workshopen trenger, husk å bruk ```pip3``` dersom du bruker ```python3``` for å kjøre applikasjonen.
```
pip install -r requirements.txt
```
4. Start appen
```
python manage.py runserver
```

## Oppgaver
Oppgavene finner dere ved å starte opp applikasjonen.

## Bonusoppgaver
Hvis dere blir fort ferdig har vi et forslag til noe dere kan bryne dere på, men
dere må gjerne finne på noe selv også.

Forslag til utvidelse:
På en ekte nettside kan det komme mange brukere på en gang. Slik tjenesten vår
er nå har den kun støtte for at en bruker autentiserer seg om gangen.
Hvordan kan vi utvide tjenesten for å støtte at flere brukere logger seg på
samtidig?

Hint-1:
Hvordan kan dere gjenkjenne brukerne nå de kommer tilbake fra Vipps?

Hint-2:
MMMMMmmmm KAKER!
