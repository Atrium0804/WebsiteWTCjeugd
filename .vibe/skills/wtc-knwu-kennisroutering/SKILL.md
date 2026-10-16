---
name: wtc-knwu-kennisroutering
description: "Vragen over wielrennen worden beantwoord volgens een vaste bronvolgorde, afhankelijk van het onderwerp. Gebruik deze Vaardigheid voor het routeren van KNWU- en WTC-vragen naar de juiste bronnen."
user-invocable: true
allowed-tools:
  - library_search
  - web_search
  - open_url
  - ask_user_question
---

# WTC/KNWU kennisroutering

Vragen over wielrennen worden beantwoord volgens een vaste bronvolgorde, afhankelijk van het onderwerp.

## Bibliotheken

**WTC/Regio-bibliotheek:** `doclib://01a1411f-ea98-70a8-a3af-b9631fd39baa` (naam: "WTC en regio kennis")
- Documenten: ZMC Zaterdagmiddag Competitie, MNC Reglement Veldrijden 2025, MNC Hans van den Hengel-competitie 2026, NRC-artikel "Hoe kweek je sportplezier bij kinderen" (contextbron over jeugdsport, geen wedstrijdreglement).

**KNWU-bibliotheek:** `doclib://01a1411d-e9bc-747c-98c8-2808dae2094e` (naam: "KNWU-kennis")
- Documenten: Titel 20 Jeugdwielrennen (2026-05-05), Nationale Besluiten (2026-07-01).

**KNWU Kenniscentrum:** [https://kenniscentrum.knwu.nl/](https://kenniscentrum.knwu.nl/) (online, raadpleeg via websearch/open_url).
- Relevante secties: **Regelgeving** ([reglementen-en-jaarlijkse-besluiten](https://kenniscentrum.knwu.nl/regelgeving/reglementen-en-jaarlijkse-besluiten): reglementen, Nationale Besluiten, memo's met wijzigingen) en **Verzekeringen** (dekking en aansprakelijkheid). Andere secties zijn normaal gesproken niet nodig.

**Let op — zichtbare revisies:** de documenten in de doclibs **én** de regelgeving-PDF's op het Kenniscentrum bevatten zichtbare revisies: doorgestreepte (verwijderde) tekst en toegevoegde tekst staan door elkaar. Er zijn geen schone versies.

---

## Regels per vraagtype

### 1. Vraag over een regionale wedstrijd (MNC, ZMC, Hans van den Hengel-competitie, club-/regiowedstrijden)

Zoek **EERST** met `library_search` scoped naar de WTC/Regio-bibliotheek (uri van die bibliotheek).

Antwoord met kennis uit het document van de betreffende wedstrijd. Noem het document als bron met een doclib-link.

Alleen als de WTC/Regio-bibliotheek onvoldoende antwoord geeft, val dan terug op de KNWU-bibliotheek en vermeld expliciet dat de bron KNWU-reglementen zijn in plaats van het wedstrijdreglement.

Eventueel aanvullen met het KNWU-kenniscentrum als beide bibliotheken onvoldoende bieden; vermeld dan de online bron.

---

### 2. Vraag over nationale wedstrijden of KNWU-zaken (Titel 20, nationale besluiten, licenties, NK's, KNWU-beleid)

Gebruik **ALLEEN** de KNWU-bibliotheek en/of het KNWU-kenniscentrum ([https://kenniscentrum.knwu.nl/](https://kenniscentrum.knwu.nl/)).

Zoek **NIET** in de WTC/Regio-bibliotheek voor deze vragen en gebruik die documenten niet als bron.

#### Regelgevingvragen — versiecontrole en wijzigingsmarkeringen

- De doclib-versies bevatten zichtbare revisies (zie "Let op" hierboven): doorgestreepte tekst is vervallen, toegevoegde tekst is nieuw. Het **Kenniscentrum is de autoritatieve bron voor de nieuwste versie** (met versiedata en wijzigingsmemo's).
- **Versiecontrole bij elke nationale regelgevingvraag:** vergelijk de versie/datum van het doclib-document (in de bestandsnaam) met de actueel gepubliceerde versie op de Kenniscentrum-regelgevingpagina. Is de Kenniscentrum-versie nieuwer, gebruik dan de Kenniscentrum-versie als bron voor wat gewijzigd is, en meld de gebruiker expliciet dat de doclib-versie verouderd is (noem beide datums), zodat de doclib geüpdatet kan worden. Leg de werkwijze niet stil maar antwoord met de nieuwste regel.
- Voorbeeld: de KNWU-bibliotheek bevat de Nationale Besluiten van 2026-07-01; het Kenniscentrum publiceert intussen nieuwere versies met memo's t.o.v. de voorgaande versie.

#### Documenten met revisies lezen — wijzigingen en doorgestreepte tekst

- De documenten in de doclibs én de regelgeving-PDF's in het Kenniscentrum zijn exports met zichtbare revisies: doorgestreepte tekst is vervallen, nieuw toegevoegde tekst staat ertussen. Deze beperking kan bij conversie (library_search/websearch/open_url) tot fouten leiden.
- **Doorgestreepte tekst is nooit de huidige regel** — citeer deze niet als antwoord. Baseer je uitsluitend op de definitieve tekst.
- Lijkt een passage tegenstrijdig, dubbel of onduidelijk gemarkeerd, en kan de precieze status (vervallen/nieuw) niet worden vastgesteld, signaleer dit dan expliciet bij het antwoord: meld dat de passage uit een document met zichtbare revisies komt en dat de precieze status niet zeker is (zie ook "Verzin niets — onzekerheid en conflicten signaleren").

---

## Licentievragen — extra bronverplichting

De KNWU-bibliotheek bevat alleen de regelgeving (categorieën, startrecht, NK-selectie), **niet** de pakketstructuur en tarieven.

Raadpleeg bij licentievragen daarom **altijd** ook het KNWU-kenniscentrum (websearch/open_url), ook als de bibliotheek al antwoord lijkt te geven. De licenties U13, U17 en 17+ bestaan elk in drie pakketten: **Basis, Plus en Premium** — noem deze varianten in het antwoord.

**Belangrijk verschil om te melden:** het startrecht (bijv. voor een NK) zit in de licentie zelf; de pakketten verschillen alleen in buitenlandstartrecht, verzekeringsdekking en extra's (UCI-ID, fysieke pas, Fondo-abonnement).

---

## Verzekeringsvragen — bron

Vragen over verzekeringen (dekking, aansprakelijkheid, wat is verzekerd bij welk pakket) beantwoord je primair met de sectie **Verzekeringen** van het Kenniscentrum; raadpleeg daarnaast eventueel de relevante tabel in de Nationale Besluiten (KNWU-bibliotheek).

---

## NK-vragen — verifieer de specifieke context

Bepaal **vóór** het antwoord welke discipline (weg, veldrijden, MTB, baan, BMX) en welke leeftijdscategorie de vraag betreft; de eisen verschillen per NK en per categorie.

Staat discipline of leeftijdscategorie niet in de vraag, haal dan eerst de relevante informatie op (de NK-lijst en eisen per discipline/categorie uit de Nationale Besluiten) en bepaal op basis daarvan welke vragen echt nodig zijn. Stel alleen vragen over parameters die niet uit de bronnen af te leiden zijn **én** die tot een wezenlijk ander antwoord leiden — en stel die vragen in één keer tegelijk (zie paragraaf 3).

---

## 3. Onduidelijk onderwerp of ontbrekende context

**Volgorde:** eerst bronnen raadplegen, dan pas vragen stellen. Stel geen vragen voordat je hebt gecheckt wat de bronnen zelf al opleveren.

Bepaal de mogelijke varianten die de vraag kan hebben (bijv. regio- vs. nationaal; discipline; leeftijdscategorie).

Raadpleeg eerst de bronnen (`library_search` in de relevante bibliotheek, eventueel het Kenniscentrum) om te zien welke varianten daadwerkelijk bestaan en welke eisen/antwoorden per variant gelden.

Filter daarna de vragen: stel alleen vragen over parameters die (a) niet uit de vraag, context of bronnen af te leiden zijn **én** (b) tot een wezenlijk ander antwoord leiden. Leidt een parameter niet tot een ander antwoord, vraag er dan niet naar maar noem eventuele variantie in het antwoord.

Stel alle resterende vragen in **één keer tegelijk** via `ask_user_question` (max. 4 korte vragen met concrete opties), zodat de gebruiker na één ronde een eenduidig antwoord krijgt — geen tussenliggende follow-up-rondes.

Kun je uitsluitend door vragen stellen de juiste bron/bibliotheek bepaald worden (regionaal vs. nationaal), vraag dan eerst alleen dát (met concrete opties, bijv. "gaat dit over de MNC-veldritcompetitie of over nationale KNWU-regels?") en ga daarna pas de bronnen in.

Beantwoord liever **één specifieke situatie concreet** dan dat je een generiek overzicht geeft dat niet past bij de renner in kwestie.

---

## Algemeen

### Taalniveau — keuze bij eerste gebruik van deze Vaardigheid

Is er nog geen taalniveau vastgelegd in de kennisbasis (onderwerp WTC-communicatie, bestand taalniveau)? Vraag dan bij de eerste keer dat deze Vaardigheid wordt gebruikt naar het gewenste taalniveau, met deze twee opties:

- **Begrijpelijk (niveau B1):** korte zinnen, actieve vorm, gewone woorden; vaktermen kort uitleggen (bijv. "startrecht" → "je mag meedoen aan").
- **Uitgebreid (niveau B2):** volledigere zinnen met bijzinnen, ruimere woordenschat.

Leg de keuze direct vast in de kennisbasis (WTC-communicatie → taalniveau) en pas het gekozen niveau daarna automatisch toe op alle antwoorden.

Heeft de gebruiker **Uitgebreid (B2)** gekozen? Bied dan zo nodig aan om het antwoord (of een deel ervan) om te zetten naar begrijpelijk Nederlands (B1) — vooral als het antwoord bedoeld is om te delen met leden of ouders.

---

### Bronvermelding

Citeer **altijd** het gebruikte document met een Markdown-link naar de `doclib://` URI.

Scope `library_search` altijd naar de juiste bibliotheek via de `uri`-parameter; zoek niet ongescoped over alle bibliotheken.

Als een document een datum/versie in de naam heeft, gebruik dan de nieuwste versie en vermeld de datum van het reglement in het antwoord (zie ook de versiecontrole bij nationale regelgevingvragen).

---

## Verzin niets — onzekerheid en conflicten signaleren

Verzin nooit informatie. Geen regels, data, bedragen, uitspraken of conclusies die niet (direct) in de geraadpleegde bronnen staan. Ontbreekt informatie, zeg dat dan gewoon.

Ben je onzeker van een uitleg of status van een passage, signaleer dit dan expliciet in het antwoord — benoem wat onzeker is en waarom.

Geven bronnen conflicterende of tegengestelde informatie, signaleer dit dan ook expliciet: benoem het verschil en noem de betrokken bronnen (met links).

Gaat het over KNWU-zaken en blijft de onzekerheid of het conflict bestaan, raad de gebruiker dan aan contact op te nemen met de KNWU: +31 (0)85 070 1900, dinsdag tot en met vrijdag van 8.30–12.00 uur.
