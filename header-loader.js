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
      // Always inject header at very top so it stacks above all content
      document.body.prepend(newHeader);
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