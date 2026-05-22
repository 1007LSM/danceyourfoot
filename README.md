# Dance Your Foot -- Site Web

Site one-page pour l'evenement Dance Your Foot.
Tournoi fusionnant football, danse et improvisation.

## Lancer le site

Le site necessite un serveur local (les scripts JSX sont charges via fetch) :

```bash
cd site/
npx serve .
```

Puis ouvrir http://localhost:3000

## Structure

- `index.html` -- Point d'entree
- `styles.css` -- Styles globaux (charte graphique officielle)
- `app.jsx` -- Composant principal React
- `components/` -- Composants React (hero, sections, equipes, footer)
- `assets/` -- Logo et visuels
- `tweaks-panel.jsx` -- Panneau de reglages (animations, couleurs)
- `image-slot.js` -- Composant d'upload d'images

## Charte graphique

- Rouge cramoisi : #C41E3A
- Orange vif : #E86A17
- Jaune dore : #F5B731
- Bordeaux : #6B1D3A
- Fond sombre : #1A0A12
