"""Monta la web estática a partir de fragmentos en contenido/."""
import re, sys, pathlib, datetime

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
SITIO = "Mi Agua del Grifo"
DOMINIO = "https://mi-agua-del-grifo.vercel.app"  # cámbialo cuando tengas dominio propio

LOGO = '''<svg width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C16 3 6 14.5 6 20.5a10 10 0 0 0 20 0C26 14.5 16 3 16 3z" fill="#2aa5c9"/><path d="M11.5 21a4.5 4.5 0 0 0 4.5 4.5" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'''

MENU = [("index.html","Inicio"),("calculadora-dureza-agua.html","Calculadora"),("articulos.html","Artículos"),("dureza-agua-por-ciudad.html","Ciudades"),("sobre-nosotros.html","Sobre nosotros")]

def pagina(meta, cuerpo):
    ruta = meta["path"]
    menu = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h==ruta else ""}>{t}</a>' for h,t in MENU)
    canon = DOMINIO + "/" + ("" if ruta=="index.html" else ruta[:-5])
    extra_head = meta.get("schema","")
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta["title"]}</title>
<meta name="description" content="{meta["desc"]}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{meta["title"]}">
<meta property="og:description" content="{meta["desc"]}">
<meta property="og:type" content="{"article" if meta.get("tipo")=="articulo" else "website"}">
<meta property="og:locale" content="es_ES">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M16 3C16 3 6 14.5 6 20.5a10 10 0 0 0 20 0C26 14.5 16 3 16 3z' fill='%232aa5c9'/%3E%3C/svg%3E">
<link rel="stylesheet" href="css/estilo.css">
<meta name="google-adsense-account" content="ca-pub-3880195370765258">
{extra_head}
</head>
<body>
<header class="cabecera"><div class="contenedor">
<a class="logo" href="index.html">{LOGO}<span>{SITIO}</span></a>
<nav class="menu" aria-label="Principal">{menu}</nav>
</div></header>
<main>
{cuerpo}
</main>
<footer class="pie"><div class="contenedor">
<div><strong>{SITIO}</strong><br>Información clara sobre el agua que sale de tu grifo en España.<br>© {datetime.date.today().year} {SITIO}</div>
<nav aria-label="Legal"><a href="sobre-nosotros.html">Sobre nosotros</a><a href="contacto.html">Contacto</a><a href="aviso-legal.html">Aviso legal</a><a href="politica-privacidad.html">Privacidad</a><a href="politica-cookies.html">Cookies</a></nav>
</div></footer>
<div class="aviso-cookies" id="cookies" role="dialog" aria-label="Aviso de cookies">
Usamos cookies propias y de terceros (Google AdSense) para mostrar anuncios y analizar el uso de la web. Puedes aceptarlas o rechazar las no necesarias. <a href="politica-cookies.html">Más información</a>.
<div class="botones"><button class="boton" data-c="si">Aceptar</button><button class="boton sec" data-c="no">Rechazar</button></div>
</div>
<script>
document.querySelectorAll('.tabla-scroll table').forEach(function(t){{var h=[].map.call(t.querySelectorAll('thead th'),function(x){{return x.textContent}});t.querySelectorAll('tbody tr').forEach(function(r){{[].forEach.call(r.children,function(td,i){{if(h[i])td.setAttribute('data-l',h[i])}})}})}});
(function(){{var k="cookies-ok",b=document.getElementById("cookies");var v=null;try{{v=localStorage.getItem(k)}}catch(e){{}}
if(!v)b.style.display="block";b.querySelectorAll("button").forEach(function(x){{x.onclick=function(){{try{{localStorage.setItem(k,x.dataset.c)}}catch(e){{}}b.style.display="none"}}}})}})();
</script>
</body>
</html>
'''

paginas = []
for f in sorted(SRC.glob("*.html")):
    txt = f.read_text(encoding="utf-8")
    meta = dict(re.findall(r"<!--(\w+):\s*(.*?)-->", txt.split("\n\n",1)[0]))
    cuerpo = re.sub(r"^(<!--\w+:.*?-->\s*)+", "", txt, flags=re.S)
    if meta.get("tipo") == "articulo":
        meta["schema"] = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
            f'"headline":"{meta["title"].split(" | ")[0]}","description":"{meta["desc"]}",'
            f'"dateModified":"{meta.get("fecha","")}","author":{{"@type":"Person","name":"Ismael"}},'
            f'"publisher":{{"@type":"Organization","name":"{SITIO}"}},"inLanguage":"es-ES"}}</script>')
    (OUT / meta["path"]).write_text(pagina(meta, cuerpo), encoding="utf-8")
    paginas.append(meta["path"])

hoy = datetime.date.today().isoformat()
urls = "".join(f"<url><loc>{DOMINIO}/{'' if p=='index.html' else p[:-5]}</loc><lastmod>{hoy}</lastmod></url>" for p in paginas)
(OUT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}/sitemap.xml\n", encoding="utf-8")
print("\n".join(paginas))
