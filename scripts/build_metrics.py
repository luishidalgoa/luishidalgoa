#!/usr/bin/env python3
"""Genera la tarjeta de métricas del perfil (assets/metrics-{dark,light}.svg).

Por qué existe: los widgets de terceros se caen y el README queda roto
(github-readme-stats -> 503 DEPLOYMENT_PAUSED, github-profile-trophy -> 402
DEPLOYMENT_DISABLED, streak-stats -> timeouts del proxy camo). Esta tarjeta se
genera aquí, en Actions, con el GITHUB_TOKEN por defecto, y se sirve como
fichero del propio repo: no hay instancia externa que pueda morirse.

Solo datos públicos (endpoint /users/...): el trabajo privado queda fuera a
propósito, y el README ya lo advierte.

Uso local:  GITHUB_TOKEN=$(gh auth token) python scripts/build_metrics.py
"""
import datetime
import json
import os
import urllib.error
import urllib.request

USER = "luishidalgoa"
# crafty-4 vendorea ace-builds y compañía (~2.3 MB de CSS ajeno): ahogaría el
# reparto real de lenguajes, así que se excluye SOLO del cómputo de lenguajes.
LANG_EXCLUDE = {"crafty-4"}
TOP_N = 7

# Colores linguist de GitHub para los lenguajes que aparecen en mis repos.
LANG_COLORS = {
    "TypeScript": "#3178c6", "Java": "#b07219", "Dart": "#00B4AB",
    "C#": "#178600", "Python": "#3572A5", "PHP": "#4F5D95",
    "JavaScript": "#f1e05a", "HTML": "#e34c26", "CSS": "#563d7c",
    "SCSS": "#c6538c", "Kotlin": "#A97BFF", "Swift": "#F05138",
    "Shell": "#89e051", "PowerShell": "#012456", "Blade": "#f7523f",
    "Hack": "#878787", "Dockerfile": "#384d54", "GLSL": "#5686a5",
    "Batchfile": "#C1F12E", "Inno Setup": "#264b99", "TeX": "#3D6117",
    "Other": "#8b949e",
}


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "User-Agent": USER,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def has_workflows(repo_name):
    try:
        entries = api(f"/repos/{USER}/{repo_name}/contents/.github/workflows")
        return isinstance(entries, list) and len(entries) > 0
    except urllib.error.HTTPError:
        return False


def collect():
    profile = api(f"/users/{USER}")
    repos, page = [], 1
    while True:
        batch = api(f"/users/{USER}/repos?per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]

    stars = sum(r["stargazers_count"] for r in own)
    with_ci = sum(1 for r in own if has_workflows(r["name"]))

    langs = {}
    for r in own:
        if r["name"] in LANG_EXCLUDE:
            continue
        for lang, size in api(f"/repos/{USER}/{r['name']}/languages").items():
            langs[lang] = langs.get(lang, 0) + size
    total = sum(langs.values()) or 1
    ranked = sorted(langs.items(), key=lambda kv: -kv[1])
    top = [(l, s / total * 100) for l, s in ranked[:TOP_N]]
    rest = 100 - sum(p for _, p in top)
    if rest > 0.05:
        top.append(("Other", rest))

    return {
        "stars": stars,
        "repos": len(own),
        "ci": with_ci,
        "followers": profile["followers"],
        "langs": top,
        "date": datetime.date.today().isoformat(),
    }


def render(m, p):
    """Dibuja la tarjeta con la paleta `p` (dark o light)."""
    W, H, PAD = 820, 214, 24
    bar_w = W - 2 * PAD

    chips = [
        (m["stars"], "stars earned"),
        (m["repos"], "public repos"),
        (m["ci"], "repos with own CI"),
        (m["followers"], "followers"),
    ]
    chip_svg = ""
    for i, (value, label) in enumerate(chips):
        x = PAD + i * 195
        chip_svg += (
            f'<text x="{x}" y="92" font-size="26" font-weight="700" '
            f'fill="{p["value"]}">{value}</text>'
            f'<text x="{x}" y="110" font-size="12" fill="{p["label"]}">{label}</text>'
        )

    # Barra apilada de lenguajes, con esquinas redondeadas vía clipPath.
    bar_svg, x = "", 0.0
    for lang, pct in m["langs"]:
        w = bar_w * pct / 100
        color = LANG_COLORS.get(lang, LANG_COLORS["Other"])
        bar_svg += f'<rect x="{PAD + x:.1f}" y="128" width="{w:.1f}" height="12" fill="{color}"/>'
        x += w

    legend_svg = ""
    for i, (lang, pct) in enumerate(m["langs"]):
        lx = PAD + (i % 4) * 195
        ly = 166 + (i // 4) * 24
        color = LANG_COLORS.get(lang, LANG_COLORS["Other"])
        legend_svg += (
            f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{color}"/>'
            f'<text x="{lx + 17}" y="{ly}" font-size="12" fill="{p["legend"]}">'
            f"{lang} {pct:.1f}%</text>"
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub metrics for {USER}">
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{p['bg']}" stroke="{p['border']}"/>
  <g font-family="'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif">
    <text x="{PAD}" y="40" font-size="17" font-weight="600" fill="{p['title']}">{USER} — public GitHub activity</text>
    <text x="{W - PAD}" y="40" font-size="11" text-anchor="end" fill="{p['footer']}">updated {m['date']} by scripts/build_metrics.py</text>
    {chip_svg}
    <clipPath id="bar"><rect x="{PAD}" y="128" width="{bar_w}" height="12" rx="6"/></clipPath>
    <g clip-path="url(#bar)">{bar_svg}</g>
    {legend_svg}
  </g>
</svg>
"""


PALETTES = {
    "dark": {
        "bg": "#1a1b27", "border": "#30363d", "title": "#7aa2f7",
        "value": "#c0caf5", "label": "#565f89", "legend": "#a9b1d6",
        "footer": "#565f89",
    },
    "light": {
        "bg": "#ffffff", "border": "#d8dee4", "title": "#3868d6",
        "value": "#1f2328", "label": "#59636e", "legend": "#424a53",
        "footer": "#8c959f",
    },
}


def main():
    metrics = collect()
    os.makedirs("assets", exist_ok=True)
    for name, palette in PALETTES.items():
        path = f"assets/metrics-{name}.svg"
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(metrics, palette))
        print(f"escrito {path}")
    print(json.dumps({k: v for k, v in metrics.items() if k != "langs"}))
    print("langs:", ", ".join(f"{l} {p:.1f}%" for l, p in metrics["langs"]))


if __name__ == "__main__":
    main()
