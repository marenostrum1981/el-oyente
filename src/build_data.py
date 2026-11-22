import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from obras import OBRAS
from personas import PERSONAS
from escuela import EPOCAS, ARTICULOS, GLOSARIO, CURIOSIDADES, DESTACADO
from imagenes import IMAGENES
out = Path(__file__).resolve().parent.parent / "data"; out.mkdir(parents=True, exist_ok=True)
# imágenes: se añaden a cada obra, persona y época por su id
for lista, clave in ((OBRAS, "obras"), (PERSONAS, "personas"), (EPOCAS, "epocas")):
    for x in lista:
        if x["id"] in IMAGENES[clave]: x["imagen"] = IMAGENES[clave][x["id"]]
glos = [dict(id=i, termino=t, def_=d) for i,t,d in GLOSARIO]
for g in glos: g["def"] = g.pop("def_")
# integridad: ids referenciados
P = {p["id"] for p in PERSONAS}; G = {g["id"] for g in glos}; E = {e["id"] for e in EPOCAS}; A={a["id"] for a in ARTICULOS}; O={o["id"] for o in OBRAS}
errs = []
for clave, ids in (("obras", O), ("personas", P), ("epocas", E)):
    for k, im in IMAGENES[clave].items():
        if k not in ids: errs.append(("imagen", clave, k))
        if not im.get("archivo") or not im.get("pie") or not im.get("alt"): errs.append(("imagen incompleta", k))
for o in OBRAS:
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
if DESTACADO not in A: errs.append(("destacado", DESTACADO))
if errs: print("ERRORES:", errs); sys.exit(1)
(out/"obras.json").write_text(json.dumps(OBRAS, ensure_ascii=False, indent=0))
(out/"personas.json").write_text(json.dumps(PERSONAS, ensure_ascii=False, indent=0))
(out/"escuela.json").write_text(json.dumps(dict(epocas=EPOCAS, articulos=ARTICULOS, glosario=glos, curiosidades=CURIOSIDADES, destacado=DESTACADO), ensure_ascii=False, indent=0))
for f in out.iterdir(): print(f.name, f.stat().st_size)
