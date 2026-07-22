/* Giants & Gears — codex edition (no animated backgrounds; the paper is still).
   Handles reveal-on-scroll and reliable canvas sizing. */
(function () {
  const io = new IntersectionObserver((es) => {
    for (const e of es) if (e.isIntersecting) { e.target.classList.add('lit'); io.unobserve(e.target); }
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
  // safety: if the page loaded hidden/zero-sized (embedded panes), never leave content invisible
  setTimeout(() => {
    if (!document.querySelector('.reveal.lit'))
      document.querySelectorAll('.reveal').forEach((el) => el.classList.add('lit'));
  }, 1600);

  /* Canvas labs size their backing store from clientWidth at construction. If the
     page first lays out at zero/estimated width (embedded panes, slow font/layout),
     that store is wrong and content draws blank or in the corner until the user
     interacts. Every lab already redraws on window 'resize', so watch each canvas
     with a ResizeObserver — its first callback fires only once layout has truly
     settled (correct width), and again on any later change — and turn that into a
     resize event that makes every lab repaint at its real size. rAF-coalesced so
     many canvases don't each trigger a separate pass. */
  if ('ResizeObserver' in window) {
    let pending = false;
    const lastW = new WeakMap();
    const ro = new ResizeObserver((entries) => {
      // react to WIDTH changes only — our own backing-store writes touch height
      // and must never re-trigger the loop
      let changed = false;
      for (const e of entries) {
        const w = Math.round(e.contentRect.width);
        if (lastW.get(e.target) !== w) { lastW.set(e.target, w); changed = true; }
      }
      if (!changed || pending) return;
      pending = true;
      requestAnimationFrame(() => { pending = false; window.dispatchEvent(new Event('resize')); });
    });
    document.querySelectorAll('canvas').forEach((c) => ro.observe(c));
  }
  // belt-and-braces for very old engines
  window.addEventListener('load', () => window.dispatchEvent(new Event('resize')));

  /* Tag wide ink diagrams (anything that isn't an f-*.svg formula) so CSS can
     shrink them into short, horizontally scrollable plate windows. */
  document.querySelectorAll('.formula-artifact img').forEach((img) => {
    const name = (img.getAttribute('src') || '').split('/').pop();
    if (name && !name.startsWith('f-'))
      img.closest('.formula-artifact').classList.add('plate-diagram');
  });
})();
