/* global React */
const { useEffect: useEffectS } = React;

// ============ CONCEPT (4 piliers) ============
function Concept() {
  const pillars = [
    { n: "01", title: "Foot", icon: "⚽", desc: "Vrai terrain, vrais buts, vraies règles. On joue pour de bon — arbitré sérieusement.", gold: false },
    { n: "02", title: "Danse", icon: "💃", desc: "Chaque équipe est une école : hip-hop, afro, krump, voguing… Une discipline, un style.", gold: true },
    { n: "03", title: "Impro", icon: "🎵", desc: "Le DJ change de style toutes les 1 à 2 minutes. Adapte-toi ou perds le rythme.", gold: false },
    { n: "04", title: "Public", icon: "🔥", desc: "Pas de juges. Le public vote, le public tranche, le public fait l'événement.", gold: true },
  ];
  return (
    <section className="section concept" id="concept">
      <div className="container">
        <div className="section-head" data-reveal>
          <div>
            <div className="section-num">02 · Le concept</div>
            <h2 className="section-title" style={{ marginTop: 16 }}>
              4 écoles.<br/>1 terrain.<br/>1 DJ. <em style={{ color: "var(--cream)" }}>Le public décide.</em>
            </h2>
          </div>
          <p style={{ maxWidth: 360, color: "var(--cream-dim)", fontSize: 16, marginTop: 8 }}>
            Dance Your Foot fusionne le football, la danse et l'improvisation en un seul tournoi spectaculaire.
            Chaque but est une fête. Chaque match, un battle.
          </p>
        </div>

        <div className="concept-grid">
          {pillars.map((p, i) => (
            <div key={p.n} className={`pillar ${p.gold ? "gold" : ""}`} data-reveal="scale" style={{ "--reveal-delay": `${i * 0.08}s` }}>
              <div>
                <div className="pillar-num">{p.n}</div>
                <div className="pillar-title">{p.title}</div>
                <p className="pillar-desc">{p.desc}</p>
              </div>
              <div className="pillar-icon">{p.icon}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// ============ RÈGLES ============
function Rules() {
  const rules = [
    { n: "01", text: "Toujours danser et jouer le ballon", detail: "Le corps reste en rythme, même balle au pied." },
    { n: "02", text: "Interdit de courir", detail: "On glisse, on tourne, on roule — jamais on ne sprinte." },
    { n: "03", text: "S'adapter à la musique", detail: "Le DJ change de style toutes les 1 à 2 min. Suis ou sanctionne." },
    { n: "04", text: "Respecter les règles du football", detail: "Touches, sorties, fautes. Un vrai match, arbitré sérieusement." },
    { n: "05", text: "Célébrer en équipe après chaque but", detail: "5 morceaux par équipe : chaque but devient chorégraphie." },
  ];
  return (
    <section className="section rules">
      <div className="container">
        <div data-reveal>
          <div className="section-num" style={{ color: "var(--gold)", opacity: 1 }}>03 · Les règles</div>
          <h2 className="section-title" style={{ marginTop: 16 }}>
            Cinq règles.<br/><em style={{ color: "var(--cream)" }}>Zéro exception.</em>
          </h2>
          <p style={{ maxWidth: 540, marginTop: 24, color: "var(--cream-dim)", fontSize: 16 }}>
            Le tournoi tient en cinq commandements. On les rappelle au public, à voix haute, avant chaque match.
          </p>
        </div>

        <div className="rule-list">
          {rules.map((r, i) => (
            <div key={r.n} className="rule" data-reveal="slide-left" style={{ "--reveal-delay": `${i * 0.08}s` }}>
              <div className="rule-num">{r.n}</div>
              <div className="rule-text">{r.text}</div>
              <div className="rule-detail">{r.detail}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// ============ FORMAT ============
function Format() {
  const stats = [
    { num: "4",   suffix: "",  label: "Écoles de danse" },
    { num: "3",   suffix: "",  label: "Matchs (2 qualifs + finale)" },
    { num: "1",   suffix: "h35", label: "Show complet, pauses incluses" },
    { num: "200", suffix: "m²",label: "Terrain en moquette" },
  ];
  const compo = [
    { count: "4×", name: "Danseurs de champ", role: "Cœur de l'équipe" },
    { count: "1×", name: "Gardien de la vibe", role: "Gardien de but" },
    { count: "1×", name: "Coach remplaçant", role: "Entre si blessure" },
  ];
  const orga = [
    { name: "DJ",       role: "Impose le tempo" },
    { name: "Arbitre",  role: "Cartons & sifflet" },
    { name: "Speaker",  role: "Mène le public" },
  ];
  return (
    <section className="section format" id="format">
      <div className="container">
        <div className="section-head" data-reveal>
          <div>
            <div className="section-num">04 · Le format</div>
            <h2 className="section-title" style={{ marginTop: 16 }}>
              L'événement<br/>en chiffres.
            </h2>
          </div>
        </div>

        <div className="format-stats">
          {stats.map((s, i) => (
            <div key={i} data-reveal="scale" style={{ "--reveal-delay": `${i * 0.1}s` }}>
              <div className="stat-num">{s.num}<span className="suffix">{s.suffix}</span></div>
              <div className="stat-label">{s.label}</div>
            </div>
          ))}
        </div>

        <div data-reveal>
          <div className="eyebrow" style={{ marginBottom: 16 }}>12 minutes par match</div>
          <h3 style={{
            fontFamily: "var(--font-display)", fontStyle: "italic", fontWeight: 900,
            textTransform: "uppercase", fontSize: "clamp(36px, 5vw, 64px)", lineHeight: 0.9,
            color: "var(--cream)", marginBottom: 16
          }}>
            Une partie, trois temps.
          </h3>
        </div>

        <div className="timeline" data-reveal>
          <div className="timeline-bar">
            <div className="timeline-seg s-tirs">2' · SOLO + TIR</div>
            <div className="timeline-seg s-jeu">10' · JEU</div>
            <div className="timeline-seg s-cel">4' · CÉLÉBRATIONS</div>
          </div>
          <div className="timeline-labels">
            <div className="tl-label">
              <div className="tl-time">2'</div>
              <div className="tl-name">Solo capitaine + tir au but</div>
              <div className="tl-desc">Chaque capitaine ouvre par une danse solo qui se termine sur un tir au but. Le score s'ouvre en rythme.</div>
            </div>
            <div className="tl-label">
              <div className="tl-time">10'</div>
              <div className="tl-name">Phase de jeu</div>
              <div className="tl-desc">Le DJ change de style toutes les 1 à 2 min. Les équipes s'adaptent en continu.</div>
            </div>
            <div className="tl-label">
              <div className="tl-time">4'</div>
              <div className="tl-name">Célébrations</div>
              <div className="tl-desc">À chaque but, jusqu'à 1 min de chorégraphie collective sur la musique de l'équipe.</div>
            </div>
          </div>
        </div>

        <div data-reveal style={{ marginTop: 80 }}>
          <div className="eyebrow" style={{ marginBottom: 16 }}>Déroulé complet · 1 h 35</div>
          <h3 style={{
            fontFamily: "var(--font-display)", fontStyle: "italic", fontWeight: 900,
            textTransform: "uppercase", fontSize: "clamp(32px, 4.5vw, 56px)", lineHeight: 0.95,
            color: "var(--cream)", marginBottom: 24, paddingRight: "0.15em"
          }}>
            Trois matchs.<br/>Trois votes. Un cypher final.
          </h3>
        </div>

        <div className="show-timeline" data-reveal>
          <div className="show-bar">
            <div className="show-seg s-match" title="Qualif 1">QUALIF 1 · 16'</div>
            <div className="show-seg s-vote" title="Vote">VOTE · 1'</div>
            <div className="show-seg s-pause" title="Interlude musicale">INTERLUDE · 5'</div>
            <div className="show-seg s-vote" title="Résultat">RÉSULTAT · 1'</div>
            <div className="show-seg s-match" title="Qualif 2">QUALIF 2 · 16'</div>
            <div className="show-seg s-vote" title="Vote">VOTE · 1'</div>
            <div className="show-seg s-pause" title="Interlude musicale">INTERLUDE · 5'</div>
            <div className="show-seg s-vote" title="Résultat">RÉSULTAT · 1'</div>
            <div className="show-seg s-final" title="Finale">FINALE · 16'</div>
            <div className="show-seg s-vote" title="Vote">VOTE · 1'</div>
            <div className="show-seg s-cypher" title="Cypher">CYPHER · 30'</div>
            <div className="show-seg s-vote" title="Résultat final">RÉSULTAT · 1'</div>
          </div>
          <div className="show-legend">
            <div className="show-step">
              <span className="show-step-num">01</span>
              <div>
                <div className="show-step-name">Qualif 1 — 16'</div>
                <div className="show-step-desc">Solo + tir des capitaines, jeu, célébrations.</div>
              </div>
            </div>
            <div className="show-step">
              <span className="show-step-num">02</span>
              <div>
                <div className="show-step-name">Vote 1' · Interlude 5' · Résultat 1'</div>
                <div className="show-step-desc">Le public lève son carton, le DJ enchaîne, le speaker annonce.</div>
              </div>
            </div>
            <div className="show-step">
              <span className="show-step-num">03</span>
              <div>
                <div className="show-step-name">Qualif 2 — 16'</div>
                <div className="show-step-desc">Deuxième duel pour désigner le second finaliste.</div>
              </div>
            </div>
            <div className="show-step">
              <span className="show-step-num">04</span>
              <div>
                <div className="show-step-name">Vote 1' · Interlude 5' · Résultat 1'</div>
                <div className="show-step-desc">Même rituel : carton, son, annonce du finaliste.</div>
              </div>
            </div>
            <div className="show-step">
              <span className="show-step-num">05</span>
              <div>
                <div className="show-step-name">Finale — 16'</div>
                <div className="show-step-desc">Les deux gagnants s'affrontent pour le titre.</div>
              </div>
            </div>
            <div className="show-step">
              <span className="show-step-num">06</span>
              <div>
                <div className="show-step-name">Vote 1' · Cypher 30' · Résultat final 1'</div>
                <div className="show-step-desc">Public et équipes mélangés sur le terrain. Remise des prix à la fin.</div>
              </div>
            </div>
          </div>
        </div>

        <div className="team-compo">
          <div data-reveal="slide-left">
            <div className="compo-title">Une équipe · 6 membres</div>
            {compo.map((c, i) => (
              <div key={i} className="compo-row">
                <div className="compo-count">{c.count}</div>
                <div className="compo-name">{c.name}</div>
                <div className="compo-role">{c.role}</div>
              </div>
            ))}
          </div>
          <div data-reveal="slide-right">
            <div className="compo-title">L'organisation · 6 rôles</div>
            {orga.map((c, i) => (
              <div key={i} className="compo-row">
                <div className="compo-count">·</div>
                <div className="compo-name">{c.name}</div>
                <div className="compo-role">{c.role}</div>
              </div>
            ))}
            <div className="compo-row">
              <div className="compo-count">·</div>
              <div className="compo-name">Coordo, Photo, Vidéo</div>
              <div className="compo-role">Captation & temps</div>
            </div>
          </div>
        </div>

        <div className="cards-row" data-reveal>
          <div className="ref-card pink">
            <div>
              <div className="ref-tag">Sanction · 01</div>
              <div className="ref-title">Carton<br/>rose</div>
              <p className="ref-desc">Arrêt de danse ou participation insuffisante au jeu.</p>
            </div>
            <div className="ref-icon" style={{ background: "#FFB8CC" }}></div>
          </div>
          <div className="ref-card violet">
            <div>
              <div className="ref-tag">Sanction · 02</div>
              <div className="ref-title">Carton<br/>violet</div>
              <p className="ref-desc">Expulsion immédiate du terrain pour le reste du match.</p>
            </div>
            <div className="ref-icon" style={{ background: "#B89FC9" }}></div>
          </div>
        </div>
      </div>
    </section>
  );
}

// ============ VOTE ============
function Vote() {
  const criteria = [
    { n: "01", name: "Créativité",          w: 92, meta: "Style · Originalité" },
    { n: "02", name: "Qualité de la danse", w: 86, meta: "Technique · Engagement" },
    { n: "03", name: "Respect des rythmes", w: 78, meta: "Tempo · Adaptation" },
    { n: "04", name: "Jeu footballistique", w: 70, meta: "Passes · Tirs · Gardien" },
    { n: "05", name: "Célébrations",        w: 95, meta: "Chorés · Énergie" },
  ];
  return (
    <section className="section vote" id="vote">
      <div className="container">
        <div data-reveal>
          <div className="eyebrow" style={{ color: "var(--cream)" }}>05 · Vote du public</div>
          <h2 className="section-title" style={{ marginTop: 16 }}>
            C'est <em style={{ color: "var(--cream)" }}>vous</em><br/>qui décidez.
          </h2>
          <p className="vote-lead">
            Pas de jury. Pas de juges experts. Le public lève un <em>carton coloré</em> en fin de match.
          </p>
        </div>

        <div className="criteria">
          {criteria.map((c, i) => (
            <div key={c.n} className="criterion" data-reveal="scale" style={{ "--reveal-delay": `${i * 0.08}s` }}>
              <div className="crit-num">{c.n}</div>
              <div className="crit-name">{c.name}</div>
              <div className="crit-bar" style={{ "--w": `${c.w}%`, "--d": `${0.3 + i * 0.1}s` }}></div>
              <div className="crit-meta">{c.meta}</div>
            </div>
          ))}
        </div>

        <div className="vote-card-demo" data-reveal>
          <div className="card-visual" aria-hidden="true"></div>
          <p>
            <strong>Carton bicolore</strong> distribué à l'entrée. Un vote par spectateur, en fin de match.
            En cas d'égalité, <strong>trois spectateurs tirés au sort</strong> tranchent.
          </p>
        </div>
      </div>
    </section>
  );
}

window.Concept = Concept;
window.Rules = Rules;
window.Format = Format;
window.Vote = Vote;
