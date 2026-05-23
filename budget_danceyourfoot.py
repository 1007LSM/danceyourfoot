import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Budget DYF 2027"

# ── Couleurs ──────────────────────────────────────────────────────────────────
C_DARK      = "1A0A12"
C_GOLD      = "F5B731"
C_CRIMSON   = "C41E3A"
C_ORANGE    = "E86A17"
C_BORDEAUX  = "6B1D3A"
C_CREAM     = "FFF5E6"
C_LIGHTGOLD = "FDF3D5"
C_GREY      = "F2F2F2"
C_WHITE     = "FFFFFF"
C_MISSING   = "FFF0E0"
C_MISSING_H = "E86A17"

def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def border(style="thin", color="CCCCCC"):
    s = Side(style=style, color=color)
    return Border(left=s, right=s, top=s, bottom=s)

def font(bold=False, color="000000", size=11, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Calibri")

def align(h="left", v="center", wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

# ── Largeurs colonnes ─────────────────────────────────────────────────────────
ws.column_dimensions["A"].width = 32
ws.column_dimensions["B"].width = 36
ws.column_dimensions["C"].width = 16
ws.column_dimensions["D"].width = 14

# ── Ligne 1 : Titre principal ─────────────────────────────────────────────────
ws.row_dimensions[1].height = 48
ws.merge_cells("A1:D1")
c = ws["A1"]
c.value = "DANCE YOUR FOOT · BUDGET ÉDITION 2027"
c.font = Font(bold=True, color=C_GOLD, size=18, name="Calibri")
c.fill = fill(C_DARK)
c.alignment = align("center", "center")

# ── Ligne 2 : sous-titre ──────────────────────────────────────────────────────
ws.row_dimensions[2].height = 22
ws.merge_cells("A2:D2")
c = ws["A2"]
c.value = "Suisse romande · Première édition · Contact : Sylvain@danceyourfoot.com"
c.font = Font(italic=True, color="BBBBBB", size=10, name="Calibri")
c.fill = fill(C_DARK)
c.alignment = align("center", "center")

ws.row_dimensions[3].height = 10  # espace

# ── En-têtes colonnes ─────────────────────────────────────────────────────────
ws.row_dimensions[4].height = 24
headers = ["POSTE", "DÉTAIL / NOTE", "MONTANT (CHF)", "STATUT"]
for col, h in enumerate(headers, 1):
    c = ws.cell(row=4, column=col, value=h)
    c.font = Font(bold=True, color=C_CREAM, size=10, name="Calibri")
    c.fill = fill(C_BORDEAUX)
    c.alignment = align("center", "center")
    c.border = border("thin", "6B1D3A")

# ── Données ───────────────────────────────────────────────────────────────────
sections = [
    {
        "title": "👥  RH & CACHETS",
        "color_h": C_CRIMSON,
        "color_row": "FDF0F2",
        "rows": [
            ("Coordination",               "Responsable événement — journée complète",        200,   "Confirmé"),
            ("DJ",                         "Cachet artiste (tarif à revoir : +300 CHF min.)",  200,   "À négocier"),
            ("MC / Speaker",               "Animation publique — cachet",                      200,   "À négocier"),
            ("Arbitre",                    "Match officiel, briefing inclus",                  200,   "Confirmé"),
            ("Photo & vidéo",              "Captation jour J + traitement + montage",          2000,  "Confirmé"),
            ("Défraiements équipes",       "4 équipes × 200 CHF",                              800,   "Confirmé"),
        ],
    },
    {
        "title": "📦  MATÉRIEL & LOGISTIQUE",
        "color_h": C_BORDEAUX,
        "color_row": "F5F0F3",
        "rows": [
            ("Ballon personnalisé",        "Ballon officiel aux couleurs DYF",                 60,    "Confirmé"),
            ("Chasubles personnalisées",   "30 pièces — crew + équipes",                       400,   "Confirmé"),
            ("Terrain gonflable",          "Location + installation + personnalisation",        2000,  "Confirmé"),
            ("Transport & logistique",     "Déplacement matériel, manutention",                300,   "Confirmé"),
            ("Cartons public & arbitres",  "~500 cartons bicolores",                           200,   "Confirmé"),
        ],
    },
    {
        "title": "🎨  ORGANISATION & COMMUNICATION",
        "color_h": "7B3A8F",
        "color_row": "F7F0FA",
        "rows": [
            ("SUISA",                      "Droits musique live — Suisse (selon nb spectateurs)", 200, "À vérifier"),
            ("Organisation générale",      "Frais admin, imprévus ops",                         2000,  "Confirmé"),
            ("Création graphique & tech",  "Identité visuelle, supports, site",                 2000,  "Confirmé"),
            ("Divers & imprévus",          "Réserve 5 %",                                        500,  "Réserve"),
        ],
    },
    {
        "title": "⚠️  POSTES MANQUANTS (à budgéter)",
        "color_h": C_MISSING_H,
        "color_row": C_MISSING,
        "rows": [
            ("Location salle / lieu",      "Estimation : 1 500–5 000 CHF selon lieu",           0,    "Non budgété"),
            ("Sonorisation",               "Enceintes, table de mix, câblage DJ — 500–1 500",    0,    "Non budgété"),
            ("Éclairage",                  "Jeux de lumière, projecteurs — 300–800",             0,    "Non budgété"),
            ("Assurance événementielle",   "RC obligatoire pour la plupart des salles",          0,    "Non budgété"),
            ("Trophées / Prix",            "Récompenses équipes + MVP — 200–500",                0,    "Non budgété"),
            ("Communication",             "Affiches, flyers, boost réseaux — 300–600",          0,    "Non budgété"),
            ("Sécurité",                   "Souvent exigé selon le lieu — 300–800",              0,    "Non budgété"),
        ],
    },
]

current_row = 5
subtotals = []

for sec in sections:
    # En-tête section
    ws.row_dimensions[current_row].height = 26
    ws.merge_cells(f"A{current_row}:D{current_row}")
    c = ws.cell(row=current_row, column=1, value=sec["title"])
    c.font = Font(bold=True, color=C_WHITE, size=12, name="Calibri")
    c.fill = fill(sec["color_h"])
    c.alignment = align("left", "center")
    c.border = border("medium", sec["color_h"])
    current_row += 1

    # Lignes de données
    sec_start = current_row
    for i, (poste, detail, montant, statut) in enumerate(sec["rows"]):
        ws.row_dimensions[current_row].height = 20
        row_color = C_GREY if i % 2 == 0 else C_WHITE
        if sec["title"].startswith("⚠️"):
            row_color = "FFF4E6" if i % 2 == 0 else C_MISSING

        data = [poste, detail, montant if montant else "—", statut]
        for col, val in enumerate(data, 1):
            c = ws.cell(row=current_row, column=col, value=val)
            c.fill = fill(row_color)
            c.font = Font(color="333333" if col != 3 else ("C41E3A" if sec["title"].startswith("⚠️") and montant == 0 else "1A1A1A"),
                          size=10, bold=(col == 3 and montant > 0), name="Calibri",
                          italic=(col == 3 and montant == 0 and sec["title"].startswith("⚠️")))
            c.alignment = align("right" if col == 3 else "left", "center")
            c.border = border("thin", "DDDDDD")
            if col == 3 and isinstance(val, int) and val > 0:
                c.number_format = '#,##0" CHF"'

        current_row += 1

    # Sous-total (seulement pour les 3 premières sections)
    if not sec["title"].startswith("⚠️"):
        ws.row_dimensions[current_row].height = 22
        ws.merge_cells(f"A{current_row}:B{current_row}")
        c = ws.cell(row=current_row, column=1, value=f"Sous-total  {sec['title'].split('  ')[1]}")
        c.font = Font(bold=True, color=C_WHITE, size=10, name="Calibri")
        c.fill = fill(sec["color_h"])
        c.alignment = align("right", "center")

        st_cell = ws.cell(row=current_row, column=3,
                          value=f"=SUM(C{sec_start}:C{current_row-1})")
        st_cell.font = Font(bold=True, color=C_GOLD, size=11, name="Calibri")
        st_cell.fill = fill(C_DARK)
        st_cell.number_format = '#,##0" CHF"'
        st_cell.alignment = align("right", "center")
        subtotals.append(f"C{current_row}")

        ws.cell(row=current_row, column=4).fill = fill(C_DARK)
        current_row += 1

    current_row += 1  # ligne vide entre sections

# ── Total général ─────────────────────────────────────────────────────────────
current_row += 1
ws.row_dimensions[current_row].height = 36
ws.merge_cells(f"A{current_row}:B{current_row}")
c = ws.cell(row=current_row, column=1, value="💰  TOTAL BUDGETÉ (hors postes manquants)")
c.font = Font(bold=True, color=C_GOLD, size=14, name="Calibri")
c.fill = fill(C_DARK)
c.alignment = align("right", "center")

total_formula = "=" + "+".join(subtotals)
tc = ws.cell(row=current_row, column=3, value=total_formula)
tc.font = Font(bold=True, color=C_GOLD, size=16, name="Calibri")
tc.fill = fill(C_DARK)
tc.number_format = '#,##0" CHF"'
tc.alignment = align("right", "center")

ws.cell(row=current_row, column=4).fill = fill(C_DARK)

# ── Note estimation réaliste ──────────────────────────────────────────────────
current_row += 2
ws.row_dimensions[current_row].height = 22
ws.merge_cells(f"A{current_row}:D{current_row}")
c = ws.cell(row=current_row, column=1,
            value="ℹ️  Budget réaliste estimé avec tous les postes manquants comblés : 15 000 – 18 000 CHF")
c.font = Font(italic=True, color="666666", size=10, name="Calibri")
c.alignment = align("left", "center")
c.fill = fill("FFFDE7")

# ── Freeze panes ──────────────────────────────────────────────────────────────
ws.freeze_panes = "A5"

# ── Tab color ─────────────────────────────────────────────────────────────────
ws.sheet_properties.tabColor = C_GOLD

out = "/home/user/danceyourfoot/Budget_DanceYourFoot_2027.xlsx"
wb.save(out)
print(f"Fichier créé : {out}")
