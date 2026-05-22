/* global React, DancerSilhouette */

// ============ TEAMS ============
function Teams() {
  const teams = [
    { name: "À venir", disc: "Hip-hop", tag: "École · 01" },
    { name: "À venir", disc: "Afro", tag: "École · 02" },
    { name: "À venir", disc: "Krump", tag: "École · 03" },
    { name: "À venir", disc: "Voguing", tag: "École · 04" },
  ];
  return (
    <section className="section teams" id="teams">
      <div className="container">
        <div className="section-head" data-reveal>
          <div>
            <div className="section-num">06 · Les équipes</div>
            <h2 className="section-title" style={{ marginTop: 16 }}>
              Quatre écoles.<br/>Quatre <em style={{ color: "var(--cream)" }}>battles</em>.
            </h2>
          </div>
          <p style={{ maxWidth: 360, color: "var(--cream-dim)", fontSize: 16 }}>
            Quatre écoles locales, quatre disciplines. Une équipe = six membres, dont un gardien de la vibe.
          </p>
        </div>

        <div className="teams-grid">
          {teams.map((t, i) => (
            <div key={i} className="team-card" data-reveal="scale" style={{ "--reveal-delay": `${i * 0.08}s` }}>
              <div className="tc-bg"></div>
              <DancerSilhouette variant={(i % 3) + 1} className="tc-silhouette"/>
              <div className="tc-overlay"></div>
              <div className="tc-placeholder-mark">À venir</div>
              <div className="tc-content">
                <div className="tc-tag">{t.tag}</div>
                <div className="tc-name">{t.name}</div>
                <div className="tc-discipline">{t.disc}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// ============ DJ ============
function DJ() {
  const styles = ["Hip-hop", "Afro", "Électro", "Kuduro", "Baile funk", "Dancehall"];
  const bars = Array.from({ length: 24 });
  return (
    <section className="section dj" id="dj">
      <div className="container">
        <div className="dj-grid">
          <div data-reveal="slide-left">
            <div className="section-num">07 · Le DJ</div>
            <h2 className="dj-title" style={{ marginTop: 16 }}>
              Le DJ<br/>impose <span className="em">le tempo.</span>
            </h2>
            <div className="dj-tags">
              {styles.map((s) => <span key={s} className="dj-tag">{s}</span>)}
            </div>
            <p className="dj-meta">
              Le tournoi se joue au rythme qu'il décide. <strong>5 styles min. par match.</strong><br/>
              Les équipes doivent s'adapter en continu, sous peine de sanction.
            </p>
          </div>

          <div className="equalizer" data-reveal="slide-right" aria-hidden="true">
            {bars.map((_, i) => (
              <div
                key={i}
                className="eq-bar"
                style={{
                  animationDelay: `${(i * 0.08) % 1}s`,
                  animationDuration: `${0.6 + (i % 4) * 0.15}s`,
                  height: `${30 + (i % 6) * 12}%`,
                }}
              ></div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

// ============ INFOS ============
function Infos() {
  const [email, setEmail] = React.useState("");
  const [subscribed, setSubscribed] = React.useState(false);
  function submit(e) { e.preventDefault(); if (email) setSubscribed(true); }

  return (
    <section className="section infos" id="infos">
      <div className="container">
        <div className="section-head" data-reveal>
          <div>
            <div className="section-num">08 · Infos pratiques</div>
            <h2 className="section-title" style={{ marginTop: 16 }}>
              Date.<br/>Lieu.<br/><em style={{ color: "var(--cream)" }}>Énergie.</em>
            </h2>
          </div>
          <p style={{ color: "var(--cream-dim)", fontSize: 16, lineHeight: 1.6, alignSelf: "end" }}>
            Édition fondatrice — tout reste à définir <em style={{ color: "var(--gold)", fontStyle: "italic" }}>avec vous</em>.
            Date, lieu, format précis : on construit cette première édition main dans la main avec nos partenaires.
          </p>
        </div>

        <div className="infos-grid">
          <div data-reveal="slide-left">
            <div className="info-block">
              <div className="info-label">Date</div>
              <div className="info-value">
                À définir
                <small>1ʳᵉ édition prévue automne 2027 — contactez-nous pour caler la date.</small>
              </div>
            </div>
            <div className="info-block">
              <div className="info-label">Lieu</div>
              <div className="info-value">
                À définir
                <small>Suisse romande. On cherche un espace urbain à la hauteur de l'événement.</small>
              </div>
            </div>
            <div className="info-block">
              <div className="info-label">Durée</div>
              <div className="info-value">
                1 h 30
                <small>3 matchs de 12 min, danses libres entre chaque round, cypher final.</small>
              </div>
            </div>
            <div className="info-block">
              <div className="info-label">Terrain</div>
              <div className="info-value">
                10 × 20 m
                <small>Moquette personnalisée, entourée de bancs. Public à 2 m du jeu.</small>
              </div>
            </div>
            <div className="info-block">
              <div className="info-label">Format</div>
              <div className="info-value">
                4 écoles · 1 DJ
                <small>Vote du public, cypher final ouvert à tous.</small>
              </div>
            </div>
            <div className="info-block">
              <div className="info-label">Construction</div>
              <div className="info-value">
                Avec vous
                <small>Écoles, sponsors, lieux, DJ : on cherche les partenaires fondateurs.</small>
              </div>
            </div>
          </div>

          <div data-reveal="slide-right" className="infos-cta-stack">
            <a href="#inscription" className="info-cta">
              <div className="info-cta-eyebrow">Première édition · 2027</div>
              <div className="info-cta-title">
                Aidez-nous à construire<br/>le 1<sup>er</sup> tournoi.
              </div>
              <div className="info-cta-arrow">
                Nous contacter <span>→</span>
              </div>
            </a>

            <form className="newsletter" onSubmit={submit}>
              <div className="newsletter-eyebrow">Newsletter</div>
              <div className="newsletter-title">Restez dans la boucle.</div>
              <p className="newsletter-desc">
                Recevez les news : date, lieu, équipes confirmées, billetterie.
              </p>
              {subscribed ? (
                <div className="newsletter-done">✓ Inscrit. On vous tient au courant.</div>
              ) : (
                <div className="newsletter-row">
                  <input
                    type="email"
                    required
                    placeholder="vous@email.ch"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                  <button type="submit">S'inscrire <span>→</span></button>
                </div>
              )}
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}

window.Teams = Teams;
window.DJ = DJ;
window.Infos = Infos;
