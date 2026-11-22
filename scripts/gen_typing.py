# Regenerates assets/typing.svg. Needs fonttools + brotli and the Geist Pixel Circle woff2.
# Usage: python scripts/gen_typing.py path/to/geist-pixel-circle.woff2 assets/typing.svg
import sys, re, base64, io
from html import escape
from fontTools.ttLib import TTFont
from fontTools import subset

LINES = ["Systems · Backend · Frontend", "Fast backends, from scratch",
         "UIs people enjoy using", "Desktop, web and mobile apps"]
FONT, OUT = sys.argv[1], sys.argv[2]
W, H, SIZE, BASE = 1200, 99, 68, 74.0
TYPE, DEL, HOLD, GAP = 75.0, 30.0, 2030.0, 475.0   # ms, matched to the previous file

f = TTFont(FONT); cm = f.getBestCmap(); hm = f['hmtx']; upm = f['head'].unitsPerEm
adv = lambda c: hm[cm[ord(c)]][0] * SIZE / upm

# subset the font to just the glyphs used
opts = subset.Options(); opts.flavor = 'woff2'; opts.layout_features = []; opts.name_IDs = []
sub = subset.Subsetter(opts); sub.populate(text=''.join(set(''.join(LINES)) - {' '}))
fs = TTFont(FONT); sub.subset(fs); buf = io.BytesIO(); fs.save(buf)
b64 = base64.b64encode(buf.getvalue()).decode()

# timeline
events = []  # (t, kind, payload)
chars = []   # (line, char, x, t_on, t_off)
cur = []     # (t, x)
t = 0.0
starts = []
for li, line in enumerate(LINES):
    w = sum(adv(c) for c in line)
    x0 = (W - w) / 2
    xs = []; x = x0
    for c in line:
        xs.append(x); x += adv(c)
    ends = xs[1:] + [x]
    starts.append((x0, x))
    if li == 0: cur.append((0.0, x0))
    on = []
    for k in range(len(line)):
        t += TYPE; on.append(t); cur.append((t, ends[k]))
    t += HOLD
    off = [0]*len(line)
    for k in range(len(line)-1, -1, -1):
        off[k] = t; cur.append((t, xs[k]))
        if k: t += DEL
    for k, c in enumerate(line):
        if c != ' ': chars.append((li, c, xs[k], on[k], off[k]))
    t += GAP
TOTAL = t
pc = lambda ms: f"{ms / TOTAL * 100:.3f}%"

css = [f"@font-face{{font-family:'GPC';src:url(data:font/woff2;base64,{b64}) format('woff2')}}",
       ".ch{font-family:GPC;font-size:68px;fill:#0b0a14;stroke:#ffffff;stroke-width:2.6px;paint-order:stroke;stroke-linejoin:round}text{font-kerning:none}",
       f".ch{{animation-duration:{TOTAL/1000:.2f}s;animation-iteration-count:infinite;animation-timing-function:step-end}}"]
texts = []
for i, (li, c, x, ton, toff) in enumerate(chars):
    css.append(f"@keyframes c{i}{{0%{{opacity:0}}{pc(ton)}{{opacity:1}}{pc(toff)}{{opacity:0}}100%{{opacity:0}}}}.c{i}{{animation-name:c{i}}}")
    op = '' if li == 0 else ' opacity="0"'
    texts.append(f'<text y="0" class="ch c{i}" x="{x:.1f}"{op}>{escape(c)}</text>')
kf = ''.join(f"{pc(tt)}{{transform:translateX({x:.1f}px)}}" for tt, x in cur)
kf += f"100%{{transform:translateX({cur[0][1]:.1f}px)}}"
css.append(f"@keyframes cur{{{kf}}}.cur{{transform:translateX({starts[0][1]:.1f}px);animation:cur {TOTAL/1000:.2f}s step-end infinite}}")
css.append(".blk{animation:bl 1s steps(1) infinite}@keyframes bl{50%{opacity:0}}@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
label = escape(' / '.join(LINES))
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
       f'<style>{"".join(css)}</style><g transform="translate(0 {BASE})">{"".join(texts)}</g>'
       f'<g class="cur"><rect class="blk" x="6" y="25.0" width="23.1" height="49.1" rx="3" fill="#0b0a14" stroke="#ffffff" stroke-width="2"/></g></svg>')
open(OUT, 'w').write(svg)
for (a, b), l in zip(starts, LINES): print(f"{a:7.1f} {b:7.1f}  {l}")
print('total', TOTAL/1000, 's, bytes', len(svg))
