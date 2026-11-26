import pathlib
OUT=pathlib.Path("/home/claude/agua/contenido")
def cls(f):
    return "Blanda" if f<12 else "Medianamente dura" if f<30 else "Dura" if f<=40 else "Muy dura"
def ff(mg): return f"{mg/10:.1f}".replace(".",",")
def dh(mg): return f"{mg/17.848:.0f}"
import sys
CITIES=[
dict(slug="madrid",nombre="Madrid",prov="Madrid",
 desc="¿El agua de Madrid es blanda? Dureza por distritos según los últimos análisis oficiales del SINAC (2026) y qué significa para tu lavavajillas y tu termo.",
 resumen=["El agua de Madrid es <strong>muy blanda</strong>: entre <strong>0 y 4,7 ºf</strong> en los análisis de 2026 de los distritos de la capital.","En muchos distritos el análisis da 0: hay tan poco calcio y magnesio que el laboratorio no llega a medirlo.","<strong>No necesitas descalcificador</strong>. En el lavavajillas, pon el nivel de dureza más bajo."],
 gestor="Canal de Isabel II",
 filas=[("Villaverde",47,"29/09/2026"),("Retiro – Jerónimos",45,"04/08/2026"),("Usera",40,"07/10/2026"),("Salamanca – Fuente del Berro",38,"07/10/2026"),("Carabanchel – San Isidro, Vista Alegre, Puerta Bonita y Abrantes",34,"07/10/2026"),("Centro – Palacio y Embajadores",34,"15/06/2026"),("Latina – Aluche, Campamento, Cuatro Vientos y Las Águilas",33,"14/09/2026"),("Moncloa-Aravaca – Argüelles, Ciudad Universitaria y otros",33,"03/08/2026"),("Chamberí – Gaztambide, Arapiles, Trafalgar y Almagro",31,"21/09/2026"),("Arganzuela",31,"22/06/2026"),("Aravaca",30,"06/10/2026"),("Centro – Cortes, Justicia, Universidad y Sol",0,"15/04/2026"),("Chamartín",0,"24/06/2026"),("Tetuán",0,"24/08/2026"),("Fuencarral-El Pardo",0,"24/08/2026"),("Hortaleza",0,"28/09/2026"),("Barajas",0,"15/06/2026"),("San Blas",0,"27/05/2026"),("Ciudad Lineal – Quintana, Concepción y otros",0,"15/06/2026"),("Puente de Vallecas – Entrevías, San Diego, Palomeras Bajas y Numancia",0,"28/09/2026"),("Villa de Vallecas",0,"24/08/2026"),("Vicálvaro",0,"16/09/2026")],
 nota_tabla="Selección de las redes por distrito que el SINAC lista para el municipio de Madrid. Un valor de 0 indica que la dureza está por debajo de lo que cuantifica el laboratorio.",
 porque="""<p>Madrid capital bebe sobre todo agua de los embalses de la sierra de Guadarrama y de Somosierra, que recogen agua de lluvia y nieve sobre terrenos de granito y gneis. Estas rocas casi no se disuelven, así que el agua apenas se carga de calcio y magnesio. Según el SINAC, las redes de la capital combinan agua de río y embalse con algunos pozos, y pasa por varias potabilizadoras antes de llegar al grifo.</p>
<p>Por eso el agua de Madrid tiene fama de ser de las mejores de España: es muy ligera, casi sin sabor. En los análisis de 2026 el calcio va de 0 a 18 mg/L según el distrito, cuando en ciudades del Mediterráneo suele estar entre 60 y 110 mg/L.</p>""",
 beber="Sí, y es de las más agradables de España por su baja mineralización. Si notas sabor, suele ser el cloro: deja una jarra abierta en la nevera unas horas.",
 lavav="Pon el nivel de dureza <strong>más bajo</strong> que permita tu lavavajillas (0–4 ºdH). Con agua tan blanda, si pones un nivel alto gastarás sal para nada.",
 desc_txt="<strong>No compensa.</strong> Con 0–5 ºf no hay cal que quitar. Si alguien te ofrece uno en Madrid, desconfía.",
 extra="<h3>Un detalle con agua muy blanda</h3><p>El agua muy blanda hace mucha espuma y cuesta aclarar el jabón. Puedes usar algo menos de detergente que lo que indica el envase para agua dura.</p>"),
dict(slug="barcelona",nombre="Barcelona",prov="Barcelona",
 desc="¿El agua de Barcelona es dura? Dureza por zonas según el SINAC (2026): de 20 a 43 ºf. Qué poner en el lavavajillas y si compensa un descalcificador.",
 resumen=["En la zona principal (72 % de la población) el agua es <strong>medianamente dura: 26,7 ºf</strong>.","Hay una zona <strong>muy dura (42,7 ºf)</strong> que abastece a un 10 % y otra más suave (20,1 ºf) para un 9 %.","La cal se nota: en la mayor parte de la ciudad, pon unos <strong>15 ºdH</strong> en el lavavajillas."],
 gestor="Aigües de Barcelona",
 filas=[("Barcelona – Zona D",267,"14/09/2026","513.538 hab. (72 %)"),("Barcelona – Zona B",427,"19/10/2026","71.325 hab. (10 %)"),("Barcelona – Zona E",201,"19/10/2026","64.192 hab. (9 %)")],
 nota_tabla="Redes y porcentajes de población según el SINAC. El SINAC no detalla en la ficha a qué barrios corresponde cada zona.",
 porque="""<p>Barcelona se abastece principalmente de los ríos <strong>Ter</strong> y <strong>Llobregat</strong>, además de agua desalada. El Llobregat atraviesa terrenos calizos y con sales, así que aporta un agua bastante dura y mineralizada; el Ter y el agua desalada son mucho más suaves.</p>
<p>La mezcla que llega a cada zona de la ciudad depende de qué potabilizadora la abastece. Por eso hay tanta diferencia entre la zona B (42,7 ºf) y la zona E (20,1 ºf). Además, la proporción de cada origen cambia con la sequía y la demanda, así que la dureza de tu grifo puede variar a lo largo del año.</p>""",
 beber="Sí, cumple la normativa. Su sabor, a veces criticado, se debe más a la mineralización y al cloro que a un problema sanitario. Una jarra con filtro de carbón activado mejora mucho el sabor.",
 lavav="Zona D: <strong>15 ºdH</strong>. Zona B: <strong>24 ºdH</strong>. Zona E: <strong>11 ºdH</strong>. Si no sabes tu zona, mide con tiras reactivas o pon 15–17 ºdH.",
 desc_txt="En la zona D (26,7 ºf) es <strong>opcional</strong>: para 3 personas bastaría un equipo de unos 11 litros de resina. En la zona B (42,7 ºf) <strong>suele merecer la pena</strong>. En la E, normalmente no.",
 extra=""),
dict(slug="murcia",nombre="Murcia",prov="Murcia",
 desc="¿El agua de Murcia es dura? Dureza del casco urbano y de las pedanías según el SINAC (2026), por qué varía y qué hacer con la cal en casa.",
 resumen=["En el <strong>casco urbano</strong> el último dato de dureza es de <strong>27,8 ºf</strong> (medianamente dura, casi dura).","En muchas pedanías es <strong>dura</strong>: El Palmar 35,9 ºf, Algezares–Santo Ángel–Los Garres 37,9 ºf, Sangonera la Verde 39,6 ºf.","Para el lavavajillas, entre <strong>16 y 22 ºdH</strong> según tu zona."],
 gestor="EMUASA",
 filas=[("Casco urbano (El Carmen, Vista Alegre, San Antón, La Flota, Santa Eulalia…)",278,"22/06/2026"),("La Paloma (El Palmar)",359,"03/08/2026"),("El Valle (Algezares, Santo Ángel, Los Garres)",379,"03/06/2026"),("Sangonera la Verde",396,"06/08/2026"),("C6 (La Gloria, Llano de Brujas…)",403,"05/06/2026"),("Javalí",330,"10/07/2026"),("C2-C3 (La Ñora…)",297,"02/11/2026"),("Torreagüera",293,"01/10/2026"),("Monteagudo",240,"08/09/2026"),("C1 (Alquerías, La Barca…)",217,"02/10/2026"),("Corvera",184,"09/10/2026")],
 nota_tabla="Redes de EMUASA en el municipio de Murcia según el SINAC (selección de las que abastecen a más población).",
 porque="""<p>Según el SINAC, la red del casco urbano mezcla agua de ríos y canales, captaciones costeras (desalación), pozos y un manantial. El agua de río que llega por los canales del sureste y la de los pozos de la zona es dura; la desalada es muy blanda. La dureza que sale del grifo depende de la proporción de cada una en cada momento.</p>
<p>Un ejemplo de lo que varía: en el análisis de junio de 2026 la dureza del casco urbano era de 278 mg/L, pero en una muestra de septiembre el calcio había bajado a 20 mg/L, señal de que en ese momento llegaba mucha más agua desalada. Por eso conviene ajustar los aparatos pensando en el valor alto.</p>""",
 beber="Sí, cumple la normativa. Si te molesta el sabor, una jarra con filtro de carbón quita el cloro; para un agua más ligera, la ósmosis inversa es la opción más completa.",
 lavav="Casco urbano: <strong>16 ºdH</strong>. Pedanías con 33–40 ºf (El Palmar, El Valle, Sangonera, Javalí): <strong>19–22 ºdH</strong>.",
 desc_txt="En el casco urbano es <strong>opcional</strong> (para 3 personas, unos 12 litros de resina). En las pedanías con más de 33 ºf <strong>suele merecer la pena</strong>.",
 extra=""),
dict(slug="elche",nombre="Elche (Elx)",prov="Alicante",
 desc="¿El agua de Elche es dura? Dureza del casco urbano, Torrellano y partidas según el SINAC (2026), con consejos para el lavavajillas y el descalcificador.",
 resumen=["El agua de Elche es <strong>dura</strong>: <strong>34,4 ºf</strong> en la red del casco urbano, que abastece al 90 % de la población.","Torrellano y otras entidades: 31,6 ºf. Diseminado de Santa Ana: <strong>51,8 ºf</strong> (muy dura).","Pon unos <strong>19 ºdH</strong> en el lavavajillas; un descalcificador suele compensar."],
 gestor="Aigües d'Elx",
 filas=[("Elche 1 – Casco urbano",344,"06/10/2026","178.466 hab. (90 %)"),("Elche 2 – Torrellano y otras entidades",316,"06/10/2026","Torrellano y partidas"),("Elche 4 – Penya les Àguiles",346,"06/10/2026","Penya les Àguiles, Altamira"),("Elche 3 – Diseminado de Santa Ana",518,"06/10/2026","Jubalcoi (diseminado)")],
 nota_tabla="Redes y población según el SINAC.",
 porque="""<p>Elche comparte con buena parte del sur de Alicante un abastecimiento basado en agua de río que llega por grandes canales, agua subterránea y aportes de desalación. Tanto el agua de los ríos del sureste como la de los acuíferos de la zona atraviesan terrenos calizos y yesíferos, y llegan cargadas de calcio y magnesio. El resultado es un agua dura en casi todo el municipio.</p>
<p>Como en Alicante o Murcia, la proporción de cada origen cambia a lo largo del año, así que la dureza puede subir o bajar varios grados de un análisis a otro.</p>""",
 beber="Sí, cumple la normativa. Su sabor mineral es lo que más se nota; una jarra con filtro de carbón activado ayuda.",
 lavav="Casco urbano y Torrellano: <strong>18–19 ºdH</strong>. Santa Ana: <strong>29 ºdH</strong> o el máximo de tu aparato.",
 desc_txt="Con 34 ºf <strong>suele merecer la pena</strong>, sobre todo si tienes termo eléctrico. Para 3 personas, un equipo de unos 15 litros de resina.",
 extra=""),
dict(slug="benidorm",nombre="Benidorm",prov="Alicante",
 desc="¿El agua de Benidorm es dura? Dureza de las redes del Pueblo y del Parque según el SINAC (2026) y qué hacer con la cal en casa o en el apartamento.",
 resumen=["El agua de Benidorm es <strong>medianamente dura</strong>: <strong>20,8 ºf</strong> en la red Benidorm Pueblo y 17,0 ºf en Benidorm Parque.","Deja algo de cal, pero no tanta como en Alicante, Elche o Murcia.","En el lavavajillas, unos <strong>10–12 ºdH</strong>. Un descalcificador es opcional."],
 gestor="Hidraqua",
 filas=[("Benidorm Pueblo",208,"07/10/2026","37.632 hab. (50 %) + Coblanca"),("Benidorm Parque",170,"31/08/2026","3.763 hab. (5 %)")],
 nota_tabla="Redes listadas en el SINAC para el municipio de Benidorm y porcentajes de población que declara cada una.",
 porque="""<p>Benidorm se abastece del sistema de la Marina Baixa, que combina agua de embalses de la comarca y de acuíferos de las sierras calizas cercanas. Esos terrenos aportan calcio, pero en menor cantidad que en el sur de la provincia: según el SINAC, el calcio ronda los 53–62 mg/L y el magnesio los 9–13 mg/L.</p>
<p>Por eso el agua de Benidorm es medianamente dura: la cal se nota en grifos y mamparas si no se limpian, pero no llega a los niveles de Elche o Alicante en sus peores épocas.</p>""",
 beber="Sí, cumple la normativa. Si estás de vacaciones y no te gusta el sabor, deja el agua en una jarra en la nevera para que pierda el olor a cloro.",
 lavav="Benidorm Pueblo: <strong>12 ºdH</strong>. Benidorm Parque: <strong>10 ºdH</strong>.",
 desc_txt="<strong>Opcional.</strong> Para 3 personas bastaría un equipo pequeño, de unos 8 litros de resina. En un apartamento de uso vacacional normalmente no compensa: es mejor limpiar la cal con ácido cítrico de vez en cuando.",
 extra=""),
]
if len(sys.argv)>1:
    exec(open(sys.argv[1]).read())
for c in CITIES:
    s=c["slug"]; n=c["nombre"]
    has_pop=len(c["filas"][0])==4
    head="<tr><th>Red (SINAC)</th>"+("<th>Población abastecida</th>" if has_pop else "")+"<th>Dureza</th><th>Fecha del análisis</th></tr>"
    rows=""
    for f in c["filas"]:
        mg=f[1]
        dur=f"<strong>{ff(mg)} ºf</strong> ({mg} mg/L) · {cls(mg/10)}"
        rows+=f"<tr><td>{f[0]}</td>"+(f"<td>{f[3]}</td>" if has_pop else "")+f"<td>{dur}</td><td>{f[2]}</td></tr>\n"
    res="".join(f"<li>{x}</li>" for x in c["resumen"])
    filas_g=[f for f in c["filas"] if f[1]>0] or c["filas"]
    mxv=max(f[1] for f in c["filas"]); top=max(50,mxv/10*1.1)
    grafica='<figure class="figura"><div class="barras">'
    for f in c["filas"][:10]:
        v=f[1]/10; cc="c1" if v<12 else "c2" if v<30 else "c3" if v<=40 else "c4"
        nom=f[0].split(" (")[0]
        grafica+=f'<div class="barra"><span>{nom}</span><div class="pista"><div class="relleno {cc}" style="width:{min(100,v/top*100):.1f}%">'+f"{v:.1f}".replace(".",",")+' ºf</div></div></div>'
    grafica+='</div><div class="leyenda"><span><i class="c1"></i>Blanda</span><span><i class="c2"></i>Medianamente dura</span><span><i class="c3"></i>Dura</span><span><i class="c4"></i>Muy dura</span></div><figcaption>Dureza del último análisis de cada red, en grados franceses (ºf).</figcaption></figure>'

    html=f'''<!--path: dureza-agua-{s}.html-->
<!--title: Dureza del agua en {n}: datos oficiales 2026 | Mi Agua del Grifo-->
<!--desc: {c["desc"]}-->
<!--tipo: articulo-->
<!--fecha: 2026-11-26-->

<article class="articulo">
<div class="migas"><a href="index.html">Inicio</a> › <a href="dureza-agua-por-ciudad.html">Dureza por ciudad</a> › {n}</div>
<h1>Dureza del agua en {n}: datos oficiales 2026</h1>
<p class="meta">Actualizado el 26 de noviembre de 2026 · Por Ismael · Datos: {c.get("datos","SINAC, Ministerio de Sanidad")}</p>

<div class="resumen"><strong>En resumen</strong>
<ul>{res}</ul></div>

<h2>Dureza del agua en {n} por redes</h2>
<p>{c.get("intro_tabla", f"Estos son los últimos análisis de dureza que el SINAC, el sistema oficial del Ministerio de Sanidad, publica para las redes de agua de {n}:")}</p>
<div class="tabla-scroll"><table>
<thead>{head}</thead>
<tbody>
{rows}</tbody></table></div>
<p style="font-size:.9rem;color:var(--suave)">{c["nota_tabla"]} Consulta del 26/11/2026. 1 ºf = 10 mg/L de CaCO₃. Clasificación según la escala de la OCU.</p>

{grafica}
<!--INC:unidades-->
<h2>¿Por qué el agua de {n} es así?</h2>
{c["porque"]}
<p>Si quieres entender la química de fondo, lo explicamos en <a href="que-es-la-dureza-del-agua.html">qué es la dureza del agua</a>.</p>

<h2>¿Se puede beber el agua del grifo en {n}?</h2>
<p>{c["beber"]} La dureza no tiene límite sanitario en el Real Decreto 3/2023; lo explicamos en <a href="es-malo-beber-agua-dura.html">¿es malo beber agua dura?</a>.</p>

<h2>Qué hacer con el agua de {n}</h2>
<h3>Lavavajillas</h3>
<p>{c["lavav"]} Si tu aparato usa otra unidad, pásala con la <a href="calculadora-dureza-agua.html">calculadora de dureza</a>.</p>
<h3>¿Merece la pena un descalcificador?</h3>
<p>{c["desc_txt"]} Calcula tu caso con la <a href="calculadora-dureza-agua.html#descalcificador">calculadora de descalcificador</a> y lee <a href="descalcificador-merece-la-pena.html">¿merece la pena un descalcificador?</a>.</p>
{c["extra"]}
<h2>Cómo saber a qué red pertenece tu casa</h2>
<p>El agua de {n} la gestiona {c["gestor"]}. En el teléfono de tu factura o en su web pueden decirte qué red te abastece y darte los análisis más recientes. También puedes consultarlos tú en el SINAC: entra en "Acceso ciudadano", elige la provincia de {c["prov"]} y el municipio. Más opciones en <a href="como-saber-la-dureza-del-agua-de-mi-casa.html">cómo saber la dureza del agua de tu casa</a>.</p>

<div class="fuentes"><strong>Fuentes:</strong> {c.get("fuentes_extra","")}Ministerio de Sanidad, <a href="https://sinacv2.sanidad.gob.es/SinacV2/Index.do" rel="nofollow noopener">SINAC, redes de distribución de {n}</a> (consulta del 26/11/2026); Real Decreto 3/2023 (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2023-628" rel="nofollow noopener">BOE</a>); OCU, <a href="https://www.ocu.org/vivienda-y-energia/equipamiento-hogar/informe/dureza-del-agua" rel="nofollow noopener">Dureza del agua</a>.</div>
</article>
<aside class="relacionados"><h2>Otras ciudades</h2><ul>
<li><a href="dureza-agua-por-ciudad.html">Dureza del agua por ciudades</a></li>
<li><a href="calculadora-dureza-agua.html">Calculadora de dureza y de descalcificador</a></li>
</ul></aside>
'''
    (OUT/f"c-{s}.html").write_text(html,encoding="utf-8")
print("ok")
