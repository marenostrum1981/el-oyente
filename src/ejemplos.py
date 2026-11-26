# Ejemplos para escuchar cada término del glosario.
# Cada ejemplo es uno de estos:
#   dict(o=<id de obra>, t=<segundo>, txt=...)  -> suena ese momento en el reproductor (t debe ser
#                                                  el inicio de un capítulo de esa obra, o 0)
#   dict(o=<id de obra>, txt=...)               -> enlace a la ficha (cuando no hay minuto exacto)
#   dict(x=<id de REFERENCIAS>, t=<segundo>, txt=...) -> obra de fuera del diario (src/referencias.py)
#   dict(url=..., quien=..., txt=...)           -> enlace externo sin reproductor
#   dict(txt=...)                               -> ejemplo escrito (para términos que no se oyen)
# build_data.py comprueba que las obras existen y que los segundos son capítulos reales.

CE = "cuatro-estaciones"   # Vivaldi, Voices of Music
SU = "suite-chelo-2"       # Bach, Maisky
BA = "balada-1-chopin"     # Chopin, Zimerman (sin capítulos: solo t=0)
MA = "adagietto-mahler"    # Mahler, Bernstein (sin capítulos: solo t=0)
CI = "el-cisne"            # Saint-Saëns, Yo-Yo Ma y Kathryn Stott (sin capítulos: solo t=0)
VE = "venus-holst"         # Holst, Karajan y la Filarmónica de Berlín (sin capítulos: solo t=0)
AOB = "https://www.bachvereniging.nl/en/bwv/bwv-"

EJEMPLOS = {
 "trompa": [
  dict(o=VE, t=0, txt="Venus empieza con la trompa sola, muy suave: cuatro notas que suben."),
  dict(x="mahler-5", t=1716, txt="En el Scherzo de la Quinta de Mahler, una trompa solista lleva la voz cantante de principio a fin."),
  dict(x="planetas", t=0, txt="La otra cara: en Marte, las seis trompas de Holst suenan como un ejército."),
 ],
 "celesta": [
  dict(o=VE, t=0, txt="En Venus, la celesta salpica notas de campanita sobre los acordes de flautas y arpas (paso 2 de la guía)."),
  dict(x="cascanueces-hada", txt="La Danza del hada de azúcar de El cascanueces: aquí la celesta lleva la melodía."),
  dict(x="planetas", t=2561, txt="En Neptuno, la celesta y las arpas crean un brillo misterioso."),
 ],
 "timbre": [
  dict(x="schoenberg-farben", t=0, txt="«Colores», de Schönberg: los acordes casi no cambian; lo que cambia es el color de los instrumentos que los tocan."),
  dict(o=VE, t=0, txt="Venus está hecha de colores: trompa, flautas, arpas, celesta y violín solo."),
  dict(x="carnaval", t=973, txt="En «Fósiles», el xilófono suena a huesos que chocan: el timbre cuenta la broma."),
 ],
 "ostinato": [
  dict(x="planetas", t=0, txt="Marte: el mismo ritmo de cinco tiempos, una y otra vez, como una máquina."),
  dict(x="st-paul", t=253, txt="El segundo movimiento de la St Paul's Suite de Holst se llama así, «Ostinato»: una figura que gira sin parar."),
 ],
 "arreglo": [
  dict(o=CI, t=0, txt="El cisne en su arreglo para violonchelo y un solo piano, el que se publicó en 1887."),
  dict(x="carnaval", t=1058, txt="El original, dentro del Carnaval, con dos pianos. Compara los dos acompañamientos."),
  dict(x="bwv-1065", txt="Bach también hacía arreglos: convirtió un concierto de Vivaldi para cuatro violines en este para cuatro claves."),
 ],
 "arpegio": [
  dict(o=CI, t=0, txt="El piano desgrana acordes nota a nota, sin parar, por debajo del violonchelo: es el agua."),
  dict(o=MA, t=0, txt="En el Adagietto de Mahler, el arpa hace lo mismo bajo la melodía de la cuerda."),
  dict(x="carnaval", t=500, txt="En «Acuario», los pianos ondulan con arpegios rapidísimos: otra vez agua."),
 ],
 "legato": [
  dict(o=CI, t=0, txt="La melodía del violonchelo, sin un solo corte entre nota y nota."),
  dict(x="carnaval", t=973, txt="Lo contrario: en «Fósiles», el xilófono toca notas cortas y secas, como huesos que chocan."),
 ],
 "vibrato": [
  dict(o=CI, t=0, txt="Escucha las notas largas del violonchelo: tiemblan un poco. Ese temblor es el vibrato."),
  dict(url="https://youtu.be/xPsOt6fLDFY", quien="Mischa Maisky", txt="Otro violonchelista, otro vibrato: compara cómo hace temblar Maisky las notas largas."),
 ],
 "metronomo": [
  dict(o=SU, t=16, txt="El preludio de Bach avanza con un pulso regular, casi de metrónomo."),
  dict(o=BA, t=0, txt="Compáralo con Chopin: el pulso se estira y se recoge, nada de metrónomo (rubato)."),
 ],
 "mecenas": [
  dict(x="bwv-1048", txt="Bach envió este concierto y otros cinco al margrave de Brandeburgo, con una dedicatoria llena de reverencias."),
  dict(o=CE, t=0, txt="Vivaldi dedicó el Opus 8, el de las Estaciones, al conde Wenzel von Morzin."),
 ],
 "cantata": [
  dict(x="bwv-1", txt="Una cantata de Bach de 1725: empieza con un gran coro y sigue con recitativos y arias."),
 ],
 "mazurca": [
  dict(x="chopin-op24", t=2815, txt="La primera de las cuatro mazurcas del Op. 24 de Chopin. Cuenta 1-2-3 y busca dónde cae el acento."),
  dict(x="chopin-op24", t=3019, txt="La segunda, más animada."),
 ],
 "nocturno": [
  dict(x="chopin-nocturno-postumo", txt="El nocturno que suena en «El pianista»: la mano derecha canta y la izquierda ondula."),
 ],
 "requiem": [
  dict(x="mozart-requiem", t=79, txt="El comienzo del Réquiem de Mozart: «Requiem aeternam»."),
  dict(x="mozart-requiem", t=1369, txt="El Lacrimosa, uno de sus fragmentos más conocidos."),
 ],
 "sonata": [
  dict(x="beethoven-claro-de-luna", txt="Una sonata para piano en tres movimientos, aquí en un fortepiano como el de la época de Beethoven."),
  dict(x="beethoven-claro-de-luna", t=418, txt="El tercer movimiento, rapidísimo: el contraste con el primero."),
 ],
 "allemande": [
  dict(o=SU, t=278, txt="Paso moderado, en cuatro tiempos, que avanza con calma. Fíjate en las notas dobles que lo frenan de vez en cuando."),
 ],
 "bajo-continuo": [
  dict(o=CE, t=0, txt="Debajo del estribillo, los instrumentos graves llevan el bajo y un instrumento de acordes lo rellena. No paran ni un momento: ese suelo es el continuo."),
  dict(o=CE, t=1574, txt="Aquí el instrumento de acordes del continuo pasa al primer plano: Vivaldi escribe en la partitura «il cembalo arpeggio», que el clave toque los acordes nota a nota, mientras las cuerdas tocan con sordina."),
  dict(o=SU, t=16, txt="El contraste: en la suite de Bach no hay continuo. El violonchelo, solo, hace a la vez de melodía y de bajo."),
 ],
 "catalogo": [
  dict(txt="<b>BWV 1008</b> es la Suite n.º 2 para violonchelo de Bach; <b>RV 269</b>, la Primavera de Vivaldi; <b>Op. 23</b>, la Balada n.º 1 de Chopin."),
 ],
 "clave": [
  dict(o=CE, t=1574, txt="Escucha el clave arpegiando acordes, nota a nota, sobre las cuerdas veladas: un sonido punteado y brillante, que no crece ni se apaga como el del piano."),
 ],
 "concierto": [
  dict(o=CE, t=0, txt="El grupo toca un estribillo y, entre medias, el violín solista se separa para pintar escenas: los pájaros, las fuentes que murmuran, la tormenta."),
  dict(o=CE, t=212, txt="El segundo movimiento, lento. Tras él vendrá otro rápido: rápido, lento, rápido."),
 ],
 "contrapunto": [
  dict(o=SU, t=16, txt="Contrapunto escondido: una sola línea que tu oído separa en dos voces."),
  dict(x="bwv-1065", t=0, txt="Contrapunto a la vista: cuatro claves, cada uno con su línea, que encajan entre sí. Es su versión del concierto para cuatro violines RV 580 de Vivaldi."),
 ],
 "courante": [
  dict(o=SU, t=527, txt="Rápida, de notas cortas sin parar, como si alguien te persiguiera."),
 ],
 "da-capo": [
  dict(o=SU, t=1127, txt="En la partitura, al acabar el Minueto II pone «Menuet I da capo»: hay que volver al primero. Escucha desde aquí y comprueba si el chelista repite el Minueto I antes de la giga."),
 ],
 "dinamica-terrazas": [
  dict(o=CE, t=609, txt="El verano empieza con frases cansadas, cortadas por silencios, y de golpe el viento del norte entra a todo volumen. No hay crescendo: se pasa de un bloque a otro."),
  dict(x="haydn-94-ii", t=0, txt="Para no confundirte: un golpe de volumen no basta para decir «Barroco». Este Andante de Haydn, del Clasicismo, empieza muy suave y al final de la segunda frase suelta un acorde fortísimo, por sorpresa."),
 ],
 "sinfonia": [
  dict(x="mahler-5", t=33, txt="La Quinta de Mahler empieza con una trompeta sola que abre una marcha fúnebre: más de una hora de sinfonía por delante."),
  dict(x="haydn-94-ii", t=0, txt="El movimiento lento de una sinfonía clásica de Haydn: más corta, más ligera y con una orquesta más pequeña."),
 ],
 "arpa": [
  dict(o=MA, t=0, txt="Desde el principio, el arpa sostiene la armonía por debajo de las cuerdas, casi como un bajo continuo."),
 ],
 "cuerda": [
  dict(o=MA, t=0, txt="Solo cuerda y arpa: el sonido de la cuerda de una gran orquesta, sin nada más."),
  dict(o=CE, t=0, txt="Una orquesta barroca de cuerda, con su bajo continuo."),
 ],
 "tempo": [
  dict(o=CE, t=0, txt="Primavera I, <i lang=\"it\">Allegro</i>: rápido y alegre."),
  dict(o=CE, t=212, txt="Primavera II, <i lang=\"it\">Largo</i>: muy lento."),
  dict(o=MA, t=0, txt="Mahler, <i lang=\"de\">Sehr langsam</i>, «muy lento». Cada director lo entiende a su manera: hay versiones de 7 minutos y de casi 14."),
 ],
 "lied": [
  dict(x="mahler-ich-bin", t=0, txt="Un lied de Mahler con orquesta, sobre un poema de Friedrich Rückert. Su melodía es la que cierra el Adagietto."),
 ],
 "director": [
  dict(o=MA, t=0, txt="Bernstein se toma unos 12 minutos para el Adagietto. Mahler y Mengelberg lo tocaban en unos 7."),
  dict(x="mahler-5", t=2779, txt="El mismo Adagietto con otro director y otra orquesta: compara el tempo y el carácter."),
 ],
 "crescendo": [
  dict(o=MA, txt="En el Adagietto de Mahler, la melodía crece y se calma varias veces, como respiraciones cada vez más hondas (paso 3 de la guía)."),
  dict(o=BA, txt="En la balada, el paso 5 de la guía: el primer tema crece y crece hasta que el segundo vuelve, convertido en una declaración apasionada a pleno volumen."),
  dict(txt="En el Barroco no busques crescendos largos: los cambios van por bloques. Compáralo con el <a href=\"#g-dinamica-terrazas\">Verano de Vivaldi</a>."),
 ],
 "doble-cuerda": [
  dict(o=SU, t=649, txt="La zarabanda está llena de acordes de dos y tres notas: un solo chelo suena más lleno, casi como varios."),
  dict(o=SU, t=1048, txt="El Minueto I arranca con un acorde de re menor tocado de golpe."),
 ],
 "forma-sonata": [
  dict(o=BA, t=0, txt="La balada juega con este molde: dos temas que se presentan, se transforman y vuelven en otro orden. Síguelos con los pasos 2, 4 y 6 de la guía de la ficha."),
 ],
 "fuga": [
  dict(x="bwv-565", t=0, txt="Tras la tocata del principio empieza la fuga: un tema suena solo y las demás voces entran después, una a una, imitándolo."),
 ],
 "galanterias": [
  dict(o=SU, t=1048, txt="Los dos minuetos de esta suite son sus galanterías: danzas de moda, más ligeras, entre la zarabanda y la giga."),
 ],
 "giga": [
  dict(o=SU, t=1256, txt="Saltos grandes y ritmo saltarín: así se cierra la suite, con energía."),
 ],
 "minueto": [
  dict(o=SU, t=1048, txt="Cuenta 1-2-3 mientras suena: es un baile elegante, de salón."),
 ],
 "movimiento": [
  dict(x="mahler-5", t=2779, txt="El Adagietto es el cuarto de los cinco movimientos de la Quinta de Mahler: aquí empieza, justo después del Scherzo."),
  dict(o=CE, t=212, txt="Aquí acaba el primer movimiento de la Primavera y empieza el segundo: hay una pausa y cambian el tempo y el ambiente. En concierto, no se aplaude aquí."),
 ],
 "musica-programatica": [
  dict(o=CE, t=0, txt="Pájaros, fuentes que murmuran y una tormenta. Todo está descrito en un soneto impreso junto a la música."),
  dict(o=CE, t=1916, txt="El invierno: tiritar, pisotones para entrar en calor y dientes que castañetean."),
 ],
 "opus": [
  dict(txt="El <b>Op. 23</b> de Chopin es una sola balada; su <b>Op. 28</b> son veinticuatro preludios. La Primavera de Vivaldi es el <b>Op. 8 n.º 1</b>: el primero de los doce conciertos de su Op. 8."),
 ],
 "pizzicato": [
  dict(o=CE, t=2129, txt="Los violines pellizcan las cuerdas: son las gotas de lluvia que caen fuera mientras el solista canta tranquilo junto al fuego."),
 ],
 "polifonia-implicita": [
  dict(o=SU, t=16, txt="Una sola línea que salta entre notas graves y agudas. Al rato, tu oído la oye como dos voces."),
 ],
 "preludio": [
  dict(x="chopin-op28", t=246, txt="Los preludios de Chopin son piezas cortas e independientes, uno en cada tonalidad. Este es el n.º 4, uno de los más famosos."),
  dict(o=SU, t=16, txt="Abre la suite antes de las danzas, con aire libre, como si el chelista pensara en voz alta. Al final, cinco acordes largos."),
 ],
 "ritornello": [
  dict(o=CE, t=0, txt="El estribillo del principio vuelve una y otra vez entre las escenas del solista. Después de la tormenta, regresa en menor."),
 ],
 "sordina": [
  dict(o=CE, t=1574, txt="La partitura pide las cuerdas «con sordino»: el sonido se vuelve velado, de duermevela. Son los borrachos dormidos tras la fiesta."),
 ],
 "suite": [
  dict(o=SU, t=16, txt="La suite entera: un preludio y luego las danzas seguidas, todas girando en torno a la misma nota, el re."),
  dict(x="planetas", t=0, txt="Una suite del siglo XX: Los planetas de Holst, siete piezas para orquesta, cada una con su carácter."),
 ],
 "balada": [
  dict(o=BA, t=0, txt="Diez minutos que suenan a historia contada: un comienzo que duda, dos temas que se transforman y un final desbocado."),
 ],
 "coda": [
  dict(o=BA, txt="La coda de la balada es el paso 7 de la guía, «Presto con fuoco»: el final rapidísimo y salvaje."),
 ],
 "compas": [
  dict(o=SU, t=1048, txt="Minueto: compás de tres. Cuenta 1-2-3, con el apoyo en el 1."),
  dict(o=SU, t=1256, txt="Giga: también de tres (3/8), pero mucho más rápido y saltarín."),
  dict(o=BA, t=0, txt="Tras la introducción lenta, la balada se mece en 6/4: dos grupos de tres, como una barca."),
  dict(x="planetas", t=0, txt="Marte, de Holst, en 5/4: cinco tiempos, 1-2-3-4-5. Intenta marchar al paso: no se puede."),
 ],
 "pedal": [
  dict(o=BA, t=0, txt="Desde la introducción, fíjate en cómo las notas siguen sonando unas sobre otras después de soltar las teclas."),
 ],
 "pieza-de-caracter": [
  dict(o=BA, t=0, txt="Una sola pieza para piano que retrata un mundo entero, sin palabras."),
 ],
 "rubato": [
  dict(o=BA, t=0, txt="Escucha cómo el pulso respira: el pianista se demora en unas notas y avanza en otras, con libertad. Nunca suena a metrónomo."),
 ],
 "tema": [
  dict(o=CE, t=0, txt="El estribillo de la Primavera es un tema: apréndetelo en los primeros segundos y reconócelo cada vez que vuelve."),
  dict(o=BA, txt="En la balada hay dos temas: uno melancólico que se mece y otro suave, como una canción de amor. La guía de la ficha te dice cuándo llega cada uno (pasos 2 y 4)."),
 ],
 "tocata": [
  dict(x="bwv-565", t=0, txt="El comienzo es la tocata: arranques libres, como improvisados, para lucir el órgano."),
 ],
 "tonalidad": [
  dict(o=CE, t=0, txt="La Primavera, en mi mayor: luminosa."),
  dict(o=CE, t=609, txt="El Verano, en sol menor: el mismo tipo de concierto, pero sombrío y agobiante. Compara los dos comienzos."),
 ],
 "transportar": [
  dict(txt="Muchas canciones se publican en tres versiones, para voz aguda, media y grave: es la misma música, transportada."),
 ],
 "tremolo": [
  dict(o=CE, t=1916, txt="En el invierno, trémolos fuertes de las cuerdas interrumpen al violín: ráfagas de viento helado."),
  dict(o=CE, t=1066, txt="En el verano, el granizo: notas repetidas rapidísimas."),
 ],
 "trino": [
  dict(o=CE, t=0, txt="Los pájaros de la Primavera cantan con trinos."),
  dict(o=CE, t=1916, txt="El invierno empieza con notas repetidas y adornadas con trinos: es el tiritar de frío."),
 ],
 "tutti": [
  dict(o=CE, t=0, txt="El principio: todo el grupo a la vez tocando el estribillo, antes de que el solista se separe."),
 ],
 "zarabanda": [
  dict(o=SU, t=649, txt="Lenta, grave, con acordes: el centro emocional de la suite."),
 ],
}
