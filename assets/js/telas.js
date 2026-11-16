/* Amplia telas da galeria e desenha gráficos declarados em data-barras. */
(function () {
  document.addEventListener('click', function (e) {
    const a = e.target.closest('a[data-ampliar]');
    if (!a) return;
    e.preventDefault();
    const leg = a.parentElement.querySelector('figcaption');
    const cx = document.createElement('div');
    cx.className = 'ampliada';
    cx.setAttribute('role', 'dialog');
    cx.setAttribute('aria-modal', 'true');
    cx.innerHTML = '<button type="button" aria-label="Fechar">×</button><img alt=""><p></p>';
    cx.querySelector('img').src = a.href;
    cx.querySelector('img').alt = a.querySelector('img').alt;
    cx.querySelector('p').textContent = leg ? leg.textContent : '';
    const fechar = () => { cx.remove(); document.removeEventListener('keydown', tecla); a.focus(); };
    const tecla = (ev) => { if (ev.key === 'Escape') fechar(); };
    cx.addEventListener('click', fechar);
    document.addEventListener('keydown', tecla);
    document.body.appendChild(cx);
    cx.querySelector('button').focus();
  });
  function graficos() {
    if (!window.G || !G.barrasH) return;
    document.querySelectorAll('[data-barras]').forEach(function (el) {
      const d = JSON.parse(el.getAttribute('data-barras'));
      const casas = d.casas || 0, suf = d.sufixo || '';
      const fmt = (v) => new Intl.NumberFormat('pt-BR', { minimumFractionDigits: casas, maximumFractionDigits: casas }).format(v) + suf;
      const maior = Math.max(...d.itens.map((i) => fmt(i.valor).length));
      const rot = Math.max(...d.itens.map((i) => String(i.rotulo).length));
      G.barrasH(el, d.itens, { titulo: d.titulo, casas: casas, formato: fmt, direita: maior * 8 + 22, esquerda: Math.min(260, Math.max(90, rot * 7.4 + 16)) });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', graficos); else graficos();
})();
