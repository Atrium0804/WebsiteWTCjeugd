---
name: website-structuur
description: "Gebruik deze Vaardigheid voor het beoordelen, verfijnen en uitbreiden van de websitestructuur van WTC Woerden. Laad bij aanvragen voor structuurcontrole, structuurreview, het toevoegen van pagina's of het herordenen van de site."
user-invocable: true
allowed-tools:
  - read_file
  - write_file
  - edit
  - bash
  - ask_user_question
---

# WTC Woerden website-structuur

Deze Vaardigheid ondersteunt het beoordelen, verfijnen en uitbreiden van de websitestructuur van WTC Woerden. De Vaardigheid wijzigt de structuur zelf; het schrijven van teksten gebeurt met de Vaardigheid `jeugdsport-teksten`.

## Bron van waarheid

- De sectie "Huidige structuur" in deze Vaardigheid is de bron van waarheid voor de jeugdsectie: vijf onderdelen (6.1 t/m 6.5) met in totaal 21 pagina's.
- Repository: Atrium0804/WebsiteWTCjeugd, hoofdbranch main. Het bestand `Websitestructuur-jeugd.md` in deze repository hoort synchroon te zijn met de structuur in deze Vaardigheid. Is het bestand afwezig of niet synchroon, stel de gebruiker dan voor het te herstellen vanuit deze Vaardigheid.
- Het bestand `Websitestructuur.md` in de repository is een AI-gegenereerd voorstel en is geen bron van waarheid. Gebruik het hooguit als inspiratie; neem er geen feitelijke gegevens uit over zonder verificatie door de gebruiker.
- Het referentiemateriaal in de map `context/` van de repository (welkomstdocument, inhoud van de huidige site, teksten van januari 2025) dient als stijl- en toonreferentie, niet als feitenbron.
- Na een structuurwijziging moet de website-structuursectie in de Vaardigheid `jeugdsport-teksten` synchroon worden gehouden. Wijs de gebruiker hierop na elke wijziging.

## Huidige structuur

De jeugdsectie bestaat uit vijf onderdelen met in totaal 21 pagina's. De bestandsnamen verwijzen naar de map `websiteteksten/`.

### 6.1 Jeugd — startpagina (werving)

| Pagina | Bestandsnaam | Doelgroep | Intentie |
|---|---|---|---|
| Startpagina | 01-startpagina.md | Jeugd (6-14) en ouders | Enthousiasmeren, uitnodigen |

### 6.2 Wat we doen (enthousiasmeren, gericht op jeugd 6-14 jaar)

| Pagina | Bestandsnaam | Doelgroep | Intentie |
|---|---|---|---|
| Wegwielrennen | 02-wegwielrennen.md | Jeugd (6-14) | Enthousiasmeren |
| Veldrijden / cross | 03-veldrijden.md | Jeugd (6-14) | Enthousiasmeren |
| Clubkampioenschap en activiteiten | 04-clubkampioenschap-activiteiten.md | Jeugd (6-14) | Enthousiasmeren, informeren |
| Wedstrijden: club naar regionaal naar nationaal | 05-wedstrijden.md | Jeugd (6-14) en ouders | Informeren, enthousiasmeren |

### 6.3 Nieuw bij de jeugd? / Voor ouders (praktisch, drempel wegnemen)

| Pagina | Bestandsnaam | Doelgroep | Intentie |
|---|---|---|---|
| Kom meetrainen | 06-kom-meetrainen.md | Ouders van niet-leden | Uitnodigen, geruststellen |
| Leenfietsen | 07-leenfietsen.md | Ouders van niet-leden | Informeren |
| Benodigd materiaal | 08-benodigd-materiaal.md | Ouders van niet-leden | Informeren |
| Kleding | 09-kleding.md | Ouders van niet-leden | Informeren |
| Contributie | 10-contributie.md | Ouders van niet-leden | Informeren |
| Wat verwachten we van ouders | 11-wat-verwachten-we-van-ouders.md | Ouders van niet-leden | Informeren |
| Veelgestelde vragen (FAQ) | 12-veelgestelde-vragen.md | Ouders van niet-leden | Informeren, geruststellen |
| Aanmelden / inschrijfformulier | 13-aanmelden.md | Ouders van niet-leden | Werven |

### 6.4 Voor leden — praktisch en actueel (naslag)

| Pagina | Bestandsnaam | Doelgroep | Intentie |
|---|---|---|---|
| Trainingstijden en locaties per seizoen | 14-trainingstijden-locaties.md | Ouders van leden | Informeren |
| Leeftijdscategorieën 1 t/m 7 | 15-leeftijdscategorieen.md | Ouders van leden | Informeren |
| Wedstrijdlicentie | 16-wedstrijdlicentie.md | Ouders van leden | Informeren |
| Toegestane verzetten | 17-toegestane-verzetten.md | Ouders van leden | Informeren |
| Wedstrijdkalender, uitslagen en standen | 18-wedstrijdkalender-uitslagen.md | Ouders van leden | Informeren |
| De wedstrijd (hoe verloopt een clubwedstrijd) | 19-de-wedstrijd.md | Ouders van leden en jeugd | Informeren |
| Communicatie en afmelden | 20-communicatie-afmelden.md | Ouders van leden | Informeren, herinneren |

### 6.5 Vervolgpad

| Pagina | Bestandsnaam | Doelgroep | Intentie |
|---|---|---|---|
| WSR Cyclingteam | 21-wsr-cyclingteam.md | Oudere jeugdleden en ouders | Informeren, enthousiasmeren |

Vastgestelde afspraken binnen deze structuur:

- Nieuwe leden kunnen ieder moment instromen; iedere eerste dinsdag van de maand is er een open training. Vooraf aanmelden is gewenst, zodat materiaal kan worden uitgezocht.
- Baanwielrennen en mountainbiken worden kort vermeld als incidentele activiteiten, zonder aparte pagina (op de startpagina of binnen de pagina Wegwielrennen).
- Gedragscode en vertrouwenspersoon staan alleen centraal onder Over de club, niet in de jeugdsectie.
- WSR Cyclingteam is een raceteam voor oudere jeugdleden; nadere details volgen later.

## Beoordelingskader

Beoordeel de structuur op de volgende acht criteria:

1. Doelgroeprouting: werving vooraan, leden-naslag achteraan.
2. Menudiepte: maximaal vijf onderdelen per menuniveau.
3. Eén pagina, één doel: elke pagina heeft precies één hoofddoelgroep en één intentie.
4. Geen overlap: geen twee pagina's die hetzelfde onderwerp behandelen.
5. Volledigheid: alle terugkerende vragen van ouders en jeugd zijn gedekt.
6. Tijdloosheid: actualiteit hoort bij Nieuws en Agenda, niet in de vaste structuur.
7. Vindbaarheid: elke doelgroep vindt de eigen informatie binnen drie klikken.
8. Paginagrootte: een pagina met meerdere intenties of doelgroepen is een signaal om te splitsen.

De doelgroepen en intenties volgen de definities uit de Vaardigheid `jeugdsport-teksten`: jeugd die overweegt lid te worden (6-14 jaar), ouders van niet-leden, en ouders van bestaande leden; intenties zijn enthousiasmeren, informeren, uitnodigen, werven, herinneren en bedanken.

## Gebruiksmodi

### Modus 1: Snelle controle (consistentiecheck)

Bedoeld voor het commando "controleer de structuur" of vergelijkbaar. Vragen geen input aan de gebruiker.

1. Vertrek vanuit de sectie Huidige structuur in deze Vaardigheid; haal ter aanvulling het bestand `Websitestructuur-jeugd.md` uit de repository op indien aanwezig.
2. Doorloop alle acht criteria systematisch.
3. Rapporteer de bevindingen als een genummerde lijst, per criterium, met per bevinding: de locatie in de structuur, het overtreden criterium en een concrete suggestie.
4. Vraag aan het eind of de gebruiker een of meer bevindingen wil uitwerken in een interactieve review.

Rapporteer ook wat goed is: benoem expliciet welke criteria zijn gehaald.

### Modus 2: Interactieve review

Bedoeld voor het reviewen van één onderdeel of de gehele jeugdsectie.

1. Bepaal het bereik met de gebruiker: de gehele jeugdsectie of één onderdeel (6.1 t/m 6.5).
2. Presenteer de huidige stand van het gekozen bereik: onderdelen, pagina's, doelgroepen en intenties.
3. Stel per onderdeel gerichte vragen, maximaal vier tegelijk. Gebruik de vraagpatronen hieronder.
4. Verwerk de antwoorden in een voorgestelde wijziging.
5. Presenteer de wijziging met onderbouwing: welk criterium de aanleiding was en wat er verandert.
6. Vraag goedkeuring per wijziging of voor het gehele voorstel.
7. Werk na goedkeuring het structuurbestand bij en werk de wijzigingslog bij.

### Modus 3: Gerichte wijziging

Bedoeld voor "voeg een pagina toe over ..." of "verplaats ... naar ...".

1. Bepaal doelgroep, intentie en onderdeel voor het nieuwe of verplaatste onderwerp.
2. Controleer tegen de acht criteria: ontstaat overlap, wordt de menudiepte overschreden, blijft de routing logisch?
3. Stel een bestandsnaam voor, passend in de bestaande nummering.
4. Presenteer het voorstel, vraag goedkeuring, en werk het structuurbestand bij.

## Vraagpatronen voor de interactieve review

- "Op welke plek verwacht een ouder die enkel de trainingstijd zoekt dit antwoord: [onderdeel A] of [onderdeel B]?"
- "Deze pagina combineert [intentie 1] en [intentie 2]. Wilt u dat splitsen in twee pagina's?"
- "Welke vragen krijgt u in de praktijk het vaakst van nieuwe ouders, en zijn die allemaal gedekt in 6.3?"
- "Deze informatie staat nu op twee plaatsen. Welke plek is de hoofdlocatie en welke wordt een verwijzing?"
- "Dit onderdeel telt [n] pagina's. Blijft dat overzichtelijk in het menu, of is een tussenniveau gewenst?"

Stel geen vragen waarvan het antwoord al uit het structuurbestand of eerdere antwoorden bekend is.

## Wijzigingsworkflow

1. Vertrek vanuit de sectie Huidige structuur in deze Vaardigheid; haal ter controle het bestand `Websitestructuur-jeugd.md` uit de repository op indien aanwezig.
2. Presenteer de voorgestelde wijziging met onderbouwing per criterium.
3. Vraag goedkeuring aan de gebruiker, per wijziging of voor het geheel.
4. Werk het structuurbestand bij: pagina's per onderdeel in tabelvorm (pagina, bestandsnaam, doelgroep, intentie), met daaronder een korte inhoudsbeschrijving.
5. Werk de wijzigingslog onderaan het bestand bij: datum, korte omschrijving, en waar mogelijk de reden.
6. Controleer of de wijziging doorwerkt naar de tabellen in de Vaardigheid `jeugdsport-teksten` en wijs de gebruiker hierop.
7. Leg de wijziging vast in de repository: op een nieuwe branch met een duidelijke commit-boodschap, bijvoorbeeld "Structuur gewijzigd: [onderwerp]", en open een pull request naar main.

## Formaat van de wijzigingslog

Onderaan het structuurbestand staat een vaste logsectie:
