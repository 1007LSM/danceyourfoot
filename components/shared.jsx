/* global React */
const { useState, useEffect, useRef } = React;

// ============ LOGO ============
function Logo({ size = 40, rounded = true }) {
  return (
    <img
      src="assets/logo.jpg"
      alt="Dance Your Foot"
      width={size}
      height={size}
      style={{
        width: size,
        height: size,
        display: "block",
        borderRadius: rounded ? "14%" : 0,
        objectFit: "cover",
      }}
    />
  );
}

// ============ Dancing silhouette (for hero bg) ============
function DancerSilhouette({ className = "", variant = 1 }) {
  if (variant === 1) {
    return (
      <svg className={`silhouette ${className}`} viewBox="0 0 200 400" preserveAspectRatio="xMidYMax meet">
        <g>
          <circle cx="100" cy="40" r="22"/>
          <path d="M82 64 L 122 64 L 130 84 C 138 92 150 96 162 90 L 168 110 C 152 124 132 124 120 116 L 124 188 L 76 188 L 80 116 C 68 124 48 124 32 110 L 38 90 C 50 96 62 92 70 84 Z"/>
          <path d="M76 188 L 124 188 L 132 240 L 68 240 Z"/>
          <path d="M68 240 L 100 240 L 90 320 L 60 348 L 56 360 L 80 360 L 96 340 L 110 280 Z"/>
          <path d="M100 240 L 132 240 L 144 340 L 152 360 L 128 360 L 120 340 L 110 280 Z"/>
        </g>
      </svg>
    );
  }
  if (variant === 2) {
    return (
      <svg className={`silhouette ${className}`} viewBox="0 0 200 400" preserveAspectRatio="xMidYMax meet">
        <g>
          <circle cx="110" cy="50" r="20"/>
          {/* arms up */}
          <path d="M90 70 L 130 70 L 140 90 C 148 70 158 50 168 40 L 180 50 C 168 70 152 100 142 116 L 138 180 L 82 180 L 78 116 C 68 100 52 70 40 50 L 52 40 C 62 50 72 70 80 90 Z"/>
          <path d="M82 180 L 138 180 L 144 232 L 76 232 Z"/>
          {/* dancing legs */}
          <path d="M76 232 L 108 232 L 88 320 L 52 360 L 80 360 L 100 332 L 116 270 Z"/>
          <path d="M108 232 L 144 232 L 152 320 L 168 360 L 144 360 L 132 332 L 116 270 Z"/>
        </g>
      </svg>
    );
  }
  return (
    <svg className={`silhouette ${className}`} viewBox="0 0 200 400" preserveAspectRatio="xMidYMax meet">
      <g>
        <circle cx="100" cy="46" r="20"/>
        <path d="M82 70 L 120 66 L 132 84 C 150 96 168 90 178 76 L 182 92 C 168 112 144 116 128 108 L 128 184 L 78 184 L 82 108 C 68 112 50 108 38 92 L 42 76 C 52 90 70 96 86 84 Z"/>
        <path d="M78 184 L 128 184 L 132 232 L 72 232 Z"/>
        <path d="M72 232 L 102 232 L 96 320 L 70 356 L 92 356 L 108 332 L 116 280 Z"/>
        <path d="M102 232 L 132 232 L 148 320 L 158 356 L 134 356 L 126 332 L 116 280 Z"/>
      </g>
    </svg>
  );
}

// ============ Floating emojis ============
function FloatingEmojis({ enabled = true }) {
  if (!enabled) return null;
  const items = [
    { e: "⚽", x: 8,  d: 0,    dur: 22 },
    { e: "🕺", x: 22, d: 4,    dur: 18 },
    { e: "💃", x: 78, d: 8,    dur: 20 },
    { e: "🎵", x: 92, d: 2,    dur: 24 },
    { e: "🔥", x: 50, d: 12,   dur: 19 },
    { e: "⚽", x: 65, d: 16,   dur: 21 },
  ];
  return (
    <div style={{ position: "fixed", inset: 0, zIndex: 4, pointerEvents: "none", overflow: "hidden" }}>
      {items.map((it, i) => (
        <span
          key={i}
          className="floater"
          style={{ left: `${it.x}%`, animationDelay: `${it.d}s`, animationDuration: `${it.dur}s` }}
        >
          {it.e}
        </span>
      ))}
    </div>
  );
}

// ============ Reveal helper ============
function useRevealOnScroll() {
  useEffect(() => {
    const els = document.querySelectorAll("[data-reveal]");
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -60px 0px" }
    );
    els.forEach((el) => io.observe(el));
    return () => io.disconnect();
  }, []);
}

// ============ Countdown ============
function Countdown({ target }) {
  const [t, setT] = useState(() => calc(target));
  useEffect(() => {
    const id = setInterval(() => setT(calc(target)), 1000);
    return () => clearInterval(id);
  }, [target]);
  function calc(target) {
    const diff = Math.max(0, target - Date.now());
    const days = Math.floor(diff / 86400000);
    const hours = Math.floor((diff % 86400000) / 3600000);
    const mins = Math.floor((diff % 3600000) / 60000);
    const secs = Math.floor((diff % 60000) / 1000);
    return { days, hours, mins, secs };
  }
  const pad = (n) => String(n).padStart(2, "0");
  return (
    <div className="countdown" role="timer" aria-label="Compte à rebours">
      <div className="countdown-label">
        <span>· Coup d'envoi</span>
        <span style={{ display: "inline-flex", alignItems: "center", gap: 8 }}>
          <span className="pulse"></span> LIVE
        </span>
      </div>
      <div className="cd-cell"><div className="cd-num">{pad(t.days)}</div><div className="cd-unit">Jours</div></div>
      <div className="cd-cell"><div className="cd-num">{pad(t.hours)}</div><div className="cd-unit">Heures</div></div>
      <div className="cd-cell"><div className="cd-num">{pad(t.mins)}</div><div className="cd-unit">Min</div></div>
      <div className="cd-cell"><div className="cd-num">{pad(t.secs)}</div><div className="cd-unit">Sec</div></div>
    </div>
  );
}

// ============ Nav ============
function Nav() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 60);
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);
  const close = () => setMenuOpen(false);
  return (
    <nav className={`nav ${scrolled ? "scrolled" : ""}`}>
      <a href="#top" className="nav-logo" onClick={close}>
        <Logo size={40}/>
        <span>Dance <span className="accent">Your</span> Foot</span>
      </a>
      <div className="nav-links">
        <a href="#concept">Concept</a>
        <a href="#format">Format</a>
        <a href="#vote">Vote</a>
        <a href="#teams">Équipes</a>
        <a href="#dj">DJ</a>
        <a href="#infos">Infos</a>
        <a href="#inscription" className="btn btn-primary" style={{ padding: "10px 18px", fontSize: 14 }}>
          Inscription <span className="arrow">→</span>
        </a>
      </div>
      <button
        className={`nav-hamburger${menuOpen ? " open" : ""}`}
        aria-label={menuOpen ? "Fermer le menu" : "Ouvrir le menu"}
        onClick={() => setMenuOpen((o) => !o)}
      >
        <span></span><span></span><span></span>
      </button>
      {menuOpen && (
        <div className="nav-mobile-menu">
          <a href="#concept" onClick={close}>Concept</a>
          <a href="#format" onClick={close}>Format</a>
          <a href="#vote" onClick={close}>Vote</a>
          <a href="#teams" onClick={close}>Équipes</a>
          <a href="#dj" onClick={close}>DJ</a>
          <a href="#infos" onClick={close}>Infos</a>
          <a href="#inscription" className="btn btn-primary nav-mobile-cta" onClick={close}>
            Inscription <span className="arrow">→</span>
          </a>
        </div>
      )}
    </nav>
  );
}

// ============ Marquee ============
function Marquee() {
  const item = (
    <span>
      Bouge <span className="ball"/> Tire <span className="ball"/> Improvise
      <span className="ball"/> Libère ton rythme <span className="ball"/>
      4 écoles <span className="ball"/> 1 terrain <span className="ball"/> 1 DJ <span className="ball"/>
      le public décide <span className="ball"/>
    </span>
  );
  return (
    <div className="marquee" aria-hidden="true">
      <div className="marquee-track">
        {item}{item}{item}
      </div>
    </div>
  );
}

// expose
Object.assign(window, { Logo, DancerSilhouette, FloatingEmojis, useRevealOnScroll, Countdown, Nav, Marquee });
