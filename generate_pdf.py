from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Flowable
import os

# ── Palette ───────────────────────────────────────────────────────────────────
DARK     = colors.HexColor("#1A0A12")
DARKER   = colors.HexColor("#0E0509")
CRIMSON  = colors.HexColor("#C41E3A")
ORANGE   = colors.HexColor("#E86A17")
GOLD     = colors.HexColor("#F5B731")
BORDEAUX = colors.HexColor("#6B1D3A")
CREAM    = colors.HexColor("#FFF5E6")
CREAM_D  = colors.HexColor("#E8DCC5")
NAVY     = colors.HexColor("#1A3A6B")
TEAL     = colors.HexColor("#1A6B5A")
PURPLE   = colors.HexColor("#5C2D8F")
WHITE    = colors.white
W, H     = A4  # 595 x 842 pt

# ── Styles de texte ───────────────────────────────────────────────────────────
def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10, leading=14,
                textColor=DARK, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)

sTitle    = S("Title",   fontName="Helvetica-Bold", fontSize=32, leading=36,
              textColor=GOLD, spaceAfter=8, alignment=TA_CENTER)
sSubtitle = S("Sub",     fontName="Helvetica-Oblique", fontSize=13, leading=17,
              textColor=CREAM_D, spaceAfter=6, alignment=TA_CENTER)
sSection  = S("Sec",     fontName="Helvetica-Bold", fontSize=20, leading=24,
              textColor=GOLD, spaceAfter=6)
sSecSm    = S("SecSm",   fontName="Helvetica-Bold", fontSize=14, leading=18,
              textColor=CREAM, spaceAfter=4)
sBody     = S("Body",    fontName="Helvetica",       fontSize=10, leading=15,
              textColor=CREAM_D, spaceAfter=4)
sBodyDark = S("BodyD",   fontName="Helvetica",       fontSize=10, leading=15,
              textColor=DARK, spaceAfter=4)
sEye      = S("Eye",     fontName="Helvetica-BoldOblique", fontSize=9,
              textColor=GOLD, spaceAfter=2, leading=13)
sSmall    = S("Sm",      fontName="Helvetica-Oblique", fontSize=8, leading=12,
              textColor=CREAM_D, spaceAfter=2)
sMono     = S("Mono",    fontName="Courier", fontSize=9, leading=13,
              textColor=GOLD)
sNum      = S("Num",     fontName="Helvetica-Bold", fontSize=36, leading=38,
              textColor=GOLD, spaceAfter=0)
sNumSm    = S("NumSm",   fontName="Helvetica-Bold", fontSize=11,
              textColor=ORANGE, spaceAfter=0)
sCenter   = S("Ctr",     fontName="Helvetica",       fontSize=10, leading=15,
              textColor=CREAM_D, alignment=TA_CENTER)
sCenterB  = S("CtrB",    fontName="Helvetica-Bold",  fontSize=11, leading=15,
              textColor=CREAM, alignment=TA_CENTER, spaceAfter=2)
sContact  = S("Contact", fontName="Helvetica-Bold",  fontSize=13, leading=18,
              textColor=GOLD, spaceAfter=4)

# ── Helpers Flowable ──────────────────────────────────────────────────────────
def sp(h=6):
    return Spacer(1, h)

def hr(color=GOLD, thickness=1, opacity=0.25):
    return HRFlowable(width="100%", thickness=thickness,
                      color=color, spaceAfter=8, spaceBefore=4)

class ColorBlock(Flowable):
    """Rectangle plein en arrière-plan d'une ligne."""
    def __init__(self, w, h, color):
        super().__init__()
        self.w, self.h, self.color = w, h, color
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.w, self.h, fill=1, stroke=0)
    def wrap(self, *args):
        return self.w, self.h

# ── Fond de page ──────────────────────────────────────────────────────────────
def page_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # Bande dorée en bas
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, W, 4, fill=1, stroke=0)
    # Numéro de page
    if doc.page > 1:
        canvas.setFillColor(CREAM_D)
        canvas.setFont("Helvetica", 8)
        canvas.drawCentredString(W / 2, 12, f"Dance Your Foot · Dossier de présentation 2027 · {doc.page}")
    canvas.restoreState()

def cover_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    # Quadrant crimson gauche
    canvas.setFillColor(CRIMSON)
    p = canvas.beginPath()
    p.moveTo(0, H); p.lineTo(W * 0.55, H)
    p.lineTo(W * 0.3, 0); p.lineTo(0, 0)
    p.close()
    canvas.drawPath(p, fill=1, stroke=0)
    # Quadrant gold bas-droite
    canvas.setFillColor(GOLD)
    p = canvas.beginPath()
    p.moveTo(W * 0.5, H * 0.45); p.lineTo(W, H * 0.45)
    p.lineTo(W, 0); p.lineTo(W * 0.3, 0)
    p.close()
    canvas.drawPath(p, fill=1, stroke=0)
    # Quadrant orange haut-droite
    canvas.setFillColor(ORANGE)
    p = canvas.beginPath()
    p.moveTo(W * 0.55, H); p.lineTo(W, H)
    p.lineTo(W, H * 0.45); p.lineTo(W * 0.5, H * 0.45)
    p.close()
    canvas.drawPath(p, fill=1, stroke=0)
    # Overlay sombre
    canvas.setFillColor(colors.HexColor("#1A0A12"))
    canvas.setFillAlpha(0.62)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.setFillAlpha(1)
    # Bande dorée en bas
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, W, 5, fill=1, stroke=0)
    canvas.restoreState()

# ── Contenu ───────────────────────────────────────────────────────────────────
story = []

# ═══════════════════════════════════════════════════════════════
#  PAGE 1 · COUVERTURE
# ═══════════════════════════════════════════════════════════════
story.append(Spacer(1, 90))
story.append(Paragraph("DANCE YOUR FOOT", sTitle))
story.append(sp(4))
story.append(Paragraph("Bouge · Tire · Improvise", sSubtitle))
story.append(sp(32))

# Tagline centrale
tag_data = [["Bouge", "·", "Tire", "·", "Improvise"]]
tag_style = TableStyle([
    ("FONTNAME",    (0,0), (-1,-1), "Helvetica-BoldOblique"),
    ("FONTSIZE",    (0,0), (-1,-1), 18),
    ("TEXTCOLOR",   (0,0), (-1,-1), CREAM),
    ("TEXTCOLOR",   (1,0), (1,0),  ORANGE),
    ("TEXTCOLOR",   (3,0), (3,0),  ORANGE),
    ("ALIGN",       (0,0), (-1,-1), "CENTER"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("BOTTOMPADDING",(0,0),(-1,-1), 0),
    ("TOPPADDING",  (0,0), (-1,-1), 0),
])
story.append(Table(tag_data, colWidths=[90, 20, 60, 20, 90],
                   style=tag_style, hAlign="CENTER"))
story.append(sp(40))

# 4 piliers
pillar_data = [
    [Paragraph("⚽\nFOOT",      S("p1", fontName="Helvetica-BoldOblique", fontSize=14,
               textColor=GOLD, alignment=TA_CENTER, leading=18)),
     Paragraph("💃\nDANSE",     S("p2", fontName="Helvetica-BoldOblique", fontSize=14,
               textColor=GOLD, alignment=TA_CENTER, leading=18)),
     Paragraph("🎵\nIMPRO",     S("p3", fontName="Helvetica-BoldOblique", fontSize=14,
               textColor=GOLD, alignment=TA_CENTER, leading=18)),
     Paragraph("🔥\nPUBLIC",    S("p4", fontName="Helvetica-BoldOblique", fontSize=14,
               textColor=GOLD, alignment=TA_CENTER, leading=18))],
]
pillar_style = TableStyle([
    ("BACKGROUND",  (0,0), (-1,-1), BORDEAUX),
    ("ALIGN",       (0,0), (-1,-1), "CENTER"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("GRID",        (0,0), (-1,-1), 0.5, colors.HexColor("#3A0E22")),
    ("TOPPADDING",  (0,0), (-1,-1), 14),
    ("BOTTOMPADDING",(0,0),(-1,-1), 14),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
    ("RIGHTPADDING",(0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[BORDEAUX]),
])
story.append(Table(pillar_data, colWidths=[119]*4,
                   style=pillar_style, hAlign="CENTER"))
story.append(sp(48))

story.append(Paragraph("DOSSIER DE PRÉSENTATION · ÉDITION 2027", sEye))
story.append(Paragraph("Sylvain Nicolier · Sylvain@danceyourfoot.com · +41 78 849 00 89", sSmall))
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
#  PAGE 2 · LE CONCEPT
# ═══════════════════════════════════════════════════════════════
story.append(sp(16))
story.append(Paragraph("— 01 · LE CONCEPT", sEye))
story.append(Paragraph("Un tournoi inédit.", sSection))
story.append(sp(4))
story.append(Paragraph(
    "Dance Your Foot fusionne le football, la danse et l'improvisation en un seul événement "
    "spectaculaire. 4 écoles de danse s'affrontent sur un terrain de foot. Chaque but devient "
    "une fête. Chaque match, un battle. Et c'est le public qui tranche.", sBody))
story.append(sp(12))
story.append(hr())

# 4 piliers détaillés
pillars = [
    ("01", "FOOT",   CRIMSON,  "Vrai terrain, vrais buts, vraies règles. On joue pour de bon — arbitré sérieusement."),
    ("02", "DANSE",  ORANGE,   "Chaque équipe est une école : hip-hop, afro, krump, voguing… Une discipline, un style."),
    ("03", "IMPRO",  GOLD,     "Le DJ change de style toutes les 1 à 2 minutes. Adapte-toi ou perds le rythme."),
    ("04", "PUBLIC", BORDEAUX, "Pas de juges. Le public vote, le public tranche, le public fait l'événement."),
]
for num, title, color, desc in pillars:
    row = [
        Paragraph(num,   S("pn", fontName="Courier", fontSize=9, textColor=color)),
        Paragraph(title, S("pt", fontName="Helvetica-Bold", fontSize=16,
                            textColor=color, leading=18)),
        Paragraph(desc,  S("pd", fontName="Helvetica", fontSize=9,
                            textColor=CREAM_D, leading=13)),
    ]
    t = Table([row], colWidths=[28, 80, 368], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#200A14")),
        ("LEFTBORDERCOLOR",(0,0),(0,0), color),
        ("LINEAFTER",     (0,0), (0,0), 3, color),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (0,0), 10),
        ("LEFTPADDING",   (1,0), (1,0), 10),
    ]))
    story.append(KeepTogether([t, sp(4)]))

story.append(sp(12))
story.append(hr())
story.append(Paragraph("— 02 · LES RÈGLES", sEye))
story.append(Paragraph("Cinq règles. Zéro exception.", sSection))
story.append(sp(4))

rules = [
    ("01", "Toujours danser et jouer le ballon",     "Le corps reste en rythme, même balle au pied."),
    ("02", "Interdit de courir",                     "On glisse, on tourne, on roule — jamais on ne sprinte."),
    ("03", "S'adapter à la musique",                 "Le DJ change de style toutes les 1–2 min. Suis ou sanctionne."),
    ("04", "Respecter les règles du football",       "Touches, sorties, fautes. Un vrai match, arbitré sérieusement."),
    ("05", "Célébrer en équipe après chaque but",    "5 morceaux par équipe : chaque but devient chorégraphie."),
]
rule_rows = [[
    Paragraph(n,    S("rn", fontName="Helvetica-Bold", fontSize=22, textColor=GOLD, leading=24)),
    Paragraph(txt,  S("rt", fontName="Helvetica-BoldOblique", fontSize=11, textColor=CREAM, leading=14)),
    Paragraph(det,  S("rd", fontName="Helvetica-Oblique", fontSize=9, textColor=CREAM_D, leading=13)),
] for n, txt, det in rules]

rule_table = Table(rule_rows, colWidths=[40, 220, 216])
rule_table.setStyle(TableStyle([
    ("LINEABOVE",       (0,0), (-1,-1), 0.5, colors.HexColor("#3A1A2A")),
    ("LINEBELOW",       (0,-1),(-1,-1), 0.5, colors.HexColor("#3A1A2A")),
    ("VALIGN",          (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",      (0,0), (-1,-1), 8),
    ("BOTTOMPADDING",   (0,0), (-1,-1), 8),
    ("LEFTPADDING",     (0,0), (0,-1), 0),
    ("ROWBACKGROUNDS",  (0,0), (-1,-1), [DARK, colors.HexColor("#200A14")]),
]))
story.append(rule_table)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
#  PAGE 3 · FORMAT & VOTE
# ═══════════════════════════════════════════════════════════════
story.append(sp(16))
story.append(Paragraph("— 03 · LE FORMAT", sEye))
story.append(Paragraph("L'événement en chiffres.", sSection))
story.append(sp(8))

# Stats clés
stats = [
    ("4",    "Écoles de danse"),
    ("3",    "Matchs (2 qualifs + finale)"),
    ("1h35", "Show complet"),
    ("200",  "m² terrain moquette"),
]
stat_data = [[
    [Paragraph(n,  S("sn", fontName="Helvetica-Bold", fontSize=28, textColor=GOLD,
                       leading=30, alignment=TA_CENTER)),
     Paragraph(l,  S("sl", fontName="Helvetica", fontSize=8, textColor=CREAM_D,
                       leading=11, alignment=TA_CENTER))]
    for n, l in stats
]]
flat_stat = [[
    Table([[Paragraph(n, S("sn2", fontName="Helvetica-Bold", fontSize=28, textColor=GOLD,
                            leading=30, alignment=TA_CENTER)),
            Paragraph(l, S("sl2", fontName="Helvetica", fontSize=8, textColor=CREAM_D,
                            leading=11, alignment=TA_CENTER))]], colWidths=[119])
    for n, l in stats
]]
st = Table(flat_stat, colWidths=[119]*4, hAlign="CENTER")
st.setStyle(TableStyle([
    ("BACKGROUND",      (0,0), (-1,-1), colors.HexColor("#200A14")),
    ("LINEAFTER",       (0,0), (2,0), 0.5, colors.HexColor("#3A1A2A")),
    ("TOPPADDING",      (0,0), (-1,-1), 14),
    ("BOTTOMPADDING",   (0,0), (-1,-1), 14),
    ("ALIGN",           (0,0), (-1,-1), "CENTER"),
    ("LINEABOVE",       (0,0), (-1,0), 2, GOLD),
]))
story.append(st)
story.append(sp(16))

# Timeline match
story.append(Paragraph("UN MATCH · TROIS TEMPS", sEye))
story.append(sp(4))
tl_data = [[
    Paragraph("2'\nSOLO\n+ TIR",  S("tl1", fontName="Helvetica-Bold", fontSize=9,
              textColor=GOLD, alignment=TA_CENTER, leading=12)),
    Paragraph("10'\nJEU",         S("tl2", fontName="Helvetica-Bold", fontSize=12,
              textColor=DARK, alignment=TA_CENTER, leading=14)),
    Paragraph("4'\nCÉLÉBRATIONS",S("tl3", fontName="Helvetica-Bold", fontSize=9,
              textColor=DARK, alignment=TA_CENTER, leading=12)),
]]
tl = Table(tl_data, colWidths=[55, 338, 83])
tl.setStyle(TableStyle([
    ("BACKGROUND",      (0,0),(0,0), BORDEAUX),
    ("BACKGROUND",      (1,0),(1,0), GOLD),
    ("BACKGROUND",      (2,0),(2,0), ORANGE),
    ("VALIGN",          (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",      (0,0),(-1,-1), 14),
    ("BOTTOMPADDING",   (0,0),(-1,-1), 14),
    ("ROWHEIGHT",       (0,0),(-1,-1), 52),
]))
story.append(tl)
story.append(sp(16))

# Déroulé show
story.append(Paragraph("DÉROULÉ COMPLET · 1 H 35", sEye))
story.append(sp(4))
show_rows = [
    ("QUALIF 1", "16'", CRIMSON, CREAM, "Solo capitaines + tir au but, jeu, célébrations."),
    ("VOTE",      "1'", CREAM, BORDEAUX, "Le public lève son carton bicolore."),
    ("INTERLUDE", "5'", BORDEAUX, GOLD, "Le DJ enchaîne, transition musicale."),
    ("QUALIF 2", "16'", CRIMSON, CREAM, "Deuxième duel pour désigner le second finaliste."),
    ("VOTE",      "1'", CREAM, BORDEAUX, "Même rituel : carton, son, annonce."),
    ("INTERLUDE", "5'", BORDEAUX, GOLD, ""),
    ("FINALE",   "16'", GOLD, DARK, "Les deux gagnants s'affrontent pour le titre."),
    ("CYPHER",   "30'", ORANGE, DARK, "Équipes et public mélangés. Remise des prix."),
    ("RÉSULTAT",  "1'", BORDEAUX, GOLD, ""),
]
show_data = [[
    Paragraph(name, S(f"sn{i}", fontName="Helvetica-Bold", fontSize=9,
              textColor=tc, alignment=TA_CENTER)),
    Paragraph(dur,  S(f"sd{i}", fontName="Helvetica-BoldOblique", fontSize=11,
              textColor=tc, alignment=TA_CENTER)),
    Paragraph(desc, S(f"ss{i}", fontName="Helvetica-Oblique", fontSize=8,
              textColor=CREAM_D)),
] for i, (name, dur, bg, tc, desc) in enumerate(show_rows)]

show_bgs = [r[2] for r in show_rows]
show_tcs = [r[3] for r in show_rows]
show_tbl = Table(show_data, colWidths=[72, 40, 364])
ts_show = TableStyle([
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("LINEBELOW",     (0,0),(-1,-1), 0.3, colors.HexColor("#3A1A2A")),
])
for i, (_, _, bg, tc, _) in enumerate(show_rows):
    ts_show.add("BACKGROUND", (0,i), (1,i), bg)
    ts_show.add("BACKGROUND", (2,i), (2,i), colors.HexColor("#200A14"))
show_tbl.setStyle(ts_show)
story.append(show_tbl)
story.append(sp(16))
story.append(hr())

# Vote
story.append(Paragraph("— 04 · VOTE DU PUBLIC", sEye))
story.append(Paragraph("Pas de juges. Vous décidez.", sSection))
story.append(sp(6))
story.append(Paragraph(
    "Un carton bicolore distribué à l'entrée. En fin de match, le public lève son carton. "
    "En cas d'égalité, trois spectateurs tirés au sort tranchent. Cinq critères guidés "
    "par le speaker :", sBody))
story.append(sp(8))

criteria = [
    ("01", "Créativité",           "92%"),
    ("02", "Qualité de la danse",  "86%"),
    ("03", "Respect des rythmes",  "78%"),
    ("04", "Jeu footballistique",  "70%"),
    ("05", "Célébrations",         "95%"),
]
crit_data = [[
    Paragraph(n,   S("cn", fontName="Courier", fontSize=8, textColor=GOLD)),
    Paragraph(name,S("cm", fontName="Helvetica-Bold", fontSize=10, textColor=CREAM)),
    Paragraph(pct, S("cp", fontName="Helvetica-Bold", fontSize=10, textColor=ORANGE,
                       alignment=TA_RIGHT)),
] for n, name, pct in criteria]
crit_tbl = Table(crit_data, colWidths=[32, 370, 74])
crit_tbl.setStyle(TableStyle([
    ("BACKGROUND",      (0,0),(-1,-1), colors.HexColor("#200A14")),
    ("LINEABOVE",       (0,0),(-1,-1), 0.5, colors.HexColor("#3A1A2A")),
    ("LINEBELOW",       (0,-1),(-1,-1),0.5, colors.HexColor("#3A1A2A")),
    ("VALIGN",          (0,0),(-1,-1), "MIDDLE"),
    ("TOPPADDING",      (0,0),(-1,-1), 7),
    ("BOTTOMPADDING",   (0,0),(-1,-1), 7),
    ("LEFTPADDING",     (0,0),(0,-1), 10),
]))
story.append(crit_tbl)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
#  PAGE 4 · BUDGET
# ═══════════════════════════════════════════════════════════════
story.append(sp(16))
story.append(Paragraph("— 05 · BUDGET", sEye))
story.append(Paragraph("Édition fondatrice 2027.", sSection))
story.append(sp(4))
story.append(Paragraph(
    "Budget estimé pour la première édition. Les postes marqués 'Estimé' sont des fourchettes "
    "de marché suisse romand. Les postes 'Confirmé' sont validés.", sBody))
story.append(sp(10))

budget_sections = [
    ("👥  RH & CACHETS", CRIMSON, [
        ("Coordination",            "Responsable événement",              200,  "Confirmé"),
        ("DJ",                      "Cachet artiste",                     200,  "À négocier"),
        ("MC / Speaker",            "Animation publique",                 200,  "À négocier"),
        ("Arbitre",                 "Match officiel",                     200,  "Confirmé"),
        ("Photo & vidéo",           "Captation + traitement + montage",  2000,  "Confirmé"),
        ("Défraiements équipes",    "4 équipes × 200 CHF",                800,  "Confirmé"),
    ]),
    ("🏟️  LIEU & TECHNIQUE", NAVY, [
        ("Location salle / lieu",   "Espace urbain couvert",             2500,  "Estimé"),
        ("Sonorisation",            "Enceintes, table de mix, câblage",   800,  "Estimé"),
        ("Éclairage",               "Jeux de lumière, projecteurs",       500,  "Estimé"),
        ("Électricité",             "Raccordement / générateur",          200,  "Estimé"),
    ]),
    ("📦  MATÉRIEL & LOGISTIQUE", BORDEAUX, [
        ("Terrain gonflable",       "Location + installation",           2000,  "Confirmé"),
        ("Chasubles personnalisées","30 pièces crew + équipes",           400,  "Confirmé"),
        ("Ballon personnalisé",     "Aux couleurs DYF",                    60,  "Confirmé"),
        ("Cartons public",          "~500 cartons bicolores",             200,  "Confirmé"),
        ("Transport & logistique",  "Déplacement matériel",              300,  "Confirmé"),
    ]),
    ("🛡️  SÉCURITÉ & COUVERTURE", TEAL, [
        ("Sécurité / Service d'ordre","Selon exigences du lieu",          500,  "Estimé"),
        ("Assurance événementielle", "RC obligatoire",                    300,  "Estimé"),
        ("SUISA",                    "Droits musique live",               200,  "À vérifier"),
    ]),
    ("📣  COMMUNICATION & RÉCOMPENSES", ORANGE, [
        ("Communication",            "Affiches, flyers, réseaux",         400,  "Estimé"),
        ("Trophées / Prix",          "Équipes, MVP, DJ",                  350,  "Estimé"),
        ("Badges & accréditations",  "Staff, presse, sponsors",           100,  "Estimé"),
    ]),
    ("🎨  ORGANISATION & ADMINISTRATION", PURPLE, [
        ("Organisation générale",    "Frais admin, coordination",        2000,  "Confirmé"),
        ("Création graphique & tech","Identité visuelle, site web",      2000,  "Confirmé"),
        ("Divers & imprévus",        "Réserve ~5%",                       500,  "Réserve"),
    ]),
]

grand_total = 0

for sec_title, color, rows in budget_sections:
    # En-tête section
    hdr = Table([[Paragraph(sec_title, S("bh", fontName="Helvetica-Bold", fontSize=11,
                                          textColor=WHITE, leading=14))]],
                colWidths=[476])
    hdr.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), color),
        ("TOPPADDING",    (0,0),(-1,-1), 7),
        ("BOTTOMPADDING", (0,0),(-1,-1), 7),
        ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ]))
    story.append(hdr)

    subtotal = sum(r[2] for r in rows)
    grand_total += subtotal

    # Lignes
    budget_rows = []
    for i, (poste, detail, montant, statut) in enumerate(rows):
        sc = {"Confirmé": TEAL, "Estimé": ORANGE, "À négocier": CRIMSON,
              "À vérifier": colors.HexColor("#888888"), "Réserve": NAVY}.get(statut, DARK)
        budget_rows.append([
            Paragraph(poste,  S("bp", fontName="Helvetica-Bold", fontSize=9,
                                 textColor=CREAM, leading=13)),
            Paragraph(detail, S("bd", fontName="Helvetica-Oblique", fontSize=8,
                                 textColor=CREAM_D, leading=12)),
            Paragraph(f"{montant:,} CHF".replace(",", " "),
                                S("bm", fontName="Helvetica-Bold", fontSize=10,
                                 textColor=GOLD, alignment=TA_RIGHT, leading=13)),
            Paragraph(statut, S("bs", fontName="Helvetica", fontSize=7,
                                 textColor=sc, alignment=TA_CENTER, leading=11)),
        ])

    # Sous-total
    budget_rows.append([
        Paragraph("Sous-total", S("bst", fontName="Helvetica-Bold", fontSize=9,
                                    textColor=WHITE, alignment=TA_RIGHT, leading=13)),
        Paragraph("", sBody),
        Paragraph(f"{subtotal:,} CHF".replace(",", " "),
                  S("bsv", fontName="Helvetica-Bold", fontSize=11,
                    textColor=GOLD, alignment=TA_RIGHT, leading=13)),
        Paragraph("", sBody),
    ])

    bt = Table(budget_rows, colWidths=[148, 190, 90, 48])
    ts = TableStyle([
        ("BACKGROUND",      (0,0),(-1,-2), colors.HexColor("#200A14")),
        ("BACKGROUND",      (0,-1),(-1,-1), colors.HexColor("#0E0509")),
        ("ROWBACKGROUNDS",  (0,0),(-1,-2),
         [colors.HexColor("#200A14"), colors.HexColor("#180811")]),
        ("LINEBELOW",       (0,0),(-1,-2), 0.3, colors.HexColor("#3A1A2A")),
        ("LINEABOVE",       (0,-1),(-1,-1),0.5, color),
        ("VALIGN",          (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",      (0,0),(-1,-1), 5),
        ("BOTTOMPADDING",   (0,0),(-1,-1), 5),
        ("LEFTPADDING",     (0,0),(0,-1), 10),
    ])
    bt.setStyle(ts)
    story.append(KeepTogether([bt, sp(6)]))

# Total général
story.append(sp(6))
total_data = [[
    Paragraph("💰  TOTAL GÉNÉRAL", S("tg", fontName="Helvetica-Bold", fontSize=14,
              textColor=GOLD, alignment=TA_RIGHT, leading=18)),
    Paragraph(f"{grand_total:,} CHF".replace(",", " "),
              S("tv", fontName="Helvetica-Bold", fontSize=18,
                textColor=GOLD, alignment=TA_RIGHT, leading=22)),
]]
total_tbl = Table(total_data, colWidths=[356, 120])
total_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), DARK),
    ("LINEABOVE",     (0,0),(-1,-1), 3, GOLD),
    ("TOPPADDING",    (0,0),(-1,-1), 12),
    ("BOTTOMPADDING", (0,0),(-1,-1), 12),
    ("RIGHTPADDING",  (0,0),(-1,-1), 8),
]))
story.append(total_tbl)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
#  PAGE 5 · PARTENAIRES & CONTACT
# ═══════════════════════════════════════════════════════════════
story.append(sp(16))
story.append(Paragraph("— 06 · DEVENIR PARTENAIRE", sEye))
story.append(Paragraph("Construisons ensemble.", sSection))
story.append(sp(6))
story.append(Paragraph(
    "Dance Your Foot cherche ses partenaires fondateurs. Nous proposons trois niveaux "
    "d'engagement, chacun avec une visibilité et des avantages exclusifs.", sBody))
story.append(sp(12))

partners = [
    ("MVP",     "12 000 CHF", GOLD,    DARK,
     "Logo principal sur tous les supports · Mention au micro à chaque match\n"
     "Bannières terrain · Contenu vidéo dédié · Activation sur place"),
    ("CAPTAIN", "6 000 CHF",  CRIMSON, CREAM,
     "Logo sur les chasubles et le terrain · Mention speaker\n"
     "Présence sur le site et réseaux · Pack billetterie VIP"),
    ("CREW",    "2 500 CHF",  BORDEAUX,CREAM,
     "Logo sur les supports print · Mention site web\n"
     "Invitations pour l'équipe · Visibilité réseaux sociaux"),
]
for level, price, bg, tc, benefits in partners:
    pd = [
        [Paragraph(level, S(f"pl{level}", fontName="Helvetica-Bold", fontSize=22,
                              textColor=tc, leading=24)),
         Paragraph(price, S(f"pp{level}", fontName="Helvetica-BoldOblique", fontSize=18,
                              textColor=tc, alignment=TA_RIGHT, leading=22))],
        [Paragraph(benefits.replace("\n", "<br/>"),
                   S(f"pb{level}", fontName="Helvetica", fontSize=9,
                     textColor=CREAM_D if tc == DARK else CREAM_D,
                     leading=14), ), ""],
    ]
    pt = Table(pd, colWidths=[238, 238])
    pt.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), bg),
        ("SPAN",          (0,1),(1,1)),
        ("TOPPADDING",    (0,0),(-1,-1), 12),
        ("BOTTOMPADDING", (0,0),(-1,-1), 12),
        ("LEFTPADDING",   (0,0),(-1,-1), 16),
        ("RIGHTPADDING",  (0,0),(-1,-1), 16),
        ("LINEABOVE",     (0,0),(-1,0), 3, tc if bg != GOLD else DARK),
    ]))
    story.append(pt)
    story.append(sp(6))

story.append(sp(20))
story.append(hr(GOLD, 2))
story.append(sp(12))

# Contact
story.append(Paragraph("— 07 · CONTACT", sEye))
story.append(Paragraph("On vous rappelle dans les 48 h.", sSection))
story.append(sp(10))

contact_data = [
    ["Organisateur",  "Sylvain Nicolier"],
    ["Email",         "Sylvain@danceyourfoot.com"],
    ["Téléphone",     "+41 78 849 00 89"],
    ["Région",        "Suisse romande"],
    ["Site web",      "danceyourfoot.com"],
]
for label, val in contact_data:
    row = Table([[
        Paragraph(label, S("cl", fontName="Courier", fontSize=9, textColor=GOLD)),
        Paragraph(val,   S("cv", fontName="Helvetica-Bold", fontSize=11,
                             textColor=CREAM, leading=14)),
    ]], colWidths=[110, 366])
    row.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), colors.HexColor("#200A14")),
        ("LINEABOVE",     (0,0),(-1,-1), 0.5, colors.HexColor("#3A1A2A")),
        ("TOPPADDING",    (0,0),(-1,-1), 8),
        ("BOTTOMPADDING", (0,0),(-1,-1), 8),
        ("LEFTPADDING",   (0,0),(0,0), 10),
        ("LEFTPADDING",   (1,0),(1,0), 10),
    ]))
    story.append(row)

story.append(sp(6))
story.append(Table([[
    Paragraph("BOUGE · TIRE · IMPROVISE",
              S("ft", fontName="Helvetica-BoldOblique", fontSize=9,
                textColor=colors.HexColor("#333333"), alignment=TA_CENTER))
]], colWidths=[476]))

# ── Build ──────────────────────────────────────────────────────────────────────
out = "/home/user/danceyourfoot/DanceYourFoot_Presentation_2027.pdf"

doc = SimpleDocTemplate(
    out,
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=16*mm, bottomMargin=18*mm,
    title="Dance Your Foot · Dossier de présentation 2027",
    author="Sylvain Nicolier",
    subject="Tournoi danse + football · Édition fondatrice 2027",
)

def onPage(canvas, doc):
    if doc.page == 1:
        cover_bg(canvas, doc)
    else:
        page_bg(canvas, doc)

doc.build(story, onFirstPage=onPage, onLaterPages=onPage)
print(f"PDF généré : {out}  ({os.path.getsize(out)//1024} Ko)")
