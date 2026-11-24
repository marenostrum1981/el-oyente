"""Enlaza automáticamente los términos del glosario en los textos.

Cada término se enlaza (#g-ID) solo la primera vez que aparece en cada página
(ficha, artículo, época o persona) y nunca si esa página ya lo enlaza a mano.
No toca títulos (h1-h3), enlaces ya existentes ni textos en otro idioma (lang=).
Las palabras ambiguas se buscan solo en formas seguras: «el clave» (instrumento)
y no «la clave»; «director de orquesta» y no «director»; «concierto», «tema» y
«cuerda» no se enlazan solos porque tienen otros sentidos.
"""
import re

# Más largos primero: así «forma sonata» gana a «sonata» y «doble cuerda» a nada.
PATRONES = [
    ("polifonia-implicita", r"polifonía implícita"),
    ("musica-programatica", r"música programática"),
    ("dinamica-terrazas", r"dinámica (?:en|por) terrazas"),
    ("pieza-de-caracter", r"piezas? de carácter"),
    ("bajo-continuo", r"bajo continuo"),
    ("director", r"director(?:a|es)? de orquesta"),
    ("forma-sonata", r"forma sonata"),
    ("doble-cuerda", r"dobles? cuerdas?"),
    ("da-capo", r"da capo"),
    ("contrapunto", r"contrapunto"),
    ("arpegio", r"arpegi(?:os?|ados?|adas?)"),
    ("arreglo", r"arreglos?"),
    ("vibrato", r"vibratos?"),
    ("legato", r"legato"),
    ("galanterias", r"galanterías"),
    ("ritornello", r"ritornellos?"),
    ("pizzicato", r"pizzicatos?"),
    ("crescendo", r"crescendos?|diminuendos?"),
    ("zarabanda", r"zarabandas?"),
    ("allemande", r"allemandes?"),
    ("courante", r"courantes?"),
    ("metronomo", r"metrónomos?"),
    ("transportar", r"transporta(?:r|rla|rlo|do|da)"),
    ("tonalidad", r"tonalidad(?:es)?"),
    ("movimiento", r"movimientos?"),
    ("sinfonia", r"sinfonías?"),
    ("nocturno", r"nocturnos?"),
    ("preludio", r"preludios?"),
    ("catalogo", r"catálogos?"),
    ("minueto", r"minuetos?"),
    ("mazurca", r"mazurcas?"),
    ("cantata", r"cantatas?"),
    ("requiem", r"réquiem"),
    ("mecenas", r"mecenas"),
    ("sordina", r"sordinas?"),
    ("tremolo", r"trémolos?"),
    ("balada", r"baladas?"),
    ("sonata", r"sonatas?"),
    ("compas", r"compás|compases"),
    ("rubato", r"rubato"),
    ("tocata", r"tocatas?"),
    ("pedal", r"pedal(?:es)?"),
    ("suite", r"suites?"),
    ("tempo", r"tempos?"),
    ("trino", r"trinos?"),
    ("tutti", r"tutti"),
    ("giga", r"gigas?"),
    ("fuga", r"fugas?"),
    ("coda", r"codas?"),
    ("opus", r"opus"),
    ("arpa", r"arpas?"),
    ("lied", r"lied(?:er)?"),
    ("clave", r"\b(?:el|del|un|al|los|unos) (?P<w>claves?)"),
]
# Términos que no se enlazan solos (tienen otros sentidos); se enlazan a mano.
NO_AUTO = {"concierto", "tema", "cuerda"}
COMP = [(g, re.compile(r"\b(?:%s)\b" % p, re.I)) for g, p in PATRONES]
TAG = re.compile(r"(<[^>]+>)")
SALTA = {"a", "h1", "h2", "h3", "summary", "dt"}
VACIAS = {"br", "img", "hr", "input", "meta", "link", "wbr"}


def _uno(html, pat, gid):
    partes = TAG.split(html)
    pila = []
    for i, seg in enumerate(partes):
        if i % 2:
            m = re.match(r"<\s*(/)?\s*([a-zA-Z0-9]+)([^>]*)>", seg)
            if not m:
                continue
            cierra, nombre, attrs = m.groups()
            nombre = nombre.lower()
            if nombre in VACIAS:
                continue
            if cierra:
                for j in range(len(pila) - 1, -1, -1):
                    if pila[j][0] == nombre:
                        del pila[j:]
                        break
            elif not attrs.rstrip().endswith("/"):
                pila.append((nombre, "lang=" in attrs))
            continue
        if any(n in SALTA or lang for n, lang in pila):
            continue
        mm = pat.search(seg)
        if mm:
            a, b = mm.span("w") if "w" in pat.groupindex else mm.span()
            partes[i] = seg[:a] + f'<a href="#g-{gid}">' + seg[a:b] + "</a>" + seg[b:]
            return "".join(partes), True
    return html, False


def enlazar_pagina(bloques, glos_ids):
    """bloques: lista de (contenedor, clave) en el orden en que se leen en la página."""
    texto = " ".join(c[k] for c, k in bloques if isinstance(c[k], str))
    usados = set(re.findall(r"#g-([a-z0-9-]+)", texto))
    n = 0
    for gid, pat in COMP:
        if gid not in glos_ids or gid in usados:
            continue
        for c, k in bloques:
            html = c[k]
            if not isinstance(html, str):
                continue
            nuevo, ok = _uno(html, pat, gid)
            if ok:
                c[k] = nuevo
                usados.add(gid)
                n += 1
                break
    return n


def enlazar_todo(obras, personas, epocas, articulos, glos_ids):
    total = 0
    for o in obras:
        b = [(x, "h") for x in o.get("partes", [])] + [(x, "txt") for x in o.get("escucha", [])] + [(x, "h") for x in o.get("secciones", [])]
        total += enlazar_pagina(b, glos_ids)
    for p in personas:
        b = [(p, "h")] if p.get("h") else []
        if p.get("huella"):
            b += [(p["huella"], i) for i in range(len(p["huella"]))]
        total += enlazar_pagina(b, glos_ids)
    for e in epocas:
        b = [(e, "h")] if e.get("h") else []
        if e.get("rasgos"):
            b += [(e["rasgos"], i) for i in range(len(e["rasgos"]))]
        total += enlazar_pagina(b, glos_ids)
    for a in articulos:
        total += enlazar_pagina([(a, "h")], glos_ids)
    return total
