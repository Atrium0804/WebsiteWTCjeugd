---
name: clubapp-naar-html
description: "Sla ClubApp-pagina's op als HTML-bestand in de repository met metadata, scheiding tussen introductie/details en voettekst. Gebruik voor WTC Woerden websiteteksten."
user-invocable: true
allowed-tools:
  - ask_user_question
  - read_file
  - write_file
  - edit
---

# Skill: clubapp-naar-html

## ClubApp-tekst opslaan als HTML

**Doel:** ClubApp-teksten opslaan als **één HTML-bestand** in de repository, met een duidelijke scheiding tussen introductie en details.

**Gebruik deze Vaardigheid wanneer:** de gebruiker een ClubApp-pagina wil opslaan als HTML in de repository.

---

## Werkinstructie

Wanneer een gebruiker een ClubApp-pagina wil opslaan als HTML, volg dan deze stappen:

### Stap 1: Metadata verzamelen
Vraag de gebruiker om de volgende **verplichte metadata**. Gebruik `ask_user_question` als informatie ontbreekt:

| **Veld** | **Beschrijving** | **Voorbeeld** | **Verplicht** |
|---------|----------------|---------------|---------------|
| `pagina` | Titel van de pagina | "Welkom bij de jeugd", "Hoe werkt het/wedstrijden" | ✅ |
| `doelgroep` | Doelgroep van de tekst | "jeugd die overweegt lid te worden (6-14 jaar)", "ouders van nieuwe leden" | ✅ |
| `kanaal` | Publicatiekanaal | "websitetekst" | ✅ |
| `intentie` | Doel van de tekst | "enthousiasmeren", "informeren", "uitnodigen" | ✅ |
| `clubapp artikel-id` | Artikel-ID uit ClubApp | 54, 1010, 1011 | ✅ |
| `paginacode` | Paginacode uit ClubApp | "jeugd_welkom", "jeugd_watdoenwe" | ✅ |
| `versie` | Versienummer | "1.0" | ✅ |

**Optionele velden:**
- `datum`: Publicatiedatum (indien relevant)
- `auteur`: Auteur van de tekst

**Vraagpatroon:**
```
"Geef aub de volgende metadata voor de ClubApp-pagina:
- Pagina: 
- Doelgroep: 
- Kanaal: 
- Intentie: 
- ClubApp Artikel-ID: 
- Paginacode: 
- Versie: "
```

### Stap 2: Tekstdelen ontvangen
Vraag de gebruiker om **beide tekstdelen** van de ClubApp-pagina:

1. **Introductie** (korte inleidingstekst)
2. **Details** (uitgebreide inhoud)

**Belangrijk:**
- Beide delen zijn **verplicht**
- Als de gebruiker **markdown** levert, gebruik dan de skill `markdown-naar-clubapp-html` om deze om te zetten naar HTML

### Stap 3: HTML-bestand samenstellen
Voeg de tekstdelen samen in **één HTML-bestand** met de volgende structuur:

```html
<!--
metadata:
- pagina: [pagina]
- doelgroep: [doelgroep]
- kanaal: [kanaal]
- intentie: [intentie]
- clubapp artikel-id: [clubapp artikel-id]
- paginacode: [paginacode]
- versie: [versie]
-->

[INTRODUCTIE-TEKST]

<!-- --- -->

[DETAILS-TEKST]

<p><span style="color: #ffffff;">pagina: [pagina]; versie [versie]</span></p>
```

**Opmerking:**
- Tussen introductie en details: **witregel + `<!-- --- -->` + witregel**
- Voettekst **alleen onderaan** (na de details)

### Stap 4: Bestandsnaam bepalen
Gebruik de volgende naamconventie:
```
[pagina] - [clubapp artikel-id].html
```

**Voorbeelden:**
| **Pagina** | **Artikel-ID** | **Bestandsnaam** |
|------------|----------------|------------------|
| Welkom bij de jeugd | 54 | `Welkom bij de jeugd - 54.html` |
| Wat doen we | 1011 | `Wat doen we - 1011.html` |
| Hoe werkt het/wedstrijden | 1015 | `Hoe werkt het/wedstrijden - 1015.html` |

**Regels:**
- Behoud de originele pagina-titel (inclusief spaties en leestekens)
- Voeg het artikel-ID toe na een koppelteken
- Gebruik `.html` extensie

### Stap 5: Locatie
Sla het bestand op in:
```
C:\git_prive\WebsiteWTCjeugd\websiteteksten\website_teksten html\[bestandsnaam].html
```

### Stap 6: Bestandsvalidatie
Controleer voor het opslaan:
- [ ] Metadata is compleet
- [ ] Scheiding tussen introductie en details: witregel + `<!-- --- -->` + witregel
- [ ] Voettekst is toegevoegd (alleen onderaan)
- [ ] Alle afbeeldings-URLs zijn correct
- [ ] HTML is valide (geen open tags, correcte structuur)
- [ ] Bestandsnaam volgt de conventie `{pagina} - {artikel-id}.html`

### Stap 7: Opslaan en bevestigen
Sla het bestand op en bevestig aan de gebruiker:
```
"ClubApp-pagina opgeslagen als: websiteteksten/website_teksten html/[pagina] - [artikel-id].html

Met de volgende metadata:
- pagina: [pagina]
- doelgroep: [doelgroep]
- intentie: [intentie]
- clubapp artikel-id: [id]
- versie: [versie]

Scheiding: witregel + <!-- --- --> + witregel"
```

---

## Gebruiksvoorbeelden

### Voorbeeld 1: Nieuwe pagina opslaan
**Gebruiker:** "Ik wil de ClubApp-pagina 'Welkom bij de jeugd' (artikel 54) opslaan."

**Actie:**
1. Vraag om metadata (doelgroep, kanaal, intentie, paginacode, versie)
2. Vraag om beide tekstdelen (introductie en details)
3. Voeg samen met scheiding: witregel + `<!-- --- -->` + witregel
4. Voeg metadata en voettekst toe
5. Sla op als `websiteteksten/website_teksten html/Welkom bij de jeugd - 54.html`

### Voorbeeld 2: Bestaand bestand bijwerken
**Gebruiker:** "De tekst van 'Wat doen we - 1011.html' moet bijgewerkt worden."

**Actie:**
1. Lees het bestaande bestand
2. Vraag om de nieuwe tekstdelen (introductie en details)
3. Behoud de metadata of vraag om updates
4. Verhoog het versienummer (bijv. 1.0 → 1.1)
5. Sla het bijgewerkte bestand op met de scheiding

---

## Bestandsnaamconventie

| **Pagina** | **Artikel-ID** | **Bestandsnaam** |
|------------|----------------|------------------|
| Welkom bij de jeugd | 54 | `Welkom bij de jeugd - 54.html` |
| Wat doen we | 1011 | `Wat doen we - 1011.html` |
| Hoe werkt het/wedstrijden | 1015 | `Hoe werkt het/wedstrijden - 1015.html` |

**Regels:**
- Behoud de originele titel (inclusief spaties, leestekens, schuine streepjes)
- Voeg het artikel-ID toe na een koppelteken
- Gebruik `.html` extensie

---

## Notities

- **Metadata in HTML-comments** blijft niet bewaard in het CMS. De voettekst (`pagina: ...; versie ...`) is essentieel voor traceerbaarheid.
- Gebruik **UTF-8 encoding** voor alle HTML-bestanden.
- **Afbeeldingen**: Controleer altijd of de afbeeldings-URLs correct zijn en wijzen naar `https://www.wtcwoerden.nl/userfiles/...`
- **Consistentie**: Gebruik dezelfde metadata-velden als in de skill `jeugdsport-teksten` voor consistentie.
- **Één bestand**: Elke ClubApp-pagina wordt opgeslagen als **één HTML-bestand** met scheiding tussen introductie en details.
- **Scheiding**: Gebruik **witregel + `<!-- --- -->` + witregel** tussen introductie en details.
- **Versiebeheer**: Verhoog het versienummer bij elke wijziging (bijv. 1.0 → 1.1 → 1.2).

---

## Gerelateerde Skills

- `jeugdsport-teksten`: Voor het schrijven van teksten volgens WTC Woerden-stijl
- `markdown-naar-clubapp-html`: Voor het converteren van markdown/tekst naar ClubApp-HTML
- `website-structuur`: Voor het beoordelen van de websitestructuur
