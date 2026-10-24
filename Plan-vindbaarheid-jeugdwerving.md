# Conceptplan: vindbaarheid en jeugdwerving WTC Woerden

**Status:** concept, versie 0.1 — bedoeld om verder uit te werken.
**Doelgroep:** kinderen van 7 t/m 14 jaar (en hun ouders) in Woerden en omstreken: Waarder, Harmelen, Woerdense Verlaat, Kanis, Kamerik, Kockengen, Utrecht (De Meern / Vleuten).
**Kernvraag die ouders stellen:** "wielrennen of veldrijden voor mijn kind, bij mij in de buurt — waar kan dat?"
**Onderbouwing:** platform- en organisatieonderzoek staat in `context/onderzoek-sportpromotie-platforms.md` (onderzoeksdatum 24 oktober 2026, alle claims met bron-URL). De website-analyse in dit plan is uitgevoerd op de live site (wtcwoerden.nl).

---

## 1. Analyse huidige situatie

### 1.1 Sterke punten

- **Nieuwe jeugdsectie is inhoudelijk sterk:** kindgerichte, tijdloze teksten (repo: 13 pagina's) met helder pad "Ontdek → Kom meetrainen → Lid worden", en de sectie zit in het hoofdmenu met leesbare URL's (`index.php?page=jeugd_proeftraining`).
- **De vereniging is al aantoonbaar vindbaar bij "Woerden"-zoekopdrachten:**
  - Beweegwijzer Woerden staat nr. 1 op "wielrennen jeugd Woerden" en "wielrennen kinderen Woerden vereniging" (profiel bestaat).
  - De KNWU-clubgids staat nr. 2, met een "Direct aanmelden"-knop.
  - Fietssport.nl-clubgids en DoeMeeInWoerden.nl hebben profielen; de Woerdense Courant bericht structureel over de jeugdafdeling; er is een Facebookpagina (ca. 828 volgers) en een YouTube-kanaal.
- **De vereniging organiseert grote evenementen** (Nacht van Woerden, Ronde van Woerden) met jeugdonderdelen — een showcase die landelijk/regional aandacht trekt.
- **Er is al laagdrempelig aanbod om naar te verwijzen:** instroom op elk moment, proeftraining met leenfietsen en helmen.

### 1.2 Zwakke punten — website (gemeten op de live site)

| Bevinding | Evidence | Gevolg |
|---|---|---|
| Generieke pagina-titels, zonder zoekwoorden | "Welkom bij de jeugd · WTC Woerden", "Kom meetrainen · WTC Woerden", "Home · WTC Woerden" — geen "wielrennen", "kinderen", "veldrijden", "jeugd" in combinatie met plaats | Slechte ranking op de vragen die ouders écht stellen; Google herschrijft/rangschikt deze titels laag |
| Dunne/lege meta descriptions | Homepage: `content="WTC Woerden"`; jeugdpagina's: alleen de eerste intro-zin | Lage klikbereidte in zoekresultaten |
| Dubbele URL's voor dezelfde content, geen canonical | Dezelfde jeugd-pagina bereikbaar via `page=1010`, `page=Jeugd_welkom`, en oude artikel-id's (bv. `page=54`, `page=293`, `page=860`), met `sid`-varianten | Google versnipperd zijn vertrouwen over varianten; bij `site:wtcwoerden.nl jeugd` verschijnen vooral **oude** jeugdpagina's, niet de nieuwe sectie |
| robots.txt en sitemap.xml onbereikbaar | Beide geven 403 (CloudFront-blokkade), ook voor Googlebot-gebruikersagent | Geen sitemap; Google ontdekt nieuwe/verplaatste pagina's langzaam |
| Geen gestructureerde data | Geen JSON-LD (SportsClub/Organization) op de pagina's | Geen verrijkte zoekresultaten; Google Maps/wijkinfo mist verband vereniging-locatie |
| Geen zichtbaar Google Business Profile | Geen Maps-vermelding/reviews in zoekresultaten; niet machinaal te verifiëren (handmatige check nodig) | Vereniging mist het kaartblok bij "wielrennen Woerden" — vaak het eerste wat ouders zien |
| Geen regionaal bereik in de teksten | Teksten noemen alleen Woerden, niet de omliggende kernen | Vindbaarheid blijft beperkt tot letterlijk "Woerden"-zoekopdrachten |

### 1.3 Zwakke punten — zoekresultaten per kern

Getest met zoekopdrachten zoals een ouder die zou doen:

- **Woerden:** goed geregistreerd (Beweegwijzer, KNWU, Woerdense Courant), maar de eigen site komt op deze zoekwoorden zelf nauwelijks naar voren.
- **Harmelen, Kamerik, Woerdense Verlaat, Waarder, Kanis, Kockengen:** WTC Woerden verschijnt nergens; resultaten worden gedomineerd door hardlopevenementen en algemene gidsen.
- **Utrecht / De Meern / Vleuten:** concurrent WV Het Stadion domineert; het Wielerplatform Utrecht heeft een cluboverzicht waar WTC niet in staat.

Conclusie: de vereniging is ankerpunt in Woerden, maar onzichtbaar in de omliggende kernen — precies de gebieden waar de groeikans zit.

### 1.4 Zwakke punten — platformen (samenvatting; details en bronnen in het onderzoeksdossier)

- **DoeMeeInWoerden.nl**: profiel bestaat ("Deze pagina is nog niet helemaal ingevuld"), maar de twee kennismakingsactiviteiten wielrennen/veldrijden (7-12 jr) hebben "Datum nog onbekend". Dit is hét gratis, gemeentelijke kennismakingskanaal (incl. het Sjors-boekje 2026-2027).
- **Beweegwijzer Woerden**: profieltekst verouderd ("ruim 35 jeugdleden", algemene clubtekst) en de kenmerken bevatten fouten (bijv. "Alleen voor jongens en mannen" én "Alleen voor meisjes en vrouwen" tegelijk); geen link naar de proeftraining-pagina.
- **"Vereniging in de school"** (schoolclinics via Beweegteam Woerden): WTC staat niet op de aanbiederslijst 2025/2026, terwijl ca. 30 andere verenigingen er wél op staan en wielrennen als sport geheel ontbreekt.
- **KNWU/Fietssport-profielen**: aanwezig, maar verouderd (ledenaantallen).
- **Niet aanwezig op:** Uniek Sporten-Sportzoeker (niet gecontroleerd/verifieerbaar), sportvereniging-info.nl (gratis), Uitmetkinderen.nl (€ 49/jr), Kidsproof.nl; niet bij Montfoort Vitaal (Montfoort/Linschoten) en Sportpunt Stichtse Vecht.
- **Financiële drempels:** de gemeente Woerden is niet aangesloten bij het Jeugdfonds Sport & Cultuur; de lokale regeling is de Groene Hart Pas — WTC Woerden moet nog partner worden, anders kunnen gezinnen het tegoed niet bij de club besteden. Gemeente Woerden kent wel een Subsidieregeling Sport.

---

## 2. Conceptplan: vijf sporen

### Spoor 1 — De website vindbaar maken (fundament)

**Doel: gevonden worden op "wielrennen/veldrijden + kinderen + plaats".**

**Uitgangspunt (bevestigd door AllUnited, oktober 2026):** aangepaste meta-titel (max. 55 tekens) en meta-beschrijving (max. 164 tekens) zijn mogelijk voor **maximaal 5 pagina's**, via een supportticket; robots.txt, sitemap en canonical tags zijn niet te beheren; verkorte URL's en doorverwijzingen kunnen zelf via `Website > Instellingen > .htaccess`. In het nieuwe CMS (verwacht in 2026) komen meer SEO-mogelijkheden.

1. **Supportticket bij AllUnited: meta-titel en -beschrijving instellen voor de vijf belangrijkste pagina's.** Kies bewust op zoekintentie van ouders — kant-en-klaar voorstel:

   | Pagina | Meta-titel (max. 55 tekens) | Meta-beschrijving (max. 164 tekens) |
   |---|---|---|
   | Home | `Wielrennen & veldrijden in Woerden eo \| WTC` | `WTC Woerden is de wielervereniging van Woerden en omstreken: wielrennen, veldrijden, mountainbiken en toerfietsen, voor jeugd (vanaf 7 jaar) en volwassenen.` |
   | Welkom bij de jeugd | `Wielrennen voor kinderen 7-14 in Woerden eo` | `Jeugdwielrennen bij WTC Woerden: kinderen van 7 t/m 14 jaar trainen wielrennen en veldrijden, met plezier voorop. Kennismaken kan altijd.` |
   | Kom meetrainen | `Proeftraining wielrennen kinderen \| WTC Woerden` | `Nieuwsgierig naar wielrennen of veldrijden? Meld je kind aan voor een proeftraining in Woerden. Leenfiets en helm beschikbaar, instroom het hele jaar.` |
   | Lid worden | `Lid worden jeugd · wielrennen \| WTC Woerden` | `Zo wordt je kind lid van WTC Woerden: inschrijven via het webformulier, ClubApp installeren en meefietsen. Instroom mogelijk op elk moment.` |
   | Wat doen we | `Wat doen we: wielrennen & veldrijden \| WTC Woerden` | `Bij de jeugd van WTC Woerden leren kinderen wielrennen op de weg en in de winter veldrijden: techniek, samenwerken en vooral plezier.` |

   Toelichting op de keuze: de homepage vangt zoekopdrachten op de clubnaam en op "wielrennen Woerden" op; de drie wervingspagina's dekken de vragen van ouders ("wielrennen kinderen", "proeftraining", "lid worden"); "Wat doen we" dekt de uitleg-vragen. Titel in de website zelf (het CMS-menu) ongewijzigd laten — het gaat alleen om de meta-titel in de zoekresultaten.
2. **Regionale kernen zichtbaar in de teksten:** op de pagina's "Kom meetrainen" en "Welkom bij de jeugd" een zin als "We trainen in Woerden; kinderen uit Harmelen, Woerdense Verlaat, Waarder, Kanis, Kamerik, Kockengen, Montfoort en De Meern/Vleuten fietsen bij ons mee." Dat maakt de kernen zoekbaar en spreekt ouders uit die kernen aan.
3. **Dubbele URL's aanpakken via .htaccess:** canonical tags zijn niet mogelijk, maar via `Website > Instellingen > .htaccess` kunnen wel verkorte URL's en doorverwijzingen worden ingesteld. Streefbeeld: doorverwijzingen van de oude jeugd-artikel-URL's (page=54, page=293, page=860 e.d.) naar de huidige leesbare URL's (`Jeugd_welkom` e.d.), en interne links in nieuwsberichten consequent naar één URL-vorm laten verwijzen. Kan het .htaccess-menu geen doorverwijzing op query-parameters aan, dan via het supportticket laten bevestigen en anders minimaal de oude artikelen offline halen.
4. **Google Business Profile aanmaken/claimen** (gratis) met clubhuis Sur-Place, Waardsedijk 40: categorie "Wielervereniging"; jeugdcontactgegevens; foto's van trainingen; ouders vragen om een review na de proeftraining. Dit is nu het belangrijkste on-site-adjacent kanaal, juist omdat de SEO-mogelijkheden van het CMS beperkt zijn.
5. **Gestructureerde data (JSON-LD SportsClub):** navragen bij AllUnited of een script-blok in het detailveld van een artikel blijft staan (zoals het Umami-script blijkbaar wel). Zo ja, dan plaatsen op de jeugdpagina's.
6. **Niet mogelijk in het huidige CMS, wel bewaken:** robots.txt/sitemap vrijgeven en canonical tags. Deze agendapunten terug oppakken zodra het nieuwe CMS (verwacht in 2026) live is; Google Search Console kan dan ook geregistreerd worden (verificatie via een DNS-record, mits de vereniging het domein beheert).

### Spoor 2 — Lokale platformen compleet benutten (quick wins, vooral gratis)

1. **DoeMeeInWoerden.nl-profiel afmaken** en echte data bij de kennismakingsactiviteiten wielrennen en veldrijden zetten — dit is het directe wervingskanaal van de gemeente, gratis, incl. vermelding in het Sjors-boekje.
2. **Aanmelden voor "Vereniging in de school"** bij Beweegteam Woerden (info@beweegteamwoerden.nl / 06 58772402) zodat scholen een wielrenclinic kunnen aanvragen; grote kans: wielrennen staat als sport nog helemaal niet op de lijst.
3. **Beweegwijzer-profiel actualiseren en corrigeren** (via Beweegteam): actuele tekst, correcte kenmerken, link naar de proeftraining-pagina.
4. **KNWU- en Fietssport-profielen actualiseren** (ledenaantallen, jeugdaanbod, proeftraining-vermelding).
5. **Gratis aanvullende vermeldingen:** Uniek Sporten-Sportzoeker (via sportconsulent), sportvereniging-info.nl; eventueel Uitmetkinderen.nl (€ 49/jr) en Kidsproof evalueren.
6. **Perscontact onderhouden:** redactie Woerdense Courant (redactie.woerdensecourant@kmp.nl) blijft berichten over jeugdprestaties — dat werkt al; structureel persbericht bij start veldseizoen + proeftraining-aanbod.

### Spoor 3 — Regionale dekking in de omliggende kernen

1. **Gemeente Woerden-kernen (Harmelen, Kamerik, Woerdense Verlaat, Waarder, Kanis, Zegveld):** deze vallen onder Beweegwijzer en DoeMeeInWoerden — spoor 2 dekt ze al. Aanvullen met vermeldingen/posts in lokale Facebook-groepen ("Woerden 0348", "Ontmoetingsgroep Woerden en omgeving", dorpelgroepen Harmelen/Kamerik — voorwaarden navragen).
2. **Kockengen / Montfoort / Oudewater:** deze kernen vallen buiten de gemeente Woerden. Montfoort Vitaal (Montfoort/Linschoten) en Sportpunt Stichtse Vecht (Kockengen) hebben eigen platformen zonder wielrennen — contact zoeken om opgenomen te worden.
3. **Utrecht (De Meern / Vleuten):** hier is WV Het Stadion dominant. Realistische inschatting: geen grote winst verwachten; hooguit blijven de MNC-wedstrijden en samenwerkingsvormen (WTC en Het Stadion hebben al een gezamenlijk jeugdteam) die zichtbaarheid geven.
4. **Groene Hart Pas-partnerschap regelen** (gratie: anders kunnen gezinnen uit Montfoort, Oudewater, De Ronde Venen e.d. hun tegoed níet bij WTC besteden) en verwijzing naar Stichting Leergeld Groene Hart op de pagina "Lid worden" — haalt de financiële drempel weg die in kleine kernen zwaarder weegt.

### Spoor 4 — Evenementen als wervingsmotor

1. **Ready2Race (KNWU/Stichting Ready2Race):** een Dikke Banden Race (kinderen 2-12) of Schoolclinic in Woerden organiseren of meedoen (info@ready2race.nl); landelijk bewezen wervingsformat (in 2023 ca. 6.000 kinderen op de fiets, deelnemers werden nadien lid). Voor de oudste jeugd is er Ready2Race Junior (11-15).
2. **Nacht van Woerden en Ronde van Woerden** benutten als open dag: jeugddemo's, leenfietsen, flyer met QR-code naar de proeftraining-pagina, leden als gastheren voor kinderen uit de kernen.
3. **Jaarlijks terugkerend "open trainingsmoment"** in het veldseizoen (lage drempel, samen met DoeMeeInWoerden als geregistreerde activiteit).

### Spoor 5 — Onderhoud en financiering

1. **Beweegteam Woerden als vaste contactpersoon** inrichten (zij doen sportstimulering, Beweegwijzer, schoolkoppelingen, verenigingsondersteuning op maat).
2. **Subsidieregeling Sport gemeente Woerden** toetsen voor wervingsactiviteiten (budget + activiteitenplan nodig; aanvraag via woerden.nl).
3. **Rabo Clubsupport-workshops** (via KNWU-clubsupport, gratis): bijv. ledenwerving/werving bij Gen-Z-ouders.
4. **Eén coordinator werving/bereik** aanwijzen binnen de jeugdcommissie die dit plan bewaakt en de platformprofielen jaarlijks actualiseert (seizoensstart).

---

## 3. Prioritering

| Actie | Spoor | Moeite | Verwacht effect | Timing |
|---|---|---|---|---|
| DoeMeeInWoerden-profiel + data invullen | 2 | Laag (uurtje werk) | Hoog — direct wervingskanaal gemeente | Deze maand |
| Aanmelden "Vereniging in de school" | 2 | Laag (mail + eventueel clinic-preparaat) | Hoog — 30+ scholen bereikbaar | Deze maand |
| Beweegwijzer-profiel corrigeren | 2 | Laag | Middel — staat nu nr. 1 op de beste zoekwoorden | Deze maand |
| Google Business Profile checken/aanmaken | 1 | Laag | Hoog — kaartblok bij lokale zoekopdrachten | Deze maand |
| Meta-titel + beschrijving (5 pagina's) doorgeven aan AllUnited | 1 | Laag (supportticket, voorstel staat in spoor 1) | Hoog — op termijn | Korte termijn (1-3 mnd) |
| Regio-kernen noemen op de website | 1 | Laag | Middel | Korte termijn |
| Oude jeugd-URL's doorverwijzen via .htaccess | 1 | Middel (instellen + navragen bij AllUnited) | Middel | Korte termijn |
| KNWU/Fietssport-profielen actualiseren | 2 | Laag | Middel | Korte termijn |
| Groene Hart Pas-partnerschap | 3 | Middel | Middel — opent kernen buiten Woerden | Korte termijn |
| JSON-LD-scriptblok: mogelijkheid navragen bij AllUnited | 1 | Laag | Laag/middel | Middellang (3-12 mnd) |
| SEO-mogelijkheden her-evalueren zodra het nieuwe CMS live is (robots, sitemap, canonical, Search Console) | 1 | Laag (evaluatie) | Middel — fundament | Middellang |
| Ready2Race-event organiseren | 4 | Hoog | Hoog — bewezen format | Middellang |
| Montfoort Vitaal / Sportpunt Stichtse Vecht | 3 | Laag | Middel | Middellang |
| Facebook-groepen per kern benutten | 3 | Laag, terugkerend | Middel | Doorlopend |
| Subsidietoets + Rabo Clubsupport-workshop | 5 | Middel | Afhankelijk van resultaat | Middellang |

## 4. Meten (voorstel)

- **Primair:** aantal aanmeldingen voor de proeftraining per maand (bron: contactformulier/mail).
- **Aanvullend:** nieuwe jeugdleden per seizoen; herkomstvraag bij aanmelding ("Hoe heb je ons gevonden?").
- **SEO:** Google Search Console (queries, posities, klikken); aanwezigheid in de map-kaart.
- **Platforms:** aanmeldingen via DoeMeeInWoerden; weergaven/reacties op Beweegwijzer (indien meetbaar); clinic-aanvragen via "Vereniging in de school".

## 5. Openstaande vragen (uit te werken)

1. ~~CMS-mogelijkheden~~ — beantwoord door AllUnited (oktober 2026): meta-titel + beschrijving voor max. 5 pagina's via supportticket; geen robots.txt, sitemap of canonical tags; .htaccess zelf te beheren; meer mogelijkheden in het nieuwe CMS (verwacht 2026). Open restpunt: ondersteunt het .htaccess-menu ook doorverwijzingen op query-parameters (page=54 → Jeugd_welkom), en blijft een JSON-LD-scriptblok in het detailveld staan?
2. Is er al een Google Business Profile (handmatig check in Maps; er is al een YouTube-kanaal, dus er is mogelijk een Google-accountstructuur)?
3. Wie wordt coordinator werving/bereik en wat is het budget (bv. € 49/jr Uitmetkinderen, flyer-productie, Ready2Race)?
4. Contributiebedragen en proefperiode: nu als placeholder in de repo — bevestigen, want ouders zoeken hiernaar en dit hoort bij de drempelwegruiming (spoor 5).
5. Is de vermelding bij de Woerdense Courant-agenda en het Sjors-boekje 2027-geïnitieerd door de vereniging, of automatisch door Beweegteam?
