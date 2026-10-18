"""Synchroniseer websiteteksten tussen Markdown (bron, bewerken in Typora) en ClubApp-HTML.

Markdown in `websiteteksten/website_teksten md/` is de bron. De ClubApp-HTML in
`websiteteksten/website_teksten html/` wordt daaruit gegenereerd.

Commando's:
    build  [bestanden...]  Markdown -> HTML (standaard: alle .md-bestanden)
    import [bestanden...]  HTML -> Markdown, na wijzigingen die direct in ClubApp zijn gedaan
    check  [bestanden...]  Controleer of HTML en Markdown in sync zijn
    watch                  Bouw HTML automatisch opnieuw zodra een .md-bestand wordt opgeslagen

Markdown-conventies:
    - YAML front matter bevat de metadata (pagina, doelgroep, ..., versie).
    - De eerste `---` scheidingslijn scheidt introductie en details.
    - `##` wordt een sectiekop (header4), `###` een tussenkop (header5).
    - Twee of meer afbeeldingen in één alinea worden naast elkaar gezet.
    - Het Umami-script en de witte voettekst worden automatisch toegevoegd
      (zet `umami: false` in de front matter om het script weg te laten).

Vereist: pandoc en de Python-pakketten beautifulsoup4 en PyYAML.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

import yaml
from bs4 import BeautifulSoup, Comment, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent
HTML_DIR = ROOT / "websiteteksten" / "website_teksten html"
MD_DIR = ROOT / "websiteteksten" / "website_teksten md"

SEPARATOR = "<!-- --- -->"
TABLE_STYLE = "border-collapse: collapse; width: 100%;"
CELL_STYLE = "padding: 8px; border: 1px solid #ddd;"
PHOTO_CELL_STYLE = "padding: 0; text-align: center; vertical-align: top; width: {w}%;"
FOOTER_STYLE = "color: #ffffff;"

UMAMI_SCRIPT = """<script>// <![CDATA[
\t(function () {
\t\tvar s = document.createElement('script');
\t\ts.src = 'https://cloud.umami.is/script.js'; // zie opmerking hieronder
\t\ts.defer = true;
\t\ts.setAttribute('data-website-id', 'b348627f-6db1-4ad8-9c47-3599b6bdd248');
\t\ts.setAttribute('data-auto-track', 'false');
\t\ts.onload = function () {
\t\t\tvar params = new URLSearchParams(location.search);
\t\t\tvar page = params.get('page') || 'home';
\t\t\tumami.track(function (props) {
\t\t\t\treturn Object.assign({}, props, {
\t\t\t\t\turl: '/' + page,
\t\t\t\t\ttitle: document.title
\t\t\t\t});
\t\t\t});
\t\t};
\t\tdocument.head.appendChild(s);
\t})();
\t// ]]></script>"""

VOID_TAGS = {"img", "br", "hr", "col", "input", "meta", "link", "source", "wbr"}
BLOCK_TAGS = {
    "p", "ul", "ol", "li", "table", "thead", "tbody", "tfoot", "tr", "td", "th",
    "div", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "pre", "hr",
    "figure", "section", "form", "iframe", "script", "style", "colgroup", "dl",
}
HEADINGS = ("h1", "h2", "h3", "h4", "h5", "h6")


# --------------------------------------------------------------------------- #
# Gemeenschappelijke HTML-serialisatie
# --------------------------------------------------------------------------- #

def esc_text(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\xa0", "&nbsp;")
    )


def esc_attr(value: str) -> str:
    return value.replace("&", "&amp;").replace('"', "&quot;")


def attrs_html(tag: Tag) -> str:
    parts = []
    for key, value in tag.attrs.items():
        if isinstance(value, list):
            value = " ".join(value)
        parts.append(f'{key}="{esc_attr(str(value))}"')
    return (" " + " ".join(parts)) if parts else ""


def open_tag(tag: Tag) -> str:
    return f"<{tag.name}{attrs_html(tag)}>"


def inline_html(node) -> str:
    """Serialiseer inline-inhoud naar compacte HTML."""
    if isinstance(node, Comment):
        return f"<!--{node}-->"
    if isinstance(node, NavigableString):
        return esc_text(re.sub(r"[ \t\r\n\f]+", " ", str(node)))
    if node.name in VOID_TAGS:
        return f"<{node.name}{attrs_html(node)} />"
    inner = "".join(inline_html(c) for c in node.children)
    return f"{open_tag(node)}{inner}</{node.name}>"


def children_html(tag: Tag) -> str:
    html = "".join(inline_html(c) for c in tag.children).strip()
    return re.sub(r"\s*<br />\s*", "<br />", html)


# --------------------------------------------------------------------------- #
# Hulpfuncties voor de HTML-structuur
# --------------------------------------------------------------------------- #

def meaningful_children(tag: Tag) -> list:
    return [
        c for c in tag.children
        if not isinstance(c, Comment)
        and not (isinstance(c, NavigableString) and not c.strip())
    ]


def only_images(tag: Tag) -> list[Tag] | None:
    """Geef de afbeeldingen terug als het element (eventueel via spans) alleen afbeeldingen bevat."""
    imgs: list[Tag] = []
    for child in meaningful_children(tag):
        if isinstance(child, NavigableString):
            return None
        if child.name == "img":
            imgs.append(child)
        elif child.name == "span":
            sub = only_images(child)
            if sub is None:
                return None
            imgs.extend(sub)
        else:
            return None
    return imgs or None


def header_level(p: Tag) -> str | None:
    kids = meaningful_children(p)
    if len(kids) != 1 or not isinstance(kids[0], Tag) or kids[0].name != "span":
        return None
    classes = kids[0].get("class") or []
    if "header5" in classes:
        return "###"
    if "header4" in classes or "header3" in classes:
        return "##"
    return None


def is_footer(node: Tag) -> bool:
    span = node.find("span", style=re.compile(r"#ffffff", re.I))
    return bool(span) and span.get_text().strip().startswith("pagina:")


# --------------------------------------------------------------------------- #
# HTML -> Markdown (import)
# --------------------------------------------------------------------------- #

def md_escape(text: str) -> str:
    text = text.replace("\\", "\\\\")
    text = re.sub(r"([`*\[\]<~])", r"\\\1", text)
    text = re.sub(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", r"\\_", text)
    text = re.sub(r"&(?=#?\w+;)", "&amp;", text)
    return text.replace("\xa0", "&nbsp;")


def escape_line_starts(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        line = re.sub(r"^(\s*)([#>+=-])(?=\s|$)", r"\1\\\2", line)
        line = re.sub(r"^(\s*\d+)([.)])(?=\s|$)", r"\1\\\2", line)
        lines.append(line)
    return "\n".join(lines)


def wrap_emphasis(inner: str, marker: str) -> str:
    if not re.sub(r"(&nbsp;|\s)", "", inner):
        return inner
    stripped = inner.strip()
    lead = inner[: len(inner) - len(inner.lstrip())]
    trail = inner[len(inner.rstrip()):]
    return f"{lead}{marker}{stripped}{marker}{trail}"


def md_url(url: str) -> str:
    url = url.replace(" ", "%20")
    if re.search(r"[()<>]", url):
        return "<" + url.replace("<", "%3C").replace(">", "%3E") + ">"
    return url


def md_inline(node, in_table: bool = False) -> str:
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        text = md_escape(re.sub(r"[ \t\r\n\f]+", " ", str(node)))
        return text.replace("|", "\\|") if in_table else text
    name = node.name
    inner = "".join(md_inline(c, in_table) for c in node.children)
    if name in ("strong", "b"):
        return wrap_emphasis(inner, "**")
    if name in ("em", "i"):
        return wrap_emphasis(inner, "*")
    if name == "br":
        return "<br />" if in_table else "\\\n"
    if name == "img":
        return inline_html(node)
    if name == "a" and set(node.attrs) <= {"href", "title"} and node.get("href"):
        title = node.get("title")
        title_md = f' "{title}"' if title else ""
        lead = " " if inner[:1].isspace() else ""
        trail = " " if inner[-1:].isspace() else ""
        return f"{lead}[{inner.strip()}]({md_url(node['href'])}{title_md}){trail}"
    if name == "span" and not node.attrs:
        return inner
    return f"{open_tag(node)}{inner}</{name}>"


def md_children(node: Tag, in_table: bool = False) -> str:
    return "".join(md_inline(c, in_table) for c in node.children)


def finish_inline(text: str) -> str:
    """Ruim een inline-Markdown-blok op; regeleinden aan de randen worden <br />."""
    text = re.sub(r" *\\\n *", "\\\n", text)
    text = re.sub(r" {2,}", " ", text).strip(" ")
    trailing = ""
    while text.endswith("\\\n"):
        text = text[:-2].rstrip(" ")
        trailing += "<br />"
    leading = ""
    while text.startswith("\\\n"):
        text = text[2:].lstrip(" ")
        leading += "<br />"
    return escape_line_starts(leading + text.strip() + trailing)


def md_list(tag: Tag, indent: str = "") -> str:
    lines = []
    number = int(tag.get("start", 1))
    for li in tag.find_all("li", recursive=False):
        marker = f"{number}. " if tag.name == "ol" else "- "
        number += 1
        sub_indent = indent + " " * len(marker)
        text_parts, sublists = [], []
        for child in li.children:
            if isinstance(child, Tag) and child.name in ("ul", "ol"):
                sublists.append(md_list(child, sub_indent))
            elif isinstance(child, Tag) and child.name == "p":
                text_parts.append(md_children(child) + "\\\n")
            else:
                text_parts.append(md_inline(child))
        text = finish_inline("".join(text_parts)).replace("\n", "\n" + sub_indent)
        lines.append(f"{indent}{marker}{text}")
        lines.extend(sublists)
    return "\n".join(lines)


def table_rows(table: Tag) -> list[Tag]:
    return [tr for tr in table.find_all("tr") if tr.find_parent("table") is table]


def md_table(table: Tag) -> str:
    rows = table_rows(table)
    cells_per_row = [row.find_all(["td", "th"], recursive=False) for row in rows]

    if rows and all(only_images(c) for cells in cells_per_row for c in cells):
        lines = []
        for cells in cells_per_row:
            imgs = [img for c in cells for img in only_images(c)]
            lines.append(" ".join(inline_html(i) for i in imgs))
        return "\n\n".join(lines)

    simple = all(
        not c.get("colspan") and not c.get("rowspan")
        and not c.find(["p", "ul", "ol", "table", "div"])
        for cells in cells_per_row for c in cells
    )
    if not rows or not simple or len({len(c) for c in cells_per_row}) != 1:
        return raw_block_html(table)

    def row_md(cells):
        return "| " + " | ".join(finish_inline(md_children(c, in_table=True)) for c in cells) + " |"

    out = [row_md(cells_per_row[0]), "| " + " | ".join("---" for _ in cells_per_row[0]) + " |"]
    out += [row_md(cells) for cells in cells_per_row[1:]]
    return "\n".join(out)


def raw_block_html(tag: Tag) -> str:
    """Ruwe HTML zonder lege regels, zodat Markdown het als één HTML-blok ziet."""
    html = format_block(tag, 0)
    return "\n".join(line for line in html.split("\n") if line.strip())


def md_blocks(nodes) -> list[str]:
    blocks = []
    for node in nodes:
        if isinstance(node, Comment):
            continue
        if isinstance(node, NavigableString):
            if node.strip():
                blocks.append(finish_inline(md_inline(node)))
            continue
        name = node.name
        if name == "script" or (name == "p" and is_footer(node)):
            continue
        if name == "p":
            level = header_level(node)
            imgs = only_images(node)
            if imgs:
                blocks.append(" ".join(inline_html(i) for i in imgs))
            elif level:
                span = meaningful_children(node)[0]
                blocks.append(f"{level} {finish_inline(md_children(span))}")
            else:
                text = finish_inline(md_children(node))
                blocks.append(text or "&nbsp;")
        elif name in HEADINGS:
            level = "##" if name in ("h1", "h2") else "###"
            blocks.append(f"{level} {finish_inline(md_children(node))}")
        elif name in ("ul", "ol"):
            prev = node.find_previous_sibling(lambda t: isinstance(t, Tag))
            if prev is not None and prev.name in ("ul", "ol"):
                # Zonder scheiding voegt Markdown opeenvolgende lijsten samen.
                blocks.append("<!-- -->")
            blocks.append(md_list(node))
        elif name == "table":
            blocks.append(md_table(node))
        elif name == "hr":
            continue
        elif name == "img":
            blocks.append(inline_html(node))
        elif name in BLOCK_TAGS:
            blocks.append(raw_block_html(node))
        else:
            blocks.append(finish_inline(md_inline(node)))
    return [b for b in blocks if b.strip()]


def parse_metadata(html: str) -> dict:
    match = re.search(r"<!--\s*metadata:(.*?)-->", html, re.S)
    meta: dict = {}
    if not match:
        return meta
    for line in match.group(1).splitlines():
        m = re.match(r"\s*-\s*([^:]+):\s*(.*)$", line)
        if m:
            value = m.group(2).strip()
            meta[m.group(1).strip()] = int(value) if value.isdigit() else value
    return meta


def read_front_matter(md: str) -> tuple[dict, str]:
    match = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(\r?\n|$)", md, re.S)
    if not match:
        return {}, md
    return (yaml.safe_load(match.group(1)) or {}), md[match.end():]


def html_to_md(html: str, fallback_meta: dict | None = None, stem: str = "") -> str:
    meta = parse_metadata(html) or {k: v for k, v in (fallback_meta or {}).items() if k != "umami"}
    if not meta.get("pagina"):
        # Zonder metadata-blok: haal pagina/versie uit de voettekst en het artikel-id uit de bestandsnaam.
        footer = re.search(r"pagina:\s*([^;<]*);\s*versie\s*([^<]*)<", html)
        if footer:
            meta.setdefault("pagina", footer.group(1).strip())
        article = re.search(r" - (\d+)$", stem)
        if article:
            meta.setdefault("clubapp artikel-id", int(article.group(1)))
        if footer:
            meta.setdefault("versie", footer.group(2).strip())
    if "<script" not in html.lower():
        meta["umami"] = False

    body = re.sub(r"<!--\s*metadata:.*?-->", "", html, count=1, flags=re.S)
    if SEPARATOR in body:
        intro_html, details_html = body.split(SEPARATOR, 1)
    else:
        intro_html, details_html = "", body

    intro = md_blocks(BeautifulSoup(intro_html, "html.parser").contents)
    details = md_blocks(BeautifulSoup(details_html, "html.parser").contents)

    front = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=1000).strip()
    parts = [f"---\n{front}\n---", *intro, "---", *details]
    return "\n\n".join(parts) + "\n"


# --------------------------------------------------------------------------- #
# Markdown -> HTML (build)
# --------------------------------------------------------------------------- #

def pandoc(md: str) -> str:
    try:
        result = subprocess.run(
            ["pandoc", "-f", "gfm-autolink_bare_uris-emoji", "-t", "html", "--wrap=none"],
            input=md.encode("utf-8"),
            capture_output=True,
            check=True,
        )
    except FileNotFoundError:
        sys.exit("pandoc niet gevonden; installeer pandoc (https://pandoc.org/installing.html)")
    return result.stdout.decode("utf-8")


def new_tag(soup: BeautifulSoup, name: str, **attrs) -> Tag:
    tag = soup.new_tag(name)
    for key, value in attrs.items():
        tag[key] = value
    return tag


def photo_table(soup: BeautifulSoup, imgs: list[Tag]) -> Tag:
    table = new_tag(soup, "table", style=TABLE_STYLE)
    tbody = new_tag(soup, "tbody")
    tr = new_tag(soup, "tr")
    width = round(100 / len(imgs))
    for img in imgs:
        td = new_tag(soup, "td", style=PHOTO_CELL_STYLE.format(w=width))
        td.append(img.extract())
        tr.append(td)
    tbody.append(tr)
    table.append(tbody)
    return table


def style_table(table: Tag) -> None:
    for colgroup in table.find_all("colgroup"):
        colgroup.decompose()
    if not table.get("style"):
        table["style"] = TABLE_STYLE
    for cell in table.find_all(["td", "th"]):
        if cell.get("style") and "padding" in cell["style"]:
            continue
        align = re.search(r"text-align:\s*\w+", cell.get("style", ""))
        cell["style"] = CELL_STYLE + (f" {align.group(0)};" if align else "")
        cell.attrs.pop("align", None)


def transform(soup: BeautifulSoup) -> tuple[list[Tag], list[Tag], list[str]]:
    """Zet pandoc-HTML om naar ClubApp-blokken; geeft (intro, details, waarschuwingen)."""
    intro: list[Tag] = []
    details: list[Tag] = []
    nodes = list(soup.contents)
    has_separator = any(isinstance(n, Tag) and n.name == "hr" for n in nodes)
    target = intro if has_separator else details
    seen_separator = False
    pending_inline: list = []

    def flush_inline():
        if any(not isinstance(n, NavigableString) or n.strip() for n in pending_inline):
            p = soup.new_tag("p")
            for n in pending_inline:
                p.append(n.extract())
            target.append(p)
        pending_inline.clear()

    for node in nodes:
        if isinstance(node, Comment):
            continue
        if isinstance(node, NavigableString):
            pending_inline.append(node)
            continue
        if node.name not in BLOCK_TAGS:
            pending_inline.append(node)
            continue
        flush_inline()

        if node.name == "hr":
            if not seen_separator:
                seen_separator = True
                target = details
            continue
        if node.name in HEADINGS:
            cls = "header4" if node.name in ("h1", "h2") else "header5"
            p = soup.new_tag("p")
            span = new_tag(soup, "span", **{"class": cls})
            for child in list(node.children):
                span.append(child.extract())
            p.append(span)
            target.append(p)
            continue
        if node.name == "p":
            imgs = only_images(node)
            if imgs and len(imgs) > 1:
                target.append(photo_table(soup, imgs))
                continue
        if node.name == "table":
            style_table(node)
        if node.name in ("ul", "ol"):
            for lst in [node, *node.find_all(["ul", "ol"])]:
                lst.attrs.pop("type", None)
            for li in node.find_all("li"):
                ps = li.find_all("p", recursive=False)
                if len(ps) == 1:
                    ps[0].unwrap()
        target.append(node)
    flush_inline()

    warnings = set()
    for block in intro + details:
        for img in [block] if block.name == "img" else block.find_all("img"):
            src = img.get("src", "")
            if src and not src.startswith(("http://", "https://")):
                warnings.add(f"afbeelding met lokaal pad (eerst uploaden naar ClubApp): {src}")
    return intro, details, sorted(warnings)


def format_block(tag: Tag, depth: int) -> str:
    ind = "\t" * depth
    name = tag.name
    if name in ("ul", "ol"):
        lines = [ind + open_tag(tag)]
        for li in tag.find_all("li", recursive=False):
            subs = [c for c in li.children if isinstance(c, Tag) and c.name in ("ul", "ol")]
            text = "".join(inline_html(c) for c in li.children if c not in subs).strip()
            if subs:
                lines.append(f"{ind}\t{open_tag(li)}{text}")
                lines += [format_block(s, depth + 2) for s in subs]
                lines.append(f"{ind}\t</li>")
            else:
                lines.append(f"{ind}\t{open_tag(li)}{text}</li>")
        lines.append(f"{ind}</{name}>")
        return "\n".join(lines)
    if name in ("table", "thead", "tbody", "tfoot", "tr"):
        lines = [ind + open_tag(tag)]
        lines += [format_block(c, depth + 1) for c in tag.children if isinstance(c, Tag)]
        lines.append(f"{ind}</{name}>")
        return "\n".join(lines)
    if name in ("td", "th"):
        return f"{ind}{open_tag(tag)}{children_html(tag)}</{name}>"
    if name in ("script", "style", "pre"):
        return ind + str(tag)
    if name in VOID_TAGS:
        return f"{ind}<{name}{attrs_html(tag)} />"
    if any(isinstance(c, Tag) and c.name in BLOCK_TAGS for c in tag.children):
        lines = [ind + open_tag(tag)]
        for child in tag.children:
            if isinstance(child, Tag) and child.name in BLOCK_TAGS:
                lines.append(format_block(child, depth + 1))
            elif inline_html(child).strip():
                lines.append(ind + "\t" + inline_html(child).strip())
        lines.append(f"{ind}</{name}>")
        return "\n".join(lines)
    content = children_html(tag)
    core = re.sub(r"(<br />)+$", "", content)
    if name == "p" and "<br />" in core and core.replace("<br />", "").strip():
        parts = [part for part in re.split(r"(?<=<br />)", content) if part]
        return f"{ind}<p>\n" + "\n".join(f"{ind}\t{part}" for part in parts) + f"\n{ind}</p>"
    return f"{ind}{open_tag(tag)}{content}</{name}>"


def format_blocks(blocks: list[Tag]) -> str:
    out = []
    for i, block in enumerate(blocks):
        if i > 0 and block.name == "p" and header_level(block):
            out.append("")
        out.append(format_block(block, 0))
    return "\n".join(out)


def md_to_html(md: str) -> tuple[str, list[str]]:
    meta, body = read_front_matter(md)
    soup = BeautifulSoup(pandoc(body), "html.parser")
    intro, details, warnings = transform(soup)

    if not meta.get("pagina"):
        warnings.append("front matter mist 'pagina'")
    meta_lines = "\n".join(f"- {k}: {v}" for k, v in meta.items() if k != "umami")
    pagina = esc_text(str(meta.get("pagina", "")))
    versie = esc_text(str(meta.get("versie", "")))

    parts = [f"<!--\nmetadata:\n{meta_lines}\n-->", ""]
    if intro:
        parts.append(format_blocks(intro))
    if meta.get("umami", True) is not False:
        parts.append(UMAMI_SCRIPT)
    parts += ["", SEPARATOR, ""]
    if details:
        parts += [format_blocks(details), ""]
    parts.append(f'<p><span style="{FOOTER_STYLE}">pagina: {pagina}; versie {versie}</span></p>')
    return "\n".join(parts) + "\n", warnings


# --------------------------------------------------------------------------- #
# Bestanden en commando's
# --------------------------------------------------------------------------- #

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and read(path) == content:
        return False
    path.write_text(content, encoding="utf-8", newline="\n")
    return True


def counterpart(path: Path) -> Path:
    if path.suffix.lower() == ".md":
        return HTML_DIR / (path.stem + ".html")
    return MD_DIR / (path.stem + ".md")


def resolve(files: list[str], directory: Path, suffix: str) -> list[Path]:
    if not files:
        return sorted(directory.glob(f"*{suffix}"))
    paths = []
    for f in files:
        p = Path(f)
        if not p.exists():
            p = directory / p.name
        if p.suffix.lower() != suffix:
            p = counterpart(p)
        if not p.exists():
            sys.exit(f"bestand niet gevonden: {p}")
        paths.append(p.resolve())
    return paths


def build_file(md_path: Path) -> bool:
    html, warnings = md_to_html(read(md_path))
    html_path = counterpart(md_path)
    changed = write_if_changed(html_path, html)
    print(f"[build] {md_path.name} -> {html_path.name} ({'bijgewerkt' if changed else 'ongewijzigd'})")
    for w in warnings:
        print(f"  ! {w}")
    return changed


def safe_build(md_path: Path) -> None:
    try:
        build_file(md_path)
    except Exception as exc:  # de watcher moet blijven draaien bij een fout in één bestand
        print(f"[build] {md_path.name}: FOUT {exc}")


def git_dirty(path: Path) -> bool:
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return False
    return bool(out.strip())


def cmd_build(args) -> int:
    for md_path in resolve(args.files, MD_DIR, ".md"):
        build_file(md_path)
    return 0


def cmd_import(args) -> int:
    skipped = 0
    for html_path in resolve(args.files, HTML_DIR, ".html"):
        md_path = counterpart(html_path)
        old_meta = read_front_matter(read(md_path))[0] if md_path.exists() else {}
        md = html_to_md(read(html_path), old_meta, html_path.stem)
        if md_path.exists() and read(md_path) == md:
            print(f"[import] {html_path.name} -> {md_path.name} (ongewijzigd)")
            continue
        if md_path.exists() and git_dirty(md_path) and not args.force:
            print(
                f"[import] {md_path.name} heeft niet-gecommitte wijzigingen; "
                "overgeslagen (gebruik --force om te overschrijven)"
            )
            skipped += 1
            continue
        MD_DIR.mkdir(parents=True, exist_ok=True)
        write_if_changed(md_path, md)
        print(f"[import] {html_path.name} -> {md_path.name} (bijgewerkt)")
    return 1 if skipped else 0


def cmd_check(args) -> int:
    problems = 0
    for md_path in resolve(args.files, MD_DIR, ".md"):
        html_path = counterpart(md_path)
        if not html_path.exists():
            print(f"[check] {md_path.name}: HTML ontbreekt (draai build)")
            problems += 1
        elif read(html_path) != md_to_html(read(md_path))[0]:
            print(f"[check] {md_path.name}: HTML wijkt af van Markdown (build of import nodig)")
            problems += 1
    if not args.files:
        for html_path in sorted(HTML_DIR.glob("*.html")):
            if not counterpart(html_path).exists():
                print(f"[check] {html_path.name}: Markdown ontbreekt (draai import)")
                problems += 1
    print("[check] alles in sync" if not problems else f"[check] {problems} bestand(en) niet in sync")
    return 1 if problems else 0


def cmd_watch(args) -> int:
    print(f"[watch] bewaakt {MD_DIR} (Ctrl+C om te stoppen)", flush=True)
    mtimes: dict[Path, float] = {}
    for md_path in sorted(MD_DIR.glob("*.md")):
        html_path = counterpart(md_path)
        mtimes[md_path] = md_path.stat().st_mtime
        if not html_path.exists() or mtimes[md_path] > html_path.stat().st_mtime:
            safe_build(md_path)
    try:
        while True:
            time.sleep(args.interval)
            for md_path in sorted(MD_DIR.glob("*.md")):
                try:
                    mtime = md_path.stat().st_mtime
                except FileNotFoundError:
                    continue
                if mtimes.get(md_path) != mtime:
                    mtimes[md_path] = mtime
                    safe_build(md_path)
                    sys.stdout.flush()
    except KeyboardInterrupt:
        print("[watch] gestopt")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="Markdown -> HTML")
    p_build.add_argument("files", nargs="*")
    p_build.set_defaults(func=cmd_build)

    p_import = sub.add_parser("import", help="HTML -> Markdown")
    p_import.add_argument("files", nargs="*")
    p_import.add_argument("--force", action="store_true", help="overschrijf ook niet-gecommitte Markdown")
    p_import.set_defaults(func=cmd_import)

    p_check = sub.add_parser("check", help="controleer of HTML en Markdown in sync zijn")
    p_check.add_argument("files", nargs="*")
    p_check.set_defaults(func=cmd_check)

    p_watch = sub.add_parser("watch", help="bouw HTML bij elke wijziging in Markdown")
    p_watch.add_argument("--interval", type=float, default=1.0)
    p_watch.set_defaults(func=cmd_watch)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
