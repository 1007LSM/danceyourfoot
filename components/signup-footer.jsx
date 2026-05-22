/* global React, Logo */
const { useState: useStateF } = React;

// ============ SIGNUP ============
function Signup() {
  const [form, setForm] = useStateF({
    school: "", discipline: "", captain: "", contact: "", message: "", kind: "team",
  });
  const [submitted, setSubmitted] = useStateF(false);

  function update(k) {
    return (e) => setForm((f) => ({ ...f, [k]: e.target.value }));
  }
  function submit(e) {
    e.preventDefault();
    setSubmitted(true);
  }

  return (
    <section className="section signup" id="inscription">
      <div className="container">
        <div className="signup-grid">
          <div data-reveal="slide-left">
            <div className="eyebrow">09 · Inscription</div>
            <h2 className="section-title" style={{ marginTop: 16 }}>
              On fait<br/>équipe ?
            </h2>
            <p className="signup-lead" style={{ marginTop: 24 }}>
              Inscris ton école.<br/>Réserve ton crew.<br/>Rejoins le 1<sup>er</sup> tournoi du genre.
            </p>
            <p className="signup-note">
              Dance Your Foot 2027 cherche ses écoles fondatrices. On serait honorés de construire cette première édition avec vous.
            </p>
            <div style={{ marginTop: 32, paddingTop: 32, borderTop: "1px solid rgba(26,10,18,0.2)" }}>
              <div style={{ fontFamily: "var(--font-mono)", fontSize: 11, letterSpacing: "0.3em", textTransform: "uppercase", color: "var(--bordeaux)", marginBottom: 8 }}>
                Contact direct
              </div>
              <div style={{ fontFamily: "var(--font-display)", fontStyle: "italic", fontWeight: 900, fontSize: 28, color: "var(--bordeaux)", textTransform: "uppercase", lineHeight: 1 }}>
                Sylvain Nicolier
              </div>
              <a href="mailto:sylvain@danseyourfoot.com" style={{ display: "block", marginTop: 8, fontFamily: "var(--font-mono)", fontSize: 14, color: "var(--dark)" }}>
                sylvain@danseyourfoot.com
              </a>
              <a href="tel:+41788490089" style={{ display: "block", marginTop: 4, fontFamily: "var(--font-mono)", fontSize: 14, color: "var(--dark)" }}>
                +41 78 849 00 89
              </a>
            </div>
          </div>

          <form className="form-card" data-reveal="slide-right" onSubmit={submit}>
            <div className="form-field">
              <label htmlFor="kind">Je m'inscris en tant que</label>
              <select id="kind" value={form.kind} onChange={update("kind")}>
                <option value="team">École de danse</option>
                <option value="dj">DJ / artiste</option>
                <option value="sponsor">Sponsor / partenaire</option>
                <option value="info">Pour en savoir plus</option>
              </select>
            </div>

            {form.kind === "team" && (
              <div className="form-row">
                <div className="form-field">
                  <label htmlFor="school">Nom de l'école</label>
                  <input id="school" type="text" placeholder="ex. Studio Krump LSN" value={form.school} onChange={update("school")} required/>
                </div>
                <div className="form-field">
                  <label htmlFor="discipline">Discipline principale</label>
                  <input id="discipline" type="text" placeholder="ex. Hip-hop, Voguing…" value={form.discipline} onChange={update("discipline")} required/>
                </div>
              </div>
            )}

            <div className="form-row">
              <div className="form-field">
                <label htmlFor="captain">{form.kind === "team" ? "Nom du capitaine" : "Votre nom"}</label>
                <input id="captain" type="text" placeholder="Prénom Nom" value={form.captain} onChange={update("captain")} required/>
              </div>
              <div className="form-field">
                <label htmlFor="contact">Email ou téléphone</label>
                <input id="contact" type="text" placeholder="vous@email.ch" value={form.contact} onChange={update("contact")} required/>
              </div>
            </div>

            <div className="form-field">
              <label htmlFor="message">Message (optionnel)</label>
              <textarea id="message" placeholder="Parlez-nous de votre projet…" value={form.message} onChange={update("message")}></textarea>
            </div>

            <button type="submit" className="btn btn-primary form-submit">
              Envoyer <span className="arrow">→</span>
            </button>

            {submitted && (
              <div className="form-success">
                ✓ Bien reçu. On revient vers vous sous 48 h.
              </div>
            )}
          </form>
        </div>
      </div>
    </section>
  );
}

// ============ FOOTER ============
function Footer() {
  return (
    <footer className="footer">
      <div className="footer-grid">
        <div className="footer-brand">
          <div className="nav-logo">
            <Logo size={56}/>
            <span>Dance <span className="accent">Your</span> Foot</span>
          </div>
          <p>
            Tournoi inédit qui fusionne football, danse et improvisation.
            Édition fondatrice 2027 — Suisse romande.
          </p>
          <div className="socials">
            <a href="#" aria-label="Instagram">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.5 1 .5.5.8.9 1 1.5.2.4.4 1 .4 2.2.1 1.2.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-1 1.5-.5.5-.9.8-1.5 1-.4.2-1 .4-2.2.4-1.2.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.5-1-.5-.5-.8-.9-1-1.5-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8c.1-1.2.2-1.8.4-2.2.2-.6.5-1 1-1.5.5-.5.9-.8 1.5-1 .4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.1 0-3.5 0-4.7.1-1.1.1-1.7.2-2.1.4-.5.2-.9.4-1.3.8-.4.4-.6.8-.8 1.3-.2.4-.3 1-.4 2.1-.1 1.2-.1 1.6-.1 4.7s0 3.5.1 4.7c.1 1.1.2 1.7.4 2.1.2.5.4.9.8 1.3.4.4.8.6 1.3.8.4.2 1 .3 2.1.4 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1.1-.1 1.7-.2 2.1-.4.5-.2.9-.4 1.3-.8.4-.4.6-.8.8-1.3.2-.4.3-1 .4-2.1.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c-.1-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.3-.4-.4-.8-.6-1.3-.8-.4-.2-1-.3-2.1-.4-1.2-.1-1.6-.1-4.7-.1zm0 3.1a5 5 0 110 10 5 5 0 010-10zm0 1.8a3.2 3.2 0 100 6.4 3.2 3.2 0 000-6.4zm5.2-2a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"/></svg>
            </a>
            <a href="#" aria-label="TikTok">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.6 6.4c-1.5-.1-2.8-.9-3.6-2-.5-.7-.8-1.5-.8-2.4h-3.4v13.8c0 1.4-1.1 2.6-2.5 2.6s-2.5-1.2-2.5-2.6 1.1-2.6 2.5-2.6c.3 0 .6.1.8.2v-3.5c-.3 0-.5-.1-.8-.1-3.3 0-6 2.7-6 6s2.7 6 6 6 6-2.7 6-6V9c1.3 1 2.9 1.5 4.5 1.5V7c-.1 0-.2 0-.2-.6z"/></svg>
            </a>
            <a href="#" aria-label="YouTube">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2c-.2-.9-.9-1.5-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4c-.9.2-1.5.9-1.8 1.8C2 8.8 2 12 2 12s0 3.2.4 4.8c.2.9.9 1.5 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4c.9-.2 1.5-.9 1.8-1.8.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3-5.2 3z"/></svg>
            </a>
            <a href="#" aria-label="Spotify">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm4.6 14.4c-.2.3-.5.4-.9.2-2.4-1.5-5.5-1.8-9.1-1-.4.1-.7-.2-.8-.5-.1-.4.2-.7.5-.8 4-.9 7.4-.5 10.1 1.1.3.2.4.6.2 1zm1.2-2.7c-.2.4-.7.5-1.1.3-2.8-1.7-7-2.2-10.3-1.2-.4.1-.9-.1-1-.5-.1-.4.1-.9.5-1 3.7-1.1 8.4-.6 11.6 1.4.4.2.5.7.3 1zm.1-2.8c-3.3-2-8.8-2.2-12-1.2-.5.2-1-.1-1.2-.6-.2-.5.1-1 .6-1.2 3.7-1.1 9.7-.9 13.5 1.4.5.3.6.9.3 1.4-.3.4-.9.5-1.2.2z"/></svg>
            </a>
          </div>
        </div>

        <div className="foot-col">
          <h4>Naviguer</h4>
          <ul>
            <li><a href="#concept">Concept</a></li>
            <li><a href="#format">Format</a></li>
            <li><a href="#vote">Vote</a></li>
            <li><a href="#teams">Équipes</a></li>
            <li><a href="#dj">DJ</a></li>
            <li><a href="#infos">Infos pratiques</a></li>
          </ul>
        </div>

        <div className="foot-col">
          <h4>Contact</h4>
          <ul>
            <li>Sylvain Nicolier</li>
            <li><a href="mailto:sylvain@danseyourfoot.com">sylvain@danseyourfoot.com</a></li>
            <li><a href="tel:+41788490089">+41 78 849 00 89</a></li>
            <li>Suisse romande</li>
          </ul>
        </div>

        <div className="foot-col">
          <h4>Partenaires</h4>
          <ul>
            <li><a href="#inscription">Devenir sponsor</a></li>
            <li>Crew · 2 500 CHF</li>
            <li>Captain · 6 000 CHF</li>
            <li>MVP · 12 000 CHF</li>
          </ul>
        </div>
      </div>

      <div className="footer-mega" aria-hidden="true">
        Bouge · Tire · Improvise ·
      </div>

      <div className="footer-base">
        <span>© 2027 Dance Your Foot · Édition fondatrice</span>
        <span>danceyourfoot.com</span>
      </div>
    </footer>
  );
}

window.Signup = Signup;
window.Footer = Footer;
