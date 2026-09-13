"""Build the artwork on github.com/niaga-labs (profile/assets/, HQ-123).

Every word is drawn as vector paths from the Geist fonts, so the SVGs look the same on every
machine and need no web font. Colours are the Ledger palette: navy #0B1F3A and one teal #0F8B8D.
The mark is the Niaga Labs interrupted N, unchanged.

What the cards say is the company's published product line-up: Niaga Commerce and the quant
research platform lead, the two Chain products are "Coming soon" and Kilat is "Later". Change it
only together with the company site. Every number in STATS is counted, not estimated; the README
says where.

Run from the repo root. --fonts is a folder holding the Geist variable fonts as GeistVF.woff and
GeistMonoVF.woff (the files create-next-app ships in app/fonts/; Geist is under the SIL OFL):

    uv run --with fonttools python scripts/build-profile-assets.py --fonts <dir>
"""

import argparse
from pathlib import Path

from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parents[1] / "profile" / "assets"

NAVY = "#0B1F3A"
TEAL = "#0F8B8D"

# The interrupted N in its 64-unit box, as in the brand kit.
MARK = '<path d="M8 56V12h12l20 26V24h12v32H40L20 30v26Z"/><rect x="40" y="6" width="12" height="12" rx="2"/>'

THEMES = {
    "light": {
        "card": "#FFFFFF",
        "border": "#D9E1EA",
        "title": NAVY,
        "body": "#4A5A6E",
        "strong": "#243447",
        "muted": "#6B7C90",
        "accent": "#0C7A7C",
        "tint": "#E3F2F2",
        "icon": TEAL,
        "chip": "#EEF3F7",
        "chip_text": "#2E3F52",
        "rule": "#E6ECF2",
        "later": "#EEF1F5",
        "later_text": "#5B6B80",
    },
    "dark": {
        "card": NAVY,
        "border": "#1E3A5F",
        "title": "#FFFFFF",
        "body": "#B6C4D4",
        "strong": "#DCE5EE",
        "muted": "#8FA3B8",
        "accent": "#5FC3C5",
        "tint": "#123F4F",
        "icon": "#5FC3C5",
        "chip": "#12294A",
        "chip_text": "#C8D3DF",
        "rule": "#173154",
        "later": "#1A2B42",
        "later_text": "#9AABBD",
    },
}

# Lucide-style icons on a 24-unit grid, stroke 2.
ICONS = {
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    "flask": '<path d="M10 2v7.5a2 2 0 0 1-.2.9L4.7 20.6a1 1 0 0 0 .9 1.4h12.8a1 1 0 0 0 .9-1.4l-5.1-10.2a2 2 0 0 1-.2-.9V2"/><path d="M8.5 2h7"/><path d="M7 16h10"/>',
    "chart": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "bot": '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "arrow": '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
}

FEATURED = [
    {
        "slug": "commerce",
        "icon": "bag",
        "overline": "E-COMMERCE PLATFORM",
        "title": "Niaga Commerce",
        "status": ("In development", "active"),
        "summary": "A commerce platform that connects a storefront with catalogue, orders, payments and "
        "fulfilment. Our own dropship store is the starting point.",
        "features": [
            "Catalogue, orders, payments and refunds",
            "Shopee and TikTok Shop sync",
            "Multi-courier shipping and returns",
        ],
        "chips": ["Go", "Next.js", "PostgreSQL", "NATS"],
        "link": "Write-up",
    },
    {
        "slug": "quant",
        "icon": "flask",
        "overline": "QUANTITATIVE RESEARCH",
        "title": "Quant research platform",
        "status": ("Paper trading", "active"),
        "summary": "Our own paper-trading platform for testing strategies. Every idea is judged the same "
        "way, and failures stay on the record. It is not a service.",
        "features": [
            "Pre-registered strategy specs",
            "One shared walk-forward audit",
            "Eleven-criterion promotion gate",
        ],
        "chips": ["Python", "FastAPI", "React", "PostgreSQL"],
        "link": "Notes",
    },
]

NEXT = [
    {
        "slug": "chain-analytics",
        "icon": "chart",
        "overline": "ROBINHOOD CHAIN",
        "title": "Chain Analytics",
        "status": ("Coming soon", "soon"),
        "body": "A dashboard for Robinhood Chain market activity. Read-only research is under way first.",
    },
    {
        "slug": "chain-tool",
        "icon": "bot",
        "overline": "ROBINHOOD CHAIN",
        "title": "Chain trading tool",
        "status": ("Coming soon", "soon"),
        "body": "A tool for traders on Robinhood Chain, planned once the dashboard has proven useful.",
    },
    {
        "slug": "kilat",
        "icon": "truck",
        "overline": "LOGISTICS",
        "title": "Kilat Pet Delivery",
        "status": ("Later", "later"),
        "body": "Booking and live tracking for pet transport. Paused while we focus on commerce.",
    },
]

# (tag, number, label, detail). Sources are listed under the stats image in profile/README.md.
STATS = [
    ("ORG", "65", "repositories, one organisation", "29 public · 8 archived"),
    ("NIAGA", "10 + 3", "Go services + Next.js apps", "behind one storefront"),
    ("NIAGA", "17", "PostgreSQL schemas", "one database, schema per service"),
    ("NIAGA", "2 + 1", "marketplaces", "Shopee, TikTok Shop · Lazada built"),
    ("QUANT", "20", "audited strategy trials", "every one kept on the record"),
    ("QUANT", "0", "promoted to real money", "none passed every gate criterion"),
]
STATS_CAPTION = "Counted 13 Sep 2026 from GitHub and the two public write-ups. Quant figures as of 10 Sep 2026."

BANNER_ROWS = [
    ("Niaga Commerce", "In development", "active"),
    ("Quant research", "Paper trading", "active"),
    ("Chain Analytics", "Coming soon", "soon"),
    ("Chain trading tool", "Coming soon", "soon"),
    ("Kilat Pet Delivery", "Later", "later"),
]


def num(v: float) -> str:
    return f"{v:.1f}".removesuffix(".0")


class Doc:
    """The glyph outlines one SVG file uses, each written once into its <defs>."""

    def __init__(self) -> None:
        self.defs: dict[str, str] = {}

    def glyph(self, face: "Face", ch: str) -> str:
        gid = f"{face.key}{ord(ch):x}"
        if gid not in self.defs:
            pen = SVGPathPen(face.glyphs, ntos=lambda v: str(round(v)))
            face.glyph(ch).draw(pen)
            d = pen.getCommands()
            self.defs[gid] = f'<path id="{gid}" d="{d}"/>' if d else ""
        return gid if self.defs[gid] else ""

    def render(self) -> str:
        return f"<defs>{''.join(self.defs.values())}</defs>"


class Face:
    """One weight of a Geist variable font, drawn as SVG outlines."""

    def __init__(self, path: Path, weight: int, key: str) -> None:
        font = TTFont(path)
        self.glyphs = font.getGlyphSet(location={"wght": weight})
        self.cmap = font.getBestCmap()
        self.upm = font["head"].unitsPerEm
        self.key = key
        self.doc = Doc()
        self._advance: dict[str, float] = {}

    def glyph(self, ch: str):
        name = self.cmap.get(ord(ch))
        if name is None:
            raise SystemExit(f"Geist has no glyph for {ch!r} (U+{ord(ch):04X})")
        return self.glyphs[name]

    def advance(self, ch: str) -> float:
        """Advance width at this weight. A variable-font glyph reports its instanced width only
        after it has been drawn, and only on that same object; a fresh one gives the default
        master's width (N at 550: 747 drawn, 743 undrawn), which clipped the first wordmark."""
        if ch not in self._advance:
            g = self.glyph(ch)
            g.draw(RecordingPen())
            self._advance[ch] = g.width
        return self._advance[ch]

    def width(self, text: str, size: float, tracking: float = 0.0) -> float:
        scale = size / self.upm
        return sum(self.advance(c) * scale + tracking for c in text) - (tracking if text else 0)

    def text(
        self, s: str, x: float, y: float, size: float, fill: str, tracking: float = 0.0, anchor: str = "start"
    ) -> str:
        """One run of text: each glyph is defined once per file (Doc) and placed with <use>."""
        scale = size / self.upm
        w = self.width(s, size, tracking)
        x = x - w if anchor == "end" else x - w / 2 if anchor == "middle" else x
        uses, cursor = [], 0.0
        for c in s:
            gid = self.doc.glyph(self, c)
            if gid:
                uses.append(f'<use href="#{gid}" x="{round(cursor)}"/>' if round(cursor) else f'<use href="#{gid}"/>')
            cursor += self.advance(c) + tracking / scale
        k = f"{scale:.5f}".rstrip("0")
        return f'<g fill="{fill}" transform="translate({num(x)} {num(y)}) scale({k} -{k})">{"".join(uses)}</g>'

    def wrap(self, s: str, size: float, max_width: float) -> list[str]:
        lines, line = [], ""
        for word in s.split():
            trial = f"{line} {word}".strip()
            if line and self.width(trial, size) > max_width:
                lines.append(line)
                line = word
            else:
                line = trial
        return lines + [line] if line else lines


def icon(name: str, x: float, y: float, size: float, color: str) -> str:
    k = num(size / 24)
    return (
        f'<g transform="translate({num(x)} {num(y)}) scale({k})" fill="none" stroke="{color}" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'
    )


class Kit:
    def __init__(self, fonts: Path) -> None:
        self.sans = Face(fonts / "GeistVF.woff", 400, "r")
        self.medium = Face(fonts / "GeistVF.woff", 500, "m")
        self.semi = Face(fonts / "GeistVF.woff", 600, "b")
        self.brand = Face(fonts / "GeistVF.woff", 550, "w")
        self.mono = Face(fonts / "GeistMonoVF.woff", 450, "c")
        self.faces = [self.sans, self.medium, self.semi, self.brand, self.mono]

    def svg(self, w: int, h: int, title: str, body: str) -> str:
        """Wrap a drawing, emit the glyphs it used, and start a fresh Doc for the next file."""
        defs = "".join(f.doc.render() for f in self.faces if f.doc.defs)
        for f in self.faces:
            f.doc = Doc()
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img"><title>{title}</title>{defs}{body}</svg>\n'
        )

    def lockup(self, x: float, top: float, k: float, color: str) -> str:
        """The brand wordmark (mark + "Niaga Labs" at Geist 550), placed by its inked top-left corner."""
        cursor, parts, scale = 110.0, [], 48 / self.brand.upm
        for ch in "Niaga Labs":
            g = self.brand.glyph(ch)
            pen = SVGPathPen(self.brand.glyphs, ntos=num)
            g.draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, 77)))
            parts.append(pen.getCommands())
            cursor += g.width * scale - (0.8 if ch != " " else 0)
        # Inked box of the original lockup starts at (26, 31): mark at translate(18 25), square top at y=6.
        return (
            f'<g transform="translate({num(x - 26 * k)} {num(top - 31 * k)}) scale({num(k)})" fill="{color}">'
            f'<g transform="translate(18 25)">{MARK}</g><path d="{"".join(parts)}"/></g>'
        )

    def lockup_width(self, k: float) -> float:
        scale = 48 / self.brand.upm
        cursor = 110.0
        for ch in "Niaga Labs":
            cursor += self.brand.advance(ch) * scale - (0.8 if ch != " " else 0)
        return (cursor - 26) * k

    def pill(self, label: str, kind: str, right: float, top: float, h: float, size: float, t: dict) -> str:
        pad, dot = h * 0.42, h * 0.16
        tw = self.medium.width(label, size)
        w = pad + dot * 2 + h * 0.28 + tw + pad
        x, cy = right - w, top + h / 2
        base = top + h / 2 + size * 0.36
        if kind == "active":
            shell = f'<rect x="{num(x)}" y="{num(top)}" width="{num(w)}" height="{num(h)}" rx="{num(h / 2)}" fill="{t["tint"]}"/>'
            mark = f'<circle cx="{num(x + pad + dot)}" cy="{num(cy)}" r="{num(dot)}" fill="{TEAL}"/>'
            color = t["accent"]
        elif kind == "soon":
            shell = (
                f'<rect x="{num(x + 0.75)}" y="{num(top + 0.75)}" width="{num(w - 1.5)}" height="{num(h - 1.5)}" '
                f'rx="{num(h / 2)}" fill="none" stroke="{TEAL}" stroke-width="1.5" stroke-dasharray="4 3"/>'
            )
            mark = f'<circle cx="{num(x + pad + dot)}" cy="{num(cy)}" r="{num(dot - 0.75)}" fill="none" stroke="{TEAL}" stroke-width="1.5"/>'
            color = t["accent"]
        else:
            shell = f'<rect x="{num(x)}" y="{num(top)}" width="{num(w)}" height="{num(h)}" rx="{num(h / 2)}" fill="{t["later"]}"/>'
            mark = f'<circle cx="{num(x + pad + dot)}" cy="{num(cy)}" r="{num(dot)}" fill="{t["later_text"]}"/>'
            color = t["later_text"]
        return shell + mark + self.medium.text(label, x + pad + dot * 2 + h * 0.28, base, size, color)

    # ------------------------------------------------------------------ banner (one version: it carries its own navy)
    def banner(self) -> str:
        W, H = 1200, 420
        b = [
            (
                '<defs><clipPath id="c"><rect width="1200" height="420" rx="20"/></clipPath>'
                f'<radialGradient id="g1" cx="1060" cy="30" r="560" gradientUnits="userSpaceOnUse">'
                f'<stop offset="0" stop-color="{TEAL}" stop-opacity=".42"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>'
                f'<radialGradient id="g2" cx="60" cy="440" r="420" gradientUnits="userSpaceOnUse">'
                f'<stop offset="0" stop-color="{TEAL}" stop-opacity=".16"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient></defs>'
            ),
            '<g clip-path="url(#c)">',
            f'<rect width="{W}" height="{H}" fill="{NAVY}"/>',
            '<g stroke="#FFFFFF" stroke-opacity=".05" stroke-width="1">'
            + "".join(f'<path d="M{x} 0V{H}"/>' for x in range(60, W, 60))
            + "".join(f'<path d="M0 {y}H{W}"/>' for y in range(60, H, 60))
            + "</g>",
            f'<rect width="{W}" height="{H}" fill="url(#g1)"/><rect width="{W}" height="{H}" fill="url(#g2)"/>',
            "</g>",
        ]
        x0 = 64
        b.append(self.mono.text("INDEPENDENT SOFTWARE STUDIO · MALAYSIA", x0, 94, 17, "#7FD0D1", tracking=2.2))
        b.append(self.lockup(x0, 124, 1.6, "#FFFFFF"))
        b.append(self.medium.text("Software for commerce.", x0, 274, 40, "#FFFFFF"))
        b.append(self.medium.text("Tools for what’s next.", x0, 324, 40, "#7FD0D1"))
        b.append(self.mono.text("niagalabs.com  ·  hello@niagalabs.com", x0, 370, 18, "#9FB3C8"))

        px, py, pw, ph = 700, 60, 436, 300
        b.append(
            f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="14" fill="#FFFFFF" fill-opacity=".04" '
            f'stroke="#FFFFFF" stroke-opacity=".14"/>'
        )
        left, right = px + 26, px + pw - 26
        b.append(self.mono.text("PRODUCT LINE", left, py + 38, 14, "#7FD0D1", tracking=2))
        b.append(self.mono.text("STATUS", right, py + 38, 14, "#7FD0D1", tracking=2, anchor="end"))
        b.append(f'<path d="M{left} {py + 56}H{right}" stroke="#FFFFFF" stroke-opacity=".16"/>')
        for i, (name, status, kind) in enumerate(BANNER_ROWS):
            base = py + 96 + i * 45
            b.append(self.medium.text(name, left, base, 21, "#EEF3F8"))
            colour = {"active": "#9FDCDD", "soon": "#9FB3C8", "later": "#8CA0B6"}[kind]
            b.append(self.sans.text(status, right, base, 18, colour, anchor="end"))
            cx, cy = right - self.sans.width(status, 18) - 14, base - 6
            if kind == "active":
                b.append(f'<circle cx="{num(cx)}" cy="{cy}" r="5" fill="#2BB3B5"/>')
            elif kind == "soon":
                b.append(f'<circle cx="{num(cx)}" cy="{cy}" r="4.3" fill="none" stroke="#2BB3B5" stroke-width="1.5"/>')
            else:
                b.append(f'<circle cx="{num(cx)}" cy="{cy}" r="5" fill="#5B6B80"/>')
            if i < len(BANNER_ROWS) - 1:
                b.append(f'<path d="M{left} {base + 19}H{right}" stroke="#FFFFFF" stroke-opacity=".07"/>')
        return self.svg(W, H, "Niaga Labs. Software for commerce. Tools for what’s next.", "".join(b))

    # ------------------------------------------------------------------ stats strip
    def stats(self, t: dict) -> str:
        W, cols, gap, th = 1200, 3, 24, 150
        tw = (W - gap * (cols - 1)) / cols
        b = []
        for i, (tag, value, label, detail) in enumerate(STATS):
            x, y = (i % cols) * (tw + gap), (i // cols) * (th + gap)
            b.append(
                f'<rect x="{num(x + 0.5)}" y="{num(y + 0.5)}" width="{num(tw - 1)}" height="{th - 1}" rx="16" '
                f'fill="{t["card"]}" stroke="{t["border"]}"/>'
            )
            b.append(f'<rect x="{num(x + 28)}" y="{y + 30}" width="4" height="40" rx="2" fill="{TEAL}"/>')
            b.append(self.semi.text(value, x + 46, y + 68, 48, t["title"]))
            b.append(self.mono.text(tag, x + tw - 26, y + 36, 13, t["accent"], tracking=1.6, anchor="end"))
            for words, size, face, colour, base in (
                (label, 20, self.medium, t["strong"], 104),
                (detail, 17, self.sans, t["muted"], 128),
            ):
                assert face.width(words, size) < tw - 56, f"stat {value}: {words!r} does not fit on one line"
                b.append(face.text(words, x + 28, y + base, size, colour))
        cap_y = 2 * th + gap + 44
        b.append(self.mono.text(STATS_CAPTION, 2, cap_y, 15, t["muted"]))
        return self.svg(W, cap_y + 8, "Niaga Labs by the numbers", "".join(b))

    # ------------------------------------------------------------------ featured product card
    def featured(self, p: dict, t: dict) -> str:
        W, H, pad = 600, 540, 40
        b = [
            (
                f'<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="20" fill="{t["card"]}" '
                f'stroke="{t["border"]}" stroke-width="1.5"/>'
            )
        ]
        b.append(f'<rect x="{pad}" y="{pad}" width="60" height="60" rx="15" fill="{t["tint"]}"/>')
        b.append(icon(p["icon"], pad + 15, pad + 15, 30, t["icon"]))
        b.append(self.pill(p["status"][0], p["status"][1], W - pad, pad + 12, 36, 17, t))
        b.append(self.mono.text(p["overline"], pad, 146, 16, t["accent"], tracking=2))
        b.append(self.semi.text(p["title"], pad, 194, 38, t["title"]))
        for j, line in enumerate(self.sans.wrap(p["summary"], 21, W - 2 * pad)[:3]):
            b.append(self.sans.text(line, pad, 236 + j * 30, 21, t["body"]))
        b.append(f'<path d="M{pad} 338H{W - pad}" stroke="{t["rule"]}" stroke-width="1.5"/>')
        for j, feat in enumerate(p["features"]):
            base = 378 + j * 34
            b.append(icon("check", pad, base - 17, 20, TEAL))
            b.append(self.medium.text(feat, pad + 32, base, 20, t["strong"]))
        cx, top, ch = pad, 472, 32
        for chip in p["chips"]:
            w = self.mono.width(chip, 15) + 24
            b.append(f'<rect x="{num(cx)}" y="{top}" width="{num(w)}" height="{ch}" rx="8" fill="{t["chip"]}"/>')
            b.append(self.mono.text(chip, cx + 12, top + 21, 15, t["chip_text"]))
            cx += w + 8
        lw = self.medium.width(p["link"], 18)
        b.append(self.medium.text(p["link"], W - pad - 22, top + 22, 18, t["accent"], anchor="end"))
        b.append(icon("arrow", W - pad - 18, top + 7, 18, t["accent"]))
        assert cx < W - pad - 22 - lw - 12, f"{p['slug']}: chips run into the link"
        return self.svg(W, H, f"{p['title']}: {p['status'][0]}", "".join(b))

    # ------------------------------------------------------------------ coming-next card
    def upcoming(self, p: dict, t: dict) -> str:
        W, H, pad = 400, 272, 30
        b = [
            (
                f'<rect x=".75" y=".75" width="{W - 1.5}" height="{H - 1.5}" rx="18" fill="{t["card"]}" '
                f'stroke="{t["border"]}" stroke-width="1.5"/>'
            )
        ]
        b.append(f'<rect x="{pad}" y="{pad}" width="46" height="46" rx="12" fill="{t["tint"]}"/>')
        b.append(icon(p["icon"], pad + 11, pad + 11, 24, t["icon"]))
        b.append(self.pill(p["status"][0], p["status"][1], W - pad, pad + 8, 30, 15, t))
        b.append(self.mono.text(p["overline"], pad, 114, 14, t["accent"], tracking=1.8))
        b.append(self.semi.text(p["title"], pad, 152, 28, t["title"]))
        for j, line in enumerate(self.sans.wrap(p["body"], 19, W - 2 * pad)[:3]):
            b.append(self.sans.text(line, pad, 190 + j * 27, 19, t["body"]))
        return self.svg(W, H, f"{p['title']}: {p['status'][0]}", "".join(b))

    def wordmark(self, color: str) -> str:
        w = self.lockup_width(1) + 2
        return self.svg(round(w), 56, "Niaga Labs", self.lockup(1, 1, 1, color))


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the artwork on github.com/niaga-labs.")
    ap.add_argument("--fonts", type=Path, required=True, help="folder holding GeistVF.woff and GeistMonoVF.woff")
    kit = Kit(ap.parse_args().fonts)
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "banner.svg": kit.banner(),
        "wordmark-navy.svg": kit.wordmark(NAVY),
        "wordmark-white.svg": kit.wordmark("#FFFFFF"),
    }
    for theme, t in THEMES.items():
        files[f"stats-{theme}.svg"] = kit.stats(t)
        for p in FEATURED:
            files[f"card-{p['slug']}-{theme}.svg"] = kit.featured(p, t)
        for p in NEXT:
            files[f"card-{p['slug']}-{theme}.svg"] = kit.upcoming(p, t)
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8", newline="\n")
        print(f"{name:32} {len(content.encode()):>7,} bytes")
    print(f"{len(files)} files written to {OUT}")


if __name__ == "__main__":
    main()
