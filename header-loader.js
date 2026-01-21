document.addEventListener('DOMContentLoaded',async function(){
  try {
    const resp = await fetch('components/header.html', { cache: 'no-store' });
    if (!resp.ok) return;
    const html = await resp.text();

    const temp = document.createElement('div');
    temp.innerHTML = html.trim();
    const newHeader = temp.firstElementChild;
    // Detect an existing header on pages exported from Webflow (different structures)
    const existingHeaderCandidate =
      document.querySelector('.header-wrapper-absolute') ||
      document.querySelector('.header.w-nav') ||
      document.querySelector('.w-nav[role="banner"]') ||
      document.querySelector('[role="banner"].w-nav');

    if (existingHeaderCandidate && newHeader) {
      const nodeToReplace = existingHeaderCandidate.closest('.header-wrapper-absolute') || existingHeaderCandidate;
      nodeToReplace.replaceWith(newHeader);
    } else if (newHeader) {
      // Prefer injecting inside the hero so the logo sits within the blue banner
      const heroContainer =
        document.querySelector('.hero-wrapper') ||
        document.querySelector('.section.hero-v1') ||
        document.querySelector('.hero-v1') ||
        null;

      if (heroContainer) {
        heroContainer.prepend(newHeader);
      } else {
        document.body.prepend(newHeader);
      }
    }

    // Re-initialize Webflow interactions so button animations work
    if (window.Webflow) {
      try {
        var ix = window.Webflow.require && window.Webflow.require('ix2');
        if (ix && ix.init) {
          ix.init();
        }
        if (window.Webflow.ready) {
          window.Webflow.ready();
        }
        if (window.Webflow.require) {
          var navbar = window.Webflow.require('navbar');
          if (navbar && navbar.ready) navbar.ready();
        }
      } catch (err) {
        console.warn('Webflow re-init failed', err);
      }
    }
  } catch (e) {
    console.warn('Header loader failed', e);
  }
});