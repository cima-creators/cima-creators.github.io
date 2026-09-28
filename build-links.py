#!/usr/bin/env python3
"""Genera los links cortos de las apps UGC (videos y panel) para cada marca.

    python3 build-links.py [ruta/a/cima-admin.html]

Lee las marcas de `cima-admin.html` (BRAND_CONFIGS) y escribe una carpeta por
marca con un redirect chiquito:

    /<marca>/videos  -> cima-creators.html?brand=<marca>   (las creadoras suben sus videos)
    /<marca>/admin   -> cima-admin.html?brand=<marca>      (panel de la marca y de CIMA)
    /vista           -> cima-general.html                  (Vista General, interna)

Los links de las collabs (/<marca>, /<marca>/app, /<marca>/panel) los arma el
chat de canjes y no se tocan acá.
"""
import os, re, sys

BASE = "https://cima-creators.github.io/cleargy.ugc/"
DASH = "https://cima-creators.github.io/cleargy.dashboard/cima-general.html"
ADMIN = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Desktop/claude/cima-admin.html")

PLANTILLA = """<!doctype html>
<html lang="es"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>{titulo}</title>
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<script>
/* Link corto: lleva a la pagina de siempre{conmarca}, conservando los parametros que vengan. */
(function(){{var q=new URLSearchParams(location.search);{setmarca}q.set("v",Date.now().toString(36));location.replace("{destino}?"+q.toString()+location.hash);}})();
</script>
<noscript><meta http-equiv="refresh" content="0;url={destino}{qmarca}"></noscript>
</head><body style="font-family:system-ui,sans-serif;background:#fff;color:#222;padding:24px">Abriendo {titulo}… <a href="{destino}{qmarca}">Toca aca si no abre</a>.</body></html>
"""

def escribir(carpeta, titulo, desc, destino, marca=None):
    os.makedirs(carpeta, exist_ok=True)
    with open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8") as f:
        f.write(PLANTILLA.format(
            titulo=titulo, desc=desc, destino=destino,
            conmarca=f" con ?brand={marca}" if marca else "",
            setmarca=f'q.set("brand","{marca}");' if marca else "",
            qmarca=f"?brand={marca}" if marca else ""))

src = open(ADMIN, encoding="utf-8").read()
bloque = src[src.index("const BRAND_CONFIGS"):]
marcas = []
for m in re.finditer(r"\n  ([a-z0-9]+): \{", bloque):
    slug = m.group(1)
    nom = re.search(r"name:'([^']+)'", bloque[m.end():m.end() + 900])
    marcas.append((slug, nom.group(1) if nom else slug))

for slug, nombre in marcas:
    escribir(f"{slug}/videos", f"{nombre} · Subí tus videos", "App de creadoras de CIMA",
             BASE + "cima-creators.html", slug)
    escribir(f"{slug}/admin", f"{nombre} · Panel de videos", "Panel de la marca",
             BASE + "cima-admin.html", slug)
escribir("vista", "CIMA · Vista General", "Panel del equipo de CIMA", DASH)
print(f"{len(marcas)} marcas: " + ", ".join(s for s, _ in marcas))
