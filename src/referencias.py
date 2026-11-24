# Obras de fuera del diario que se mencionan en textos o ejemplos.
# Cada una con una grabación real comprobada y que se puede incrustar (oEmbed de YouTube correcto).
# En los textos se enlazan con #x-ID (desde el principio) o #x-ID@SEG (SEG debe estar en "caps").
# "ini" (opcional): segundo por el que empieza la obra si el vídeo trae más cosas antes; debe estar en "caps".
# "caps": inicios de capítulo comprobados en la descripción del vídeo, {segundo: "nombre"}.

REFERENCIAS = {
 "rv-580": dict(compositor="Vivaldi", titulo="Concierto para cuatro violines en si menor, RV 580",
   url="https://youtu.be/fABaPU8e40c", fuente="Voices of Music", caps={}),
 "bwv-1065": dict(compositor="Bach", titulo="Concierto para cuatro claves en la menor, BWV 1065",
   url="https://youtu.be/emkJ0A7IfkY", fuente="Netherlands Bach Society", caps={246: "II. Largo", 377: "III. Allegro"}),
 "bwv-565": dict(compositor="Bach", titulo="Tocata y fuga en re menor, BWV 565",
   url="https://youtu.be/Pi0IuyTS_ic", fuente="Leo van Doeselaar, órgano · Netherlands Bach Society", caps={}),
 "chopin-op28-15": dict(compositor="Chopin", titulo="Preludio «Gota de agua», Op. 28 n.º 15",
   url="https://youtu.be/R2d2spnXyLA", fuente="Lang Lang · Steinway & Sons", caps={}),
 "haydn-94-ii": dict(compositor="Haydn", titulo="Sinfonía n.º 94 «La sorpresa», II. Andante",
   url="https://youtu.be/ydh8yp1pkg0", fuente="Filarmónica de Berlín", caps={}),
 "mahler-5": dict(compositor="Mahler", titulo="Sinfonía n.º 5",
   url="https://youtu.be/fEGNNuEM3Fc", fuente="Orquesta Sinfónica de la Radio de Hesse · Andrés Orozco-Estrada",
   caps={33: "I. Marcha fúnebre", 782: "II. Tempestuoso", 1716: "III. Scherzo", 2779: "IV. Adagietto", 3413: "V. Rondo-Finale"}),
 "mahler-ich-bin": dict(compositor="Mahler", titulo="«Ich bin der Welt abhanden gekommen» (Rückert-Lieder)",
   url="https://youtu.be/KNcx6iPT9GA", fuente="Janet Baker y John Barbirolli (Warner Classics)", caps={}),
 "chopin-nocturno-postumo": dict(compositor="Chopin", titulo="Nocturno en do sostenido menor (póstumo)",
   url="https://youtu.be/6xQ0QnbpTi4", fuente="Janusz Olejniczak, banda sonora de «El pianista» (Sony Classical)", caps={}),
 "bwv-1048": dict(compositor="Bach", titulo="Concierto de Brandeburgo n.º 3, BWV 1048",
   url="https://youtu.be/qr0f6t2UbOo", fuente="Netherlands Bach Society · Shunske Sato (All of Bach)", caps={}),
 "bwv-1": dict(compositor="Bach", titulo="Cantata «Wie schön leuchtet der Morgenstern», BWV 1",
   url="https://youtu.be/GcWjnPfVQWc", fuente="Emmanuel Music (Boston) · Ryan Turner", caps={}),
 "beethoven-claro-de-luna": dict(compositor="Beethoven", titulo="Sonata para piano n.º 14 «Claro de luna», Op. 27 n.º 2",
   url="https://youtu.be/mAJ9Ifcfqew", fuente="Eric Zivian, fortepiano (Voices of Music)", caps={284: "II. Allegretto", 418: "III. Presto agitato"}),
 "chopin-concierto-1": dict(compositor="Chopin", titulo="Concierto para piano n.º 1 en mi menor, Op. 11",
   url="https://youtu.be/614oSsDS734", fuente="Seong-Jin Cho, final del Concurso Chopin de 2015 (Instituto Chopin)", caps={}),
 "chopin-concierto-2": dict(compositor="Chopin", titulo="Concierto para piano n.º 2 en fa menor, Op. 21",
   url="https://youtu.be/L4okmGrixaA", fuente="Charles Richard-Hamelin, final del Concurso Chopin de 2015 (medici.tv)", caps={}),
 "chopin-op24": dict(compositor="Chopin", titulo="Cuatro mazurcas, Op. 24",
   url="https://youtu.be/H5D46aHhRDM", fuente="Rem Urasin, dentro de las mazurcas completas (Brilliant Classics)", ini=2815,
   caps={2815: "n.º 1, en sol menor", 3019: "n.º 2, en do mayor", 3177: "n.º 3, en la bemol mayor", 3319: "n.º 4, en si bemol menor"}),
 "chopin-op28": dict(compositor="Chopin", titulo="24 Preludios, Op. 28",
   url="https://youtu.be/QWFR9joxbpc", fuente="Seong-Jin Cho (Gilmore Piano Festival)",
   caps={246: "n.º 4, Largo", 1194: "n.º 15, «Gota de agua»", 2284: "n.º 24, Allegro appassionato"}),
 "mozart-requiem": dict(compositor="Mozart", titulo="Réquiem en re menor, K. 626",
   url="https://youtu.be/Dp2SJN4UiE4", fuente="Orquesta Nacional de Francia y Coro de Radio Francia · James Gaffigan (France Musique)",
   caps={79: "Introito", 493: "Dies irae", 1369: "Lacrimosa"}),
}
