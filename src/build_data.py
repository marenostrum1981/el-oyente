import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from obras import OBRAS
from personas import PERSONAS
from escuela import EPOCAS, ARTICULOS, GLOSARIO, CURIOSIDADES, DESTACADO
from imagenes import IMAGENES
from ejemplos import EJEMPLOS
from referencias import REFERENCIAS
out = Path(__file__).resolve().parent.parent / "data"; out.mkdir(parents=True, exist_ok=True)
# imágenes: se añaden a cada obra, persona y época por su id
for lista, clave in ((OBRAS, "obras"), (PERSONAS, "personas"), (EPOCAS, "epocas")):
    for x in lista:
        if x["id"] in IMAGENES[clave]: x["imagen"] = IMAGENES[clave][x["id"]]
glos = [dict(id=i, termino=t, def_=d) for i,t,d in GLOSARIO]
for g in glos: g["def"] = g.pop("def_")
for g in glos:
    if g["id"] in EJEMPLOS: g["ejemplos"] = EJEMPLOS[g["id"]]
# integridad: ids referenciados
P = {p["id"] for p in PERSONAS}; G = {g["id"] for g in glos}; E = {e["id"] for e in EPOCAS}; A={a["id"] for a in ARTICULOS}; O={o["id"] for o in OBRAS}
errs = []
for clave, ids in (("obras", O), ("personas", P), ("epocas", E)):
    for k, im in IMAGENES[clave].items():
        if k not in ids: errs.append(("imagen", clave, k))
        if not im.get("archivo") or not im.get("pie") or not im.get("alt"): errs.append(("imagen incompleta", k))
for o in OBRAS:
    if not o.get("titulo_original") or not o.get("partes"): errs.append(("falta 'cómo leer el título'", o["id"]))
    if o["compositor"] not in P: errs.append(("compositor", o["id"]))
    if o["epoca"] not in E: errs.append(("epoca", o["id"]))
    for c in o.get("conceptos", []):
        if c not in G: errs.append(("concepto", c))
    for i in o.get("interpretes", []):
        if i not in P: errs.append(("interprete", i))
    for v in o.get("versiones", []):
        if v.get("p") and v["p"] not in P: errs.append(("version", v["p"]))
import re
alltext = json.dumps([OBRAS, PERSONAS, EPOCAS, ARTICULOS, glos, CURIOSIDADES], ensure_ascii=False)
for kind, ident in re.findall(r'#([ocieag])-([a-z0-9-]+)', alltext):
    ok = {"o":O,"c":P,"i":P,"e":E,"a":A,"g":G}[kind]
    if ident not in ok: errs.append(("link", kind+"-"+ident))
# ejemplos para escuchar: obra existente y segundo = inicio de un capítulo real (o 0)
CAP = {o["id"]: {x["t"] for x in o.get("escucha", []) if x.get("t") is not None} | {0} for o in OBRAS}
for gid, lista in EJEMPLOS.items():
    if gid not in G: errs.append(("ejemplo de término inexistente", gid))
    for e in lista:
        if "o" in e and e["o"] not in O: errs.append(("ejemplo: obra", gid, e["o"]))
        elif "o" in e and e.get("t") is not None and e["t"] not in CAP[e["o"]]: errs.append(("ejemplo: segundo sin capítulo", gid, e["o"], e["t"]))
        if not e.get("txt"): errs.append(("ejemplo sin texto", gid))
for g in glos:
    if g["id"] not in EJEMPLOS: print("aviso: término sin ejemplo:", g["id"])
alltext2 = json.dumps([OBRAS, PERSONAS, EPOCAS, ARTICULOS, glos, CURIOSIDADES, EJEMPLOS], ensure_ascii=False)
for oid, seg in re.findall(r'#o-([a-z0-9-]+)@([0-9]+)', alltext2):
    if oid not in O or int(seg) not in CAP[oid]: errs.append(("enlace de escucha sin capítulo", oid, seg))
X = REFERENCIAS
for gid, lista in EJEMPLOS.items():
    for e in lista:
        if "x" in e and (e["x"] not in X or (e.get("t") and e["t"] not in X[e["x"]]["caps"])): errs.append(("ejemplo: referencia", gid, e["x"], e.get("t")))
for xid, seg in re.findall(r'#x-([a-z0-9-]+)(?:@([0-9]+))?', alltext2):
    if xid not in X or (seg and int(seg) not in X[xid]["caps"]): errs.append(("enlace a referencia", xid, seg))
for xid, r in X.items():
    if r.get("ini") and r["ini"] not in r["caps"]: errs.append(("referencia: ini sin capítulo", xid))
for o in OBRAS:
    for c in o.get("contexto", []):
        if not c.get("anio") or not c.get("txt"): errs.append(("contexto incompleto", o["id"]))
    for v in [o["grabacion"]] + o.get("versiones", []):
        if v.get("dur") and not re.fullmatch(r"\d{1,2}:\d{2}", v["dur"]): errs.append(("duración mal escrita", o["id"], v["dur"]))
for pe in PERSONAS:
    for x in pe.get("especialistas", []):
        if x.get("p") and x["p"] not in P: errs.append(("especialista", pe["id"], x["p"]))
        if not x.get("p") and not x.get("quien"): errs.append(("especialista sin nombre", pe["id"]))
    if pe.get("bachtrack") and not re.fullmatch(r"[a-z0-9-]+", pe["bachtrack"]): errs.append(("slug de Bachtrack", pe["id"]))
if DESTACADO not in A: errs.append(("destacado", DESTACADO))
if errs: print("ERRORES:", errs); sys.exit(1)
(out/"obras.json").write_text(json.dumps(OBRAS, ensure_ascii=False, indent=0))
(out/"personas.json").write_text(json.dumps(PERSONAS, ensure_ascii=False, indent=0))
(out/"escuela.json").write_text(json.dumps(dict(epocas=EPOCAS, articulos=ARTICULOS, glosario=glos, curiosidades=CURIOSIDADES, destacado=DESTACADO, referencias={k: dict(v, caps={str(s): n for s, n in v['caps'].items()}) for k, v in REFERENCIAS.items()}), ensure_ascii=False, indent=0))
for f in out.iterdir(): print(f.name, f.stat().st_size)
