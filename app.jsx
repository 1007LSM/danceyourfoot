/* global React, ReactDOM,
   Nav, Hero, Marquee, Concept, Rules, Format, Vote, Teams, DJ, Infos, Signup, Footer,
   FloatingEmojis, useRevealOnScroll,
   TweaksPanel, TweakSection, TweakRadio, TweakToggle, useTweaks */

const { useEffect: useEffectA } = React;

// Default tweakable knobs — host rewrites this JSON block when user changes values.
const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "motion": "full",
  "accent": "gold"
}/*EDITMODE-END*/;

function App() {
  useRevealOnScroll();
  const [t, setTweak] = useTweaks(TWEAK_DEFAULTS);

  // Apply tweaks
  useEffectA(() => {
    const root = document.documentElement;
    root.classList.toggle("reduce-motion", t.motion === "off");
    // Accent override
    const accents = {
      gold:    { gold: "#F5B731", orange: "#E86A17" },
      orange:  { gold: "#E86A17", orange: "#F5B731" },
      cream:   { gold: "#FFF5E6", orange: "#F5B731" },
    };
    const a = accents[t.accent] || accents.gold;
    root.style.setProperty("--gold", a.gold);
    root.style.setProperty("--orange", a.orange);
  }, [t.motion, t.accent]);

  // Event date: Sept 11, 2027 19:00
  const eventDate = new Date("2027-09-11T19:00:00").getTime();

  return (
    <>
      <Nav/>
      <main>
        <Hero eventDate={eventDate}/>
        <Marquee/>
        <Concept/>
        <Rules/>
        <Format/>
        <Vote/>
        <Teams/>
        <DJ/>
        <Infos/>
        <Signup/>
      </main>
      <Footer/>

      <TweaksPanel title="Tweaks">
        <TweakSection label="Animations"/>
        <TweakRadio
          label="Niveau"
          value={t.motion}
          onChange={(v) => setTweak("motion", v)}
          options={[
            { value: "full", label: "Full" },
            { value: "off",  label: "Calme" },
          ]}
        />
        <TweakSection label="Accent"/>
        <TweakRadio
          label="Couleur"
          value={t.accent}
          onChange={(v) => setTweak("accent", v)}
          options={[
            { value: "gold",   label: "Or" },
            { value: "orange", label: "Orange" },
            { value: "cream",  label: "Crème" },
          ]}
        />
      </TweaksPanel>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App/>);
