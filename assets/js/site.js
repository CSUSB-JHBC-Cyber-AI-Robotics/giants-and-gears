/* Giants & Gears — codex edition (no animated backgrounds; the paper is still).
   Handles reveal-on-scroll and a one-time canvas relayout. */
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
     that store stays wrong and content draws blank or in the corner until the user
     interacts. Every lab already redraws on window 'resize', so re-fire it once
     things have settled — this makes all labs paint at their true width from the
     start. */
  const relayout = () => window.dispatchEvent(new Event('resize'));
  requestAnimationFrame(() => requestAnimationFrame(relayout));
  window.addEventListener('load', relayout);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(relayout);
})();
