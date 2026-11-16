/* Mosaico vivo: grade de pixels nas cores da marca, que ondula como dados chegando.
   Pausa fora da tela e com a aba oculta; estático com movimento reduzido. */
(function () {
  const CORES = ['#4FD1D4', '#5CC98A', '#4FB3E8', '#C9E36A', '#FFD25E', '#D3A574', '#1FA5A8', '#2E9B57'];
  function montar(canvas) {
    const ctx = canvas.getContext('2d');
    const reduzido = matchMedia('(prefers-reduced-motion: reduce)').matches;
    let w = 0, h = 0, dpr = 1, celulas = [], raf = 0, ativo = true, t0 = performance.now();
    const mouse = { x: -9999, y: -9999 };
    const passo = () => (innerWidth < 700 ? 18 : 22);
    function semente(i) { const x = Math.sin(i * 12.9898) * 43758.5453; return x - Math.floor(x); }
    function medir() {
      dpr = Math.min(devicePixelRatio || 1, 1.75);
      const r = canvas.getBoundingClientRect();
      w = r.width; h = r.height;
      canvas.width = w * dpr; canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const p = passo(), cols = Math.ceil(w / p) + 1, rows = Math.ceil(h / p) + 1;
      celulas = [];
      for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) {
        const i = y * cols + x, s = semente(i + 1);
        celulas.push({ x: x * p, y: y * p, s, cor: CORES[Math.floor(semente(i + 7) * CORES.length)], fase: s * Math.PI * 2 });
      }
      desenhar(performance.now());
    }
    function desenhar(agora) {
      const t = (agora - t0) / 1000, p = passo(), tam = p - 5;
      ctx.clearRect(0, 0, w, h);
      for (const c of celulas) {
        const fx = c.x / w;
        // presença: mais densa à direita, onda diagonal passando
        const base = Math.max(0, fx - 0.28) * 1.35;
        const onda = Math.sin(c.x * 0.012 + c.y * 0.018 - t * 1.1 + c.fase * 0.35) * 0.5 + 0.5;
        const dx = c.x - mouse.x, dy = c.y - mouse.y, perto = Math.max(0, 1 - Math.sqrt(dx * dx + dy * dy) / 160);
        let a = base * (0.25 + onda * 0.75) * (c.s > 0.42 ? 1 : 0.12) + perto * 0.55;
        if (a < 0.04) continue;
        a = Math.min(a, 0.92);
        ctx.globalAlpha = a;
        ctx.fillStyle = c.cor;
        const enc = (1 - a) * 3;
        ctx.beginPath();
        ctx.roundRect ? ctx.roundRect(c.x + enc, c.y + enc, tam - enc * 2, tam - enc * 2, 2.5) : ctx.rect(c.x + enc, c.y + enc, tam - enc * 2, tam - enc * 2);
        ctx.fill();
      }
      ctx.globalAlpha = 1;
    }
    function loop(agora) { if (!ativo) return; desenhar(agora); raf = requestAnimationFrame(loop); }
    const io = new IntersectionObserver(([e]) => { ativo = e.isIntersecting && !document.hidden; cancelAnimationFrame(raf); if (ativo && !reduzido) raf = requestAnimationFrame(loop); });
    function visib() { ativo = !document.hidden; cancelAnimationFrame(raf); if (ativo && !reduzido) raf = requestAnimationFrame(loop); }
    function mover(e) { const r = canvas.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; if (reduzido) desenhar(performance.now()); }
    function sair() { mouse.x = mouse.y = -9999; }
    medir();
    addEventListener('resize', medir);
    document.addEventListener('visibilitychange', visib);
    canvas.parentElement.addEventListener('pointermove', mover);
    canvas.parentElement.addEventListener('pointerleave', sair);
    io.observe(canvas);
    return function desmontar() {
      cancelAnimationFrame(raf); io.disconnect();
      removeEventListener('resize', medir);
      document.removeEventListener('visibilitychange', visib);
      canvas.parentElement.removeEventListener('pointermove', mover);
      canvas.parentElement.removeEventListener('pointerleave', sair);
    };
  }
  document.querySelectorAll('canvas[data-mosaico]').forEach(montar);

  // revelar ao rolar
  const els = document.querySelectorAll('.revela');
  if ('IntersectionObserver' in window) {
    const ob = new IntersectionObserver((ents) => ents.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('visivel'); ob.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    els.forEach((el) => ob.observe(el));
  } else els.forEach((el) => el.classList.add('visivel'));
})();
