/* global React, Logo, DancerSilhouette, Countdown */

function Hero({ eventDate }) {
  return (
    <section className="hero" id="top">
      <div className="hero-bg" aria-hidden="true">
        <div className="quad q1"></div>
        <div className="quad q2"></div>
        <div className="quad q3"></div>
        <div className="grain"></div>
      </div>

      <div className="hero-silhouettes" aria-hidden="true">
        <DancerSilhouette className="s1" variant={1}/>
        <DancerSilhouette className="s2" variant={2}/>
        <DancerSilhouette className="s3" variant={3}/>
      </div>

      <div className="hero-content">
        <div>
          <div className="eyebrow" style={{ marginBottom: 24 }}>
            Édition 2027 · 1ʳᵉ édition
          </div>
          <h1 className="hero-title fallback-visible">
            <span className="word w1"><span className="word-inner">Dance</span></span>
            <span className="word w2"><span className="word-inner">Your</span></span>
            <span className="word w3"><span className="word-inner">Foot</span></span>
          </h1>
          <div className="hero-tagline">
            Bouge <span className="sep">·</span> Tire <span className="sep">·</span> Improvise
          </div>
          <p className="hero-sub">
            4 écoles de danse, 1 terrain de foot, 1 DJ.
            Chaque but devient une fête, chaque match un battle, et c'est <strong style={{ color: "var(--gold)" }}>le public</strong> qui tranche.
          </p>
          <div className="hero-cta">
            <a href="#inscription" className="btn btn-primary">
              Participer <span className="arrow">→</span>
            </a>
            <a href="#concept" className="btn btn-ghost">
              Découvrir
            </a>
          </div>
        </div>

        <div className="hero-side">
          <div className="hero-logo">
            <Logo size={260}/>
          </div>
          <Countdown target={eventDate}/>
        </div>
      </div>

      <div className="scroll-cue" aria-hidden="true">
        <span>Scroll</span>
        <span className="line"></span>
      </div>
    </section>
  );
}

window.Hero = Hero;
