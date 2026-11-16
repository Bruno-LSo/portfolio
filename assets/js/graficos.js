/* Gráficos leves em SVG, nas cores do portfólio. Sem dependências. */
window.G = (function () {
  const NS = 'http://www.w3.org/2000/svg';
  const fmt = (v, casas = 0, suf = '') => new Intl.NumberFormat('pt-BR', { minimumFractionDigits: casas, maximumFractionDigits: casas }).format(v) + suf;
  function el(nome, attrs = {}, pai) {
    const e = document.createElementNS(NS, nome);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (pai) pai.appendChild(e);
    return e;
  }
  function texto(pai, x, y, t, attrs = {}) { const e = el('text', Object.assign({ x, y, fill: '#A9B8C6', 'font-size': 12, 'font-family': 'Sora, sans-serif' }, attrs), pai); e.textContent = t; return e; }

  /* barras horizontais: itens [{rotulo, valor, destaque, cor}] */
  function barrasH(alvo, itens, op = {}) {
    const larg = op.largura || 640, alt = op.altura || 34, gap = op.gap || 10, esq = op.esquerda || 150, dir = op.direita || 64;
    const H = itens.length * (alt + gap) + 8;
    const max = op.max || Math.max(...itens.map((i) => i.valor));
    const min = op.min || 0;
    alvo.innerHTML = '';
    const svg = el('svg', { viewBox: `0 0 ${larg} ${H}`, role: 'img', 'aria-label': op.titulo || 'Gráfico de barras' }, alvo);
    itens.forEach((it, k) => {
      const y = k * (alt + gap) + 4;
      const w = Math.max(2, ((it.valor - min) / (max - min)) * (larg - esq - dir));
      texto(svg, esq - 12, y + alt / 2 + 4, it.rotulo, { 'text-anchor': 'end', fill: it.destaque ? '#EAF1F6' : '#A9B8C6', 'font-weight': it.destaque ? 600 : 400, 'font-size': 13 });
      el('rect', { x: esq, y, width: larg - esq - dir, height: alt, rx: 6, fill: 'rgb(234 241 246 / .04)' }, svg);
      const r = el('rect', { x: esq, y, width: 0, height: alt, rx: 6, fill: it.cor || (it.destaque ? 'var(--acento)' : '#3B5566') }, svg);
      r.style.transition = 'width .7s cubic-bezier(.25,.46,.45,.94)';
      requestAnimationFrame(() => requestAnimationFrame(() => r.setAttribute('width', w)));
      texto(svg, esq + w + 10, y + alt / 2 + 4, op.formato ? op.formato(it.valor) : fmt(it.valor, op.casas || 0), { fill: '#EAF1F6', 'font-family': 'JetBrains Mono, monospace', 'font-size': 12.5 });
    });
    return svg;
  }

  /* colunas/linhas temporais: series [{nome, cor, valores:[]}], rotulos [] */
  function linhas(alvo, rotulos, series, op = {}) {
    const larg = op.largura || 720, alt = op.altura || 280, m = { t: 16, r: 16, b: 34, l: op.esquerda || 52 };
    const todos = series.flatMap((s) => s.valores).filter((v) => v != null);
    const max = op.max || Math.max(...todos) * 1.08, min = op.min ?? 0;
    alvo.innerHTML = '';
    const svg = el('svg', { viewBox: `0 0 ${larg} ${alt}`, role: 'img', 'aria-label': op.titulo || 'Gráfico de linhas' }, alvo);
    const X = (i) => m.l + (i * (larg - m.l - m.r)) / Math.max(1, rotulos.length - 1);
    const Y = (v) => alt - m.b - ((v - min) / (max - min)) * (alt - m.t - m.b);
    for (let k = 0; k <= 4; k++) {
      const v = min + ((max - min) * k) / 4, y = Y(v);
      el('line', { x1: m.l, x2: larg - m.r, y1: y, y2: y, stroke: 'rgb(234 241 246 / .08)' }, svg);
      texto(svg, m.l - 8, y + 4, op.formatoY ? op.formatoY(v) : fmt(v), { 'text-anchor': 'end', 'font-size': 11, 'font-family': 'JetBrains Mono, monospace', fill: '#7FA3B5' });
    }
    const salto = Math.ceil(rotulos.length / (op.maxRotulos || 12));
    rotulos.forEach((r, i) => { if (i % salto === 0 || i === rotulos.length - 1) texto(svg, X(i), alt - 10, r, { 'text-anchor': 'middle', 'font-size': 11, fill: '#7FA3B5' }); });
    series.forEach((s) => {
      const pts = s.valores.map((v, i) => (v == null ? null : [X(i), Y(v)])).filter(Boolean);
      if (op.area) el('path', { d: `M${pts[0][0]},${Y(min)} L${pts.map((p) => p.join(',')).join(' L')} L${pts[pts.length - 1][0]},${Y(min)} Z`, fill: s.cor, opacity: 0.12 }, svg);
      const p = el('path', { d: 'M' + pts.map((p) => p.join(',')).join(' L'), fill: 'none', stroke: s.cor, 'stroke-width': 2.5, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }, svg);
      const L = p.getTotalLength ? p.getTotalLength() : 0;
      if (L && !matchMedia('(prefers-reduced-motion: reduce)').matches) { p.style.strokeDasharray = L; p.style.strokeDashoffset = L; p.style.transition = 'stroke-dashoffset 1.2s cubic-bezier(.25,.46,.45,.94)'; requestAnimationFrame(() => requestAnimationFrame(() => (p.style.strokeDashoffset = 0))); }
      pts.forEach((pt) => el('circle', { cx: pt[0], cy: pt[1], r: 3, fill: s.cor }, svg));
    });
    return svg;
  }

  /* colunas agrupadas: grupos [{rotulo, valores:[...]}], series [{nome,cor}] */
  function colunas(alvo, grupos, series, op = {}) {
    const larg = op.largura || 720, alt = op.altura || 280, m = { t: 20, r: 12, b: 36, l: op.esquerda || 52 };
    const max = op.max || Math.max(...grupos.flatMap((g) => g.valores)) * 1.1;
    alvo.innerHTML = '';
    const svg = el('svg', { viewBox: `0 0 ${larg} ${alt}`, role: 'img', 'aria-label': op.titulo || 'Gráfico de colunas' }, alvo);
    const Y = (v) => alt - m.b - (v / max) * (alt - m.t - m.b);
    for (let k = 0; k <= 4; k++) { const v = (max * k) / 4, y = Y(v); el('line', { x1: m.l, x2: larg - m.r, y1: y, y2: y, stroke: 'rgb(234 241 246 / .08)' }, svg); texto(svg, m.l - 8, y + 4, op.formatoY ? op.formatoY(v) : fmt(v), { 'text-anchor': 'end', 'font-size': 11, 'font-family': 'JetBrains Mono, monospace', fill: '#7FA3B5' }); }
    const gw = (larg - m.l - m.r) / grupos.length, bw = Math.min(28, (gw * 0.7) / series.length);
    grupos.forEach((g, i) => {
      const x0 = m.l + i * gw + (gw - bw * series.length) / 2;
      g.valores.forEach((v, j) => {
        const r = el('rect', { x: x0 + j * bw, y: Y(0), width: bw - 3, height: 0, rx: 3, fill: series[j].cor }, svg);
        r.style.transition = 'y .7s cubic-bezier(.25,.46,.45,.94), height .7s cubic-bezier(.25,.46,.45,.94)';
        requestAnimationFrame(() => requestAnimationFrame(() => { r.setAttribute('y', Y(v)); r.setAttribute('height', Y(0) - Y(v)); }));
        const tt = el('title', {}, r); tt.textContent = `${g.rotulo} · ${series[j].nome}: ${op.formato ? op.formato(v) : fmt(v)}`;
      });
      texto(svg, m.l + i * gw + gw / 2, alt - 12, g.rotulo, { 'text-anchor': 'middle', 'font-size': 11.5, fill: '#A9B8C6' });
    });
    return svg;
  }

  function legenda(alvo, series) {
    alvo.innerHTML = series.map((s) => `<span class="chip" style="--c:${s.cor}"><b></b>${s.nome}</span>`).join(' ');
  }
  return { barrasH, linhas, colunas, legenda, fmt };
})();
