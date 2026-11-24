# El Oyente: instrucciones para Claude

## Qué es

Un diario web para aprender a escuchar música clásica. Cada día entra una obra nueva con su ficha y, a la vez, crecen los índices de compositores, intérpretes y épocas, la escuela (artículos de fundamentos) y el glosario. Está publicado en Netlify, en `https://el-oyente.com` (dominio comprado en Netlify; `el-oyente.netlify.app` sigue funcionando y lleva al dominio principal), y Netlify vuelve a publicar la web sola con cada push a `main`, y se instala como app (PWA). Lo leen principiantes hispanohablantes.

## Estructura

- `index.html`: la app completa (una sola página, con rutas por hash). Rutas: `#portada`, `#obras`, `#o-ID`, `#compositores`, `#c-ID`, `#interpretes`, `#i-ID`, `#epocas`, `#e-ID`, `#escuela`, `#a-ID`, `#glosario`, `#g-ID` y `#conciertos` (admite `?c=<slug>` o `?i=<slug>` para llegar con un filtro puesto).
- `src/obras.py`, `src/personas.py` y `src/escuela.py`: **la fuente de verdad** del contenido. Se edita aquí.
- `src/build_data.py`: genera `data/*.json` y comprueba todos los enlaces internos (`#o-…`, `#c-…`, `#g-…`…). Si algo apunta a un id que no existe, falla.
- `src/ejemplos.py`: ejemplos para escuchar cada término del glosario.
- `src/referencias.py`: obras de fuera del diario que se mencionan, con su grabación comprobada.
- `src/imagenes.py`: imágenes de obras, compositores y épocas (Wikimedia Commons). `build_data.py` las añade a cada ficha.
- `data/*.json`: archivos generados. No se editan a mano.
- Conciertos: la app no guarda conciertos; construye búsquedas en la agenda de Bachtrack (`https://bachtrack.com/es_ES/search-events/…`) con filtros comprobados: `composer=`, `performer=`, `country=` (nombre en inglés: `spain`, `united-kingdom`…), `city=` (en inglés: `seville`, `palma-de-mallorca`…), `datefrom=AAAAMMDD;datespan=N` y `medium=2` (vídeo). Los filtros se separan con `;`.
- Visitas: GoatCounter (`https://el-oyente.goatcounter.com`, sin cookies). El script no cuenta solo (`no_onload`): la app llama a `contar()` en cada ruta (`/o-ID`, `/c-ID`, `/conciertos`…; la portada es `/`) y solo en el dominio `el-oyente.com`, nunca en local. También cuenta eventos: `escucha/o-ID@SEG`, `escucha/x-ID`, `escucha/yt-ID` y `conciertos/<filtros>` al abrir Bachtrack. El título de la pestaña es el `h1` de cada página.
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
   - `versiones`: lista de `{p}` (id de persona) o `{quien}`, con `det`, `nota` y `url` opcional. Añade `dur="m:ss"` (también en `grabacion`) cuando la duración del movimiento esté comprobada (ficha del sello o de la plataforma, o capítulos del vídeo). Con tres o más duraciones, la ficha dibuja el gráfico «La misma música, distinto tempo».
   - `contexto`: de 3 a 5 hechos comprobados de lo que pasaba alrededor (música, sociedad, técnica, vida del compositor), `dict(anio="1725", txt=…)`. Salen en el recuadro «Mientras tanto, en el mundo». Si nombran una obra, que se pueda escuchar.
   - `idagio`: texto para buscar la obra en Idagio.
   - `interpretes` y `conceptos`: ids de personas y de términos del glosario.
   - `titulo_original` y `partes` (**obligatorio**): el título tal como sale en YouTube o Idagio (normalmente en inglés) y su desglose, parte por parte: tipo de obra, número, plantilla, tonalidad (con la letra de la nota), catálogo u opus (qué significa y si el número agrupa varias piezas) y apodo. Cada parte es `dict(p=<fragmento original>, es=<en español>, h=<explicación para principiantes>)`. Responde a las dudas típicas: ¿qué es el n.º?, ¿se podría tocar en otra tonalidad?, ¿cuántas piezas hay en ese opus?
4. **Guía de escucha.**
   - Si el vídeo tiene capítulos, pon `t` en segundos, sacados de esos capítulos.
   - Si no los tiene, quita `t` y usa `cuando` (`"1"`, `"2"`…) con los pasos en orden.
   - **Nunca inventes minutos.** La app construye sola los enlaces `youtu.be/ID?t=SEG`.
5. **Personas.** Si el compositor o los intérpretes no existen, añádelos en `src/personas.py`:
   - Compositores: `tipo="compositor"`, `nace`, `epoca`, `claves`, una `ruta` de escucha, `huella` (3 o 4 rasgos para reconocerlo de oído, cada uno con un enlace para escuchar), `especialistas` (intérpretes de referencia comprobados: `{p}` o `{quien}`, con `det`, `nota` y `url` opcional; `especialistas_intro` opcional) y `bachtrack` (slug comprobado: la cabecera de `https://bachtrack.com/es_ES/search-events/composer=<slug>` tiene que mostrar su nombre).
   - Intérpretes: `tipo="solista"`, `"director"` o `"conjunto"` y `rol`. Si es un conjunto, `dirige` con la lista de directores. Si actúa hoy, `bachtrack` con su slug comprobado en `performer=<slug>` (por ejemplo, la Netherlands Bach Society es `nederlandse-bachvereniging`).
6. **Glosario.** Añade a `GLOSARIO` en `src/escuela.py` cada término nuevo que use la ficha y enlázalo en `conceptos`.
7. **Épocas.** Si es la primera obra de una época, completa su `h` y sus `rasgos` con fuentes.
8. **Curiosidades.** Añade una o dos nuevas y comprobadas a `CURIOSIDADES`. Si escribes un artículo nuevo en `ARTICULOS`, puedes ponerlo en portada con `DESTACADO`.
9. **Imágenes y vídeo.**
   - En `src/imagenes.py` añade una imagen para la obra (y el retrato del compositor si es nuevo): solo archivos de **Wikimedia Commons** de dominio público o CC0, comprobados en su página (autor, fecha, colección, licencia). `archivo` es el nombre exacto del archivo; `pie` explica qué se ve y por qué está ahí; `alt` lo describe.
   - Mejor una portada de primera edición, un manuscrito, el instrumento o un cuadro de la época que una imagen decorativa. **Nunca fotos de intérpretes vivos.**
   - El vídeo se incrusta solo en la ficha. Comprueba que se puede incrustar con `https://www.youtube.com/oembed?url=<url>&format=json` (si da error, la ficha mostrará solo el botón a YouTube).
10. **Genera y valida:** `python3 src/build_data.py`. Tiene que terminar sin errores.
11. **Comprueba en el navegador:** lanza `python3 -m http.server` y abre `#o-ID` y la portada, a ancho de móvil y de escritorio.
12. **Publica:** `git add -A && git commit -m "N.º X: Título" && git push`. Netlify publica la web nueva en un minuto.
13. **Responde en el chat** en 3 a 5 líneas: qué obra es, una idea clave para escucharla y qué se ha añadido al diario.

## Reglas de contenido

- Español de España, claro, para principiantes. Al lector se le tutea. Nada personal: ni nombres ni «tu amiga».
- Todo dato, comprobado en fuentes. Si hay duda, no se afirma. Se redacta con palabras propias, sin copiar textos.
- **Nunca sonidos sintetizados ni MIDI.** Solo grabaciones reales: YouTube, Idagio o la web del intérprete.
- Versiones para comparar: solo grabaciones que existan y estén comprobadas. Se enlazan únicamente si el enlace existe.
- Orden recomendado de secciones: «Quién era X cuando la escribió», «Para quién», «El instrumento» o «Quién la toca», «Cómo está hecha», «Cómo reconocer aquí el [época]», «[Intérprete] y esta grabación», «Curiosidades», «Cómo saborearla: cuatro escuchas» y «Para el concierto».
- «Cómo saborearla»: un plan de 3 o 4 escuchas, cada una buscando una sola cosa (dejarse llevar, seguir un tema o un instrumento, el tempo, comparar versiones), con enlaces a momentos concretos y una obra para seguir después.
- **Todo con ejemplos que se oigan.** Cada término del glosario lleva ejemplos en `src/ejemplos.py`, y cada explicación (artículos, rasgos de época, fichas) señala un momento concreto para escuchar. Los enlaces de escucha son `#o-ID@SEG` (un momento de una obra del diario: `SEG` tiene que ser el inicio de un capítulo de su `escucha`, o 0) y `#x-ID` o `#x-ID@SEG` (una obra de fuera del diario, registrada en `src/referencias.py`). Suenan en un reproductor flotante sin salir de la página. `build_data.py` rechaza segundos que no sean capítulos.
- **Si mencionas una obra, que se pueda escuchar.** Una obra del diario se enlaza con `#o-ID`; una de fuera se añade a `src/referencias.py` con una grabación real de un canal fiable (orquesta, sello, institución), comprobada con oEmbed, y se enlaza con `#x-ID`. Si el vídeo trae más cosas antes, pon `ini=<segundo>` (debe estar en `caps`) para que empiece donde toca. En las rutas de escucha y versiones, un enlace de YouTube de un vídeo concreto suena aquí mismo; evita enlaces de búsqueda.
- HTML permitido en los textos: `<p>`, `<b>`, `<i lang="…">`, `<a href="#…">`, `<ul>`, `<ol>`, `<li>` y `<blockquote>`.

## Publicación

- Repositorio: `marenostrum1981/el-oyente`, rama `main`.
- Netlify (proyecto `el-oyente`) está enlazado al repositorio: cada push a `main` publica `https://el-oyente.com`. El dominio y su DNS se gestionan en Netlify (Domains); el certificado HTTPS lo pone Netlify solo. No hay paso de build; `netlify.toml` publica la raíz tal cual.
- `data/*.json` se sube al repositorio ya generado.
