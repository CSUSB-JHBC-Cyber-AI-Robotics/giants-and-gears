/* Giants & Gears — reveal-on-scroll only (codex edition: no animated
   backgrounds; the paper is still). */
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
})();
