# Fichas de obras del diario. Cada obra nueva se añade al final con n = siguiente número.
VOM = "https://youtu.be/aryDMAP6oug"
MAISKY2 = "https://youtu.be/K37tJVbxPG0"
from pathlib import Path as _P
SONETOS = (_P(__file__).parent/"sonetos.html").read_text()

OBRAS = [
dict(
 id="cuatro-estaciones", n=1, fecha="2026-11-21", origen="Obra de concierto",
 titulo="Las Cuatro Estaciones", subtitulo="Le quattro stagioni", compositor="vivaldi",
 fechaComp="Compuestas hacia 1718–1723; publicadas en 1725", anio=1725, epoca="barroco",
 genero="Concierto para violín (cuatro conciertos)", plantilla="Violín solista, cuerdas y bajo continuo",
 tonalidad="Mi mayor · Sol menor · Fa mayor · Fa menor", catalogo="Op. 8 n.º 1–4 · RV 269, 315, 293, 297",
 titulo_original="Le quattro stagioni · Il cimento dell'armonia e dell'inventione, Op. 8 n.º 1–4 · RV 269, 315, 293, 297",
 partes=[
  dict(p="Le quattro stagioni", es="Las cuatro estaciones", h="Más que una obra, son <b>cuatro conciertos para violín</b>, uno por estación, de tres movimientos cada uno: doce en total. Ver <a href=\"#g-concierto\">concierto</a>."),
  dict(p="Il cimento dell'armonia e dell'inventione", es="El desafío entre la armonía y la invención", h="El nombre de la <b>colección de doce conciertos</b> que Vivaldi publicó en Ámsterdam en 1725. Las estaciones son los cuatro primeros; los otros ocho son conciertos distintos."),
  dict(p="Op. 8 n.º 1–4", es="Opus 8, números 1 a 4", h="<b>Opus</b> es «obra» en latín. La portada dice <i lang=\"it\">opera ottava</i>, «obra octava»: el número que recibió la colección al publicarse. Aquí un solo opus reúne <b>doce conciertos</b>, así que cada uno lleva además su propio número: la Primavera es el <b>Op. 8 n.º 1</b> y el Invierno, el n.º 4. Ver <a href=\"#g-opus\">opus</a>."),
  dict(p="RV 269, 315, 293, 297", es="Catálogo Ryom", h="Los números del <b>catálogo de Peter Ryom</b> (<i lang=\"de\">Ryom-Verzeichnis</i>), que identifica cada obra de Vivaldi. Primavera es RV 269; Verano, RV 315; Otoño, RV 293, e Invierno, RV 297. Fíjate en que no van en orden: el catálogo no sigue el de las estaciones."),
  dict(p="E major · G minor · F major · F minor", es="mi mayor · sol menor · fa mayor · fa menor", h="Cada concierto tiene su <b>tonalidad</b>. Primavera y otoño, en mayor, suenan luminosos; verano e invierno, en menor, más sombríos y tensos. En inglés las notas van con letras: E es mi, G es sol y F es fa. Ver <a href=\"#g-tonalidad\">tonalidad</a>."),
 ],
 duracion="Unos 40 minutos, en 12 movimientos",
 entradilla="Cuatro conciertos para violín que cuentan el año con un soneto como guion. Vivaldi escribió en la partitura lo que pinta cada pasaje: pájaros, tormentas, un perro que ladra o el hielo que se rompe.",
 grabacion=dict(titulo="Voices of Music, con instrumentos de época", fuente="Vídeo completo en YouTube. Con el botón CC aparece el soneto como subtítulos, en italiano o en inglés.", url=VOM,
  nota="Los minutos salen de los capítulos del vídeo. Solistas: Alana Youssefian (Primavera), Cynthia Miller Freivogel (Verano e Invierno) y Carla Moore (Otoño)."),
 escucha=[
  dict(mov="Primavera · I. Allegro", t=0, txt="Llega la primavera: estribillo alegre del grupo y, entre medias, pájaros con trinos, fuentes que murmuran y una tormenta. Después de la tormenta, el estribillo vuelve en menor."),
  dict(mov="Primavera · II. Largo", t=212, txt="El cabrero duerme. Los violines susurran como hojas, el solista canta tranquilo y la viola ladra: dos notas fuertes y ásperas, una y otra vez."),
  dict(mov="Primavera · III. Allegro", t=373, txt="Danza pastoral. Notas graves que no se mueven imitan el bordón de una zampoña."),
  dict(mov="Verano · I. Allegro non molto", t=609, txt="Calor que agota: frases cortadas por silencios. Luego cantan el cuco, la tórtola y el jilguero, sopla la brisa y de golpe llega el viento del norte."),
  dict(mov="Verano · II. Adagio – Presto", t=931, txt="El pastor no puede descansar: moscas zumbando en los violines y truenos del grupo, cada vez más cerca."),
  dict(mov="Verano · III. Presto", t=1066, txt="Estalla la tempestad. El granizo destroza el trigo: notas repetidas rapidísimas y escalas como latigazos."),
  dict(mov="Otoño · I. Allegro", t=1242, txt="Fiesta de la vendimia. Un borracho (el solista) se tambalea con trinos y saltos hasta quedarse dormido."),
  dict(mov="Otoño · II. Adagio molto", t=1574, txt="Los borrachos duermen. Cuerdas con sordina y el clave desgranando acordes."),
  dict(mov="Otoño · III. Allegro", t=1705, txt="La cacería al amanecer: los violines imitan los cuernos de caza, la fiera huye y cae."),
  dict(mov="Invierno · I. Allegro non molto", t=1916, txt="Tiritar en la nieve: notas repetidas que chocan, ráfagas de viento, pisotones y dientes que castañean."),
  dict(mov="Invierno · II. Largo", t=2129, txt="Junto al fuego mientras llueve: los violines en pizzicato son la lluvia y el solista, la calma de casa."),
  dict(mov="Invierno · III. Allegro", t=2245, txt="Caminar sobre el hielo con miedo, resbalar, caer, correr hasta que el hielo se rompe. Al final, todos los vientos en guerra."),
 ],
 secciones=[
  dict(t="Quién era Vivaldi cuando la escribió", h="""<p>Antonio Vivaldi era un violinista veneciano, sacerdote y profesor del <b>Ospedale della Pietà</b>, una institución que acogía a niños abandonados y cuyas alumnas formaban un conjunto musical famoso. Buena parte de su música se escribió para ellas. Cuando compuso las Estaciones, hacia 1718–1723, sus conciertos ya se imprimían en Ámsterdam y se estudiaban fuera de Italia: Bach los copió y transcribió en 1713–1714.</p>
<p>En 1725 el editor Michel-Charles Le Cène las publicó en Ámsterdam como los cuatro primeros de un libro de doce conciertos, el Opus 8, con un título muy suyo: <i lang="it">Il cimento dell'armonia e dell'inventione</i>, «el desafío entre la armonía y la invención».</p>"""),
  dict(t="Para quién", h="""<p>El Opus 8 está dedicado al conde bohemio <b>Wenzel von Morzin</b>, consejero del emperador Carlos VI. En la carta de dedicatoria Vivaldi se presenta como su «maestro en Italia» y reconoce que el conde ya conocía versiones anteriores de las Estaciones: la obra circulaba antes de imprimirse.</p>"""),
  dict(t="Quién la toca", h="""<p>Un <b>violín solista</b> frente a un grupo de cuerda (violines primeros y segundos, violas) y, debajo de todo, el <b>bajo continuo</b>: violonchelo y contrabajo con un instrumento de acordes, normalmente el clave. El continuo no para nunca: es el suelo armónico de toda la música barroca.</p>
<p>En el vídeo de referencia tocan con instrumentos de época. Cómo reconocerlos a simple vista, en el artículo <a href="#a-instrumentos-epoca">Instrumentos de época</a>.</p>"""),
  dict(t="Cómo está hecha", h="""<p>Son cuatro conciertos y cada uno tiene <b>tres movimientos: rápido, lento y rápido</b>. Los rápidos siguen la <a href="#g-ritornello">forma ritornello</a>: el grupo repite un estribillo y, entre estribillo y estribillo, el solista cuenta una escena.</p>
<p>El truco que lo hace único es el guion. Cada concierto llevaba un <b>soneto</b>, y en la parte del violín solista unas letras enlazaban cada verso con el pasaje que lo cuenta. Además, Vivaldi escribió rótulos sobre las notas, como <i lang="it">Il cane che grida</i> («el perro que ladra») en la parte de la viola o <i lang="it">La pioggia</i> («la lluvia»). A esto se le llama <a href="#g-musica-programatica">música programática</a>.</p>"""),
  dict(t="Los sonetos", h=SONETOS),
  dict(t="Cómo reconocer aquí el Barroco", h="""<ul>
<li><b>El continuo:</b> si escuchas con atención, el clave está siempre ahí, rellenando acordes.</li>
<li><b>El ritmo que no se detiene:</b> los movimientos rápidos avanzan como un motor.</li>
<li><b>Solo contra tutti:</b> todo el grupo con el estribillo, el solista con las escenas.</li>
<li><b>Dinámica en bloques:</b> pasa de fuerte a suave de golpe, como un eco, más que con crescendos largos.</li>
</ul>
<p>Si te parece que Vivaldi «tiene una sola voz» y eso no casa con el Barroco, lee <a href="#a-vivaldi-barroco">¿Por qué Vivaldi es barroco?</a></p>"""),
  dict(t="Curiosidades", h="""<ul>
<li>Le llamaban <i lang="it">il prete rosso</i>, «el cura rojo», por su pelo pelirrojo.</li>
<li>Vivaldi murió pobre en Viena en 1741 y su música cayó en el olvido. Su vuelta en el siglo XX la empujó precisamente la popularidad de las Estaciones, grabadas por primera vez en 1947.</li>
<li>La grabación de Nigel Kennedy de 1989 vendió más de dos millones de copias y fue el disco clásico más vendido de su época.</li>
<li>Il Giardino Armonico la grabó en 1994 con una pintura de escenas tan extrema que un crítico describió su perro como un rottweiler desafinado.</li>
</ul>"""),
  dict(t="Cómo saborearla: cuatro escuchas", h="""<p>Una obra se disfruta más cuando vuelves a ella buscando cada vez una cosa distinta. Prueba este plan con la Primavera, que dura unos diez minutos.</p>
<ol>
<li><b>Primera escucha: déjate llevar.</b> Pon la <a href="#o-cuatro-estaciones@0">Primavera</a> entera sin leer nada. Al terminar, pregúntate qué imagen te ha quedado de cada movimiento.</li>
<li><b>Segunda escucha: con el soneto.</b> Lee la primera estrofa del soneto y vuelve a empezar. Busca los pájaros, las fuentes y la tormenta. En el <a href="#o-cuatro-estaciones@212">Largo</a>, fíjate solo en la viola: es el perro que ladra mientras el cabrero duerme.</li>
<li><b>Tercera escucha: sigue al grupo, no al solista.</b> En el <a href="#o-cuatro-estaciones@0">primer movimiento</a>, cuenta cuántas veces vuelve el estribillo del grupo. Ese regreso es el <a href="#g-ritornello">ritornello</a>, la columna de la obra.</li>
<li><b>Cuarta escucha: compara.</b> Elige una versión de «Otras versiones» y escucha el mismo arranque. ¿Más rápido o más lento? ¿Más adornos? ¿Más violento?</li>
</ol>
<p>Cuando la tengas dominada, haz lo mismo con el <a href="#o-cuatro-estaciones@1916">Invierno</a>: es la estación con escenas más fáciles de oír.</p>"""),
 dict(t="Para el concierto", h="""<ol>
<li>Lee el soneto de la estación antes de que empiece: sabrás qué pasa en cada movimiento.</li>
<li>Cuenta: rápido, lento, rápido. La costumbre es aplaudir al acabar cada concierto, no entre movimientos.</li>
<li>Si entra todo el grupo con el tema, es el estribillo. Si el solista se queda casi solo, es una escena.</li>
<li>Elige un instrumento, la viola o el clave, y síguelo un minuto entero.</li>
</ol>"""),
 ],
 contexto=[
  dict(anio="1721", txt="Bach envía al margrave de Brandeburgo seis conciertos. El margrave coleccionaba conciertos, sobre todo italianos. <a href=\"#x-bwv-1048\">Escucha el n.º 3</a>."),
  dict(anio="1723", txt="Bach se instala en Leipzig como cantor de Santo Tomás: tendrá que dar música a las iglesias de la ciudad cada domingo."),
  dict(anio="1725", txt="En Viena, Johann Joseph Fux publica en latín <i lang=\"la\">Gradus ad Parnassum</i>, un manual de contrapunto."),
  dict(anio="1725", txt="En Leipzig, Bach estrena para la fiesta de la Anunciación la cantata que hoy lleva el número 1 de su catálogo, <a href=\"#x-bwv-1\">BWV 1</a>."),
 ],
 versiones=[
  dict(p="voices-of-music", det="vídeo de referencia", nota="Instrumentos de época y el soneto como subtítulos.", url=VOM),
  dict(p="il-giardino-armonico", det="1994", nota="La versión que puso patas arriba la obra: escenas pintadas al extremo."),
  dict(p="europa-galante", det="1991", nota="Con Fabio Biondi. Recuperó un grupo del tamaño que probablemente tenía Vivaldi."),
  dict(p="carmignola", det="Venice Baroque Orchestra", nota="Con Andrea Marcon. Muy valorada por su poesía y su energía."),
  dict(p="kennedy", det="1989", nota="Con instrumentos modernos. El gran éxito de ventas."),
 ],
 idagio="Vivaldi Four Seasons",
 interpretes=["voices-of-music"],
 conceptos=["musica-programatica","concierto","movimiento","ritornello","tutti","bajo-continuo","clave","pizzicato","trino","tremolo","sordina","catalogo"],
),
dict(
 id="suite-chelo-2", n=2, fecha="2026-11-21", origen="Obra del día",
 titulo="Suite n.º 2 para violonchelo solo", subtitulo="en re menor", compositor="bach",
 fechaComp="Probablemente entre 1717 y 1723, en Köthen", anio=1720, epoca="barroco",
 genero="Suite", plantilla="Violonchelo solo", tonalidad="Re menor", catalogo="BWV 1008",
 titulo_original="Cello Suite No. 2 in D minor, BWV 1008",
 partes=[
  dict(p="Cello", es="para violonchelo solo", h="La <b>plantilla</b>: un solo instrumento, sin acompañamiento. La copia de Anna Magdalena Bach las titula «suites para violonchelo solo sin bajo»."),
  dict(p="Suite", es="Suite", h="El <b>tipo de obra</b>: una serie de danzas, con un preludio delante. Por eso la guía de escucha va danza a danza. Ver <a href=\"#g-suite\">suite</a>."),
  dict(p="No. 2", es="n.º 2", h="La <b>segunda de las seis suites</b> para violonchelo de Bach. En su catálogo van seguidas, de BWV 1007 a 1012."),
  dict(p="in D minor", es="en re menor", h="La <b>tonalidad</b>: la nota «casa» es el re (en inglés, <b>D</b>) y el modo es menor, de color sombrío. Todas las danzas de la suite giran en torno a ese re. Ver <a href=\"#g-tonalidad\">tonalidad</a>."),
  dict(p="BWV 1008", es="Catálogo de las obras de Bach", h="El número del <b>catálogo de las obras de Bach</b> (<i lang=\"de\">Bach-Werke-Verzeichnis</i>), que publicó Wolfgang Schmieder en 1950, dos siglos después de la muerte del compositor. No va por fechas sino <b>por géneros</b>: primero las cantatas (BWV 1 a 224) y, mucho más adelante, la música de cámara (BWV 1001 a 1040), donde están estas suites. Un número BWV bajo no quiere decir que la obra sea antigua."),
 ],
 duracion="Entre 20 y 25 minutos, según el intérprete",
 entradilla="Un solo violonchelo, casi siempre una nota cada vez, y sin embargo oyes melodía, bajo y armonía. Un preludio y cinco danzas en re menor: la primera de las dos suites en tonalidad menor.",
 grabacion=dict(titulo="Mischa Maisky", fuente="Vídeo en YouTube (canal Newmono), con capítulos en la descripción.", url=MAISKY2,
  nota="Maisky toca un Bach romántico, muy libre y lento: es una forma de tocarlo, no la única. Compáralo con las versiones de la columna."),
 escucha=[
  dict(mov="Preludio", t=16, txt="Empieza con tres notas que suben y te sitúan en re menor. Luego, un flujo continuo que crece hasta un clímax, un silencio breve y dramático y unos acordes largos para cerrar."),
  dict(mov="Allemande", t=278, txt="Danza alemana de paso moderado, noble y contenida. Los acordes frenan su avance."),
  dict(mov="Courante", t=527, txt="Rápida y nerviosa: la tensión de la allemande se convierte en energía inquieta."),
  dict(mov="Zarabanda", t=649, txt="La más honda, un lamento majestuoso. Su seña es el apoyo en el segundo tiempo: cuenta 1-2-3 y nota que el peso cae en el 2."),
  dict(mov="Minueto I", t=1048, txt="La danza de moda en la época. Se toca Minueto I, luego Minueto II y se vuelve al I."),
  dict(mov="Minueto II", t=1127, txt="Un respiro antes del final. Es uno de los pocos movimientos de las seis suites sin ningún acorde: solo una línea."),
  dict(mov="Giga", t=1256, txt="Saltos inquietos, casi diabólicos, y un final en un re agudo."),
 ],
 secciones=[
  dict(t="Contexto", h="""<p>Entre 1717 y 1723 Bach fue maestro de capilla del príncipe Leopold en <b>Köthen</b>. Era una corte calvinista, así que no necesitaba cantatas para la iglesia cada domingo y Bach se volcó en la música instrumental: los <i>Conciertos de Brandeburgo</i>, las suites para orquesta y las obras para violín solo y violonchelo solo.</p>
<p>No sabemos para quién escribió estas suites ni por qué. Obras para un instrumento solo, sin acompañamiento, eran muy raras en su tiempo: lo normal era improvisarlas, no escribirlas.</p>"""),
  dict(t="Cómo nos han llegado", h="""<p>El manuscrito original de Bach se ha perdido. Las conocemos por copias, sobre todo la de su segunda mujer, <b>Anna Magdalena Bach</b>, titulada <i lang="fr">Suites à Violoncello Solo senza Basso</i> («suites para violonchelo solo sin bajo»). Hay otra copia, algo anterior, de Johann Peter Kellner.</p>
<p>Esas copias apenas indican ligaduras, articulación ni matices. Por eso no hay una versión «correcta» y cada violonchelista las toca a su manera, como vas a comprobar con la zarabanda.</p>"""),
  dict(t="La idea clave: una línea que suena a varias voces", h="""<p>Aquí está la clave de por qué asociamos a Bach con «muchas voces». Con un instrumento que casi siempre toca una nota cada vez, Bach te hace oír varias. Lo consigue saltando entre registros: una nota grave, otra aguda, otra grave… y tu oído las separa en un bajo y una melodía que conversan. Se llama <a href="#g-polifonia-implicita">polifonía implícita</a>.</p>
<p>Escúchalo en el preludio: cuando los saltos se ensanchan, parece que tocan dos.</p>"""),
  dict(t="Cómo está hecha", h="""<p>Una <a href="#g-suite">suite</a> es un preludio seguido de danzas estilizadas, que ya no eran para bailar. Las seis suites tienen el mismo orden: preludio, allemande, courante, zarabanda, una pareja de danzas «de moda» (aquí, dos minuetos) y giga.</p>
<p>Cada danza viene de un sitio: la courante es francesa, la zarabanda española y la giga inglesa (de la <i>jig</i>). Así, una suite es también un pequeño viaje por Europa.</p>"""),
  dict(t="Maisky y la interpretación", h="""<p>Mischa Maisky toca un Bach romántico a propósito: suele decir que Bach fue «el mayor de los románticos». Se nota en los tempos. En este vídeo la zarabanda dura unos 6 minutos y medio; Yo-Yo Ma la graba en 5:08 y Alexander Kniazev se va a 8:15. La misma partitura da tres músicas distintas.</p>
<p>Ejercicio: escucha la zarabanda de Maisky y luego la de una versión con instrumentos de época, como la de la Netherlands Bach Society. Pregúntate qué cambia: ¿el tempo, el vibrato, el peso en el segundo tiempo?</p>"""),
  dict(t="Curiosidades", h="""<ul>
<li>Durante casi dos siglos se tomaron por ejercicios de estudio. Un chico de 13 años, <a href="#i-casals">Pau Casals</a>, encontró una edición vieja en una tienda de Barcelona en 1890 y acabó convirtiéndolas en obras de concierto.</li>
<li>Maisky decidió volver a grabar las suites al no reconocer su propia grabación de 1985 mientras sonaba en una tienda de alta fidelidad.</li>
<li>Hay quien defiende que las compuso Anna Magdalena y no Bach. Es una teoría minoritaria y muy discutida.</li>
</ul>"""),
  dict(t="Cómo saborearla: cuatro escuchas", h="""<p>Son siete movimientos cortos y un solo instrumento: perfecto para escucharla por capas.</p>
<ol>
<li><b>Primera escucha: solo el preludio.</b> Escucha el <a href="#o-suite-chelo-2@16">preludio</a> con los ojos cerrados y sigue la subida hasta el clímax, el silencio y los acordes finales.</li>
<li><b>Segunda escucha: las dos voces.</b> Vuelve al preludio y trata de oír dos líneas, una grave y otra aguda, que conversan. Es la <a href="#g-polifonia-implicita">polifonía implícita</a>.</li>
<li><b>Tercera escucha: las danzas.</b> Escucha seguidas la <a href="#o-suite-chelo-2@527">courante</a> y la <a href="#o-suite-chelo-2@649">zarabanda</a>: la primera corre y la segunda pesa en el segundo tiempo. Cuenta 1-2-3 en voz baja.</li>
<li><b>Cuarta escucha: compara.</b> Escucha la zarabanda de Maisky y luego la de otro violonchelista de «Otras versiones». La misma partitura dura muy distinto según quien la toque.</li>
</ol>
<p>Si te ha gustado, sigue con otra obra de Bach que comparte esa claridad de líneas, el <a href="#x-bwv-1048">Concierto de Brandeburgo n.º 3</a>.</p>"""),
 dict(t="Para el concierto", h="""<ol>
<li>Antes de cada movimiento, piensa qué danza es y cómo debería «andar»: la allemande camina, la courante corre, la zarabanda pesa en el 2 y la giga salta.</li>
<li>Busca los momentos en que una sola línea parece dividirse en dos.</li>
<li>En los minuetos, comprueba que vuelve el primero después del segundo.</li>
<li>Fíjate en el instrumento: ¿tiene pica apoyada en el suelo? ¿Cómo coge el arco?</li>
</ol>"""),
 ],
 contexto=[
  dict(anio="1719", txt="Bach viaja a Berlín a recoger un clave nuevo para la corte de Köthen y toca ante el margrave de Brandeburgo."),
  dict(anio="1720", txt="Muere de repente Maria Barbara, su primera mujer, mientras Bach está en el balneario de Karlsbad con el príncipe Leopold. Cuando vuelve, ya la han enterrado."),
  dict(anio="1721", txt="Envía al margrave los seis <a href=\"#x-bwv-1048\">Conciertos de Brandeburgo</a> y en diciembre se casa con Anna Magdalena Wilcke, cantante, que copiará estas suites."),
  dict(anio="1721", txt="El príncipe Leopold se casa con una princesa a la que no le interesa la música, y la corte gasta menos en sus músicos."),
  dict(anio="1723", txt="Bach se marcha a Leipzig como cantor de Santo Tomás. Allí escribirá música de iglesia para cada domingo."),
 ],
 versiones=[
  dict(p="maisky", det="vídeo de referencia", nota="Romántico, libre, con tempos lentos.", url=MAISKY2),
  dict(p="casals", det="1936–1939", nota="La grabación histórica que las dio a conocer."),
  dict(p="fournier", det="1961", nota="Un crítico de BBC Music la prefiere por su nobleza y su contención clásica."),
  dict(p="netherlands-bach-society", det="Steuart Pincombe", nota="Versión filmada en el Concertgebouw de Ámsterdam para el proyecto All of Bach.", url="https://www.bachvereniging.nl/en/bwv/bwv-1008"),
  dict(quien="Yo-Yo Ma", det="", nota="Zarabanda de 5:08: más fluida que la de Maisky."),
 ],
 idagio="Bach Cello Suite 2 BWV 1008",
 interpretes=["maisky"],
 conceptos=["suite","preludio","allemande","courante","zarabanda","minueto","giga","polifonia-implicita","doble-cuerda","da-capo","catalogo"],
),
dict(
 id="balada-1-chopin", n=3, fecha="2026-11-22", origen="Obra del día",
 titulo="Balada n.º 1 en sol menor", subtitulo="Op. 23", compositor="chopin",
 fechaComp="Esbozada en Viena en 1831, terminada en París en 1835", anio=1835, epoca="romanticismo",
 genero="Balada para piano", plantilla="Piano solo", tonalidad="Sol menor", catalogo="Op. 23",
 titulo_original="Ballade No. 1 in G minor, Op. 23",
 partes=[
  dict(p="Ballade", es="Balada", h="El <b>tipo de obra</b>. Chopin fue el primero en llamar así a una pieza para piano sin palabras: música que suena a historia contada. Ver <a href=\"#g-balada\">balada</a>."),
  dict(p="No. 1", es="n.º 1", h="Es la <b>primera de sus cuatro baladas</b>, y cada una es una obra independiente: n.º 1 en sol menor (Op. 23), n.º 2 en fa mayor (Op. 38), n.º 3 en la bemol mayor (Op. 47) y n.º 4 en fa menor (Op. 52). Las escribió entre 1831 y 1842; la segunda, en parte, en Mallorca."),
  dict(p="in G minor", es="en sol menor", h="La <b>tonalidad</b>. La nota «casa» de la obra es el sol (en inglés, <b>G</b>): la nota a la que la música quiere volver para descansar. El modo es <b>menor</b>, de color sombrío. Ver <a href=\"#g-tonalidad\">tonalidad</a>.</p><p><b>¿Se podría tocar en otra tonalidad?</b> Se puede, y se llama <a href=\"#g-transportar\">transportar</a>, pero con obras de piano como esta no se hace. Los pasajes están pensados para la mano sobre esas teclas blancas y negras: en otro tono habría que cambiar todas las digitaciones. Además, la obra entera sonaría más aguda o más grave, con otro brillo. Chopin eligió el sol menor, y se respeta como se respeta la letra de un poema."),
  dict(p="Op. 23", es="Opus 23", h="<b>Opus</b> significa «obra» en latín. Es el número que recibió la balada <b>al publicarse</b>, en 1836: el 23 de la lista de obras publicadas de Chopin. <b>No indica cuántas piezas hay.</b> El Op. 23 es una sola balada de unos diez minutos; en cambio, el Op. 24 son cuatro mazurcas, y el Op. 28, veinticuatro preludios. Ver <a href=\"#g-opus\">opus</a>."),
 ],
 duracion="Entre 9 y 10 minutos, en un solo movimiento",
 entradilla="Diez minutos de piano que suenan a historia contada en voz alta: un comienzo que duda, dos temas que se transforman y un final desbocado. Chopin fue el primero en llamar «balada» a una pieza sin palabras.",
 grabacion=dict(titulo="Krystian Zimerman", fuente="Vídeo en YouTube (canal Raindrop). Zimerman grabó las cuatro baladas para Deutsche Grammophon en julio de 1987; el vídeo no indica de qué grabación sale.", url="https://youtu.be/BSFNl4roGlI",
  nota="Es una pieza de un solo movimiento y el vídeo no tiene capítulos, así que aquí no hay minutos: la guía va en orden, con lo que te ayuda a reconocer cada parte."),
 escucha=[
  dict(mov="Introducción · Largo", cuando="1", txt="Siete compases lentos. Una frase sola que sube tanteando, como quien empieza a contar una historia, y un acorde final que se queda en el aire, sin resolver."),
  dict(mov="Primer tema · Moderato", cuando="2", txt="En sol menor. Una melodía melancólica que se mece en compás de 6/4, casi un vals lento, con acordes que responden a cada nota. Este tema reaparece transformado a lo largo de toda la obra."),
  dict(mov="Transición", cuando="3", txt="La música se agita y aparece por fin el virtuosismo: pasajes rápidos que recorren el teclado."),
  dict(mov="Segundo tema", cuando="4", txt="En mi bemol mayor, muy suave (<i lang=\"it\">sotto voce</i>). Una canción de amor tras la tormenta: es el contraste con el primero."),
  dict(mov="Desarrollo", cuando="5", txt="Vuelve el primer tema y crece hasta que el segundo regresa convertido en una declaración apasionada, a pleno volumen. Luego, un episodio juguetón y ligero."),
  dict(mov="Vuelta en espejo", cuando="6", txt="Los temas regresan al revés: primero el segundo y después el primero, ya sombrío."),
  dict(mov="Coda · Presto con fuoco", cuando="7", txt="Un acorde atronador abre un final rapidísimo y salvaje, que no se parece al resto de la obra. Termina con escalas en octavas que se desploman por el teclado."),
 ],
 secciones=[
  dict(t="Quién era Chopin cuando la escribió", h="""<p>Chopin salió de Varsovia en noviembre de 1830, con 20 años, para una gira por Europa. Menos de un mes después estalló en Polonia el Levantamiento de Noviembre contra Rusia. Pasó ocho meses en Viena, y allí, en 1831, hizo los primeros esbozos de esta balada. Camino de París supo que el levantamiento había sido aplastado y sufrió una crisis nerviosa. Nunca volvió a Polonia.</p>
<p>A finales de 1831 se instaló en París, entonces la capital musical de Europa. Allí terminó la balada en 1835 y la publicó en 1836. Es la obra de un joven de 25 años en el exilio.</p>"""),
  dict(t="Para quién", h="""<p>Está dedicada al barón Nathaniel von Stockhausen, embajador del reino de Hannover en Francia y amigo de Chopin en aquellos años.</p>
<p>Robert Schumann contó que le dijo a Chopin que esta era su obra favorita. Chopin, tras una larga pausa, le contestó que también era la suya, la que más quería.</p>"""),
  dict(t="¿Qué es una balada?", h="""<p>En literatura, una balada es un poema que cuenta una historia, a menudo legendaria o trágica. Schubert y otros compositores pusieron música a baladas cantadas, muchas veces en un compás de 6/8 o 6/4 que suena a narración. Chopin fue el primero en usar el nombre para una pieza solo instrumental, sin palabras.</p>
<p>¿Cuenta una historia concreta? Según Schumann, Chopin le dijo que sus baladas se inspiraban en poemas de su amigo Adam Mickiewicz, el gran poeta polaco. Algunos relacionan esta con su poema <i>Konrad Wallenrod</i>, pero no hay pruebas de qué historia es, si es que hay una. Así que tienes permiso para imaginar la tuya.</p>"""),
  dict(t="El instrumento", h="""<p>Todas las obras de Chopin incluyen el piano, y su música ayudó a convertirlo en el instrumento más popular del siglo XIX. El piano romántico permite lo que el clave barroco no podía: tocar suave o fuerte según la fuerza del dedo y alargar el sonido con el pedal.</p>
<p>El piano de Chopin era un Pleyel, de sonido más ligero e íntimo que el de un piano de concierto moderno. Zimerman toca siempre sus propios Steinway, que él mismo afina, monta y modifica según el repertorio.</p>"""),
  dict(t="Cómo está hecha", h="""<p>La obra se construye con <b>dos temas</b>, uno en sol menor y otro en mi bemol mayor, que se alternan y se transforman. Hay tres compases distintos: la introducción va en 4/4, el cuerpo de la obra en 6/4 y la coda en 2/2.</p>
<p>Chopin mezcla ideas de la <a href="#g-forma-sonata">forma sonata</a> y de las variaciones, pero con un truco propio: cuando los temas vuelven al final, lo hacen <b>en espejo</b>, primero el segundo y luego el primero. Y la coda es casi una pieza nueva.</p>"""),
  dict(t="Cómo reconocer aquí el Romanticismo", h="""<p>Compárala con la suite de Bach, que también es para un solo instrumento:</p>
<ul>
<li><b>El tiempo respira.</b> En Bach el pulso de la danza es firme. Aquí el pianista se adelanta y se retrasa a propósito: es el <a href="#g-rubato">rubato</a>.</li>
<li><b>Contrastes enormes de volumen</b>, de un susurro a un estruendo, y el pedal dejando resonar el sonido.</li>
<li><b>Una historia, no una danza.</b> La obra va a algún sitio y llega a un clímax. No es una forma con estribillo ni una serie de danzas.</li>
<li><b>Sin bajo continuo.</b> Un solo piano hace de orquesta.</li>
</ul>
<p>Más en <a href="#e-romanticismo">Romanticismo</a> y en el artículo <a href="#a-rubato">El rubato</a>.</p>"""),
  dict(t="Zimerman y esta grabación", h="""<p>Krystian Zimerman ganó el Concurso Chopin de Varsovia en 1975, con 18 años. En julio de 1987 grabó las cuatro baladas en Bielefeld (Alemania) para Deutsche Grammophon. Esa grabación fue la primera elección del programa <i>Building a Library</i> de la BBC en 2013.</p>
<p>No a todos les convence igual. Gramophone admira su acabado técnico, casi perfecto, pero lo encuentra menos cálido que el del pianista Vlado Perlemuter. Escucha las dos y decide.</p>"""),
  dict(t="Curiosidades", h="""<ul>
<li><b>Sale en <i>El pianista</i></b> (Polanski, 2002). Es la pieza que Szpilman toca para el oficial alemán Hosenfeld entre las ruinas de Varsovia. En la vida real, Szpilman tocó otra obra de Chopin, el <a href="#x-chopin-nocturno-postumo">Nocturno en do sostenido menor</a>.</li>
<li>El periodista Alan Rusbridger, director de <i>The Guardian</i>, dedicó en 2010 un año entero a aprender a tocarla y escribió un libro sobre ello.</li>
<li><b>Chopin en Mallorca.</b> Pasó el invierno de 1838–1839 en la Cartuja de Valldemossa con la escritora George Sand. Allí terminó sus <a href="#x-chopin-op28">24 Preludios</a>, incluido el de la <a href="#x-chopin-op28@1194">«Gota de agua»</a>, en un pequeño piano Pleyel que todavía se conserva en el museo de Valldemossa.</li>
<li>Chopin está enterrado en París, pero su corazón está en la iglesia de la Santa Cruz de Varsovia, como pidió.</li>
</ul>"""),
  dict(t="Cómo saborearla: cuatro escuchas", h="""<p>Es una sola pieza de unos diez minutos que cuenta una historia. Para no perderse, conviene ir paso a paso.</p>
<ol>
<li><b>Primera escucha: los dos temas.</b> Escucha solo hasta que aparezca el segundo tema, el suave, en mayor (pasos 1 a 4 de la guía). Tararea los dos.</li>
<li><b>Segunda escucha: síguelos.</b> Escúchala entera buscando esos dos temas. Fíjate en cómo el segundo vuelve convertido en grito y en cómo al final regresan en orden inverso.</li>
<li><b>Tercera escucha: el tempo.</b> Fíjate solo en cómo se estira y se recoge la velocidad, sobre todo en el primer tema. Eso es el <a href="#g-rubato">rubato</a>.</li>
<li><b>Cuarta escucha: compara.</b> Pon la coda de Zimerman y la de otra versión. ¿Quién arriesga más?</li>
</ol>
<p>Después, escucha algo más íntimo de Chopin, el <a href="#x-chopin-nocturno-postumo">Nocturno en do sostenido menor</a>, y piensa en qué se parecen y en qué no.</p>"""),
 dict(t="Para el concierto", h="""<ol>
<li>No esperes movimientos: es una sola pieza de unos diez minutos.</li>
<li>Quédate con el primer tema, el del vals lento. Toda la obra gira alrededor de él.</li>
<li>Espera el segundo tema, suave y en mayor, y fíjate en cómo vuelve después convertido en grito.</li>
<li>La coda es el momento de máxima tensión. Se aplaude cuando el pianista levanta las manos.</li>
</ol>"""),
 ],
 contexto=[
  dict(anio="1831", txt="Robert Schumann publica su primera crítica musical, dedicada a Chopin: «¡Quítense el sombrero, señores: un genio!»."),
  dict(anio="1832", txt="26 de febrero: primer concierto de Chopin en París, en la sala Pleyel. Toca su <a href=\"#x-chopin-concierto-1\">Concierto en mi menor</a> y Liszt está entre el público."),
  dict(anio="1832", txt="Empieza a dar clases a la aristocracia de París, a unos 20 francos la lección, una tarifa muy alta. De eso vivirá."),
  dict(anio="1835", txt="Se reúne con sus padres en el balneario de Karlsbad y, de vuelta, conoce en Leipzig a Schumann, a Clara Wieck y a Mendelssohn."),
  dict(anio="1836", txt="En otra visita a Leipzig, Chopin regala a Schumann esta balada."),
 ],
 versiones=[
  dict(p="zimerman", det="1987, vídeo de referencia", nota="Perfección técnica y gran concentración.", url="https://youtu.be/BSFNl4roGlI"),
  dict(quien="Vlado Perlemuter", det="Nimbus", nota="Más cálida que la de Zimerman, según Gramophone."),
  dict(quien="Andrei Gavrilov", det="1992, Deutsche Grammophon", nota="Un crítico la sitúa justo detrás de la de Zimerman."),
  dict(quien="Nikolai Demidenko", det="", nota="Según BBC Music, una de las tres grandes versiones de su época, junto a las de Zimerman y Gavrilov."),
  dict(quien="Janusz Olejniczak", det="banda sonora de El pianista", nota="La versión que suena en la película."),
 ],
 idagio="Chopin Ballade No. 1 Op. 23",
 interpretes=["zimerman"],
 conceptos=["balada","rubato","tema","coda","compas","pedal","forma-sonata","tonalidad","pieza-de-caracter"],
),
dict(
 id="adagietto-mahler", n=4, fecha="2026-11-23", origen="Obra del día",
 titulo="Adagietto de la Sinfonía n.º 5", subtitulo="Cuarto movimiento · Sehr langsam (muy lento)",
 compositor="mahler", fechaComp="1901–1902", anio=1902, epoca="romanticismo",
 genero="Sinfonía (movimiento lento)", plantilla="Solo cuerda y arpa, dentro de una sinfonía para orquesta enorme",
 tonalidad="Fa mayor (la sinfonía empieza en do sostenido menor y acaba en re mayor)", catalogo="Sinfonía n.º 5, IV",
 titulo_original="Symphony No. 5 in C-sharp minor · IV. Adagietto. Sehr langsam",
 partes=[
  dict(p="Symphony", es="Sinfonía", h="El <b>tipo de obra</b>: una obra grande para orquesta, dividida en varios <a href=\"#g-movimiento\">movimientos</a>. La de Mahler tiene cinco y dura más de una hora. Ver <a href=\"#g-sinfonia\">sinfonía</a>."),
  dict(p="No. 5", es="n.º 5", h="La <b>quinta de sus nueve sinfonías</b> terminadas; dejó una Décima sin acabar."),
  dict(p="in C-sharp minor", es="en do sostenido menor", h="La <b>tonalidad</b> con que se suele presentar la sinfonía: C es do y <i lang=\"en\">sharp</i> (♯), sostenido. Pero solo el primer movimiento está en do sostenido menor: la sinfonía acaba en re mayor, y el propio Mahler pidió que no se le pusiera tonalidad, porque no se podía hablar de una sola para toda la obra. Este movimiento, el Adagietto, está en <b>fa mayor</b>. Ver <a href=\"#g-tonalidad\">tonalidad</a>."),
  dict(p="IV.", es="cuarto movimiento", h="Es el <b>cuarto de los cinco movimientos</b>. Mahler los agrupó en tres partes, y el Adagietto abre la tercera, junto al Rondo-Finale que llega después."),
  dict(p="Adagietto", es="«pequeño adagio»", h="El diminutivo italiano de <i lang=\"it\">adagio</i>, «lento». Indica un tempo lento, pero algo menos que un adagio. Aquí además es el nombre por el que se conoce el movimiento. Ver <a href=\"#g-tempo\">tempo</a>."),
  dict(p="Sehr langsam", es="«muy lento», en alemán", h="La indicación de tempo, escrita en alemán. Mahler daba sus instrucciones en su idioma y no en el italiano habitual: los otros movimientos dicen, por ejemplo, <i lang=\"de\">Stürmisch bewegt</i> («tempestuoso») o <i lang=\"de\">Kräftig, nicht zu schnell</i> («enérgico, no demasiado rápido»)."),
 ],
 duracion="Entre 7 y 14 minutos, según el director (aquí, unos 12)",
 entradilla="Unos diez minutos de cuerda y arpa en mitad de una sinfonía gigantesca: la música más famosa de Mahler. ¿Una carta de amor a Alma o una despedida del mundo? Las dos lecturas tienen defensores.",
 grabacion=dict(titulo="Filarmónica de Viena · Leonard Bernstein", fuente="Película de Unitel rodada en el Musikverein de Viena el 19 de abril de 1972, restaurada en YouTube", url="https://youtu.be/Bj6KLv7kv2Q",
   nota="El vídeo no tiene capítulos, así que la guía va por pasos, en orden. Dura unos 12 minutos.", dur="12:07"),
 escucha=[
  dict(mov="Comienzo", cuando="1", txt="Casi un susurro. Las cuerdas sostienen notas largas y el <a href=\"#g-arpa\">arpa</a> desgrana acordes por debajo. No hay viento ni percusión: de una orquesta enorme, Mahler se queda solo con la cuerda y el arpa."),
  dict(mov="El tema", cuando="2", txt="Los primeros violines cantan una melodía larga que sube, se detiene y vuelve a empezar, como una frase que no se atreve a terminar. Según el director Willem Mengelberg, nació de un pequeño poema de Mahler para Alma: «Cómo te quiero, sol mío, no te lo puedo decir con palabras»."),
  dict(mov="Oleadas", cuando="3", txt="La melodía crece y se calma varias veces. En la partitura, Mahler pide tocar «con sentimiento» y «con calidez». Fíjate en cómo cada <a href=\"#g-crescendo\">crescendo</a> parece una respiración más honda."),
  dict(mov="Parte central", cuando="4", txt="Cambia la luz: la música toma otro rumbo, con más tensión, antes de volver a casa. El movimiento tiene tres partes, A–B–A, y esta es la B."),
  dict(mov="Vuelve el tema", cuando="5", txt="Regresa la melodía del principio, ahora con más cuerpo. Es el mismo tema de amor, pero después de haber pasado por la tensión del centro."),
  dict(mov="Final", cuando="6", txt="El cierre, muy suave, usa la melodía de una canción del propio Mahler, <a href=\"#x-mahler-ich-bin\">«Ich bin der Welt abhanden gekommen»</a>. En ella, la voz canta justo ahí «en mi amor, en mi canción»."),
  dict(mov="Después, en la sinfonía", cuando="7", txt="En la sinfonía completa, tras el Adagietto llega el <a href=\"#x-mahler-5@3413\">Rondo-Finale</a>, alegre y rápido. A mitad del Finale, el tema del Adagietto vuelve convertido en una danza ligera y elegante."),
 ],
 secciones=[
  dict(t="Quién era Mahler cuando la escribió", h="""<p>En 1901, Gustav Mahler tenía 41 años y estaba en lo más alto: era director de la Ópera de la Corte de Viena desde 1897 y había dirigido los conciertos de la Filarmónica de Viena entre 1898 y 1901. Como director no tenía tiempo para componer durante la temporada, así que escribía en verano.</p>
<p>En febrero de 1901 sufrió una hemorragia intestinal tan grave que su médico le dijo después que había estado a una hora de morir desangrado. Ese verano estrenó su propia casa junto al lago Wörthersee, en Maiernigg (Carintia, al sur de Austria), con una cabaña para componer en el bosque. Allí empezó la Quinta.</p>
<p>En noviembre de 1901 conoció a Alma Schindler, de 22 años, hija del pintor Emil Jakob Schindler. Se prometieron en diciembre y se casaron el 9 de marzo de 1902. El verano siguiente, ya casados, terminó la sinfonía en Maiernigg: en agosto de 1902 contaba por carta que estaba acabada. Él mismo dirigió el estreno, en Colonia, el 18 de octubre de 1904, con la Orquesta del Gürzenich, y siguió retocándola hasta 1911.</p>"""),
  dict(t="Para quién: ¿una carta de amor?", h="""<p>El director holandés Willem Mengelberg, amigo de Mahler, dejó escrito en su partitura que este Adagietto fue la declaración de amor de Mahler a Alma: en lugar de una carta, le mandó el manuscrito sin una palabra más; ella lo entendió y le contestó que fuera a verla. Mengelberg añadió que los dos se lo habían contado.</p>
<p>No todos lo creen. Alma nunca lo menciona en sus escritos sobre Mahler, y el Adagietto se parece mucho a una canción que Mahler compuso ese mismo año, <a href="#x-mahler-ich-bin">«Ich bin der Welt abhanden gekommen»</a> («Me he perdido para el mundo»), que habla de soledad y de retirarse del mundo. El gran biógrafo de Mahler, Henry-Louis de La Grange, dudaba de que dos obras tan parecidas pudieran significar cosas tan distintas.</p>
<p>Lo más probable es que haya algo de las dos cosas: amor y nostalgia. Cuando lo escuches, decide tú.</p>"""),
  dict(t="Quién la toca", h="""<p>La Quinta pide una orquesta enorme: seis trompas, cuatro trompetas, mucha percusión… Pero en el Adagietto Mahler deja callar a casi todos y se queda solo con la <a href="#g-cuerda">cuerda</a> y un <a href="#g-arpa">arpa</a>. Ese contraste es parte del efecto: después del ruido, intimidad.</p>
<p>El arpa no hace melodía: sostiene la armonía por debajo, en un papel parecido al del <a href="#g-bajo-continuo">bajo continuo</a> del Barroco, que ya conoces de <a href="#o-cuatro-estaciones@1574">Vivaldi</a>.</p>
<p>La orquesta de esta grabación tiene una relación especial con Mahler: la <a href="#i-wiener-philharmoniker">Filarmónica de Viena</a> fue la que él mismo dirigió entre 1898 y 1901.</p>"""),
  dict(t="Cómo está hecha", h="""<p>La sinfonía tiene cinco movimientos agrupados en tres partes:</p>
<ol>
<li><b>Parte I.</b> Una marcha fúnebre que abre una trompeta sola (<a href="#x-mahler-5@33">escúchala</a>) y un movimiento tempestuoso (<a href="#x-mahler-5@782">escúchalo</a>).</li>
<li><b>Parte II.</b> Un Scherzo enorme, con aire de vals y de danza campesina (<a href="#x-mahler-5@1716">escúchalo</a>).</li>
<li><b>Parte III.</b> El Adagietto y el Rondo-Finale, alegre (<a href="#x-mahler-5@3413">escúchalo</a>).</li>
</ol>
<p>El viaje va de la oscuridad a la luz: de un funeral a una fiesta. El Adagietto, en fa mayor y en medio de movimientos en re mayor, es el remanso antes del final, casi su introducción.</p>
<p>Por dentro tiene tres partes (A–B–A): el tema, una sección central con más tensión y la vuelta del tema. Acaba citando la melodía de su canción <a href="#x-mahler-ich-bin">«Ich bin der Welt abhanden gekommen»</a>.</p>"""),
  dict(t="Cómo reconocer aquí el Romanticismo", h="""<p>Mahler escribe en 1901–1902, ya en el siglo XX, pero su lenguaje es el del Romanticismo llevado al extremo: es lo que se llama Romanticismo tardío.</p>
<ul>
<li><b>Una sola melodía larguísima</b> que parece no acabar nunca, frente a las frases cortas y simétricas del Clasicismo.</li>
<li><b>Tempo flexible:</b> la música se detiene y avanza con libertad (<a href="#g-rubato">rubato</a>), como en la <a href="#o-balada-1-chopin">Balada de Chopin</a>.</li>
<li><b>Instrucciones de sentimiento</b> en la partitura: «con sentimiento», «con calidez». Ya no basta con decir rápido o lento.</li>
<li><b>Orquesta gigante</b> en la sinfonía, y aquí el contraste contrario: solo cuerda y arpa.</li>
</ul>
<p>Compáralo con el Barroco: aquí no hay continuo que marque el paso ni cambios de volumen por bloques. Todo crece y se apaga poco a poco, en <a href="#g-crescendo">crescendos</a> larguísimos.</p>"""),
  dict(t="Bernstein y esta grabación", h="""<p><a href="#i-bernstein">Leonard Bernstein</a> fue el gran defensor de Mahler en el siglo XX y el primer director en grabar todas sus sinfonías, primero en disco con la Filarmónica de Nueva York, en los años sesenta, y luego en vídeo.</p>
<p>Esta grabación forma parte de ese ciclo filmado: la Quinta se rodó en el Musikverein de Viena el 19 de abril de 1972, con la Filarmónica de Viena y con Humphrey Burton como director de la realización. El vídeo que escuchas es esa película restaurada.</p>
<p>Fíjate en el tempo. El propio Mahler y Mengelberg tocaban el Adagietto en unos 7 minutos; Bernstein se toma unos 12. Con un tempo lento se acentúa la melancolía, casi de despedida; con uno más ligero, gana el impulso de la carta de amor. Bernstein lo dirigió en el funeral de Robert F. Kennedy, el 8 de junio de 1968, y eso ayudó a que mucha gente lo asocie con el duelo.</p>"""),
  dict(t="Curiosidades", h="""<ul>
<li>Se hizo famosísimo con la película <i lang="it">Muerte en Venecia</i> (1971) de Luchino Visconti, que lo usa como banda sonora.</li>
<li>En el Reino Unido, el Adagietto se estrenó solo en 1909, en los Proms de Henry Wood; la sinfonía completa no llegó hasta 1945, 36 años después.</li>
<li>Bernstein fue enterrado con una partitura de la Quinta de Mahler sobre el corazón.</li>
<li>Los patinadores canadienses Tessa Virtue y Scott Moir lo usaron en su danza libre y ganaron con ella el oro olímpico en 2010.</li>
</ul>"""),
  dict(t="Cómo saborearla: cuatro escuchas", h="""<p>Es música lenta y sin sobresaltos, así que la clave es escuchar con atención sin dejar que se convierta en música de fondo.</p>
<ol>
<li><b>Primera escucha: a oscuras.</b> Pon el vídeo, baja la luz y no hagas nada más durante sus doce minutos.</li>
<li><b>Segunda escucha: el arpa.</b> Fíjate solo en el arpa del principio. ¿Cuándo calla y cuándo vuelve?</li>
<li><b>Tercera escucha: la canción.</b> Escucha antes el lied <a href="#x-mahler-ich-bin">«Ich bin der Welt abhanden gekommen»</a> y luego el final del Adagietto. ¿Reconoces la melodía?</li>
<li><b>Cuarta escucha: dentro de la sinfonía.</b> Escúchalo en su sitio: desde el final del <a href="#x-mahler-5@1716">Scherzo</a> hasta el <a href="#x-mahler-5@3413">Rondo-Finale</a>. Después del ruido, el silencio pesa más.</li>
</ol>
<p>Y compara el tempo. La misma partitura dura 7 minutos con Mengelberg y casi 14 con Haitink: lo ves en el gráfico de duraciones de esta ficha y en el artículo <a href="#a-tempo">sobre el tempo</a>.</p>"""),
 dict(t="Para el concierto", h="""<ul>
<li>A menudo se toca solo, fuera de la sinfonía. Si va dentro de la Quinta completa, es el cuarto de cinco movimientos, en una obra de más de una hora: no se aplaude al acabar.</li>
<li>Mira a la orquesta: durante el Adagietto, los vientos y la percusión se quedan quietos. Busca el arpa.</li>
<li>Escucha el tempo que elige el director: lento y doliente, o más fluido y apasionado.</li>
</ul>"""),
 ],
 contexto=[
  dict(anio="1900", txt="Mahler lleva a la Filarmónica de Viena a su primera gira, a la Exposición Universal de París."),
  dict(anio="1902", txt="En abril, Enrico Caruso graba diez arias en un hotel de Milán. Los discos se venden muchísimo: la grabación empieza a ser un negocio."),
  dict(anio="1902", txt="También en abril, la Secesión de Viena inaugura su exposición dedicada a Beethoven, con el friso de Gustav Klimt. Mahler dirige un breve concierto en la apertura."),
  dict(anio="1947", txt="Bruno Walter, que había sido ayudante de Mahler, hace la primera grabación completa de la Quinta, con la Filarmónica de Nueva York."),
 ],
 versiones=[
  dict(p="bernstein", det="Filarmónica de Viena, 1987 (Deutsche Grammophon)", nota="Su grabación en disco, en directo en la Alte Oper de Fráncfort, quince años después de esta película."),
  dict(p="bernstein", det="Filarmónica de Nueva York, 1963 (Sony)", nota="La de su primer ciclo, con el que fue el primero en grabar todas las sinfonías de Mahler."),
  dict(quien="Willem Mengelberg", det="Orquesta del Concertgebouw, 1926", nota="De las más rápidas que existen: unos 7 minutos. Mengelberg era amigo de Mahler, y Mahler lo tocaba a un tempo parecido.", dur="7:04"),
  dict(quien="Bernard Haitink", det="Filarmónica de Berlín, 1988", nota="Una de las más lentas en disco: casi 14 minutos.", dur="13:56"),
  dict(quien="Simon Rattle", det="Filarmónica de Berlín (EMI)", nota="Grabada al empezar su etapa como titular en Berlín. Fluida y sin pesadez: no llega a los 10 minutos.", dur="9:32"),
  dict(quien="Hermann Scherchen", det="1964", nota="De las más lentas que se conocen: más de un cuarto de hora.", dur="15:15"),
  dict(quien="Andrés Orozco-Estrada", det="Orquesta Sinfónica de la Radio de Hesse", nota="Dentro de la sinfonía completa, en el canal de la orquesta: para escucharlo en su contexto. La duración sale de los capítulos del vídeo.", url="#x-mahler-5@2779", dur="10:34"),
 ],
 idagio="Mahler Symphony 5 Adagietto Bernstein",
 interpretes=["bernstein","wiener-philharmoniker"],
 conceptos=["sinfonia","movimiento","arpa","cuerda","tempo","lied","director","crescendo","rubato","tonalidad"],
),
]
