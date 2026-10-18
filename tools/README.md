# Websiteteksten: Markdown ↔ ClubApp-HTML

Met [`websiteteksten_sync.py`](websiteteksten_sync.py) bewerk je de jeugdpagina's van de website in Markdown, bijvoorbeeld in [Typora](https://typora.io). Het script maakt daar automatisch de HTML van die je in de ClubApp-editor (AllUnited) plakt.

| Map | Rol |
| --- | --- |
| [`websiteteksten/website_teksten md/`](../websiteteksten/website_teksten%20md/) | **Bron.** Hier bewerk je de teksten. |
| [`websiteteksten/website_teksten html/`](../websiteteksten/website_teksten%20html/) | **Gegenereerd.** Niet met de hand aanpassen, behalve bij een import (zie hieronder). |

Een Markdown-bestand en het bijbehorende HTML-bestand hebben dezelfde naam, bijvoorbeeld `Trainingen - 1014.md` ↔ `Trainingen - 1014.html`.

## Benodigdheden

- Python 3.10 of nieuwer
- [pandoc](https://pandoc.org/installing.html), beschikbaar op het `PATH`
- De Python-pakketten `beautifulsoup4` en `PyYAML`:

  ```powershell
  pip install beautifulsoup4 PyYAML
  ```

## Werkwijze

### 1. Tekst bewerken

1. Open een bestand uit `website_teksten md/` in Typora en sla het op.
2. De HTML wordt bijgewerkt:
   - **automatisch**, als de VS Code-taak *Websiteteksten: watch (MD → HTML)* draait (zie [VS Code-taken](#vs-code-taken)), of
   - **met de hand**: `python tools/websiteteksten_sync.py build`
3. Verhoog `versie` in de front matter als de wijziging gepubliceerd wordt.
4. Kopieer de HTML naar ClubApp (HTML-bronmodus):
   - alles **vóór** `<!-- --- -->` (inclusief het `<script>`) gaat in het introductieveld;
   - alles **na** `<!-- --- -->` gaat in het detailveld.
   - Het metadata-commentaar bovenaan hoef je niet te kopiëren.

### 2. Tekst is direct in ClubApp gewijzigd

1. Kopieer de HTML uit ClubApp naar het bijbehorende `.html`-bestand. Laat het metadata-commentaar bovenaan en de scheiding `<!-- --- -->` staan. De skill `clubapp-naar-html` kan hierbij helpen.
2. Zet de wijziging om naar Markdown:

   ```powershell
   python tools/websiteteksten_sync.py import "Trainingen - 1014.html"
   ```

3. Controleer de wijziging in de Markdown, bijvoorbeeld met `git diff`.

> **Beveiliging:** heeft het Markdown-bestand nog wijzigingen die niet gecommit zijn, dan slaat `import` het bestand over, zodat je werk niet verloren gaat. Commit eerst, of gebruik `--force` als je de Markdown echt wilt overschrijven.

### 3. Controleren

```powershell
python tools/websiteteksten_sync.py check
```

`check` meldt per bestand of de HTML afwijkt van de Markdown en of er bestanden zonder tegenhanger zijn. Als alles klopt, zie je `alles in sync`.

## Commando's

```text
python tools/websiteteksten_sync.py build  [bestanden...]   Markdown → HTML (standaard: alle bestanden)
python tools/websiteteksten_sync.py import [bestanden...]   HTML → Markdown (--force: overschrijf niet-gecommitte Markdown)
python tools/websiteteksten_sync.py check  [bestanden...]   Controleer of HTML en Markdown in sync zijn
python tools/websiteteksten_sync.py watch  [--interval 1]   Bouw HTML opnieuw bij elke opgeslagen .md
```

Je kunt bestanden opgeven als naam (`"Trainingen - 1014.md"`) of als pad. De extensie mag `.md` of `.html` zijn; het script zoekt zelf de juiste tegenhanger.

## VS Code-taken

In [`.vscode/tasks.json`](../.vscode/tasks.json) staan deze taken (*Terminal → Run Task…*):

| Taak | Wat het doet |
| --- | --- |
| Websiteteksten: watch (MD → HTML) | Start automatisch bij het openen van de map en bouwt de HTML bij elke opgeslagen `.md`. |
| Websiteteksten: build (MD → HTML) | Standaard build-taak (`Ctrl+Shift+B`). |
| Websiteteksten: import (HTML → MD) | Zet alle HTML-bestanden om naar Markdown. |
| Websiteteksten: check | Controleert of alles in sync is. |

De eerste keer vraagt VS Code of automatische taken mogen draaien. Kies *Allow*. De watcher draait alleen zolang VS Code open is. Heb je in Typora gewerkt terwijl VS Code dicht was, dan bouwt de watcher bij de volgende start alle bestanden waarvan de Markdown nieuwer is dan de HTML.

## Markdown-conventies

### Front matter (metadata)

Elk bestand begint met de metadata. Daaruit maakt het script het metadata-commentaar en de witte voettekst (`pagina: …; versie …`).

```yaml
---
pagina: Trainingen
doelgroep: ouders van nieuwe/bestaande leden
kanaal: websitetekst
intentie: uitleggen
clubapp artikel-id: 1014
paginacode: jeugd_hoewerkthet
versie: '1.0'
---
```

Met `umami: false` laat je het Umami-script weg. Standaard voegt het script het altijd toe.

### Opbouw van een pagina

| Markdown | ClubApp-HTML |
| --- | --- |
| Tekst vóór de eerste `---` | Introductie (met het Umami-script erachter) |
| Eerste `---` (scheidingslijn) | `<!-- --- -->`, de scheiding tussen introductie en details |
| `## Kop` | `<p><span class="header4">Kop</span></p>` (sectiekop) |
| `### Kop` | `<p><span class="header5">Kop</span></p>` (tussenkop) |
| Gewone alinea | `<p>…</p>` |
| `**vet**`, `*cursief*` | `<strong>`, `<em>` |
| `[tekst](https://…)` | `<a href="…">tekst</a>` |
| Opsommingen (`-`, `1.`), ook genest | `<ul>` / `<ol>` met tab-inspringing |
| Tabel | Tabel met de standaard ClubApp-opmaak; de eerste rij wordt een kopregel (`<th>`) |
| Backslash `\` aan het eind van een regel (harde regelovergang) | `<br />` |

### Afbeeldingen

- Afbeeldingen staan als HTML-tag in de Markdown, zodat breedte, hoogte en stijl bewaard blijven:

  ```html
  <img src="https://www.wtcwoerden.nl/userfiles/jeugd_welkom/foto.jpg" alt="Omschrijving" width="649" height="487" />
  ```

- Staan **twee of meer afbeeldingen in één alinea** (op één regel), dan komen ze naast elkaar in een fototabel.
- Een gewone Markdown-afbeelding `![alt](url)` werkt ook, maar heeft dan geen vaste afmetingen.
- Afbeeldingen moeten eerst naar ClubApp geüpload zijn (`https://www.wtcwoerden.nl/userfiles/…`). Bij een lokaal pad geeft `build` een waarschuwing.

### Overige HTML

HTML waarvoor geen Markdown-variant bestaat (bijvoorbeeld een `<span>` met opmaak, `<sub>` of een complexe tabel) blijft als HTML in de Markdown staan en gaat ongewijzigd naar de uitvoer.

## Aandachtspunten

- **Bewerk de HTML niet met de hand.** De volgende `build` of de watcher overschrijft die wijzigingen. Wijzigingen uit ClubApp verwerk je via `import`.
- Een kale URL in de tekst wordt **geen** link. Gebruik `[tekst](url)`.
- Alleen de **eerste** `---` geldt als scheiding. Latere scheidingslijnen vallen weg, omdat ClubApp-pagina's ze niet gebruiken.
- Twee lijsten direct na elkaar worden in de Markdown gescheiden door `<!-- -->`. Haal dat niet weg, anders worden ze één lijst.
- Na `import` en daarna `build` krijg je dezelfde HTML terug (en andersom). `check` gebruikt dat om afwijkingen te vinden.
