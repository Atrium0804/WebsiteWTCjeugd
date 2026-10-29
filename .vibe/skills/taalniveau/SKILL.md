---
name: taalniveau
description: "Taalniveau (kindniveau, B1, B2): schrijfregels en een vaste controle- en herschrijfronde voor Nederlandse teksten. Gebruik bij het controleren of herschrijven van een tekst naar begrijpelijk Nederlands, en als eindcontrole voordat een andere Vaardigheid een tekst voor leden, ouders of kinderen oplevert."
user-invocable: true
allowed-tools:
  - read_file
  - edit
  - bash
  - ask_user_question
---

# Taalniveau

Deze Vaardigheid is de enige plek met de schrijfregels voor het taalniveau van WTC-teksten. Andere Vaardigheden (`jeugdsport-teksten`, `wtc-knwu-kennisroutering`) verwijzen hiernaar en herhalen de regels niet.

De onderbouwing met bronnen staat in `context/taalniveau-B1-B2-richtlijnen.md`. Lees die alleen als de gebruiker naar de herkomst van een regel vraagt.

## Niveaus

| Niveau | Voor wie | Gemiddelde zinslengte | Langste zin |
|---|---|---|---|
| **Kindniveau** | Teksten die kinderen van 6-14 jaar zelf lezen | ≤ 10 woorden | 12 woorden |
| **B1** (standaard) | Ouders, leden, iedereen | 10-15 woorden | 20 woorden |
| **B2** | Alleen op verzoek, bijv. uitleg van reglementen voor ingewijden | ≤ 20 woorden | 25 woorden |

Kies het niveau zo:

1. Vraagt de gebruiker een niveau, gebruik dat.
2. Is de tekst gericht aan kinderen, gebruik kindniveau. Gaat een tekst naar ouders én kinderen, schrijf de stukken voor kinderen op kindniveau en de rest op B1.
3. Anders: **B1**. Dat is het vastgelegde standaardniveau voor alle teksten en antwoorden die gedeeld worden met leden of ouders.

Kindniveau volgt de AVI-leesniveaus (groep 4-5 leest zinnen van 7-9 woorden). Zinslengte is een hulpmiddel, geen doel: een tekst met alleen korte, hakkelende zinnen is niet begrijpelijker.

## Regels

De regels gelden voor B1. De kolom *Afwijking* noemt wat anders is voor kindniveau of B2. Bij B2 gelden alle regels zonder afwijking volledig; B2 geeft alleen ruimte voor langere zinnen en een rijkere woordkeus.

| # | Regel (B1) | Afwijking |
|---|---|---|
| 1 | **Kern eerst.** Begin met wat de lezer moet weten of doen. Daarna de details. | B2: na de kern mag je uitleggen waarom en opties met voor- en nadelen tegen elkaar afwegen. |
| 2 | **Eén boodschap per zin**, hoogstens één bijzin. Zinnen binnen de grenzen uit de tabel *Niveaus*. | Kind: geen bijzinnen. B2: twee bijzinnen mag, als de hoofdzaak vooraan staat. |
| 3 | **Actief, met een duidelijk onderwerp.** "Je meldt je aan via de ClubApp", niet "Aanmelden kan worden gedaan via". | B2: lijdende vorm mag af en toe. |
| 4 | **Spreek de lezer aan met je/jij.** Schrijf over "we" als de club iets doet. | — |
| 5 | **Gewone, concrete woorden.** "Begin", niet "aanvang". "Kosten", niet "contributieverplichting". Werkwoorden in plaats van naamwoorden: "we trainen", niet "de training vindt plaats". | Kind: vooral woorden van 1-3 lettergrepen. B2: abstracte woorden mogen, als de context ze verklaart. |
| 6 | **Leg vaktermen meteen uit**, de eerste keer dat ze voorkomen: "startlicentie (je pasje om mee te doen aan wedstrijden)". Gebruik daarna steeds hetzelfde woord. | Kind: vermijd vaktermen als het kan. |
| 7 | **Herhaal het zelfstandig naamwoord** in plaats van een verwijswoord ("deze", "hiervan", "laatstgenoemde") als het verband niet direct duidelijk is. | B2: meer verwijswoorden mogen. |
| 8 | **Korte alinea's** van hoogstens vier zinnen. Elke alinea heeft één onderwerp. | — |
| 9 | **Tussenkopjes zeggen waar het stuk over gaat.** "Wat neem je mee?", geen woordgrap. | — |
| 10 | **Opsommingen** bij stappen, voorwaarden, spullen of drie of meer opties. | — |
| 11 | **Concrete gegevens**: datum, tijd en bedrag precies ("zaterdag 14 september, 10.00 uur", "€ 25,00"). Geen vage tijdsaanduidingen als "binnenkort". | — |
| 12 | **Geen onbekende afkortingen.** Schrijf ze de eerste keer voluit, bijv. "Midden Nederland Competitie (MNC)". | Kind: helemaal geen afkortingen. |

## Werkwijze

### Bij het schrijven (vanuit een andere Vaardigheid)

1. Bepaal het niveau (zie *Niveaus*).
2. Schrijf de tekst met de regels in gedachten.
3. Doe de **controleronde** (hieronder) voordat je de tekst oplevert. Lever alleen de verbeterde tekst op. Een lijst met knelpunten geef je alleen als de gebruiker erom vraagt.

### Op verzoek van de gebruiker ("controleer", "maak dit B1")

1. Bepaal het niveau. Noem het in één zin aan het begin van je antwoord.
2. Doe de controleronde.
3. Lever eerst de herschreven tekst op. Geef daarna een korte lijst van de belangrijkste wijzigingen, met het nummer van de regel erbij (bijv. "regel 3: lijdende vorm actief gemaakt").
4. Verander geen feiten: data, bedragen, namen en reglementsinhoud blijven gelijk. Is een zin inhoudelijk onduidelijk, vraag het dan via `ask_user_question` en vul het niet zelf in.

### Controleronde

Loop alle twaalf regels af, voor elke zin en elke alinea. De ronde is klaar als:

- elke zin binnen de grens voor de langste zin blijft, of een bewuste uitzondering is (bijv. een opsomming in één zin);
- geen enkele regel meer een herschrijving oplevert.

Staat de tekst als bestand in `websiteteksten/website_teksten md/` en is er een shell beschikbaar? Meet dan ook:

```powershell
python tools/websiteteksten_sync.py leesbaarheid "<bestand>.md" --niveau b1
```

Gebruik `--niveau kind` of `--niveau b2` voor de andere niveaus. Het script toont de gemiddelde zinslengte, het aandeel lange woorden, de Flesch-Douma-score en de zinnen boven de grens. Zinnen die mogelijk in de lijdende vorm staan, worden apart gemeld. Pas elke gemelde zin aan, of laat hem bewust staan. Draai het commando opnieuw tot alleen bewuste uitzonderingen overblijven. De score is een indicatie: de regels hierboven gaan voor.
