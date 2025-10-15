document.addEventListener('DOMContentLoaded',async function(){
  try {
    const resp = await fetch('components/header.html', { cache: 'no-store' });
    if (!resp.ok) return;
    const html = await resp.text();

    const temp = document.createElement('div');
    temp.innerHTML = html.trim();
    const newHeader = temp.firstElementChild;
    const existingHeader = document.querySelector('.header-wrapper-absolute');

    if (existingHeader && newHeader) {
      existingHeader.replaceWith(newHeader);
    } else if (newHeader) {
      const hero = document.querySelector('.hero-wrapper') || document.body.firstElementChild || document.body;
      hero.prepend(newHeader);
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