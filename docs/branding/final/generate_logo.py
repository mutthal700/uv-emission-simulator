"""Generate BASE logo SVGs with text converted to outlines."""
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTDIR = sys.argv[1]
OUT = sys.argv[2]
_cache = {}


def font(name, wght):
    k = (name, wght)
    if k not in _cache:
        f = TTFont(f"{FONTDIR}/{name}%5Bwght%5D.ttf")
        _cache[k] = instantiateVariableFont(f, {"wght": wght})
    return _cache[k]


def text(s, x, y, size, name="Montserrat", wght=700, track=0.0, anchor="start"):
    """Return (svg path d, width). track is in em units."""
    f = font(name, wght)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    upm = f["head"].unitsPerEm
    sc = size / upm
    adv = []
    for ch in s:
        g = cmap[ord(ch)]
        adv.append((g, hmtx[g][0]))
    width = sum(a for _, a in adv) * sc + track * size * (len(s) - 1)
    if anchor == "middle":
        x -= width / 2
    pen = SVGPathPen(gs)
    cx = x
    for g, a in adv:
        gs[g].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
        cx += a * sc + track * size
    return pen.getCommands(), width


NAVY, BLUE, TEAL, GREEN, SLATE = "#0B3C5D", "#1B8BD0", "#15A39A", "#3BAA4A", "#4A6272"


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}">\n<title>{label}</title>\n{body}\n</svg>\n')


LABEL = "BASE — Building Air-conditioning and Sustainable Environment Research Laboratory"
L1, L2 = "BUILDING AIR-CONDITIONING AND SUSTAINABLE", "ENVIRONMENT RESEARCH LABORATORY"


# ---------- Mark 1: "B" monogram — building stem, air bowl, environment bowl ----------
def mark_b(c_stem=NAVY, c_top=BLUE, c_bot=GREEN, win="#FFFFFF"):
    return f'''<g>
  <path d="M10 20 L36 10 V90 H10 Z" fill="{c_stem}"/>
  <g fill="{win}">
    <rect x="16" y="30" width="13" height="7" rx="1"/><rect x="16" y="46" width="13" height="7" rx="1"/>
    <rect x="16" y="60" width="13" height="7" rx="1"/><rect x="16" y="74" width="13" height="7" rx="1"/>
  </g>
  <path d="M34 15 H55 A15 15 0 0 1 55 45 H34" fill="none" stroke="{c_top}" stroke-width="10"/>
  <path d="M34 55 H59 A15 15 0 0 1 59 85 H34" fill="none" stroke="{c_bot}" stroke-width="10"/>
</g>'''


# ---------- Mark 2: vent louvres stacked into a gabled building ----------
def mark_vent(c=(NAVY, "#145E8C", BLUE, TEAL, GREEN)):
    bars = [(50, 12, 14), (50, 30, 42), (50, 48, 70), (50, 66, 70), (50, 84, 70)]
    out = []
    for (cx, y, w), col in zip(bars, c):
        out.append(f'<rect x="{cx - w / 2}" y="{y - 6}" width="{w}" height="12" rx="6" fill="{col}"/>')
    return "<g>\n  " + "\n  ".join(out) + "\n</g>"


def lockup(mark, name, dark=False, font_name="Montserrat"):
    tc, sc = ("#FFFFFF", "#D3E4EE") if dark else (NAVY, SLATE)
    d1, w1 = text("BASE", 150, 82, 74, font_name, 700, 0.12)
    d2, w2 = text(L1, 152, 122, 14.5, font_name, 500, 0.085)
    d3, _ = text(L2, 152, 142, 14.5, font_name, 500, 0.085)
    W = int(152 + max(w1, w2) + 20)
    body = f'''<g transform="translate(16 20) scale(1.2)">{mark}</g>
<path d="{d1}" fill="{tc}"/>
<rect x="154" y="96" width="44" height="4" rx="2" fill="{GREEN}"/>
<path d="{d2}" fill="{sc}"/>
<path d="{d3}" fill="{sc}"/>'''
    open(f"{OUT}/{name}.svg", "w").write(svg(W, 160, body, LABEL))


def stacked(mark, name, dark=False, font_name="Montserrat"):
    tc, sc = ("#FFFFFF", "#D3E4EE") if dark else (NAVY, SLATE)
    d1, _ = text("BASE", 200, 272, 74, font_name, 700, 0.12, "middle")
    lines = ["BUILDING AIR-CONDITIONING AND", "SUSTAINABLE ENVIRONMENT", "RESEARCH LABORATORY"]
    subs = "".join(f'<path d="{text(t, 200, 318 + i * 22, 14.5, font_name, 500, 0.085, "middle")[0]}" fill="{sc}"/>' for i, t in enumerate(lines))
    body = f'''<g transform="translate(137 34) scale(1.5)">{mark}</g>
<path d="{d1}" fill="{tc}"/>
<rect x="178" y="288" width="44" height="4" rx="2" fill="{GREEN}"/>
{subs}'''
    open(f"{OUT}/{name}.svg", "w").write(svg(400, 380, body, LABEL))


def icon(mark, name):
    open(f"{OUT}/{name}.svg", "w").write(svg(100, 100, mark, "BASE mark"))



def badge(name):
    body = f'<circle cx="60" cy="60" r="60" fill="{NAVY}"/><g transform="translate(25.6 19) scale(0.82)">' + mark_b(c_stem="#FFFFFF", c_top="#5EC2F2", c_bot="#7AD08A", win=NAVY) + '</g>'
    open(f"{OUT}/{name}.svg", "w").write(svg(120, 120, body, "BASE badge"))

WHITE = dict(c_stem="#FFFFFF", c_top="#5EC2F2", c_bot="#7AD08A", win="#0B3C5D")
icon(mark_b(), "base-mark")
badge("base-badge")
lockup(mark_b(), "base-logo")
lockup(mark_b(**WHITE), "base-logo-white", dark=True)
stacked(mark_b(), "base-logo-stacked")
stacked(mark_b(**WHITE), "base-logo-stacked-white", dark=True)
print("ok")
