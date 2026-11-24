"""Genera los gráficos del video de demo (logo, ciclo de roles y carteles).

Escribe un SVG por gráfico en svg/ y lo pasa a PNG de 1920x1080 en png/ con Chrome sin ventana,
que trae las tipografías de la app (Space Grotesk e Inter) desde Google Fonts.

Uso, parado en cualquier carpeta:  py -I generar.py
Para cambiar un texto (por ejemplo los nombres del equipo), se edita acá y se vuelve a correr.
"""

import math
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image

AQUI = Path(__file__).resolve().parent
SVG_DIR = AQUI / "svg"
PNG_DIR = AQUI / "png"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
W, H = 1920, 1080

# Paleta "Cuidado preventivo" v2 (TIP - Frontend/src/styles/tokens.css)
BG = "#F3F4F0"
TEXT = "#1F2A24"
MUTED = "#56615B"
ACCENT = "#15616D"  # petróleo
OK = "#27804F"  # verde
CRITICAL = "#C8373F"
DARK = "#0B2E28"  # el del favicon
LINE = "#C9CDC8"  # rgba(31,42,36,.22) sobre el fondo, en sólido

EQUIPO = ["Guido Greco", "Tomás Neira Guitera"]
PIE_CIERRE = "Trabajo de Inserción Profesional · 2026"

FUENTES = (
    "@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700"
    "&amp;family=Inter:wght@400;500;600&amp;display=block');"
    ".d{font-family:'Space Grotesk',sans-serif}.b{font-family:'Inter',sans-serif}"
)


def svg(cuerpo, fondo=True):
    rect = f'<rect width="{W}" height="{H}" fill="{BG}"/>' if fondo else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
        f"<style>{FUENTES}</style>{rect}{cuerpo}</svg>"
    )


def texto(x, y, s, size, clase="d", peso=600, color=TEXT, anchor="middle", extra=""):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" class="{clase}" font-size="{size}" font-weight="{peso}" '
        f'fill="{color}" text-anchor="{anchor}" {extra}>{escape(s)}</text>'
    )


# ---------------------------------------------------------------- logo

# El camión del favicon de la app (TIP - Frontend/public/favicon.svg), en una caja de 240x240.
CAMION = """
<ellipse cx="122" cy="204" rx="104" ry="7" fill="{c}" opacity="0.14"/>
<path d="M16 90 L146 52 L146 108 L16 146 Z" fill="{c}"/>
<path d="M146 52 L168 60 L168 116 L146 108 Z" fill="{c}"/>
<path d="M16 90 L146 52 L168 60 L38 98 Z" fill="{c}"/>
<path d="M30 106 L134 74" stroke="{h}" stroke-width="4" stroke-linecap="round" opacity="0.9"/>
<path d="M164 58 C164 51 169 46 176 45 L196 42 C207 40 216 48 216 60 L216 156 L164 168 Z" fill="{c}"/>
<path d="M170 46 L214 40 L216 52 L168 58 Z" fill="{c}"/>
<path d="M174 60 L206 55 L206 78 L174 84 Z" fill="{h}"/>
<path d="M178 92 L178 150" stroke="{h}" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
<rect x="212" y="58" width="8" height="20" rx="3" fill="{c}"/>
<rect x="184" y="96" width="28" height="6" rx="2" fill="{h}"/>
<rect x="184" y="108" width="28" height="6" rx="2" fill="{h}"/>
<rect x="184" y="120" width="28" height="6" rx="2" fill="{h}"/>
<rect x="164" y="152" width="58" height="10" rx="3" fill="{c}"/>
<circle cx="60" cy="160" r="20" fill="{c}"/>
<circle cx="60" cy="160" r="8" fill="{h}"/>
<circle cx="192" cy="176" r="22" fill="{c}"/>
<circle cx="192" cy="176" r="9" fill="{h}"/>
"""

# Insignia de "inspección en orden": círculo verde con un tilde, arriba de la caja del acoplado.
INSIGNIA = f"""
<circle cx="58" cy="52" r="34" fill="{BG}"/>
<circle cx="58" cy="52" r="28" fill="{OK}"/>
<path d="M45 52 L54 61 L71 43" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"
 stroke-linejoin="round"/>
"""


def marca(cx, cy, ancho):
    """El camión con la insignia, centrado en (cx, cy)."""
    s = ancho / 240
    return (
        f'<g transform="translate({cx - 120 * s:.1f} {cy - 120 * s:.1f}) scale({s:.4f})">'
        f'{CAMION.format(c=DARK, h=BG)}{INSIGNIA}</g>'
    )


def palabra(cx, y, size):
    """FleetGuard, con "Guard" en petróleo."""
    return (
        f'<text x="{cx}" y="{y}" class="d" font-size="{size}" font-weight="700" text-anchor="middle" '
        f'letter-spacing="-2"><tspan fill="{TEXT}">Fleet</tspan><tspan fill="{ACCENT}">Guard</tspan></text>'
    )


LEMA = "Mantenimiento preventivo e inspecciones de flota"


def logo_camion():
    return marca(W / 2, 395, 330)


def logo_texto():
    return palabra(W / 2, 690, 150) + texto(W / 2, 770, LEMA, 38, "b", 500, MUTED)


def cierre():
    return (
        marca(W / 2, 250, 220)
        + palabra(W / 2, 470, 100)
        + f'<rect x="{W / 2 - 60}" y="530" width="120" height="6" rx="3" fill="{OK}"/>'
        + texto(W / 2, 668, "Muchas gracias", 96, "d", 600, TEXT)
        + texto(W / 2, 770, "  ·  ".join(EQUIPO), 40, "b", 500, TEXT)
        + texto(W / 2, 836, PIE_CIERRE, 30, "b", 400, MUTED)
    )


# ---------------------------------------------------------------- ciclo de roles

# Íconos en una caja de 24x24, con trazo (al estilo de los de Lucide).
ICONOS = {
    "chofer": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="2.5"/>'
              '<path d="M12 14.5V22M9.5 12H2M14.5 12H22"/>',
    "admin": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>'
             '<path d="M6 13l3-3 3 2 5-5"/>',
    "tecnico": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94'
               'l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}
NOMBRES = {"chofer": "Chofer", "admin": "Administrador", "tecnico": "Técnico"}
ANGULOS = {"chofer": -90, "admin": 30, "tecnico": 150}  # en grados, en sentido horario
# Cada flecha sale de un rol y va al siguiente; el texto es lo que hace el rol de origen.
FLECHAS = [("chofer", "admin", "reporta el defecto"),
           ("admin", "tecnico", "asigna la orden"),
           ("tecnico", "chofer", "repara el vehículo")]

R = 290  # radio del ciclo
RN = 96  # radio de cada rol


def punto(cx, cy, ang, r=R):
    a = math.radians(ang)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def ciclo(cx, cy, activos=(), flechas_activas=(), color_flecha=None, apagar=True, escala=1.0):
    """El ciclo de tres roles.

    activos: roles resaltados. flechas_activas: índices de FLECHAS resaltadas.
    color_flecha: dict índice -> color, para pintar una flecha de otro color que el petróleo.
    apagar: si hay algo resaltado, el resto queda más tenue.
    """
    color_flecha = color_flecha or {}
    hay_foco = bool(activos or flechas_activas)
    partes = []
    defs = []
    gap = math.degrees((RN + 26) / R)

    for i, (de, a, etiqueta) in enumerate(FLECHAS):
        activa = i in flechas_activas
        color = color_flecha.get(i, ACCENT) if activa else LINE
        opac = 1 if (activa or not hay_foco or not apagar) else 0.55
        a1 = ANGULOS[de] + gap
        a2 = ANGULOS[a] - gap
        if a2 < a1:
            a2 += 360
        x1, y1 = punto(0, 0, a1)
        x2, y2 = punto(0, 0, a2)
        defs.append(
            f'<marker id="m{i}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4.2" markerHeight="4.2" '
            f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{color}"/></marker>'
        )
        partes.append(
            f'<path d="M{x1:.1f} {y1:.1f} A{R} {R} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{10 if activa else 7}" stroke-linecap="round" marker-end="url(#m{i})" '
            f'opacity="{opac}"/>'
        )
        medio = (a1 + a2) / 2
        lx, ly = punto(0, 0, medio, R + 62)
        anchor = "middle" if abs(math.cos(math.radians(medio))) < 0.3 else (
            "start" if math.cos(math.radians(medio)) > 0 else "end")
        if anchor == "middle":
            ly += 14
        partes.append(texto(lx, ly + 10, etiqueta, 32, "b", 600 if activa else 500,
                            color if activa else MUTED, anchor, f'opacity="{opac}"'))

    for rol, ang in ANGULOS.items():
        x, y = punto(0, 0, ang)
        activo = rol in activos
        tenue = hay_foco and apagar and not activo
        g = [f'<g transform="translate({x:.1f} {y:.1f})" opacity="{0.45 if tenue else 1}">']
        if activo:
            g.append(f'<circle r="{RN + 20}" fill="{ACCENT}" opacity="0.14"/>')
            g.append(f'<circle r="{RN}" fill="{ACCENT}"/>')
            trazo = "#fff"
        else:
            g.append(f'<circle r="{RN}" fill="#fff" stroke="{LINE}" stroke-width="3"/>')
            trazo = TEXT
        s = 92 / 24
        g.append(
            f'<g transform="translate({-46} {-46}) scale({s:.4f})" fill="none" stroke="{trazo}" '
            f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{ICONOS[rol]}</g>'
        )
        # Los nombres de abajo se abren hacia afuera, para no pisar la flecha de abajo.
        lx, anchor = {"chofer": (0, "middle"), "admin": (-RN * 0.55, "start"),
                      "tecnico": (RN * 0.55, "end")}[rol]
        g.append(texto(lx, RN + 62, NOMBRES[rol], 44, "d", 600, ACCENT if activo else TEXT, anchor))
        g.append("</g>")
        partes.append("".join(g))

    return (
        f'<defs>{"".join(defs)}</defs>'
        f'<g transform="translate({cx} {cy}) scale({escala})">{"".join(partes)}</g>'
    )


CICLO_CENTRO = (W / 2, 540)

# Fondo liso, todos los roles iguales: para arrancar la escena 1.
CICLOS = {
    "ciclo-0-base": {},
    "ciclo-1-chofer": {"activos": ["chofer"]},
    "ciclo-2-admin": {"activos": ["admin"], "flechas_activas": [0]},
    "ciclo-3-tecnico": {"activos": ["tecnico"], "flechas_activas": [1]},
    "ciclo-4-completo": {"activos": ["chofer", "admin", "tecnico"], "flechas_activas": [0, 1, 2]},
}

# ---------------------------------------------------------------- carteles

CARTELES = {
    "cartel-1-chofer": ("CHOFER", "Inspecciona su vehículo y reporta los defectos", "Carlos · celular",
                        {"activos": ["chofer"]}),
    "cartel-2-admin": ("ADMINISTRADOR", "Ve el estado de la flota y organiza el trabajo", "computadora",
                       {"activos": ["admin"], "flechas_activas": [0]}),
    "cartel-3-tecnico": ("TÉCNICO", "Realiza las reparaciones", "Javier · celular",
                         {"activos": ["tecnico"], "flechas_activas": [1]}),
    "cartel-4-vuelta": ("CHOFER", "El vehículo vuelve a salir", "Carlos · celular",
                        {"activos": ["chofer"], "flechas_activas": [2], "color_flecha": {2: OK}}),
}


def cartel(titulo, bajada, quien, estado):
    x = 140
    return (
        f'<rect x="{x}" y="372" width="96" height="10" rx="5" fill="{ACCENT}"/>'
        + texto(x, 492, titulo, 88, "d", 700, ACCENT, "start", 'letter-spacing="2"')
        + texto(x, 568, bajada, 36, "b", 500, TEXT, "start")
        + texto(x, 628, quien, 30, "b", 400, MUTED, "start")
        + ciclo(1440, 530, escala=0.70, **estado)
    )


def ademas():
    return (
        f'<rect x="{W / 2 - 48}" y="400" width="96" height="10" rx="5" fill="{ACCENT}"/>'
        + texto(W / 2, 560, "Y además…", 140, "d", 700, ACCENT)
        + texto(W / 2, 650, "Todo lo que gestiona el administrador", 40, "b", 500, MUTED)
    )


# ---------------------------------------------------------------- celular

# Hueco de la pantalla: la proporción de las tomas del celular (376x822), centrado y casi del alto del cuadro.
PANT_H = 940
PANT_W = round(PANT_H * 376 / 822)  # 430
PANT_X = (W - PANT_W) // 2
PANT_Y = (H - PANT_H) // 2
BISEL = 16


def rrect(x, y, w, h, r):
    """Camino de un rectángulo redondeado, para armar el hueco con fill-rule evenodd."""
    return (f"M{x + r} {y} H{x + w - r} A{r} {r} 0 0 1 {x + w} {y + r} V{y + h - r} "
            f"A{r} {r} 0 0 1 {x + w - r} {y + h} H{x + r} A{r} {r} 0 0 1 {x} {y + h - r} "
            f"V{y + r} A{r} {r} 0 0 1 {x + r} {y} Z")


def celular():
    """Fondo de la app con el dibujo del celular encima y la pantalla transparente."""
    bx, by = PANT_X - BISEL, PANT_Y - BISEL
    bw, bh = PANT_W + 2 * BISEL, PANT_H + 2 * BISEL
    fondo = f"M0 0 H{W} V{H} H0 Z"
    pantalla = rrect(PANT_X, PANT_Y, PANT_W, PANT_H, 46)
    cuerpo = rrect(bx, by, bw, bh, 62)
    botones = (
        f'<rect x="{bx - 5}" y="{by + 190}" width="7" height="70" rx="3" fill="{TEXT}"/>'
        f'<rect x="{bx - 5}" y="{by + 280}" width="7" height="70" rx="3" fill="{TEXT}"/>'
        f'<rect x="{bx + bw - 2}" y="{by + 230}" width="7" height="110" rx="3" fill="{TEXT}"/>'
    )
    return (
        '<defs><filter id="sombra" x="-20%" y="-20%" width="140%" height="140%">'
        '<feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#1F2A24" flood-opacity="0.28"/>'
        "</filter>"
        f'<clipPath id="fuera"><path d="{fondo} {cuerpo}" clip-rule="evenodd"/></clipPath></defs>'
        # el fondo con el hueco del celular entero, la sombra (solo afuera, para que no caiga sobre la
        # pantalla), y el cuerpo con el hueco de la pantalla
        f'<path d="{fondo} {cuerpo}" fill="{BG}" fill-rule="evenodd"/>'
        f'<g clip-path="url(#fuera)"><path d="{cuerpo}" fill="{TEXT}" filter="url(#sombra)"/></g>'
        f'<path d="{cuerpo} {pantalla}" fill="{TEXT}" fill-rule="evenodd"/>'
        + botones
    )


# ---------------------------------------------------------------- etiquetas fijas del rol

ETIQUETAS = {
    "etiqueta-chofer": ("chofer", "CHOFER", "Carlos · celular"),
    "etiqueta-admin": ("admin", "ADMINISTRADOR", "computadora"),
    "etiqueta-tecnico": ("tecnico", "TÉCNICO", "Javier · celular"),
}


def etiqueta(rol, titulo, resto):
    """Píldora blanca con el ícono y el rol. El ancho lo mide Chrome con la tipografía ya cargada."""
    x, y, alto = 40, 32, 68
    t_size, r_size = 30, 27
    cy = y + alto / 2
    s = 30 / 24
    medir = (
        "<script>document.fonts.ready.then(function(){"
        "var b=document.getElementById('txt').getBBox();"
        f"document.getElementById('pildora').setAttribute('width',b.x+b.width-{x}+28);"
        "});</script>"
    )
    return (
        '<defs><filter id="sombra" x="-10%" y="-30%" width="120%" height="180%">'
        '<feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#1F2A24" flood-opacity="0.18"/>'
        "</filter></defs>"
        f'<rect id="pildora" x="{x}" y="{y}" width="600" height="{alto}" rx="{alto / 2}" fill="#fff" '
        f'stroke="{LINE}" stroke-width="1.5" filter="url(#sombra)"/>'
        f'<circle cx="{x + 20 + 24}" cy="{cy}" r="24" fill="{ACCENT}"/>'
        f'<g transform="translate({x + 44 - 15} {cy - 15}) scale({s})" fill="none" stroke="#fff" '
        f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{ICONOS[rol]}</g>'
        f'<text id="txt" x="{x + 86}" y="{cy + 10.5}" font-size="{t_size}" class="d" font-weight="700" '
        f'fill="{ACCENT}" letter-spacing="1">{escape(titulo)}<tspan class="b" font-weight="500" '
        f'font-size="{r_size}" fill="{MUTED}" letter-spacing="0" dx="14">· {escape(resto)}</tspan></text>'
        + medir
    )


# ---------------------------------------------------------------- palabras clave

ICONOS_CLAVE = {
    "alerta": '<polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/>'
              '<path d="M12 8v4M12 16h.01"/>',
    "candado": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "orden": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6'
             'a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
    "ok": '<circle cx="12" cy="12" r="10"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
}

# Colores de estado de la app: rojo para lo bloqueante, azul de "info", verde para lo resuelto.
CLAVES = {
    "clave-1-defecto-bloqueante": (["Defecto", "bloqueante"], CRITICAL, "alerta"),
    "clave-2-vehiculo-bloqueado": (["Vehículo", "bloqueado"], CRITICAL, "candado"),
    "clave-3-orden-asignada": (["Orden de trabajo", "asignada"], "#2F6DB5", "orden"),
    "clave-4-defecto-resuelto": (["Defecto", "resuelto"], OK, "ok"),
}
CLAVE_CX = (PANT_X + PANT_W + BISEL + W) / 2  # al costado derecho del celular


def clave(lineas, color, icono):
    ancho, size, ic = 580, 56, 70
    alto = 52 + ic + 30 + len(lineas) * 66 + 40
    x, y = CLAVE_CX - ancho / 2, H / 2 - alto / 2
    s = ic / 24
    partes = [
        '<defs><filter id="sombra" x="-20%" y="-20%" width="140%" height="150%">'
        '<feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#1F2A24" flood-opacity="0.25"/>'
        "</filter></defs>",
        f'<rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="32" fill="{color}" filter="url(#sombra)"/>',
        f'<g transform="translate({CLAVE_CX - ic / 2} {y + 52}) scale({s:.4f})" fill="none" stroke="#fff" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONOS_CLAVE[icono]}</g>',
    ]
    for i, linea in enumerate(lineas):
        partes.append(texto(CLAVE_CX, y + 52 + ic + 30 + 52 + i * 66, linea, size, "d", 700, "#fff"))
    return "".join(partes)


# ---------------------------------------------------------------- salida

def graficos():
    yield "logo", svg(logo_camion() + logo_texto())
    yield "logo-capa-camion", svg(logo_camion(), fondo=False)
    yield "logo-capa-texto", svg(logo_texto(), fondo=False)
    yield "cierre", svg(cierre())
    for nombre, estado in CICLOS.items():
        yield nombre, svg(ciclo(*CICLO_CENTRO, **estado))
    for nombre, (t, b, q, estado) in CARTELES.items():
        yield nombre, svg(cartel(t, b, q, estado))
    yield "cartel-5-ademas", svg(ademas())
    yield "celular", svg(celular(), fondo=False)
    for nombre, args in ETIQUETAS.items():
        yield nombre, svg(etiqueta(*args), fondo=False)
    for nombre, args in CLAVES.items():
        yield nombre, svg(clave(*args), fondo=False)


def renderizar(svg_path, png_path, perfil):
    alto = H + 200  # el modo sin ventana puede achicar el área visible: se pide de más y se recorta
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
         f"--window-size={W},{alto}", "--default-background-color=00000000", "--virtual-time-budget=10000",
         f"--user-data-dir={perfil}", f"--screenshot={png_path}", svg_path.as_uri()],
        check=True, capture_output=True,
    )
    img = Image.open(png_path)
    if img.size[0] < W or img.size[1] < H:
        raise RuntimeError(f"{png_path.name}: Chrome devolvió {img.size}, más chico que {W}x{H}")
    img.crop((0, 0, W, H)).save(png_path)


def main():
    SVG_DIR.mkdir(exist_ok=True)
    PNG_DIR.mkdir(exist_ok=True)
    perfil = tempfile.mkdtemp(prefix="fg-chrome-")
    try:
        for nombre, contenido in graficos():
            s = SVG_DIR / f"{nombre}.svg"
            s.write_text(contenido, encoding="utf-8")
            renderizar(s, PNG_DIR / f"{nombre}.png", perfil)
            print("ok", nombre)
    finally:
        shutil.rmtree(perfil, ignore_errors=True)


if __name__ == "__main__":
    os.chdir(AQUI)
    main()
