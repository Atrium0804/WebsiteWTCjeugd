# AGENTS.md — stuurinformatie voor agents

Website­teksten jeugdsectie WTC Woerden (ClubApp/AllUnited CMS). De volledige workflow, commando's en Markdown-conventies staan in `tools/README.md` — dat is de bron van waarheid voor de tooling.

## Kernregels

1. **Markdown is de bron.** Bewerk uitsluitend `websiteteksten/website_teksten md/`. De HTML in `websiteteksten/website_teksten html/` is gegenereerd; pas die nooit handmatig aan, ook niet om een tekstaanpassing door te voeren.
2. **Genereer met het script, nooit met de hand of uit het hoofd.** Na een Markdown-wijziging draai je `python tools/websiteteksten_sync.py build` en daarna `check`. Vertrouw op de deterministische output van het script; schrijf zelf geen ClubApp-HTML als een bestand in `website_teksten md/` bestaat.
3. **Publicatievolgorde:** tekstwijziging in de Markdown, versie verhogen met `python tools/websiteteksten_sync.py bump "<bestand>.md"` (herbouwt meteen de HTML), HTML kopiëren naar ClubApp (introductie vóór `<!-- --- -->`, details erna). Publiceer nooit zonder `bump`: `check` geeft een aanwijzing zodra inhoud is gewijzigd zonder nieuwe versie.
4. **Wijziging direct in ClubApp gedaan?** Zet die terug met de skill `clubapp-naar-repo`: HTML naar het `.html`-bestand, daarna `python tools/websiteteksten_sync.py import "<bestand>.html"` en controleren met `git diff`. `import` slaat bestanden met niet-gecommitte wijzigingen over; vraag de gebruiker die eerst zelf te committen.
5. **Versiebeheer doet de gebruiker.** Laat al je wijzigingen ongecommit in de werkmap staan en noem aan het eind welke bestanden je hebt aangepast. Draai zelf geen `git commit`, `git push` of andere git-opdrachten die de historie of werkmap veranderen.

Stapsgewijze procedures voor de drie standaardsituaties (publiceren, terugvoeren naar de repo, sync-check) staan in `README.md`, sectie *Hoe moet ik…*.

## Structuur en inhoud

- `Websitestructuur-jeugd.md` is de bron van waarheid voor de paginestructuur, doelgroepen en intenties per pagina.
- Bestandsnaamconventie: `<paginatitel> - <clubapp artikel-id>.md` ↔ zelfde naam met `.html`. Pagina en artikel-id staan ook in de front matter.
- Front matter (`pagina`, `doelgroep`, `kanaal`, `intentie`, `clubapp artikel-id`, `paginacode`, `versie`) is verplicht; het script waarschuwt als `pagina` ontbreekt.
- Schrijf Nederlandstalig, in de stijl van de skill `jeugdsport-teksten` (doelgroep bepaalt de toon: kinderen 6-14 enthousiasmerend, ouders praktisch) en op het taalniveau uit de skill `taalniveau` (B1 voor ouders, kindniveau voor kinderen).

## Skills

Laad de bijbehorende skill vóór het werk:

- Verenigingstekst, post, aankondiging of webcontent schrijven/herschrijven → `jeugdsport-teksten`
- Tekst controleren of herschrijven op taalniveau (kindniveau, B1, B2) → `taalniveau`
- Geplaste Markdown of tekst mét `<br />` soft returns omzetten naar ClubApp-HTML (alleen losse tekst, niet voor bestanden in `website_teksten md/`) → `markdown-naar-clubapp-html`
- Een ClubApp-pagina die direct in het CMS is gewijzigd terugzetten naar de repo (HTML opslaan + `import` naar Markdown) → `clubapp-naar-repo`
- Structuur beoordelen, pagina toevoegen of herordenen → `website-structuur`
- Vraag over KNWU-reglementen, licenties, MNC/ZMC-wedstrijden → `wtc-knwu-kennisroutering`

## Naslag

- `Bibliotheken/` is de repo-spiegel van de doclibs uit de webversie van Vibe: per bibliotheek een submap met dezelfde documenten. Werk doclib en spiegel samen bij. De skill `wtc-knwu-kennisroutering` kiest per omgeving de juiste bron: doclib (web, via `library_search`) of repo-spiegel (VS Code, geen doclib).
- `context/` is stijl- en toonreferentie, geen feitenbron. Feiten over wedstrijdreglementen komen via de skill `wtc-knwu-kennisroutering`.
- `websiteteksten/websiteteksten md - oud/` is archief; niet meer gebruiken als bron.
