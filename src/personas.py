ALLOFBACH = "https://www.bachvereniging.nl/en/bwv/bwv-"

PERSONAS = [
dict(id="vivaldi", tipo="compositor", nombre="Antonio Vivaldi", vida="1678–1741", nace=1678, lugar="Venecia → Viena", epoca="barroco",
 entradilla="Violinista virtuoso, sacerdote y empresario de ópera. Dejó una huella decisiva en la forma del concierto.",
 h="""<h2>Vida</h2>
<p>Nació en Venecia el 4 de marzo de 1678. Su padre, violinista, le enseñó el instrumento, y en 1696 ya tocaba a su lado en la basílica de San Marcos. Estudió para sacerdote desde 1693 y se ordenó en 1703. Por su pelo pelirrojo le llamaban <i lang="it">il prete rosso</i>, «el cura rojo».</p>
<p>Ese mismo año empezó como maestro de violín en el <b>Ospedale della Pietà</b>, una institución veneciana para niños abandonados cuyas alumnas formaban un conjunto musical solo de mujeres. En 1716 pasó a dirigir toda su música. Trabajó allí entre 1703 y 1715 y entre 1723 y 1740, y para ellas escribió buena parte de su obra.</p>
<p>Su gran salto llegó en 1711 con <i lang="it">L'estro armonico</i>, doce conciertos impresos en Ámsterdam. Fue también empresario de ópera y montó producciones caras en Venecia, Mantua y Viena. Escribió más de 400 conciertos.</p>
<h2>Final y resurrección</h2>
<p>Ya mayor, se trasladó a Viena con la esperanza de contar con el apoyo del emperador Carlos VI, pero el emperador murió poco después de su llegada. Vivaldi murió en la pobreza el 28 de julio de 1741 y fue enterrado en una tumba sencilla, tras un funeral sin música. Su nombre cayó en el olvido durante casi dos siglos, hasta que en el siglo XX lo devolvió a la fama, sobre todo, el éxito de las Cuatro Estaciones.</p>
<h2>Por qué importa</h2>
<p>Fijó el modelo de concierto en tres movimientos con estribillo y episodios del solista. Su influencia llegó lejos: Bach copió y transcribió conciertos suyos para clave y para órgano en 1713–1714 para aprender el estilo italiano.</p>""",
 claves=[["Nació","Venecia, 1678"],["Murió","Viena, 1741"],["Apodo","<i lang=\"it\">Il prete rosso</i>"],["Trabajo","Ospedale della Pietà"],["Obra","Más de 400 conciertos, óperas, música sacra"],["Catálogo","RV (catálogo Ryom)"]],
 ruta=[
  dict(titulo="Las Cuatro Estaciones", obra="cuatro-estaciones", nota="Por donde empezar: cuatro conciertos con guion."),
  dict(titulo="Concierto para cuatro violines, RV 580", nota="De <i lang=\"it\">L'estro armonico</i> (1711). Cuatro solistas que se pasan la palabra.", url="https://youtu.be/fABaPU8e40c", enlace="Buscar en YouTube"),
  dict(titulo="El mismo concierto, en manos de Bach (BWV 1065)", nota="Bach lo pasó a cuatro claves. Escucha los dos seguidos y oirás los dos acentos del Barroco.", url="https://youtu.be/emkJ0A7IfkY", enlace="Ver en All of Bach"),
 ]),
dict(id="bach", tipo="compositor", nombre="Johann Sebastian Bach", vida="1685–1750", nace=1685, lugar="Eisenach → Leipzig", epoca="barroco",
 entradilla="El gran arquitecto del contrapunto. Unió la riqueza armónica alemana con la energía del estilo italiano.",
 h="""<h2>Vida</h2>
<p>Nació en Eisenach en marzo de 1685, en una familia llena de músicos. Se quedó huérfano a los diez años y se fue a vivir con su hermano mayor, Johann Christoph, organista en Ohrdruf. A los quince se marchó a estudiar a Lüneburg.</p>
<p>Trabajó como organista para iglesias de Arnstadt y Mühlhausen y después en la corte de <b>Weimar</b> (1708–1717), donde transcribió conciertos italianos, sobre todo de Vivaldi. Cuando quiso irse, el duque no le dejaba y lo tuvo cuatro semanas arrestado antes de permitirle marchar.</p>
<p>En <b>Köthen</b> (1717–1723) fue maestro de capilla del príncipe Leopold. Era una corte calvinista que no necesitaba música para la iglesia, así que escribió música instrumental: los <i>Conciertos de Brandeburgo</i>, las suites para orquesta y las obras para violín y violonchelo solos.</p>
<p>Desde 1723 hasta su muerte fue <b>Thomaskantor</b> en Leipzig: componía para las principales iglesias luteranas de la ciudad (casi una cantata cada domingo) y dirigía el Collegium Musicum de los estudiantes. Allí nacieron la <i>Pasión según san Mateo</i> y la <i>Misa en si menor</i>. Murió el 28 de julio de 1750.</p>
<h2>El olvido y la vuelta</h2>
<p>Tras su muerte lo apreciaban sobre todo los entendidos. El gran renacimiento de su música empezó en 1829, cuando Felix Mendelssohn dirigió la <i>Pasión según san Mateo</i> en Berlín.</p>""",
 claves=[["Nació","Eisenach, 1685"],["Murió","Leipzig, 1750"],["Cargos","Weimar, Köthen, Leipzig"],["Obra","Cantatas, pasiones, conciertos, suites, órgano, teclado"],["Catálogo","BWV (Bach-Werke-Verzeichnis)"],["Coincidencia","Murió un 28 de julio, como Vivaldi"]],
 ruta=[
  dict(titulo="Suite n.º 2 para violonchelo", obra="suite-chelo-2", nota="Un solo instrumento que suena a varias voces."),
  dict(titulo="Concierto de Brandeburgo n.º 3, BWV 1048", nota="De la época de Köthen. Un concierto sin solista: todos los instrumentos son importantes.", url=ALLOFBACH+"1048", enlace="Ver en All of Bach"),
  dict(titulo="Concierto para cuatro claves, BWV 1065", nota="Su versión del concierto RV 580 de Vivaldi.", url="https://youtu.be/emkJ0A7IfkY", enlace="Ver en All of Bach"),
  dict(titulo="Tocata y fuga en re menor, BWV 565", nota="La pieza de órgano más famosa del mundo, aunque algunos expertos dudan de que sea suya.", url="https://youtu.be/Pi0IuyTS_ic", enlace="Ver en All of Bach"),
 ]),
dict(id="chopin", tipo="compositor", nombre="Frédéric Chopin", vida="1810–1849", nace=1810, lugar="Varsovia → París", epoca="romanticismo",
 entradilla="El poeta del piano. Polaco exiliado en París, escribió casi todo para su instrumento y cambió para siempre lo que un piano podía decir.",
 h="""<h2>Vida</h2>
<p>Nació el 1 de marzo de 1810 en Żelazowa Wola, cerca de Varsovia, hijo de padre francés y madre polaca. Fue un niño prodigio: publicó su primera composición con siete años y a los ocho ya tocaba en los salones de la aristocracia.</p>
<p>En noviembre de 1830, con 20 años, salió de Polonia para una gira, menos de un mes antes del Levantamiento de Noviembre contra Rusia. Mientras viajaba hacia París se enteró de que había sido aplastado. Nunca volvió: vivió el resto de su vida como exiliado en París, adonde llegó a finales de 1831.</p>
<p>En París triunfó en los salones más que en las grandes salas. Su forma de tocar era delicada, de sonido pequeño, y en toda su carrera dio solo unos 30 conciertos públicos. Se ganaba la vida, sobre todo, dando clases de piano.</p>
<p>En 1836 conoció en casa de Liszt a la escritora George Sand, con quien mantuvo una relación de casi diez años. Con ella y sus hijos pasó el invierno de 1838–1839 en Mallorca, en la Cartuja de Valldemossa. Tras la ruptura, en 1847, su salud se hundió. Dio sus últimos conciertos en París y en Gran Bretaña en 1848 y murió en París el 17 de octubre de 1849, con 39 años, probablemente de tuberculosis.</p>
<h2>Por qué importa</h2>
<p>Todas sus obras incluyen el piano, y su música ayudó a convertirlo en el instrumento más popular del siglo XIX. Inventó o renovó géneros enteros, como la balada, el nocturno, el estudio de concierto, la mazurca y la polonesa, y fue el primer compositor que pidió de forma habitual el <a href="#g-rubato">rubato</a>. Robert Schumann lo saludó en 1831 con una frase famosa: «¡Quítense el sombrero, señores, un genio!».</p>""",
 claves=[["Nació","Żelazowa Wola (Polonia), 1810"],["Murió","París, 1849"],["Instrumento","El piano: todas sus obras lo incluyen"],["Vivió en","Varsovia, Viena, París y un invierno en Mallorca"],["Catálogo","Números de opus (Op.)"],["Su corazón","En la iglesia de la Santa Cruz de Varsovia"]],
 ruta=[
  dict(titulo="Balada n.º 1 en sol menor, Op. 23", obra="balada-1-chopin", nota="Su obra más querida, según él mismo."),
  dict(titulo="Preludio «Gota de agua», Op. 28 n.º 15", nota="De los Preludios que terminó en Valldemossa. Una nota que se repite como lluvia.", url="https://youtu.be/R2d2spnXyLA", enlace="Lang Lang (Steinway & Sons)"),
  dict(titulo="Nocturno en do sostenido menor (póstumo)", nota="El que abre <i>El pianista</i> y el que Szpilman tocó de verdad para Hosenfeld.", url="https://www.youtube.com/results?search_query=Chopin+Nocturne+C+sharp+minor+posthumous", enlace="Buscar en YouTube"),
 ]),
dict(id="zimerman", tipo="solista", rol="Pianista", nombre="Krystian Zimerman", vida="Nacido en 1956", lugar="Zabrze (Polonia)",
 entradilla="Pianista polaco, ganador del Concurso Chopin con 18 años. Perfeccionista: viaja con sus propios pianos y graba muy poco.",
 h="""<p>Nació el 5 de diciembre de 1956 en Zabrze, en una familia de músicos. Empezó a tocar a los cinco años con su padre, pianista, y estudió en el conservatorio de Katowice con Andrzej Jasiński.</p>
<p>En 1975, con 18 años, ganó el Concurso Chopin de Varsovia. Era el más joven de los participantes y se llevó todos los premios. Al año siguiente debutó en disco con Deutsche Grammophon, con quien tiene un contrato exclusivo de por vida. Ha tocado con directores como Bernstein, Giulini y Rattle.</p>
<p>Es famoso por su exigencia. Toca siempre sus propios pianos Steinway, que él mismo afina, monta y modifica según el repertorio. Además limita mucho sus conciertos y graba poco, solo después de largos periodos de estudio.</p>""",
 claves=[["Instrumento","Piano"],["Premio clave","Concurso Chopin, 1975"],["Sello","Deutsche Grammophon"],["Manía","Viaja con sus propios pianos"]]),
dict(id="maisky", tipo="solista", rol="Violonchelista", nombre="Mischa Maisky", vida="Nacido en 1948", lugar="Riga (Letonia)",
 entradilla="Violonchelista de estilo extrovertido y romántico. El único que estudió con Rostropóvich y con Piatigorsky.",
 h="""<p>Nació en Riga el 10 de enero de 1948, cuando Letonia era parte de la Unión Soviética. Estudió con Mstislav Rostropóvich en el Conservatorio de Moscú entre 1966 y 1970. En 1970 lo detuvieron por comprar en el mercado negro una grabadora con la que quería grabar sus clases, y pasó 18 meses en prisión y en un campo de trabajo.</p>
<p>En 1972 emigró a Israel. En 1974 estudió con Gregor Piatigorsky en Los Ángeles, y desde 1985 grabó en exclusiva para Deutsche Grammophon, incluidas dos versiones de las suites de Bach. Vive en Bélgica.</p>
<p>Su Bach no busca el estilo de época: él mismo dice que Bach fue «el mayor de los románticos». Decidió regrabar las suites cuando, en una tienda de alta fidelidad, no reconoció su propia grabación de 1985.</p>""",
 claves=[["Instrumento","Violonchelo"],["Maestros","Rostropóvich, Piatigorsky"],["Estilo","Romántico, muy expresivo"],["Curiosidad","En 2000 tocó en Zúrich toda la obra de Bach para violonchelo en tres conciertos el mismo día"]]),
dict(id="voices-of-music", tipo="conjunto", rol="Conjunto de música antigua · San Francisco", nombre="Voices of Music", dirige=["Hanneke van Proosdij","David Tayler"],
 entradilla="Conjunto de San Francisco que toca con instrumentos de época y lleva sus conciertos a YouTube en alta definición.",
 h="""<p>Lo fundaron en 2007 Hanneke van Proosdij (clave y flauta de pico) y David Tayler (laúd), un matrimonio de músicos e investigadores que lo dirige desde entonces. Tocan música del Renacimiento y del Barroco con criterios históricos.</p>
<p>Fueron pioneros en publicar sus conciertos en vídeo: fueron el primer conjunto de música antigua del mundo en recibir el premio Silver Creator de YouTube. Su vídeo de las Cuatro Estaciones lleva el soneto de Vivaldi como subtítulos.</p>"""),
dict(id="casals", tipo="solista", rol="Violonchelista y director", nombre="Pau Casals", vida="1876–1973", lugar="El Vendrell → San Juan de Puerto Rico",
 entradilla="El violonchelista catalán que rescató las suites de Bach y las convirtió en obras de concierto.",
 h="""<p>Nació en El Vendrell (Tarragona) el 29 de diciembre de 1876. En 1890, con 13 años, encontró en una tienda de Barcelona una edición antigua de las suites para violonchelo de Bach, que entonces se tenían por simples ejercicios. Él las convirtió en música de concierto y las grabó entre 1936 y 1939.</p>
<p>Tras la victoria de Franco se exilió en 1939 en Prades, en el sur de Francia, donde organizó festivales entre 1950 y 1966. Desde 1956–1957 vivió en Puerto Rico, la tierra de su madre, y allí murió en 1973. Terminaba sus conciertos con la canción popular catalana <i lang="ca">El cant dels ocells</i>.</p>""",
 claves=[["Instrumento","Violonchelo"],["Grabación clave","Suites de Bach, 1936–1939"],["Exilio","Prades (1939) y Puerto Rico"]]),
dict(id="il-giardino-armonico", tipo="conjunto", rol="Conjunto barroco · Milán", nombre="Il Giardino Armonico", dirige=["Giovanni Antonini"],
 entradilla="Conjunto italiano fundado en 1985 que sacudió la forma de tocar a Vivaldi.",
 h="""<p>Lo fundaron en Milán en 1985 Giovanni Antonini, Luca Pianca y Paolo Beschi. Su grabación de las Cuatro Estaciones de 1994 rompió con las convenciones: pintaron cada escena al extremo, con un invierno helado, un verano asfixiante y un perro que ladra a lo bestia.</p>"""),
dict(id="europa-galante", tipo="conjunto", rol="Conjunto barroco", nombre="Europa Galante", dirige=["Fabio Biondi"],
 entradilla="El conjunto del violinista Fabio Biondi. Sus Estaciones de 1991 marcaron el estilo de las que vinieron después.",
 h="""<p>Su grabación de las Cuatro Estaciones de 1991 fue la primera del grupo. Biondi fue de los primeros en recuperar un número de músicos parecido al que probablemente tenía Vivaldi, con instrumentos de época. Lo que entonces sonaba radical se convirtió después en la forma habitual de tocar a Vivaldi.</p>"""),
dict(id="carmignola", tipo="solista", rol="Violinista", nombre="Giuliano Carmignola",
 entradilla="Violinista italiano, una de las grandes voces de Vivaldi con instrumentos de época.",
 h="""<p>Fue alumno de Luigi Ferro, uno de los violinistas estrella de los Virtuosi di Roma. Grabó las Cuatro Estaciones con la Venice Baroque Orchestra y Andrea Marcon, una versión muy elogiada por su energía y su poesía.</p>"""),
dict(id="kennedy", tipo="solista", rol="Violinista", nombre="Nigel Kennedy",
 entradilla="Su grabación de 1989 convirtió las Cuatro Estaciones en un fenómeno de ventas.",
 h="""<p>Su disco de las Cuatro Estaciones, publicado en 1989, pasó casi dos años en lo más alto de la lista clásica británica y vendió más de dos millones de copias: fue el disco clásico más vendido de su tiempo. Toca con instrumentos modernos.</p>"""),
dict(id="fournier", tipo="solista", rol="Violonchelista", nombre="Pierre Fournier",
 entradilla="Violonchelista de tradición romántica que, paradójicamente, tocaba a Bach con nobleza y contención clásica.",
 h="""<p>Grabó las suites de Bach para Deutsche Grammophon en 1961. Un crítico de BBC Music Magazine la prefiere a muchas otras por su nobleza, su concentración y su contención.</p>"""),
dict(id="netherlands-bach-society", tipo="conjunto", rol="Conjunto barroco · Países Bajos", nombre="Netherlands Bach Society", dirige=["Shunske Sato"],
 entradilla="Su proyecto All of Bach graba toda la obra de Bach en vídeo y la comparte gratis.",
 h="""<p>En 2013, como antesala de su centenario, la Nederlandse Bachvereniging lanzó <b>All of Bach</b>: grabar en vídeo todas las obras de Bach y publicarlas gratis. Sus vídeos están en su web y en su canal de YouTube (youtube.com/bach). Su director artístico es Shunske Sato.</p>
<p>Para aprender, es un tesoro: casi cualquier obra de Bach que te encuentres en un concierto tiene allí una versión filmada.</p>"""),
]
