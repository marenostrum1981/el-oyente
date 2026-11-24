EPOCAS = [
dict(id="renacimiento", nombre="Renacimiento", fechas="c. 1400–1600", ini=1400, fin=1600, color="var(--ren)",
 entradilla="La polifonía vocal llega a su cumbre: varias voces independientes que se entrelazan, sobre todo en la música de iglesia.",
 h="""<p>La música del Renacimiento es sobre todo vocal y polifónica: varias voces de igual importancia que se imitan unas a otras. Esta sección crecerá cuando llegue la primera obra renacentista al diario.</p>""",
 rasgos=["Predominio de las voces sobre los instrumentos.","Polifonía: varias melodías a la vez, a menudo imitándose.","Poco contraste de volumen y ritmos fluidos."],
 nombres="Josquin des Prez, Giovanni Pierluigi da Palestrina, Tomás Luis de Victoria"),
dict(id="barroco", nombre="Barroco", fechas="1600–1750", ini=1600, fin=1750, color="var(--bar)",
 entradilla="Desde el nacimiento de la ópera, hacia 1600, hasta la muerte de Bach en 1750. Todo descansa sobre el bajo continuo.",
 h="""<p>El Barroco empieza hacia 1600, cuando en Italia nace la ópera con Peri y Monteverdi, y se suele cerrar en 1750, el año en que muere Bach. Es la época en que se asientan las tonalidades mayor y menor y nacen o se consolidan géneros que todavía escuchamos: la ópera, el oratorio, el concierto, la sonata, la suite y la fuga.</p>
<p>Lo que lo une todo es el <a href="#g-bajo-continuo">bajo continuo</a>: debajo de casi cualquier obra barroca hay un bajo que no se detiene y un instrumento de acordes (clave, órgano, laúd o tiorba) que improvisa la armonía.</p>
<p>Dentro del Barroco hay acentos nacionales. El italiano (Vivaldi, Corelli) es brillante, virtuoso y teatral; el francés (Lully, Rameau), elegante y lleno de danzas y adornos; el alemán (Bach) mezcla todo eso con un contrapunto muy denso.</p>""",
 rasgos=["Un bajo continuo que suena de principio a fin: escucha si hay un clave o un laúd rellenando acordes. Ejemplo: <a href=\"#o-cuatro-estaciones@1574\">Vivaldi, Otoño II</a>.","Ritmo constante e impulso que no decae, sobre todo en los movimientos rápidos. Ejemplo: <a href=\"#o-cuatro-estaciones@1066\">Vivaldi, Verano III</a>.","<a href=\"#g-dinamica-terrazas\">Dinámica en terrazas</a>: fuerte y piano en bloques, como ecos, sin crescendos largos. Ejemplo: <a href=\"#o-cuatro-estaciones@609\">Vivaldi, Verano I</a>.","Contraste entre solista y grupo, con estribillos (<a href=\"#g-ritornello\">ritornello</a>) en los conciertos. Ejemplo: <a href=\"#o-cuatro-estaciones@0\">Vivaldi, Primavera I</a>.","Melodías muy adornadas, con trinos y floreos; los músicos improvisaban parte de los adornos. Ejemplo: <a href=\"#o-suite-chelo-2@649\">Bach, Zarabanda</a>."],
 nombres="Claudio Monteverdi, Arcangelo Corelli, Antonio Vivaldi, Georg Friedrich Händel, Johann Sebastian Bach, Jean-Philippe Rameau"),
dict(id="clasicismo", nombre="Clasicismo", fechas="c. 1750–1820", ini=1750, fin=1820, color="var(--cla)",
 entradilla="Haydn, Mozart y el primer Beethoven: textura más clara, melodía con acompañamiento y formas equilibradas.",
 h="""<p>Ya antes de la muerte de Bach el gusto estaba cambiando. La música clásica busca lo claro y lo equilibrado: una melodía principal con un acompañamiento de acordes, frases simétricas que suenan a pregunta y respuesta, y cambios de volumen graduales.</p>
<p>El continuo desaparece (hacia 1800 está prácticamente extinguido) y nacen o se fijan la sinfonía, el cuarteto de cuerda y el concierto clásico. Su molde más importante es la <a href="#g-forma-sonata">forma sonata</a>.</p>""",
 rasgos=["Sin bajo continuo: ya no hay un clave rellenando por debajo.","Melodía con acompañamiento, textura más ligera.","Frases equilibradas y simétricas, como pregunta y respuesta.","Crescendos y diminuendos, cambios de carácter dentro de un mismo movimiento.","En el piano, el bajo Alberti: acordes partidos que se repiten en la mano izquierda."],
 nombres="Joseph Haydn, Wolfgang Amadeus Mozart, Luigi Boccherini, Ludwig van Beethoven (primera etapa)"),
dict(id="romanticismo", nombre="Romanticismo", fechas="c. 1820–1900", ini=1820, fin=1900, color="var(--rom)",
 entradilla="La emoción personal, la imaginación y las historias se adueñan de la música. El piano se convierte en el instrumento estrella y la orquesta crece.",
 h="""<p>El Romanticismo nace como reacción a la razón de la Ilustración: frente al orden y el equilibrio del Clasicismo, pone por delante los sentimientos, la imaginación y al individuo. Los compositores dependen menos de un mecenas y escriben más para expresarse.</p>
<p>La música se estira hacia los dos extremos. Por un lado, piezas breves para piano y canciones que retratan un estado de ánimo, las llamadas <a href="#g-pieza-de-caracter">piezas de carácter</a>. Por otro, sinfonías y óperas cada vez más grandes, y poemas sinfónicos que cuentan una historia con la orquesta. El piano se vuelve el instrumento más popular del siglo, y aparecen músicas inspiradas en el folclore de cada país.</p>""",
 rasgos=["Tempo flexible: el intérprete se adelanta y se retrasa (<a href=\"#g-rubato\">rubato</a>). Ejemplo: <a href=\"#o-balada-1-chopin@0\">Chopin, Balada n.º 1</a>, desde el primer tema.","Contrastes enormes de volumen, del casi silencio al estruendo, a veces de golpe y a veces con crescendos muy largos; y mucho pedal en el piano. Ejemplo: la <a href=\"#o-balada-1-chopin\">Balada n.º 1 de Chopin</a>, pasos 5 y 7 de su guía.","Melodías largas y expresivas, con frases menos simétricas que en el Clasicismo.","Música que narra o pinta: baladas, poemas sinfónicos, títulos evocadores.","Menos adorno añadido y más color: armonías atrevidas y orquestas más grandes."],
 nombres="Franz Schubert, Frédéric Chopin, Robert Schumann, Franz Liszt, Richard Wagner, Giuseppe Verdi, Johannes Brahms, Piotr Chaikovski, Gustav Mahler"),
dict(id="siglo-xx", nombre="Siglo XX y XXI", fechas="1900–hoy", ini=1900, fin=2000, color="var(--xx)",
 entradilla="Se rompen las reglas: nuevos colores, nuevos ritmos y nuevas formas de ordenar los sonidos.",
 h="""<p>Esta sección se completará cuando llegue la primera obra del siglo XX al diario.</p>""",
 rasgos=["Armonías que ya no giran en torno a una tonalidad clara.","Ritmos irregulares y protagonismo de la percusión.","El timbre, el color de cada instrumento, como protagonista."],
 nombres="Claude Debussy, Maurice Ravel, Manuel de Falla, Ígor Stravinski, Dmitri Shostakóvich"),
]

ARTICULOS = [
dict(id="tempo", tema="Interpretación", titulo="El tempo: por qué la misma obra dura 7 minutos o 15",
 entradilla="El compositor escribe «lento» o «rápido», pero casi nunca dice cuánto. El resto lo decide el intérprete, y ahí empieza lo interesante.",
 h="""<h2>Palabras, no números</h2>
<p>Durante siglos, la velocidad se indicó con palabras, casi siempre en italiano: <i lang="it">largo</i> y <i lang="it">adagio</i> son lentos, <i lang="it">andante</i> va al paso, <i lang="it">allegro</i> es rápido y alegre, y <i lang="it">presto</i>, muy rápido. Más que una velocidad exacta, indican un carácter. Las tienes en el <a href="#g-tempo">glosario</a>.</p>
<p>Compáralo dentro de una misma obra: el <a href="#o-cuatro-estaciones@0">Allegro</a> y el <a href="#o-cuatro-estaciones@212">Largo</a> de la Primavera de Vivaldi.</p>
<h2>Llega el metrónomo</h2>
<p>En 1815, Johann Nepomuk Maelzel patentó en París y en Londres el <a href="#g-metronomo">metrónomo</a>, un péndulo que marca golpes por minuto. La idea del doble péndulo era del holandés Dietrich Nikolaus Winkel, y una comisión de Ámsterdam le dio la razón, pero el aparato se quedó con el nombre de Maelzel: por eso en las partituras aparece «M. M.», metrónomo de Maelzel.</p>
<p>Con él, un compositor puede escribir «negra = 60»: sesenta golpes por minuto, uno por segundo. Beethoven se entusiasmó y en diciembre de 1817 publicó las velocidades de metrónomo de sus ocho primeras sinfonías. Ni así se acabó la discusión: algunas de sus cifras parecen rapidísimas y todavía se debate si hay que seguirlas al pie de la letra.</p>
<h2>La misma partitura, distintas velocidades</h2>
<p>El mejor ejemplo del diario es el <a href="#o-adagietto-mahler">Adagietto de Mahler</a>. La partitura dice <i lang="de">Sehr langsam</i>, «muy lento», sin metrónomo. Willem Mengelberg, amigo de Mahler, lo grabó en 1926 en unos 7 minutos; Bernard Haitink, en 1988, en casi 14. En la ficha tienes un gráfico con varias versiones.</p>
<p>Escucha dos y compara: la de <a href="#o-adagietto-mahler">Bernstein</a>, de unos 12 minutos, y la de <a href="#x-mahler-5@2779">Orozco-Estrada</a>, de unos 10 y medio. Más lento suena más a despedida; más ligero, más a carta de amor.</p>
<h2>El tempo que respira</h2>
<p>Además de la velocidad de partida, está la flexibilidad. En el Barroco el pulso suele ser constante, como un motor: escucha la <a href="#o-cuatro-estaciones@1066">tempestad del Verano</a>. En el Romanticismo, el tempo se estira y se recoge dentro de cada frase, el <a href="#g-rubato">rubato</a>: escucha <a href="#o-balada-1-chopin">la Balada de Chopin</a> y lee <a href="#a-rubato">el artículo sobre el rubato</a>.</p>
<h2>Cómo escuchar el tempo</h2>
<ul>
<li>Marca el pulso con un dedo. ¿Te cuesta seguirlo porque se mueve? Eso es rubato.</li>
<li>Compara dos versiones en el mismo punto, justo al empezar.</li>
<li>Pregúntate qué gana y qué pierde la música cuando va más lenta: ¿más profundidad o más pesadez?</li>
</ul>"""),
dict(id="quien-pagaba", tema="Historia", titulo="¿Quién pagaba la música?",
 entradilla="La iglesia, los príncipes, un orfanato, los editores, los salones y, al final, el público que paga entrada. Saber quién pagaba ayuda a entender por qué cada obra suena como suena.",
 h="""<h2>La iglesia y la corte</h2>
<p>Durante siglos, la mayoría de los músicos fueron empleados de alguien. Bach trabajó para los dos grandes patronos de su tiempo.</p>
<p>En Köthen, entre 1717 y 1723, servía a un príncipe calvinista que no necesitaba música de iglesia elaborada, así que escribió sobre todo música instrumental, como las <a href="#o-suite-chelo-2">suites para violonchelo</a>. Cuando el príncipe se casó, en 1721, con una princesa a la que no le interesaba la música, la corte empezó a gastar menos en sus músicos.</p>
<p>En Leipzig, desde 1723, trabajaba para la ciudad y sus iglesias, y tenía que dar música cada domingo. De ahí salen sus cantatas, como la <a href="#x-bwv-1">BWV 1</a>.</p>
<p>Haydn pasó casi treinta años, desde 1761, al servicio de los príncipes Esterházy. Escribía lo que le pedían, incluidas unas doscientas piezas para el barítono, un instrumento de cuerda que era el favorito del príncipe Nikolaus.</p>
<h2>Dedicar una obra era pedir protección</h2>
<p>Un compositor podía dedicar una obra a un noble con la esperanza de recibir un regalo o un puesto. Vivaldi dedicó su Opus 8, el de <a href="#o-cuatro-estaciones">las Cuatro Estaciones</a>, al conde Wenzel von Morzin. Bach envió en 1721 seis conciertos al margrave de Brandeburgo, con una dedicatoria en francés llena de reverencias: hoy son los <a href="#x-bwv-1048">Conciertos de Brandeburgo</a>.</p>
<h2>Un orfanato con orquesta</h2>
<p>Vivaldi trabajó para el Ospedale della Pietà de Venecia, que acogía a niños abandonados. Sus alumnas formaban un conjunto famoso y buena parte de su música se escribió para ellas.</p>
<h2>La imprenta</h2>
<p>Vender partituras era otra fuente de ingresos. Los conciertos de Vivaldi se imprimían en Ámsterdam y desde allí llegaban a toda Europa: así los conoció Bach, que los copió y los adaptó (escucha un concierto de Vivaldi para <a href="#x-rv-580">cuatro violines</a> y la versión de Bach para <a href="#x-bwv-1065">cuatro claves</a>).</p>
<h2>El público que paga entrada</h2>
<p>En 1791, Haydn llegó a Londres contratado por el violinista y empresario Johann Peter Salomon, que organizaba conciertos por suscripción: el público pagaba por adelantado toda la temporada. Haydn ya no componía para un príncipe, sino para un público que tenía que salir contento y volver.</p>
<p>Su Sinfonía n.º 94 se estrenó allí el 23 de marzo de 1792. El golpe fuerte que le da el apodo de «La sorpresa» lo añadió Haydn al revisar la partitura: un efecto pensado para un público. <a href="#x-haydn-94-ii">Escúchalo</a>.</p>
<h2>Salones y alumnos</h2>
<p>Chopin daba pocos conciertos públicos y prefería tocar ante poca gente. En París vivía sobre todo de las clases a la aristocracia, a unos 20 francos la lección, una tarifa muy alta, y de vender sus obras a los editores. Por eso su música está pensada para salones: piezas íntimas como el <a href="#x-chopin-nocturno-postumo">Nocturno en do sostenido menor</a>.</p>
<h2>El sueldo de director</h2>
<p>A finales del siglo XIX, muchos compositores vivían de dirigir. Mahler era director de la Ópera de la Corte de Viena y solo podía componer en verano: <a href="#o-adagietto-mahler">el Adagietto</a> nació en su cabaña junto al lago.</p>
<h2>Llegan los discos</h2>
<p>En 1902, Enrico Caruso grabó diez arias en un hotel de Milán, y los discos se vendieron muchísimo. Desde entonces, la grabación es otra manera de ganarse la vida con la música, y la que te permite escuchar este diario.</p>"""),
dict(id="reconocer-compositores", tema="Estilos", titulo="Vivaldi, Bach, Chopin o Mahler: cómo distinguirlos de oído",
 entradilla="Cuatro preguntas rápidas para adivinar quién suena, con ejemplos del diario para comprobarlo.",
 h="""<h2>1. ¿Cuántos instrumentos hay?</h2>
<ul>
<li><b>Un piano solo</b> que canta: probablemente <a href="#c-chopin">Chopin</a>. Escucha el <a href="#x-chopin-nocturno-postumo">Nocturno en do sostenido menor</a>.</li>
<li><b>Un grupo de cuerda con clave</b>: Barroco, probablemente <a href="#c-vivaldi">Vivaldi</a> o <a href="#c-bach">Bach</a>. Escucha <a href="#o-cuatro-estaciones@0">la Primavera</a>.</li>
<li><b>Una orquesta enorme</b>, o una parte de ella que se queda sola: Romanticismo tardío, como <a href="#c-mahler">Mahler</a>. Escucha <a href="#x-mahler-5@33">la marcha fúnebre de la Quinta</a>.</li>
</ul>
<h2>2. ¿Una melodía o varias a la vez?</h2>
<ul>
<li><b>Una melodía clara arriba y un bajo abajo</b>: Vivaldi. Escucha <a href="#o-cuatro-estaciones@212">el Largo de la Primavera</a>.</li>
<li><b>Varias voces que se persiguen</b>, incluso con un solo instrumento: Bach. Escucha <a href="#o-suite-chelo-2@16">el preludio de la suite</a> o el <a href="#x-bwv-1048">Concierto de Brandeburgo n.º 3</a>.</li>
</ul>
<p>Lo explica a fondo <a href="#a-vivaldi-barroco">este artículo</a>.</p>
<h2>3. ¿El pulso es fijo o flexible?</h2>
<ul>
<li><b>Fijo, como un motor</b>: Barroco. Escucha <a href="#o-cuatro-estaciones@1066">la tempestad del Verano</a>.</li>
<li><b>Flexible, que se estira y se recoge</b>: Romanticismo. Escucha <a href="#o-balada-1-chopin">la Balada de Chopin</a> (<a href="#g-rubato">rubato</a>).</li>
<li><b>Muy lento y elástico, con frases que no acaban nunca</b>: Mahler. Escucha <a href="#o-adagietto-mahler">el Adagietto</a>.</li>
</ul>
<h2>4. ¿Cómo cambia el volumen?</h2>
<ul>
<li><b>Por bloques, sin crescendos largos</b>: Barroco. Escucha cómo entra y sale el grupo en <a href="#o-cuatro-estaciones@0">la Primavera</a>.</li>
<li><b>Crece poco a poco, durante minutos, hasta extremos</b>: Romanticismo. Escucha <a href="#o-adagietto-mahler">el Adagietto</a> o la coda de <a href="#o-balada-1-chopin">la Balada</a>.</li>
</ul>
<h2>Ponte a prueba</h2>
<p>Con estas cuatro preguntas, adivina de quién es cada una de estas obras antes de mirar el nombre en el reproductor:</p>
<ol>
<li><a href="#x-bwv-1065">Primera</a></li>
<li><a href="#x-chopin-op24@2815">Segunda</a></li>
<li><a href="#x-rv-580">Tercera</a></li>
<li><a href="#x-mahler-ich-bin">Cuarta</a></li>
</ol>
<p>Soluciones: Bach (adaptando a Vivaldi), Chopin, Vivaldi y Mahler. En cada compositor del diario tienes una lista de rasgos para reconocerlo y los intérpretes que mejor lo tocan.</p>"""),
dict(id="primer-concierto", tema="Conciertos", titulo="Tu primer concierto: guía práctica",
 entradilla="Cómo encontrar conciertos de lo que escuchas en el diario, qué hacer antes, cuándo aplaudir y cómo sacarle más partido.",
 h="""<h2>Elegir</h2>
<p>Empieza por algo que ya conozcas. Si te ha gustado una obra del diario, mira si se toca cerca: en <a href="#conciertos">Conciertos</a> puedes buscar por compositor, intérprete, país, ciudad y fechas. Cada ficha y cada compositor tienen además un atajo, «¿Dónde se toca?».</p>
<p>Un recital, con un solo intérprete, es más íntimo; un concierto de orquesta, más espectacular. Mira la web de la sala: muchas orquestas tienen precios reducidos para jóvenes, abonos y entradas de última hora.</p>
<h2>Antes</h2>
<ul>
<li>Escucha en casa la obra principal del programa al menos una vez. Si está en el diario, usa su guía de escucha.</li>
<li>Lee el programa de mano o la web: te dirá cuántos movimientos tiene cada obra.</li>
<li>Llega con tiempo. Si llegas tarde, normalmente tendrás que esperar a una pausa para entrar.</li>
</ul>
<h2>Durante: cuándo aplaudir</h2>
<p>Hoy la costumbre es aplaudir al final de la obra completa, no entre <a href="#g-movimiento">movimientos</a>. Si dudas, espera a que el director o el solista bajen los brazos, o a que aplaudan los demás. Nadie te va a reñir por equivocarte.</p>
<p>Mientras tanto, usa las tres preguntas de <a href="#a-como-escuchar">Cómo escuchar una obra</a>: quién toca, qué gesto hace y dónde estamos.</p>
<h2>Mira, además de escuchar</h2>
<p>En directo puedes ver lo que el disco esconde: quién lleva la melodía, cómo se miran los músicos para entrar a la vez y qué hace el director con las manos. Busca el instrumento que más te guste y síguelo un rato.</p>
<h2>Después</h2>
<p>Vuelve a escuchar la grabación del diario y compárala con lo que oíste. ¿Más rápido? ¿Más fuerte? Así se aprende a escuchar <a href="#a-tempo">el tempo</a> y las decisiones de cada intérprete.</p>"""),

dict(id="vivaldi-barroco", tema="Estilos", titulo="¿Por qué Vivaldi es barroco si parece tener una sola voz?",
 entradilla="La pregunta tiene trampa: el Barroco no se define por el número de voces. Lo que une a Vivaldi y a Bach está debajo: el bajo continuo.",
 h="""<h2>Lo que comparten: el bajo continuo</h2>
<p>Es fácil pensar que Bach son muchas voces y Vivaldi una sola, y que por eso Vivaldi sería ya clásico. Pero la frontera no está ahí. Escucha lo que pasa <b>debajo</b> de la melodía: en el Barroco casi siempre hay un <a href="#g-bajo-continuo">bajo continuo</a>, unos instrumentos graves que no paran y un instrumento de acordes (clave, órgano o laúd) que va rellenando. Ese motor desaparece en el Clasicismo.</p>
<ul>
<li><a href="#o-cuatro-estaciones@0">Vivaldi, Primavera, 0:00</a>. Debajo del estribillo, el bajo y los acordes no paran ni un momento.</li>
<li><a href="#o-cuatro-estaciones@1574">Vivaldi, Otoño II, 26:14</a>. Aquí el clave del continuo pasa al primer plano: la partitura le pide arpegiar los acordes mientras las cuerdas tocan con sordina.</li>
<li><a href="#x-bwv-1065">Bach, Concierto para cuatro claves, BWV 1065</a>. Bach también escribe con continuo: debajo de los cuatro solistas, los graves y los acordes no se detienen.</li>
</ul>
<p>La suite para violonchelo del diario es un caso especial: un chelo solo, sin continuo, que hace a la vez de melodía y de bajo (<a href="#o-suite-chelo-2@16">Bach, Preludio, 0:16</a>). Pero casi toda la música de conjunto de Bach lleva continuo, igual que la de Vivaldi.</p>
<h2>Vivaldi también tiene varias voces</h2>
<p>En sus movimientos lentos, Vivaldi superpone personajes. Escucha la <a href="#o-cuatro-estaciones@212">Primavera II, 3:32</a>: el violín solista canta tranquilo (el cabrero que duerme), los violines susurran como hojas y la viola ladra dos notas ásperas (el perro). Son tres capas a la vez.</p>
<h2>Dos acentos del mismo idioma</h2>
<p><b>Vivaldi habla italiano:</b> una melodía brillante arriba, un bajo que empuja y, a menudo, toda la orquesta tocando la misma línea al unísono, un recurso del que fue pionero con <i lang="it">L'estro armonico</i> (1711). Le importan el efecto, el virtuosismo y el teatro. Escucha la tempestad del <a href="#o-cuatro-estaciones@1066">Verano III, 17:46</a>.</p>
<p><b>Bach habla alemán con acento italiano:</b> unió la riqueza armónica del norte de Alemania con la energía del estilo italiano, y llenó cada hueco de contrapunto, varias melodías independientes a la vez. Incluso con un solo chelo sugiere dos voces (<a href="#o-suite-chelo-2@16">Preludio, 0:16</a>). Lo curioso es que aprendió ese acento italiano copiando a Vivaldi: en Weimar, en 1713–1714, transcribió conciertos suyos para clave y para órgano.</p>
<h2>La prueba: la misma música con dos acentos</h2>
<p>Bach tomó el concierto para cuatro violines de Vivaldi y lo convirtió en un concierto para cuatro claves, bajándolo de si menor a la menor. Escúchalos seguidos:</p>
<ol>
<li><a href="#x-rv-580">Vivaldi, Concierto para cuatro violines, RV 580</a>. Cuatro violines que se pasan la melodía, brillantes y directos.</li>
<li><a href="#x-bwv-1065">Bach, Concierto para cuatro claves, BWV 1065</a>. La misma música, con más notas por dentro: Bach rellena y entrelaza las líneas.</li>
</ol>
<h2>¿Y qué cambia en el Clasicismo?</h2>
<p>Con Haydn y Mozart desaparece el continuo, la textura se aclara, las frases se vuelven simétricas (pregunta y respuesta) y el piano sustituye al clave. En el volumen aparece algo nuevo: el <a href="#g-crescendo">crescendo</a>, el sonido que crece poco a poco. La orquesta de Mannheim lo convirtió en un efecto famoso en toda Europa.</p>
<h2>Cinco pistas para no confundirte</h2>
<ol>
<li><b>¿Oyes un instrumento de acordes rellenando debajo (clave, órgano o laúd)?</b> Casi seguro, Barroco. Ejemplo: <a href="#o-cuatro-estaciones@1574">Otoño II, 26:14</a>.</li>
<li><b>¿El ritmo avanza como un motor, sin frenar?</b> Barroco. Ejemplo: <a href="#o-cuatro-estaciones@1066">Verano III, 17:46</a>.</li>
<li><b>¿Cómo cambia el volumen?</b> Ojo: aquí no basta con «de golpe» o «poco a poco», porque los golpes de volumen existen en todas las épocas.
<ul>
<li><b>Barroco:</b> casi todo va por bloques, fuerte y piano, como ecos, y <b>sin crescendos largos</b>. El clave, por ejemplo, solo tiene dos niveles de volumen. Ejemplo: <a href="#o-cuatro-estaciones@609">Verano I, 10:09</a>, donde de las frases cansadas se pasa de golpe al viento del norte.</li>
<li><b>Clasicismo:</b> llegan los crescendos, y también los sustos calculados. Ejemplo: <a href="#x-haydn-94-ii">Haydn, Sinfonía «La sorpresa», II</a>: un tema muy suave y, al final de la segunda frase, un acorde fortísimo.</li>
<li><b>Romanticismo:</b> los contrastes se vuelven <b>enormes</b>, del casi silencio al estruendo, a veces de golpe y a veces creciendo durante mucho rato. Ejemplo: la <a href="#o-balada-1-chopin">Balada n.º 1 de Chopin</a>, en el paso 5 de su guía, donde el primer tema crece hasta que el segundo vuelve a pleno volumen.</li>
</ul>
La pregunta útil es otra: <b>¿hay crescendos largos?</b> y <b>¿cuánta distancia hay entre lo más suave y lo más fuerte?</b> Si todo va por bloques y no hay crescendos, piensa en Barroco.</li>
<li><b>¿Las frases son simétricas, como una canción de pregunta y respuesta?</b> Clasicismo. Escúchalo en el tema del <a href="#x-haydn-94-ii">Andante de Haydn</a>: sencillo como una canción infantil, de frases cortas y regulares.</li>
<li><b>¿El piano acompaña con acordes partidos que se repiten?</b> Es el bajo Alberti: Clasicismo. Todavía no hay ninguna obra para piano del Clasicismo en el diario.</li>
</ol>"""),
dict(id="instrumentos-epoca", tema="Instrumentos", titulo="Instrumentos de época: cómo reconocerlos en un vídeo",
 entradilla="Muchas grabaciones de música barroca usan instrumentos antiguos o copias de ellos. Se distinguen a simple vista y suenan distinto.",
 h="""<h2>Qué son</h2>
<p>Se llaman instrumentos de época los que se construyeron en el pasado o las réplicas modernas hechas según los modelos del Renacimiento y el Barroco. A tocar con ellos, y con la forma de tocar de entonces, se le llama interpretación historicista.</p>
<h2>Cómo reconocerlos a simple vista</h2>
<ul>
<li><b>Violines sin barbada:</b> el violín barroco no lleva la pieza donde hoy se apoya la barbilla. La barbada se inventó en tiempos de Beethoven.</li>
<li><b>Violonchelos sin pica:</b> el violonchelo barroco no tiene la punta metálica que hoy se apoya en el suelo. El músico lo sujeta entre las piernas.</li>
<li><b>Arcos distintos:</b> más cortos y ligeros, curvados hacia fuera, al revés que los modernos.</li>
<li><b>Instrumentos de acordes en el continuo:</b> clave, órgano pequeño, laúd o tiorba (un laúd enorme de mástil muy largo).</li>
</ul>
<h2>Cómo suenan</h2>
<ul>
<li><b>Cuerdas de tripa</b> en vez de metal: un sonido más suave, cálido y ágil, con menos potencia. Las cuerdas de tripa no se sustituyeron hasta el siglo XX.</li>
<li><b>Afinación más baja:</b> muchos grupos afinan aproximadamente un semitono por debajo del diapasón moderno.</li>
<li><b>Vibrato como adorno:</b> se usa en momentos concretos, no de forma continua como en el violín moderno.</li>
</ul>
<h2>Compáralo tú</h2>
<p>En el diario tienes los dos mundos: Voices of Music toca las Cuatro Estaciones con instrumentos de época, y Mischa Maisky toca a Bach con una sonoridad moderna y romántica. Mira los instrumentos y escucha la diferencia de sonido.</p>"""),
dict(id="rubato", tema="Interpretación", titulo="El rubato: por qué Chopin no suena a reloj",
 entradilla="Rubato significa «robado»: el pianista le roba tiempo a unas notas para dárselo a otras. Es la clave para escuchar a Chopin.",
 h="""<h2>Qué es</h2>
<p>En la suite de Bach el pulso de la danza es firme, como un paso. En Chopin el tiempo respira: la melodía se retrasa en una nota, se adelanta en otra y llega al final de la frase cuando le parece. Eso es el <b>rubato</b>, «tiempo robado».</p>
<h2>La idea original</h2>
<p>La palabra ya existía antes del Romanticismo y significaba tocar con libertad rítmica. Chopin fue el primer compositor que pidió el rubato de forma habitual en su música, y su consejo era claro: que la mano izquierda mantenga el tiempo y que la derecha, la de la melodía, se tome libertades por encima. Con los años, «rubato» pasó a significar en general acelerar y frenar.</p>
<h2>Cómo oírlo</h2>
<ol>
<li>Pon el primer tema de la <a href="#o-balada-1-chopin">Balada n.º 1</a> y marca el pulso con el pie.</li>
<li>Fíjate en qué notas de la melodía llegan tarde y en cuáles se alarga una pausa.</li>
<li>Escucha el mismo pasaje con otro pianista: cada uno «roba» en sitios distintos. Ahí está su personalidad.</li>
</ol>
<h2>Cuidado con el exceso</h2>
<p>Hay quien decía que Chopin «no sabía tocar a tempo», y hay pianistas que usan muy poco rubato. Sin pulso no hay nada que robar: el rubato solo funciona si debajo sigues notando el compás.</p>"""),
dict(id="titulos", tema="Método", titulo="Cómo leer el título de una obra",
 entradilla="«Ballade No. 1 in G minor, Op. 23». Parece un código, pero casi todos los títulos de música clásica se leen igual: tipo de obra, número, tonalidad y catálogo.",
 h="""<h2>Las cuatro piezas de un título</h2>
<p>Desmontemos <b>Ballade No. 1 in G minor, Op. 23</b>, de Chopin (<a href="#o-balada-1-chopin">está en el diario</a>):</p>
<ol>
<li><b>Ballade</b> (balada): el <b>tipo de obra</b>, también llamado género. Sinfonía, concierto, sonata, suite, nocturno o balada te dicen qué esperar: cuántos movimientos, para quién, con qué carácter.</li>
<li><b>No. 1</b> (n.º 1): el <b>número dentro de ese tipo</b>. Chopin escribió cuatro baladas y esta es la primera.</li>
<li><b>in G minor</b> (en sol menor): la <b>tonalidad</b>, la nota «casa» y su modo, mayor o menor.</li>
<li><b>Op. 23</b> (opus 23): el <b>número de catálogo</b>, para que no se confunda con ninguna otra obra.</li>
</ol>
<p>Algunas obras llevan además un <b>apodo</b>, como <i>Las cuatro estaciones</i> o la sonata <a href="#x-beethoven-claro-de-luna">«Claro de luna»</a> de Beethoven (Op. 27 n.º 2). El apodo ayuda a recordarla; el catálogo, a encontrarla.</p>
<h2>El número: no siempre es el orden en que se escribió</h2>
<p>El n.º 1 suele ser la primera obra de ese tipo, pero no siempre la primera que se compuso. Los dos conciertos para piano de Chopin son el ejemplo clásico: el <b>n.º 2</b>, en fa menor (<a href="#x-chopin-concierto-2">Op. 21</a>), lo terminó en 1829–1830 y se publicó en 1836; el <b>n.º 1</b>, en mi menor (<a href="#x-chopin-concierto-1">Op. 11</a>), es de 1830 y se publicó antes, en 1833. Se numeraron según salieron de la imprenta.</p>
<h2>La tonalidad y los nombres de las notas</h2>
<p>La tonalidad es la nota a la que la música quiere volver para descansar, y el modo: <b>mayor</b> (más luminoso) o <b>menor</b> (más sombrío). Como las grabaciones y las plataformas suelen usar el inglés o el alemán, conviene saber los nombres:</p>
<ul>
<li><b>Do</b> C · <b>Re</b> D · <b>Mi</b> E · <b>Fa</b> F · <b>Sol</b> G · <b>La</b> A · <b>Si</b> B (en alemán, H).</li>
<li><b>Sostenido</b> sharp (♯) · <b>bemol</b> flat (♭). En alemán, B a secas es si bemol.</li>
<li><b>Mayor</b> major, en alemán <i lang="de">Dur</i> · <b>menor</b> minor, en alemán <i lang="de">Moll</i>.</li>
</ul>
<p>Así, <i>G minor</i> y <i lang="de">g-Moll</i> son «sol menor», y <i>B-flat major</i> es «si bemol mayor».</p>
<h2>¿Se puede tocar en otra tonalidad?</h2>
<p>Se puede: se llama <a href="#g-transportar">transportar</a>. Los cantantes lo hacen a menudo para ajustar una canción a su voz, y muchas canciones se publicaban en versiones para voz aguda, media y grave.</p>
<p>Con una obra para piano como una balada de Chopin, en cambio, no se hace, por tres razones:</p>
<ul>
<li><b>La mano.</b> Cada tonalidad coloca los dedos de otra forma sobre las teclas blancas y negras. Los pasajes rápidos están pensados para esas teclas, y en otro tono habría que cambiar todas las digitaciones. A Chopin le importaba tanto que enseñaba a empezar las escalas por si mayor y no por do mayor, porque así los dedos largos caen sobre las teclas negras y la mano queda cómoda.</li>
<li><b>El sonido.</b> Toda la obra sonaría más aguda o más grave, y el piano resuena distinto en cada zona.</li>
<li><b>El color.</b> En el siglo XIX convivían varias maneras de afinar, y en algunas cada tonalidad sonaba un poco distinta; muchos músicos de entonces atribuían un carácter a cada una. Con la afinación actual la diferencia es sobre todo de altura, y hasta qué punto se nota es un debate abierto. Aun así, el tono forma parte de la obra tal como la escribió el compositor.</li>
</ul>
<h2>Opus y catálogos: qué significa el número</h2>
<p><b>Opus</b> es «obra» en latín. Desde comienzos del siglo XIX, los compositores solían dar un número de opus a cada obra al publicarla. Ese número <b>no dice cuántas piezas hay</b>:</p>
<ul>
<li>El <b>Op. 23</b> de Chopin es <a href="#o-balada-1-chopin">una sola balada</a> de unos diez minutos.</li>
<li>Su <b>Op. 24</b> son <a href="#x-chopin-op24@2815">cuatro mazurcas</a>, y su <b>Op. 28</b>, <a href="#x-chopin-op28">veinticuatro preludios</a>.</li>
<li>El <b>Op. 8</b> de Vivaldi reúne doce conciertos. Por eso <a href="#o-cuatro-estaciones">la Primavera</a> es el <b>Op. 8 n.º 1</b>: el segundo número dice cuál de ellos es.</li>
</ul>
<p>Muchos compositores no numeraron sus obras, o dejaron muchas sin publicar. Para ellos, los estudiosos han hecho <b>catálogos</b>, y cada uno tiene sus siglas:</p>
<ul>
<li><b>BWV</b>, Bach: de Wolfgang Schmieder (1950). Ordena por géneros, no por fechas: <a href="#x-bwv-1">BWV 1</a> no es la primera obra de Bach, sino una cantata de 1725.</li>
<li><b>RV</b>, Vivaldi: de Peter Ryom.</li>
<li><b>K.</b> o <b>KV</b>, Mozart: de Ludwig von Köchel (1862). Se pensó en orden cronológico, de K. 1, un minueto de niño, a K. 626, el <a href="#x-mozart-requiem">Réquiem</a> que dejó sin terminar.</li>
<li><b>Hob.</b>, Haydn: de Anthony van Hoboken.</li>
<li><b>D.</b>, Schubert: de Otto Erich Deutsch.</li>
</ul>
<h2>Un truco para buscar</h2>
<p>En Idagio o en YouTube, busca por <b>compositor y catálogo</b>: «Chopin Op. 23» (<a href="#o-balada-1-chopin">la balada</a>), «Bach BWV 1008» (<a href="#o-suite-chelo-2">la suite n.º 2</a>) o «Vivaldi RV 269» (<a href="#o-cuatro-estaciones">la Primavera</a>). Es la forma más segura de dar con esa obra exacta y no con otra de título parecido.</p>"""),
dict(id="como-escuchar", tema="Método", titulo="Cómo escuchar una obra: tres preguntas",
 entradilla="No hace falta saber solfeo. Con tres preguntas mientras suena, ya no estás perdido en ningún movimiento.",
 h="""<h2>Antes</h2>
<p>Lee la ficha: quién la escribió, para quién y qué cuenta. Dos minutos de contexto cambian lo que oyes.</p>
<h2>Mientras suena</h2>
<ol>
<li><b>¿Quién toca?</b> ¿Todo el grupo o un solista? ¿Qué instrumento lleva la melodía y cuál el bajo?</li>
<li><b>¿Qué gesto hace?</b> Un trino, un trémolo, un pizzicato, una nota grave que no se mueve… Son palabras con significado, y las vas sumando en el <a href="#glosario">glosario</a>.</li>
<li><b>¿Dónde estamos?</b> ¿Ha vuelto algo que ya sonó? Reconocer lo que se repite (un estribillo, un tema) es la mejor brújula.</li>
</ol>
<h2>El truco de los que saben: escuchar por capas</h2>
<p>Quien entiende de música no oye un bloque. Elige un instrumento, la viola, el clave o el bajo, y síguelo durante un minuto. Luego elige otro. Poco a poco oirás las capas a la vez.</p>
<h2>Después</h2>
<p>Escucha otra versión de la misma obra. Lo que cambia entre dos intérpretes te enseña qué decide el músico y qué está escrito.</p>"""),
]

GLOSARIO = [
 ("metronomo","Metrónomo","Aparato que marca golpes regulares, tantos por minuto como se le pida, para fijar el tempo. Lo patentó Maelzel en 1815 a partir de una idea del holandés Winkel; por eso en las partituras aparece «M. M.», metrónomo de Maelzel."),
 ("mecenas","Mecenas","Persona o institución que paga a un artista para que cree: la iglesia, un príncipe, un noble o, hoy, una fundación. Dedicarle una obra era una forma de agradecer o de pedir su protección."),
 ("cantata","Cantata","Obra para voces e instrumentos en varios movimientos: coros, arias (cantos a solo) y recitativos (canto que casi habla). Bach escribió muchísimas para los domingos de Leipzig."),
 ("mazurca","Mazurca","Danza popular polaca en compás de tres tiempos, con acentos que caen a menudo en el segundo o el tercero. Chopin la convirtió en pieza de concierto para piano."),
 ("nocturno","Nocturno","Pieza para piano lenta y soñadora: una melodía que canta sobre un acompañamiento ondulante. Lo creó el irlandés John Field y Chopin lo hizo suyo."),
 ("requiem","Réquiem","Misa de difuntos. Su texto en latín empieza con «Requiem aeternam», «descanso eterno», y por eso se llama así."),
 ("sonata","Sonata","Obra instrumental en varios movimientos para un instrumento solo, o para un instrumento con piano. No hay que confundirla con la forma sonata, que es una manera de construir un movimiento."),
 ("sinfonia","Sinfonía","Obra grande para orquesta, dividida en varios movimientos. En el Clasicismo suele tener cuatro: rápido, lento, minueto o scherzo, y rápido. Los románticos la agrandaron: la Quinta de Mahler tiene cinco movimientos y dura más de una hora."),
 ("arpa","Arpa","Instrumento de cuerdas que se pellizcan con los dedos, tensadas en un marco triangular. En la orquesta suele acompañar con acordes desgranados (arpegios) y da un brillo suave."),
 ("cuerda","Cuerda","La familia de instrumentos de cuerda frotada con arco de la orquesta: violines, violas, violonchelos y contrabajos. Es el núcleo de casi toda orquesta."),
 ("tempo","Tempo","La velocidad de la música. Se indica con palabras, casi siempre en italiano: <i lang=\"it\">largo</i> y <i lang=\"it\">adagio</i> (lentos), <i lang=\"it\">andante</i> (al paso), <i lang=\"it\">allegro</i> y <i lang=\"it\">presto</i> (rápidos). Los diminutivos suavizan: un <i lang=\"it\">adagietto</i> es algo menos lento que un adagio. Mahler escribía sus indicaciones en alemán: <i lang=\"de\">sehr langsam</i>, «muy lento»."),
 ("lied","Lied (en plural, lieder)","«Canción» en alemán. Una canción de concierto, casi siempre sobre un poema, para voz y piano o para voz y orquesta. Schubert, Schumann, Brahms y Mahler escribieron muchos."),
 ("director","Director de orquesta","Quien dirige a la orquesta: decide el tempo, el equilibrio entre los instrumentos y el carácter, y lo transmite con gestos en los ensayos y en el concierto. La partitura es la misma, pero cada director la hace sonar distinta."),
 ("arreglo","Arreglo","Adaptar una obra para instrumentos distintos de los que escribió el compositor: por ejemplo, un violonchelo con un piano en lugar de con dos, o con arpa, o con orquesta. La música es la misma; cambia quién la toca."),
 ("arpegio","Arpegio","Tocar las notas de un acorde una detrás de otra, en lugar de todas a la vez. Es el acompañamiento típico del arpa y del piano: crea un fondo que ondula."),
 ("legato","Legato","«Ligado» en italiano: tocar o cantar las notas unidas, sin cortes entre ellas, como una línea continua. Lo contrario es el staccato: notas cortas y separadas."),
 ("vibrato","Vibrato","Una oscilación pequeña y rápida de la altura de una nota, que la hace temblar y le da calor. En los instrumentos de cuerda se consigue balanceando el dedo que pisa la cuerda; en el canto, con la voz."),
 ("allemande","Allemande","Danza de origen alemán, de paso moderado y compás binario. Abre la serie de danzas en las suites de Bach."),
 ("bajo-continuo","Bajo continuo","El cimiento de la música barroca: una línea de bajo (violonchelo, contrabajo, fagot…) más un instrumento de acordes (clave, órgano, laúd o tiorba) que improvisa la armonía a partir de esa línea. Desaparece hacia 1800."),
 ("catalogo","Catálogo (BWV, RV, K., Op.)","Los números que identifican una obra. <b>BWV</b> es el catálogo de las obras de Bach (Bach-Werke-Verzeichnis), de Wolfgang Schmieder; <b>RV</b>, el de Vivaldi, de Peter Ryom; <b>K.</b> o <b>KV</b>, el de Mozart, de Ludwig von Köchel; <b>Hob.</b>, el de Haydn, de Anthony van Hoboken, y <b>D.</b>, el de Schubert, de Otto Erich Deutsch. <b>Op.</b> (<a href=\"#g-opus\">opus</a>) es el número de publicación. Más en <a href=\"#a-titulos\">Cómo leer el título de una obra</a>."),
 ("clave","Clave","Instrumento de teclado en el que las cuerdas se pellizcan con una púa, en lugar de golpearse con macillos como en el piano. Sonido brillante, sin crescendos. Es el corazón del continuo barroco."),
 ("concierto","Concierto","Obra en la que uno o varios solistas dialogan con el grupo. En el Barroco suele tener tres movimientos: rápido, lento y rápido."),
 ("contrapunto","Contrapunto","El arte de combinar varias melodías independientes que suenan a la vez y encajan entre sí."),
 ("courante","Courante","Danza rápida de origen francés, en compás ternario."),
 ("da-capo","Da capo","«Desde el principio»: volver a tocar una sección ya escuchada. En los minuetos de las suites: Minueto I, Minueto II y otra vez Minueto I."),
 ("dinamica-terrazas","Dinámica en terrazas","Cambios de volumen por bloques, de fuerte a piano y al revés, sin pasos intermedios, en vez de crescendos graduales. Es lo típico del Barroco: el clave solo tiene dos niveles de volumen, y para tocar más fuerte se suman instrumentos. Ojo: los golpes de volumen existen en todas las épocas; lo barroco es que casi todo vaya por bloques y no haya crescendos largos."),
 ("crescendo","Crescendo y diminuendo","Hacer crecer el volumen poco a poco (crescendo) o apagarlo poco a poco (diminuendo). En el Barroco casi no se escriben. En el Clasicismo, la orquesta de Mannheim los convirtió en un efecto famoso, y en el Romanticismo llegan a durar tramos muy largos, de un susurro a un estruendo."),
 ("doble-cuerda","Doble cuerda","Tocar dos cuerdas a la vez con el arco para que suenen dos notas, o acordes si son más."),
 ("forma-sonata","Forma sonata","El molde más importante del Clasicismo: se presentan dos temas contrastados (exposición), se transforman (desarrollo) y vuelven (reexposición)."),
 ("fuga","Fuga","Pieza de contrapunto en la que un tema entra sucesivamente en cada voz, que lo imitan y lo desarrollan."),
 ("galanterias","Galanterías","Las danzas «de moda» (minuetos, bourrées o gavotas) que Bach coloca entre la zarabanda y la giga en sus suites."),
 ("giga","Giga","Danza rápida y saltarina de origen inglés (la <i>jig</i>). Cierra las suites."),
 ("minueto","Minueto","Danza elegante en compás de tres, de origen francés. En las suites se toca en pareja: I, II y vuelta al I."),
 ("movimiento","Movimiento","Cada una de las partes de una obra larga, separadas por una pausa. La costumbre es no aplaudir entre ellos."),
 ("musica-programatica","Música programática","Música instrumental que cuenta o describe algo de fuera de la música (una historia, un paisaje), a menudo con un texto que la acompaña."),
 ("pizzicato","Pizzicato","Pellizcar las cuerdas con el dedo en lugar de frotarlas con el arco. Da notas cortas, como gotas."),
 ("polifonia-implicita","Polifonía implícita","Cuando una sola línea melódica, saltando entre notas graves y agudas, se oye como dos o más voces a la vez."),
 ("preludio","Preludio","Pieza de introducción, a menudo libre, que abre una suite o va delante de una fuga."),
 ("ritornello","Ritornello","El estribillo de los movimientos rápidos del concierto barroco: el grupo lo repite, a veces solo un trozo, entre las intervenciones del solista."),
 ("sordina","Sordina","Pieza que se coloca sobre el puente de un instrumento de cuerda para velar su sonido."),
 ("suite","Suite","Serie de danzas en la misma tonalidad, a menudo con un preludio delante. En las de Bach: preludio, allemande, courante, zarabanda, galanterías y giga."),
 ("balada","Balada","En literatura, un poema que cuenta una historia. Chopin fue el primero en dar el nombre a una pieza solo instrumental, sin palabras, de carácter narrativo."),
 ("coda","Coda","«Cola»: la sección final que cierra una obra o un movimiento, a menudo con un último arranque de energía."),
 ("compas","Compás","La forma en que se agrupan los pulsos. En 3/4 se cuenta 1-2-3, como en un vals; en 6/4 o 6/8, en dos grupos de tres, con un balanceo que suena a narración."),
 ("opus","Opus (Op.)","«Obra» en latín. El número que recibe una obra, o un grupo de obras, al publicarse. <b>No dice cuántas piezas hay</b>: el Op. 23 de Chopin es una sola balada, y su Op. 28, veinticuatro preludios. Cuando un opus reúne varias obras, se añade otro número: Op. 8 n.º 1. Tampoco indica siempre el orden en que se compusieron."),
 ("pedal","Pedal","En el piano, el pedal derecho deja vibrar las cuerdas al soltar las teclas. Une los sonidos y crea resonancia; los románticos lo usan muchísimo."),
 ("pieza-de-caracter","Pieza de carácter","Pieza breve para piano que retrata un estado de ánimo o una escena: nocturnos, baladas, intermezzos. Es uno de los grandes géneros del Romanticismo."),
 ("rubato","Rubato","«Tiempo robado»: el intérprete se adelanta o se retrasa a propósito para dar expresión. Chopin pedía mantener firme la mano izquierda y dejar libre la derecha."),
 ("tema","Tema","Una melodía o idea musical reconocible que la obra presenta y luego repite, transforma o desarrolla. Reconocer los temas es la mejor brújula para no perderse."),
 ("tocata","Tocata","Pieza de teclado de carácter libre, como improvisada, pensada para lucir al intérprete."),
 ("tonalidad","Tonalidad (mayor y menor)","La «casa» de una obra: la nota a la que la música quiere volver para descansar (en «sol menor», el sol) y el tipo de escala que se usa a su alrededor. Hay dos modos: simplificando, el <b>mayor</b> suena luminoso y el <b>menor</b>, sombrío. La música se aleja de su tonalidad y vuelve: ese ir y volver es lo que se oye como tensión y reposo. En inglés y alemán las notas van con letras: C do, D re, E mi, F fa, G sol, A la, B si (en alemán, H es si y B es si bemol)."),
 ("transportar","Transportar","Tocar o cantar una obra en otra tonalidad, más aguda o más grave. Los cantantes lo hacen a menudo para ajustarla a su voz, y muchas canciones se publicaban para voz aguda, media y grave. En el piano casi nunca se hace con obras de repertorio: cambia la posición de la mano sobre las teclas y el sonido del instrumento."),
 ("tremolo","Trémolo","Repetir muy rápido la misma nota, o alternar dos, creando un temblor sonoro. Vivaldi lo usa para los truenos."),
 ("trino","Trino","Alternancia rapidísima entre dos notas vecinas. Es un adorno, y también el canto de pájaro más usado en música."),
 ("tutti","Tutti","«Todos»: el grupo entero tocando, frente al solista."),
 ("zarabanda","Zarabanda","Danza lenta de origen español, en compás de tres, con el apoyo en el segundo tiempo."),
]

CURIOSIDADES = [
 dict(t="Saint-Saëns no quiso publicar <i>El carnaval de los animales</i> en vida: solo dejó salir <i>El cisne</i>, en 1887. El resto se publicó en 1922, tras su muerte, porque así lo dejó escrito en su testamento.", l="#o-el-cisne"),
 dict(t="La bailarina Anna Pávlova bailó <i>La muerte del cisne</i>, con la música de Saint-Saëns, unas 4.000 veces.", l="#x-cisne-ballet"),
 dict(t="En la final del Concurso Chopin de 2015, nueve de los diez finalistas eligieron el Concierto n.º 1. Solo uno, Charles Richard-Hamelin, tocó el n.º 2, y quedó segundo.", l="#x-chopin-concierto-2"),
 dict(t="El metrónomo lleva el nombre de Maelzel, pero el doble péndulo lo había ideado el holandés Winkel. Una comisión de Ámsterdam le dio la razón a Winkel.", l="#a-tempo"),
 dict(t="Chopin cobraba unos 20 francos por clase, una tarifa altísima para su época. Vivía más de enseñar que de dar conciertos.", l="#a-quien-pagaba"),
 dict(t="En 2021, el pianista español Martín García García ganó el tercer premio del Concurso Chopin de Varsovia.", l="#c-chopin"),
 dict(t="Leonard Bernstein fue enterrado con una partitura de la Quinta de Mahler sobre el corazón.", l="#i-bernstein"),
 dict(t="El Adagietto de Mahler se estrenó en el Reino Unido en 1909, 36 años antes que la sinfonía completa.", l="#o-adagietto-mahler"),
 dict(t="Chopin pasó el invierno de 1838–1839 en la Cartuja de Valldemossa, en Mallorca. El pequeño piano Pleyel en el que terminó sus Preludios todavía se conserva allí.", l="#c-chopin"),
 dict(t="La Balada n.º 1 de Chopin es la pieza que Szpilman toca para el oficial alemán en <i>El pianista</i>, de Polanski.", l="#o-balada-1-chopin"),
 dict(t="Chopin dio solo unos 30 conciertos públicos en toda su vida: prefería los salones a las grandes salas.", l="#c-chopin"),
 dict(t="Krystian Zimerman viaja con sus propios pianos Steinway, que él mismo afina y modifica.", l="#i-zimerman"),
 dict(t="Vivaldi y Bach murieron el mismo día del año, un 28 de julio: Vivaldi en 1741 y Bach en 1750.", l="#c-bach"),
 dict(t="A Vivaldi le llamaban <i lang=\"it\">il prete rosso</i>, «el cura rojo», por su pelo pelirrojo.", l="#c-vivaldi"),
 dict(t="Pau Casals tenía 13 años cuando encontró en una tienda de Barcelona la edición de las suites para violonchelo de Bach que acabaría haciendo famosas.", l="#i-casals"),
 dict(t="En 1717 el duque de Weimar no quería dejar marchar a Bach y lo tuvo cuatro semanas arrestado antes de permitirle irse a Köthen.", l="#c-bach"),
 dict(t="Mischa Maisky decidió regrabar las suites de Bach cuando, en una tienda, no reconoció su propia grabación.", l="#i-maisky"),
 dict(t="La Tocata y fuga en re menor, la pieza de órgano más famosa del mundo, quizá no sea de Bach: algunos expertos lo ponen en duda.", l="#c-bach"),
 dict(t="Las Cuatro Estaciones se grabaron por primera vez en 1947. Hoy existe una cantidad enorme de versiones.", l="#o-cuatro-estaciones"),
]

DESTACADO = "tempo"
