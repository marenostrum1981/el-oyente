# El Oyente: instrucciones para Claude

## Qué es

Un diario web para aprender a escuchar música clásica. Cada día entra una obra nueva con su ficha y, a la vez, crecen los índices de compositores, intérpretes y épocas, la escuela (artículos de fundamentos) y el glosario. Está publicado en Netlify (`https://el-oyente.netlify.app`), que vuelve a publicar la web sola con cada push a `main`, y se instala como app (PWA). Lo leen principiantes hispanohablantes.

## Estructura

- `index.html`: la app completa (una sola página, con rutas por hash). Rutas: `#portada`, `#obras`, `#o-ID`, `#compositores`, `#c-ID`, `#interpretes`, `#i-ID`, `#epocas`, `#e-ID`, `#escuela`, `#a-ID`, `#glosario` y `#g-ID`.
- `src/obras.py`, `src/personas.py` y `src/escuela.py`: **la fuente de verdad** del contenido. Se edita aquí.
- `src/build_data.py`: genera `data/*.json` y comprueba todos los enlaces internos (`#o-…`, `#c-…`, `#g-…`…). Si algo apunta a un id que no existe, falla.
- `data/*.json`: archivos generados. No se editan a mano.
- `manifest.webmanifest`, `sw.js` e `icons/`: la parte de app instalable. Si cambias `index.html` o los iconos, sube la versión de `CACHE` en `sw.js` (`oyente-v1` → `oyente-v2`…).

## Flujo diario: «Obra del día: <enlace o título>»

1. **Identifica la grabación.** Título, intérpretes y capítulos del vídeo. Si YouTube no deja leer la página, el título sale de `https://www.youtube.com/oembed?url=<url>&format=json`.
2. **Investiga con fuentes**, con una búsqueda por tema: vida del compositor en ese momento, para quién y por qué escribió la obra, plantilla, estructura, intérprete, otras grabaciones y curiosidades. Nada sale de memoria sin comprobarlo.
3. **Añade la obra al final de `OBRAS`** en `src/obras.py`, con el número siguiente en `n`, la fecha de hoy y `origen="Obra del día"` (u `"Obra de concierto"`). Copia la forma de las entradas que ya hay:
   - `id`: identificador corto en minúsculas y con guiones.
   - `compositor`: id de una persona.
   - `epoca`: `renacimiento`, `barroco`, `clasicismo`, `romanticismo` o `siglo-xx`.
   - `anio`: un año numérico para la línea del tiempo.
   - `grabacion`: `titulo`, `fuente`, `url` y `nota`.
   - `escucha`: la guía de escucha (paso 4).
   - `secciones`: lista de `{t, h}`, con HTML dentro de `h`.
   - `versiones`: lista de `{p}` (id de persona) o `{quien}`, con `det`, `nota` y `url` opcional.
   - `idagio`: texto para buscar la obra en Idagio.
   - `interpretes` y `conceptos`: ids de personas y de términos del glosario.
4. **Guía de escucha.**
   - Si el vídeo tiene capítulos, pon `t` en segundos, sacados de esos capítulos.
   - Si no los tiene, quita `t` y usa `cuando` (`"1"`, `"2"`…) con los pasos en orden.
   - **Nunca inventes minutos.** La app construye sola los enlaces `youtu.be/ID?t=SEG`.
5. **Personas.** Si el compositor o los intérpretes no existen, añádelos en `src/personas.py`:
   - Compositores: `tipo="compositor"`, `nace`, `epoca`, `claves` y una `ruta` de escucha.
   - Intérpretes: `tipo="solista"` o `"conjunto"` y `rol`. Si es un conjunto, `dirige` con la lista de directores.
6. **Glosario.** Añade a `GLOSARIO` en `src/escuela.py` cada término nuevo que use la ficha y enlázalo en `conceptos`.
7. **Épocas.** Si es la primera obra de una época, completa su `h` y sus `rasgos` con fuentes.
8. **Curiosidades.** Añade una o dos nuevas y comprobadas a `CURIOSIDADES`. Si escribes un artículo nuevo en `ARTICULOS`, puedes ponerlo en portada con `DESTACADO`.
9. **Genera y valida:** `python3 src/build_data.py`. Tiene que terminar sin errores.
10. **Comprueba en el navegador:** lanza `python3 -m http.server` y abre `#o-ID` y la portada, a ancho de móvil y de escritorio.
11. **Publica:** `git add -A && git commit -m "N.º X: Título" && git push`. Netlify publica la web nueva en un minuto.
12. **Responde en el chat** en 3 a 5 líneas: qué obra es, una idea clave para escucharla y qué se ha añadido al diario.

## Reglas de contenido

- Español de España, claro, para principiantes. Al lector se le tutea. Nada personal: ni nombres ni «tu amiga».
- Todo dato, comprobado en fuentes. Si hay duda, no se afirma. Se redacta con palabras propias, sin copiar textos.
- **Nunca sonidos sintetizados ni MIDI.** Solo grabaciones reales: YouTube, Idagio o la web del intérprete.
- Versiones para comparar: solo grabaciones que existan y estén comprobadas. Se enlazan únicamente si el enlace existe.
- Orden recomendado de secciones: «Quién era X cuando la escribió», «Para quién», «El instrumento» o «Quién la toca», «Cómo está hecha», «Cómo reconocer aquí el [época]», «[Intérprete] y esta grabación», «Curiosidades» y «Para el concierto».
- HTML permitido en los textos: `<p>`, `<b>`, `<i lang="…">`, `<a href="#…">`, `<ul>`, `<ol>`, `<li>` y `<blockquote>`.

## Publicación

- Repositorio: `marenostrum1981/el-oyente`, rama `main`.
- Netlify (proyecto `el-oyente`) está enlazado al repositorio: cada push a `main` publica `https://el-oyente.netlify.app`. No hay paso de build; `netlify.toml` publica la raíz tal cual.
- `data/*.json` se sube al repositorio ya generado.
