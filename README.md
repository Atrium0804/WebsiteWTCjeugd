# WebsiteWTCjeugd — websiteteksten jeugd WTC Woerden

Deze repository bevat de teksten voor de jeugdsectie van [wtcwoerden.nl](https://www.wtcwoerden.nl). De site draait op ClubApp van AllUnited: teksten worden als HTML in de pagina-editor geplakt.

**Kernprincipe: Markdown is de bron, HTML is gegenereerd.** Bewerk altijd de Markdown in `websiteteksten/website_teksten md/`. De bijbehorende ClubApp-HTML in `websiteteksten/website_teksten html/` komt daar deterministisch uit via `tools/websiteteksten_sync.py` — pas die dus nooit handmatig aan.

De documentatie is als volgt ingedeed::

- **Aan de slag** — eenmalige voorbereiding (een keer lezen)
- **Hoe moet ik…** — stapsgewijze procedures voor de drie standaardsituaties (taakgericht)
- **Naslag** — mappen, conventies en commando's (opzoeken)
- **Uitleg** — waarom het zo werkt (achtergrond)

Agent-stuurinformatie staat in [AGENTS.md](AGENTS.md).

## Aan de slag (eenmalig)

Benodigdheden: Python 3.10+, [pandoc](https://pandoc.org/installing.html) op het `PATH`, en `pip install beautifulsoup4 PyYAML`. Verder een Markdown-editor naar keuze (bijv. Typora).

1. Open de map in VS Code en kies bij de prompt *Allow*. De taak *Websiteteksten: watch* draait dan op de achtergrond en bouwt de HTML opnieuw bij elke opgeslagen `.md`.
2. Zonder VS Code: draai na elke wijziging `python tools/websiteteksten_sync.py build`.

Zodra de watcher draait is de repo klaar voor gebruik: elke Markdown-wijziging verschijnt direct als HTML ernaast. Heb je in Typora gewerkt terwijl VS Code dicht was, dan bouwt de watcher bij de volgende start alles wat nieuwer is.

## Hoe moet ik…

### 1. Een tekst bewerken en publiceren op de site

1. Open het pagina-bestand in `websiteteksten/website_teksten md/` (bijv. `Trainingen - 1014.md`) en pas de tekst aan.
2. Verhoog de versie met één commando: `python tools/websiteteksten_sync.py bump "Trainingen - 1014.md"` (bijv. 1.3 → 1.4). Het script herbouwt de HTML direct, inclusief de nieuwe versie in de voettekst.
3. Open het bijbehorende `.html`-bestand en kopieer het naar de ClubApp-pagina-editor in de HTML-bronmodus:
   - alles **vóór** `<!-- --- -->` gaat in het veld **introductie** — het metadata-commentaar bovenaan negeren, het `<script>`-blok wél meenemen;
   - alles **na** `<!-- --- -->`, inclusief de witte voettekst onderaan, gaat in het veld **details**.
4. Publiceer de pagina en controleer het resultaat op de site.

### 2. Een aanpassing op de site terugvoeren naar de repo

Voor wijzigingen die direct in ClubApp zijn gemaakt.

1. Commit eerst eventueel openstaand Markdown-werk: `import` slaat bestanden met niet-gecommitte wijzigingen over (tenzij `--force`). Agents committen niet zelf — vraag de gebruiker dit te doen.
2. Kopieer de HTML uit ClubApp (HTML-bronmodus: introductie en details) naar het bijbehorende `.html`-bestand. Behoud het metadata-commentaar bovenaan, de scheiding `<!-- --- -->` en de voettekst onderaan. De skill `clubapp-naar-repo` kan hierbij helpen.
3. Zet de wijziging om naar Markdown:

   ```powershell
   python tools/websiteteksten_sync.py import "Trainingen - 1014.html"
   ```

4. Controleer het resultaat met `git diff`. Het committen laat de agent aan de gebruiker over (zie AGENTS.md, kernregel 5).

### 3. Controleren of de repo en de site nog in sync zijn

Sync bestaat uit twee niveaus; die kunnen los van elkaar afwijken.

**Binnen de repo (Markdown ↔ HTML):**

```powershell
python tools/websiteteksten_sync.py check
```

Zie je `alles in sync`, dan passen Markdown en HTML bij elkaar. Zo niet: draai `build` als de Markdown is bijgewerkt, of volg situatie 2 als de HTML (of de site) is bijgewerkt.

Meldt `check` een *aanwijzing* "inhoud gewijzigd zonder nieuwe versie", dan is er een wijziging die niet met een versieverhoging gepubliceerd is. Draai in dat geval `bump` vóór het plakken in ClubApp, anders klopt de voettekst op de site niet meer bij de inhoud.

**Tussen de repo en de live site:** daarvoor bestaat geen automatische check — ClubApp is van buitenaf niet te bevragen. Vergelijk handmatig:

1. Open de pagina in ClubApp in de HTML-bronmodus en zoek onderaan de voettekst `pagina: …; versie …`.
2. Vergelijk dat versienummer met de voettekst in het `.html`-bestand en met `versie` in de front matter van de Markdown.
3. Is de site vooruit → volg situatie 2. Is de repo vooruit → volg situatie 1.

Wordt de versie-conventie niet gevolgd (iemand publiceerde zonder het versienummer te verhogen), dan blijft als vergelijking over: de HTML-bron van de pagina naast het `.html`-bestand in de repo leggen.

## Naslag

### Mappen

```
Websitestructuur-jeugd.md      Bron van waarheid voor de paginestructuur van de jeugdsectie
websiteteksten/
├── website_teksten md/        Bron: bewerkbare teksten (per pagina 1 bestand)
├── website_teksten html/      Gegenereerd: HTML om te plakken in ClubApp
└── websiteteksten md - oud/   Archief van eerdere teksten
context/                       Naslag: KNWU/reglementen-PDF's, referentieteksten (stijl, geen feitenbron)
media/                         Logo's
afbeeldingen/                  Werkbestanden voor foto's (niet in git)
tools/                         Conversiescript + tool-naslag (tools/README.md)
.vibe/skills/                  Vaardigheden voor agents
```

### Bestanden en metadata

- Naamconventie: `<paginatitel> - <clubapp artikel-id>.md` ↔ `.html` met dezelfde naam; het artikel-id correspondeert met het artikel in ClubApp.
- Front matter per bestand: `pagina`, `doelgroep`, `kanaal`, `intentie`, `clubapp artikel-id`, `paginacode`, `versie`; optioneel `umami: false`, `datum`, `auteur`.
- `Websitestructuur-jeugd.md` is de bron van waarheid voor paginestructuur, doelgroepen en intenties.

### Commando's

| Commando | Werking |
| --- | --- |
| `build` | Markdown → HTML (standaard: alle bestanden) |
| `import` | HTML → Markdown; slaat niet-gecommitte Markdown over (tenzij `--force`) |
| `check` | Toont of HTML en Markdown in sync zijn; plus aanwijzingen voor inhoud zonder nieuwe versie |
| `bump` | Verhoogt de versie (laatste getal +1, of `--versie x.y`) en herbouwt de HTML direct |
| `watch` | Bouwt HTML opnieuw bij elke opgeslagen `.md` |

Alle Markdown-conventies, opties en de VS Code-taken: [tools/README.md](tools/README.md).

### Vaardigheden (agents)

| Skill | Gebruik |
| --- | --- |
| `jeugdsport-teksten` | Verenigingsteksten, posts en websiteteksten in de WTC Woerden-stijl |
| `markdown-naar-clubapp-html` | Losse, geplaste tekst omzetten naar ClubApp-HTML |
| `clubapp-naar-repo` | Een direct in het CMS gewijzigde pagina terugzetten naar de repo: HTML opslaan en met `import` de Markdown bijwerken |
| `website-structuur` | Structuur beoordelen, verfijnen of uitbreiden |
| `wtc-knwu-kennisroutering` | Wedstrijd-/reglementvragen routeren naar de juiste bron |

## Uitleg

### Waarom Markdown als bron

De Markdown is leesbaar en goed bewerkbaar (Typora) en levert bruikbare git-diffs. De ClubApp-HTML is deterministisch: het script bouwt vanuit de Markdown altijd dezelfde HTML op (`import` gevolgd door `build` geeft het oorspronkelijke bestand terug). Daarom hoeft de HTML niet handmatig te worden verzorgd — en mag dat ook niet: de volgende `build` of de watcher overschrijft handwerk.

### Opbouw van een gegenereerd HTML-bestand

| Onderdeel | Rol |
| --- | --- |
| `<!-- metadata: … -->` bovenaan | Metadata voor de repo. Niet kopiëren naar ClubApp; het CMS laat comments weg. |
| Introductie-tekst + `<script>` | Naar het introductieveld. Het script meet paginaweergaven met Umami; `umami: false` in de front matter laat het weg. |
| `<!-- --- -->` | Scheiding tussen de twee velden van een ClubApp-pagina: introductie en details. In de Markdown is dit de eerste `---`. |
| Detail-tekst | Naar het detailveld. |
| `<p><span style="color: #ffffff;">pagina: …; versie …</span></p>` | Witte voettekst: onzichtbaar op de site, maar de enige traceerbaarheid die het CMS laat staan. Hiermee vergelijk je site en repo (situatie 3). |

### Waarom het versienummer

Het versienummer is het vergelijkingspunt tussen repo en site. Omdat het in de witte voettekst meereist naar de site, kun je met één blik op de HTML-bron in ClubApp zien of de repo en de site uit de pas lopen — een automatische check tegen de site is er niet. Het ophogen hoort daarom vast bij het publiceren: `bump` is één commando dat de versie verhoogt én de HTML herbouwt, en `check` geeft een aanwijzing zodra er inhoud is gewijzigd zonder nieuwe versie.
