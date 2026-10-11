
---
name: clubapp-html-conversie
description: "Converteer geplakte Markdown naar ClubApp-HTML (AllUnited) voor WTC Woerden. Gebruik bij elke aanvraag om markdown of geplakte tekst met <br /> soft returns om te zetten naar correcte ClubApp-pagina-HTML met header-span-klassen, echte alinea's en lijsten."
user-invocable: true
allowed-tools:
  - ask_user_question
---

# ClubApp HTML-conversie (WTC Woerden)

Zet geplakte Markdown om naar de HTML-structuur die de ClubApp-pagina-editor (AllUnited) verwacht. De ClubApp-editor slaat geplakte Markdown op als één `<p>` vol soft returns (`<br /><br />`); dat levert inspringende lijsten en gebroken koppen op. Deze Vaardigheid zet dat om naar de juiste paginacode.

## Herken het probleem

De input ziet er zo uit: één `<p>`-blok waarin de hele tekst zit, met:

- `#`, `##`, `###` als letterlijke tekst voor koppen;
- `**bold**`, `*italic*`, `link` als letterlijke markdown;
- `<br /><br />` tussen alinea's, `<br />` als regeleinde;
- lijsten als `- item` regels, geneste lijsten als `&#160; - item` of ingesprongen regels;
- HTML-entiteiten zoals `&#235;` (ë), `&#8211;` (–), `&gt;`, `&amp;`.

## Conversieregels

Vergelijk met een bestaande, correcte ClubApp-pagina als referentie als de gebruiker die deelt.

### Koppen

- `#` en `##` (sectiekoppen) → eigen alinea met sectiekop-klasse:
  `<p><span class="header3 header4">Titel</span></p>`
- `###` (tussenkopjes) → `<p><span class="header5">Titel</span></p>`

### Alinea's en scheidingslijnen

- Elke alinea wordt een eigen `<p>`-element; alle `<br /><br />` soft returns verdwijnen.
- `---` scheidingslijnen weglaten; correcte ClubApp-pagina's gebruiken ze niet.

### Lijsten

- `- item` → `<ul>` met elk item als `<li>`.
- Genummerde lijsten (`1.`, `2.`) → `<ol>` met `<li>`.
- Geneste lijsten (inspringing of `&#160;`) → `<ul>` binnen de betreffende `<li>`.
- Gebruik tab-inspringing voor `<li>`-elementen, zoals in bestaande ClubApp-pagina's.

### Inline opmaak en links

- `**tekst**` → `<strong>tekst</strong>`, `*tekst*` → `<em>tekst</em>`.
- `[tekst](url)` → `<a href="url">tekst</a>`; `&` in URL's als `&amp;`.
- Bestaande HTML-entiteiten (`&#235;` etc.) laten staan.

### Weglaten en melden

- `> [!note]`-blokken zijn meestal interne redactie-opmerkingen: weglaten uit de pagina en apart melden aan de gebruiker.
- Onafgemaakte zinnen ongewijzigd overnemen en markeren als aandachtspunt.
- Twijfelgevallen altijd noemen in het antwoord, niet zelf oplossen.

## Output

- Lever de volledige HTML aan in één code-blok, klaar om in de ClubApp-editor te plakken (HTML-bronmodus).
- Geef daarna kort de belangrijkste wijzigingen en eventuele aandachtspunten.