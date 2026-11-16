"""Gera o site a partir de ferramentas/conteudo.py.

Uso: python ferramentas/gerar.py

Saídas: index.html, areas/<área>.html, projetos/<projeto>.html e assets/js/projetos.js.
Páginas com manual=True são mantidas; o gerador só troca o trecho entre os marcadores
<!--cabeca-->...<!--/cabeca-->, <!--migalha-->...<!--/migalha--> e <!--nav-->...<!--/nav-->.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import modelo as M  # noqa: E402
from conteudo import AREAS, P  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
AREA = {a["id"]: a for a in AREAS}
SCRIPTS = '<script src="{r}assets/js/graficos.js"></script>\n<script src="{r}assets/js/mosaico.js"></script>\n<script src="{r}assets/js/telas.js"></script>'


def por_area(aid):
    return [p for p in P if p["area"] == aid]


def vizinhos(p):
    lista = por_area(p["area"])
    i = lista.index(p)
    return (lista[i - 1] if i > 0 else None), (lista[i + 1] if i < len(lista) - 1 else None)


def cabeca(titulo, descricao, acento, raiz, atual=None, css=""):
    return M.CABECA.format(titulo=titulo, descricao=descricao, acento=acento, raiz=raiz, css=css, menu=M.menu(AREAS, raiz, atual))


def pagina_projeto(p):
    a = AREA[p["area"]]
    ant, prox = vizinhos(p)
    partes = [cabeca(p["nome"], p["resumo"], a["cor"], "../", a["id"]), M.hero(p, a, "../"), M.numeros(p.get("numeros"))]
    for bloco in p.get("blocos", []):
        apoio = bloco[2] if len(bloco) > 2 else ""
        larga = len(bloco) > 3 and bloco[3] == "larga"
        partes.append((M.secao_larga if larga else M.secao)(bloco[0], bloco[1], apoio))
    partes.append(M.tecnologias(p["stack"], p.get("link")))
    partes.append(M.navegacao(ant, prox, a, "../"))
    partes.append(M.RODAPE.format(raiz="../", scripts=SCRIPTS.format(r="../") + "\n" + p.get("script", "")))
    (RAIZ / "projetos" / f"{p['slug']}.html").write_text("".join(partes), encoding="utf-8")


def trocar(texto, marca, novo):
    padrao = re.compile(rf"<!--{marca}-->.*?<!--/{marca}-->", re.S)
    if not padrao.search(texto):
        raise SystemExit(f"marcador {marca} ausente")
    return padrao.sub(lambda _: f"<!--{marca}-->{novo}<!--/{marca}-->", texto)


def atualizar_manual(p):
    a = AREA[p["area"]]
    ant, prox = vizinhos(p)
    arq = RAIZ / "projetos" / f"{p['slug']}.html"
    t = arq.read_text(encoding="utf-8")
    topo = f'<header class="topo"><div class="topo__in">\n  <a class="marca" href="../index.html"><img src="../assets/img/logo-negativo.svg" alt="HoldUp" width="132" height="38"><span>Portfólio</span></a>\n  <nav class="nav" aria-label="Áreas">{M.menu(AREAS, "../", a["id"])}</nav>\n</div></header>'
    t = trocar(t, "cabeca", topo)
    t = trocar(t, "migalha", f'<a href="../index.html">Portfólio</a><span aria-hidden="true">/</span><a href="../areas/{a["id"]}.html">{a["nome"]}</a>')
    t = trocar(t, "nav", M.navegacao(ant, prox, a, "../").replace("\n</main>\n", ""))
    arq.write_text(t, encoding="utf-8")


def pagina_area(a):
    itens = "".join(
        f'<li><a href="../projetos/{p["slug"]}.html"><span class="sumario__n">{i:02d}</span>'
        f'<span class="sumario__t"><strong>{p["nome"]}</strong><span>{p["resumo"]}</span></span>'
        f'<span class="sumario__tec">{p["tec"]}</span><span class="seta" aria-hidden="true">→</span></a></li>'
        for i, p in enumerate(por_area(a["id"]), 1)
    )
    outras = "".join(f'<a class="chip" style="--c:{o["cor"]}" href="{o["id"]}.html"><b></b>{o["nome"]}</a>' for o in AREAS if o["id"] != a["id"])
    corpo = f"""<main id="conteudo">
<section class="caso-hero"><div class="wrap">
  <p class="migalha entra"><a href="../index.html">Portfólio</a></p>
  <h1 class="entra" style="--o:1">{a['nome']}</h1>
  <p class="lead entra" style="--o:2">{a['texto']}</p>
</div></section>
<section class="bloco"><div class="wrap">
  <h2 class="sr">Sumário</h2>
  <ol class="sumario revela">{itens}</ol>
</div></section>
<section class="bloco"><div class="wrap"><p class="rotulo"><i></i>Outras áreas</p><div class="outras">{outras}</div></div></section>
</main>
"""
    html = cabeca(a["nome"], a["texto"], a["cor"], "../", a["id"]) + corpo + M.RODAPE.format(raiz="../", scripts=SCRIPTS.format(r="../"))
    (RAIZ / "areas" / f"{a['id']}.html").write_text(html, encoding="utf-8")


def pagina_inicial():
    cartoes = "".join(
        f'<a class="area revela" href="areas/{a["id"]}.html" style="--c:{a["cor"]}"><div class="area__mosaico">'
        + "".join(f'<b style="--o:{0.25 + ((k * 7 + i * 3) % 10) / 13:.2f}"></b>' for k in range(12))
        + f'</div><h3>{a["nome"]}</h3><p>{a["texto"]}</p><small>Ver projetos <span class="seta" aria-hidden="true">→</span></small></a>'
        for i, a in enumerate(AREAS)
    )
    corpo = f"""<main id="conteudo">
<section class="hero hero--curto">
  <canvas data-mosaico aria-hidden="true"></canvas>
  <div class="wrap">
    <p class="rotulo entra"><i></i>Portfólio</p>
    <h1 class="entra" style="--o:1">HoldUp</h1>
    <p class="lead entra" style="--o:2">Desenvolvimento de soluções. Projetos organizados por área.</p>
  </div>
</section>
<section class="secao" id="areas"><div class="wrap">
  <h2 class="sr">Áreas</h2>
  <div class="areas">{cartoes}</div>
</div></section>
<section class="secao secao--clara" id="contato"><div class="wrap contato">
  <div><p class="rotulo"><i></i>Contato</p><h2>HoldUp</h2><p>Desenvolvimento de sistemas, painéis de dados e aprendizado de máquina.</p></div>
  <div class="hero__acoes"><a class="btn" href="https://wa.me/5531987510985">WhatsApp</a><a class="btn btn--linha" href="https://holdupsolucoes.com.br/">holdupsolucoes.com.br</a><a class="btn btn--linha" href="https://github.com/Bruno-LSo">GitHub</a></div>
</div></section>
</main>
"""
    html = cabeca("Portfólio", "Projetos da HoldUp organizados por área.", "#4FD1D4", "").replace("<title>Portfólio · HoldUp</title>", "<title>Portfólio · HoldUp</title>")
    (RAIZ / "index.html").write_text(html + corpo + M.RODAPE.format(raiz="", scripts=SCRIPTS.format(r="")), encoding="utf-8")


def dados_js():
    areas = [{k: a[k] for k in ("id", "nome", "curto", "cor")} for a in AREAS]
    projs = [{"slug": p["slug"], "area": p["area"], "nome": p["nome"]} for p in P]
    (RAIZ / "assets" / "js" / "projetos.js").write_text(
        "/* Gerado por ferramentas/gerar.py */\nwindow.AREAS = " + json.dumps(areas, ensure_ascii=False) + ";\nwindow.PROJETOS = " + json.dumps(projs, ensure_ascii=False) + ";\n",
        encoding="utf-8")


PROPRIO = "https://bruno-lso.github.io/portfolio"
_LINK_FORA = re.compile(r'<a(\s[^>]*?)?\shref="(https?://[^"]+)"([^>]*)>')


def _nova_aba(m):
    antes, url, depois = m.groups()
    antes = (antes or "") + " "
    attrs = antes + depois
    if url.startswith(PROPRIO) or "target=" in attrs:
        return m.group(0)
    rel = re.search(r'\brel="([^"]*)"', attrs)
    if rel:
        valores = rel.group(1).split()
        for v in ("noopener", "noreferrer"):
            if v not in valores:
                valores.append(v)
        novo_rel = f'rel="{" ".join(valores)}"'
        antes = antes.replace(rel.group(0), novo_rel)
        depois = depois.replace(rel.group(0), novo_rel)
        return f'<a{antes}href="{url}"{depois} target="_blank">'
    return f'<a{antes}href="{url}"{depois} target="_blank" rel="noopener noreferrer">'


def links_externos_em_nova_aba():
    """Link para outra plataforma abre em nova aba (regra do Bruno, 16/11/2026)."""
    for arq in [RAIZ / "index.html", *(RAIZ / "areas").glob("*.html"), *(RAIZ / "projetos").glob("*.html")]:
        texto = arq.read_text(encoding="utf-8")
        novo = _LINK_FORA.sub(_nova_aba, texto)
        if novo != texto:
            arq.write_text(novo, encoding="utf-8", newline="")


def main():
    (RAIZ / "areas").mkdir(exist_ok=True)
    (RAIZ / "projetos").mkdir(exist_ok=True)
    slugs = [p["slug"] for p in P]
    assert len(slugs) == len(set(slugs)), "slug repetido"
    for p in P:
        atualizar_manual(p) if p.get("manual") else pagina_projeto(p)
    for a in AREAS:
        pagina_area(a)
    pagina_inicial()
    dados_js()
    links_externos_em_nova_aba()
    esperados = set(f"{s}.html" for s in slugs)
    sobra = [f.name for f in (RAIZ / "projetos").glob("*.html") if f.name not in esperados]
    if sobra:
        for nome in sobra:
            (RAIZ / "projetos" / nome).unlink()
        print("removidas:", ", ".join(sobra))
    print(f"{len(P)} projetos, {len(AREAS)} áreas")


if __name__ == "__main__":
    main()
