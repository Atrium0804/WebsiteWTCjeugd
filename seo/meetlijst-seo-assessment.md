# Meetlijst SEO-assessment jeugdpagina's WTC Woerden

Vaste lijst om de vindbaarheid van wtcwoerden.nl (jeugdsectie) te meten. Bedoeld om elk kwartaal op dezelfde manier te herhalen, zodat je trends ziet.

**Hoe te gebruiken:**

1. Voer elke meting uit in een privévenster (Brave of Google, uitgelogd), op desktop én mobiel.
2. Vul de tabellen in bij de kolom van het lopende kwartaal. Neem bij elke zoekopdracht op: positie van wtcwoerden.nl (of "niet gevonden") en welke URL verschijnt.
3. Noteer onderaan in het log welke acties eruit zijn followed.

**Baseline:** 29 oktober 2026, gemeten via Brave Search (zie kolom "Q4 2026").

---

## 1. Zoekresultaten (SERP-check)

Zoekopdrachten zoals een ouder die zoekt. Positie = eerstepagina-positie van wtcwoerden.nl; noteer ook of het een jeugdsectie-pagina is (`index.php?page=jeugd_...`) of een oud bericht.

| # | Zoekopdracht | Intentie | Q4 2026 (29 okt, Brave) | Q1 2027 | Q2 2027 | Q3 2027 |
|---|---|---|---|---|---|---|
| 1 | sporten kind Woerden | breed, ouder zoekt een sport | niet in top 10 | | | |
| 2 | sport voor kinderen Harmelen | kern Harmelen | niet in top 10 | | | |
| 3 | kinderen sporten Kamerik | kern Kamerik | niet in top 10 | | | |
| 4 | sporten kind Waarder / Woerdense Verlaat / Kanis / Kockengen / Zegveld | overige kernen | niet in top 10 | | | |
| 5 | buitensport kind Woerden | breed, buitensport | niet in top 10 | | | |
| 6 | wielrennen jeugd Woerden | specifiek | eigen site pos. 1, 3, 4, 8, 9 — maar alleen home en nieuwsberichten, geen jeugdsectie | | | |
| 7 | wielrennen kind Woerden proeftraining | proeftraining | eigen site pos. 1, 3, 4, 8, 9 (nieuws/home) + "Jeugd huurfietsen" page=57 op 9; geen jeugdsectie | | | |
| 8 | veldrijden kind Woerden | veldrijden | niet in top 10 | | | |
| 9 | proeftraining wielrennen kinderen Woerden | proeftraining | niet in top 10 | | | |
| 10 | lid worden wielerclub jeugd Woerden | aanmelden | niet in top 10 | | | |
| 11 | wielrennen kind Utrecht / De Meern / Vleuten | regio Utrecht | niet in top 10 (WV Het Stadion dominant) | | | |
| 12 | wtcwoerden.nl / WTC Woerden wielrennen | clubnaam | home pos. 3 | | | |

## 2. Indexeringscheck (site:-queries)

| # | Zoekopdracht | Wat je checkt | Q4 2026 (29 okt, Brave) | Q1 2027 | Q2 2027 | Q3 2027 |
|---|---|---|---|---|---|---|
| 13 | site:wtcwoerden.nl jeugd | welke pagina's indexeert Google? | alleen oude pagina's en nieuws (page=54, 57, 293, 743, 785, 799, 803, 807, 860) + home; geen page=jeugd_* | | | |
| 14 | site:wtcwoerden.nl wielrennen | idem | | | | |
| 15 | site:wtcwoerden.nl proeftraining | idem | | | | |

**Afspraak:** bij elke meting ook tellen hoeveel resultaten `page=jeugd_...` zijn vs. oude `page=<nummer>`.

## 3. On-page checklist per ClubApp-pagina

Per kwartaal per pagina checken in de browser (Chrome: rechtsklik → "Bron bekijken" of DevTools → Elements). v = in orde, x = ontbreekt, n.v.t. = niet van toepassing.

Paginacodes en bijbehorende artikelen (uit de front matter in `websiteteksten/website_teksten md/`):

| Paginacode | Artikelen (id) | URL-vorm |
|---|---|---|
| home | Home | wtcwoerden.nl/ |
| jeugd_welkom | Welkom bij de jeugd (1010) | index.php?page=jeugd_welkom |
| jeugd_watdoenwe | Wat doen we (1011) | index.php?page=jeugd_watdoenwe |
| jeugd_proeftraining | Kom meetrainen (1012) | index.php?page=jeugd_proeftraining |
| jeugd_lidworden | Lid worden (1013) | index.php?page=jeugd_lidworden |
| jeugd_hoewerkthet | Trainingen (1014), Wedstrijden (1015), Afspraken (1016), Een fiets en pedalen uitzoeken (1023) | index.php?page=jeugd_hoewerkthet |
| jeugd_programma | Jeugdprogramma (1030) | index.php?page=jeugd_programma |
| jeugd_naslag | Adressen andere clubs (1017), KNWU Licenties (1018), KNWU leeftijdscategorieën (1019), Materiaal - Verzetten (1021), MNC Weg (1025), MNC Cross (1026), Nationale wedstrijden (1027) | index.php?page=jeugd_naslag |
| Jeugd | Contactformulier (125) | index.php?page=Jeugd |

Per pagina checken (kolommen: Q4 2026 t/m Q3 2027):

| Check | jeugd_welkom | jeugd_proeftraining | jeugd_watdoenwe | jeugd_lidworden | jeugd_hoewerkthet | jeugd_naslag |
|---|---|---|---|---|---|---|
| Title-tag bevat zoekwoord + plaats (bv. "wielrennen kinderen Woerden") | | | | | | |
| Meta description aanwezig en <= 164 tekens | | | | | | |
| Precies één H1, met kernwoord | | | | | | |
| Koppenstructuur logisch (H2/H3) | | | | | | |
| Alle afbeeldingen hebben alt-tekst | | | | | | |
| Interne links naar andere jeugdpagina's aanwezig | | | | | | |
| Plaatsnamen genoemd (Woerden + kernen: Harmelen, Kamerik, Woerdense Verlaat, Waarder, Kanis, Kockengen, De Meern/Vleuten) | | | | | | |
| Leeftijd consequent 7-14 jaar | | | | | | |
| Trainingstijden en seizoenen consistent met andere pagina's | | | | | | |
| Geen dubbele inhoud met een andere pagina | | | | | | |
| Laadtijd acceptabel (PageSpeed Insights, mobiel) | | | | | | |
| Mobiel goed leesbaar (responsive check) | | | | | | |

## 4. Technische checks (hele site)

| Check | Hoe | Q4 2026 | Q1 2027 | Q2 2027 | Q3 2027 |
|---|---|---|---|---|---|
| robots.txt bereikbaar | browser: wtcwoerden.nl/robots.txt | 403 (CloudFront) — bekend, agenderen bij nieuw CMS | | | |
| sitemap.xml bereikbaar | browser: wtcwoerden.nl/sitemap.xml | 403 — bekend | | | |
| Lighthouse SEO-score per jeugdpagina | DevTools → Lighthouse → SEO | | | | |
| PageSpeed Insights (mobiel) per jeugdpagina | pagespeed.web.dev | | | | |
| Dubbele URL's: oude artikel-id's (page=54, 293, 860, 57...) doorverwijzen? | .htaccess check in ClubApp (Website > Instellingen) | nee — openstaand punt | | | |
| Korte URL's actief (bv. /jeugd, /proeftraining, /lidworden) | .htaccess check + test in browser | | | | |
| JSON-LD gestructureerde data aanwezig | bron bekijken, zoek "application/ld+json" | nee | | | |
| Meta-titel/-beschrijving aangepast op de 5 prioriteitsagina's | supportticket AllUnited + check in bron | nee — aan te vragen | | | |
| Google Search Console gekoppeld | search.google.com/search-console | onbekend — check of account bestaat | | | |

## 5. Kanalen buiten de eigen site

| Kanaal | Check | Q4 2026 | Q1 2027 | Q2 2027 | Q3 2027 |
|---|---|---|---|---|---|
| Google Business Profile | bestaat in Maps? categorie, foto's, reviews | onbekend — handmatig checken | | | |
| Beweegwijzer Woerden | profiel actueel? correcte kenmerken, link naar proeftraining? | verouderd, kenmerken bevatten fouten | | | |
| DoeMeeInWoerden.nl | profiel ingevuld, data bij kennismakingsactiviteiten? | data "onbekend" | | | |
| KNWU-clubzoeker / Fietssport.nl | jeugdinformatie en contactgegevens actueel? | verouderd | | | |
| "Vereniging in de school" (Beweegteam) | staat WTC op de aanbiederslijst? | nee — aanmelden | | | |

## 6. Eigen statistieken

| Meting | Bron | Q4 2026 | Q1 2027 | Q2 2027 | Q3 2027 |
|---|---|---|---|---|---|
| Pageviews per jeugdpagina | Umami (draait al op de pagina's) | | | | |
| Zoekwoorden + posities + CTR | Google Search Console (als gekoppeld) | | | | |
| Aantal proeftraining-aanmeldingen + bron ("hoe gevonden?") | contactformulier/mail | | | | |

## 7. Log per kwartaal

| Kwartaal | Datum meting | Wie | Belangrijkste bevinding | Acties afgesproken |
|---|---|---|---|---|
| Q4 2026 | 29 okt 2026 | (baseline) | eigen site vindbaar op clubnaam en "wielrennen Woerden", maar alleen via home/nieuws; bij `site:...jeugd` vooral oude pagina's; brede zoekopdrachten en kernen: niet vindbaar | zie Plan-vindbaarheid-jeugdwerving.md |
| Q1 2027 | | | | |
| Q2 2027 | | | | |
| Q3 2027 | | | | |

---

*Onderhoud: houd deze lijst bij als de pagina's of kanalen wijzigen (zie `Plan-vindbaarheid-jeugd.md` en `Plan-vindbaarheid-jeugdwerving.md`).*
