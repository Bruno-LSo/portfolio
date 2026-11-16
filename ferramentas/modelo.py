"""Partes comuns das páginas: cabeçalho, rodapé, blocos e navegação."""
from html import escape

CABECA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · HoldUp</title>
<meta name="description" content="{descricao}">
<meta name="theme-color" content="#0B1820">
<link rel="icon" href="{raiz}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{raiz}favicon-32px.png" sizes="32x32">
<link rel="apple-touch-icon" href="{raiz}apple-touch-icon.png">
<link rel="stylesheet" href="{raiz}assets/css/portfolio.css">
<style>:root{{--acento:{acento}}}{css}</style>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
<header class="topo"><div class="topo__in">
  <a class="marca" href="{raiz}index.html"><img src="{raiz}assets/img/logo-negativo.svg" alt="HoldUp" width="132" height="38"><span>Portfólio</span></a>
  <nav class="nav" aria-label="Áreas">{menu}</nav>
</div></header>
"""

RODAPE = """
<footer class="rodape"><div class="wrap rodape__in">
  <img src="{raiz}assets/img/logo-negativo.svg" alt="HoldUp" width="104" height="30">
  <p>HoldUp · <a href="https://holdupsolucoes.com.br/">holdupsolucoes.com.br</a> · <a href="https://github.com/Bruno-LSo">GitHub</a></p>
</div></footer>
{scripts}
</body>
</html>
"""


def menu(areas, raiz, atual=None):
    return "".join(
        f'<a href="{raiz}areas/{a["id"]}.html"{" aria-current=\"page\"" if a["id"] == atual else ""}>{a["curto"]}</a>'
        for a in areas
    )


def hero(p, area, raiz):
    ficha = "".join(f"<div><dt>{escape(k)}</dt><dd>{v}</dd></div>" for k, v in p.get("ficha", []))
    ficha_html = f'<dl class="ficha entra" style="--o:3">{ficha}</dl>' if ficha else ""
    return f"""<main id="conteudo">
<section class="caso-hero"><div class="wrap">
  <p class="migalha entra"><a href="{raiz}index.html">Portfólio</a><span aria-hidden="true">/</span><a href="{raiz}areas/{area['id']}.html">{area['nome']}</a></p>
  <h1 class="entra" style="--o:1">{p['nome']}</h1>
  <p class="lead entra" style="--o:2">{p['lead']}</p>
  {ficha_html}
</div></section>
"""


def numeros(lista):
    if not lista:
        return ""
    itens = "".join(f'<div class="kpi"><strong class="num">{v}</strong><span>{t}</span></div>' for v, t in lista)
    return f'<section class="bloco"><div class="wrap"><div class="kpis revela">{itens}</div></div></section>\n'


def secao(titulo, corpo, apoio=""):
    lado = f'<div><h2>{titulo}</h2>{f"<p>{apoio}</p>" if apoio else ""}</div>'
    return f'<section class="bloco"><div class="wrap bloco__grid">{lado}<div class="revela">{corpo}</div></div></section>\n'


def lista(itens):
    return '<ul class="lista">' + "".join(f"<li><strong>{t}</strong>{d}</li>" for t, d in itens) + "</ul>"


def fluxo(itens, nota=""):
    corpo = '<div class="fluxo">' + "".join(f"<div><b>{b}</b><h4>{h}</h4><p>{p}</p></div>" for b, h, p in itens) + "</div>"
    return corpo + (f'<p class="nota">{nota}</p>' if nota else "")


def texto(paragrafos):
    return '<div class="texto">' + "".join(f"<p>{p}</p>" for p in paragrafos) + "</div>"


def painel(barra, interno, nota=""):
    n = f'<p class="nota">{nota}</p>' if nota else ""
    b = f'<div class="painel__barra"><i></i><i></i><i></i><span>{barra}</span></div>' if barra else ""
    return f'<div class="painel">{b}<div class="painel__corpo">{interno}{n}</div></div>'


def tecnologias(itens, link=None):
    s = "".join(f"<span>{i}</span>" for i in itens)
    l = f'<p style="margin-top:22px"><a class="btn btn--mini btn--linha" href="{link[1]}" rel="noopener">{link[0]} <span class="seta" aria-hidden="true">→</span></a></p>' if link else ""
    return f'<section class="bloco"><div class="wrap bloco__grid"><div><h2>Tecnologias</h2></div><div><div class="stack">{s}</div>{l}</div></div></section>\n'


def navegacao(ant, prox, area, raiz):
    def item(p, rot, cls):
        if not p:
            return f'<span class="navp__item {cls}" aria-hidden="true"></span>'
        return f'<a class="navp__item {cls}" href="{raiz}projetos/{p["slug"]}.html"><small>{rot}</small><span>{p["nome"]}</span></a>'
    return (f'<nav class="navp" aria-label="Projetos da área"><div class="wrap navp__in">'
            f'{item(ant, "Anterior", "navp__ant")}'
            f'<a class="navp__item navp__sum" href="{raiz}areas/{area["id"]}.html"><small>Sumário</small><span>{area["nome"]}</span></a>'
            f'{item(prox, "Próximo", "navp__prox")}</div></nav>\n</main>\n')


# ---------------------------------------------------------------- componentes visuais
def secao_larga(titulo, corpo, apoio=""):
    """Seção em largura total: título em cima, conteúdo embaixo (telas, fluxogramas, diagramas)."""
    ap = f"<p>{apoio}</p>" if apoio else ""
    return f'<section class="bloco"><div class="wrap"><div class="bloco__cab"><h2>{titulo}</h2>{ap}</div><div class="revela">{corpo}</div></div></section>\n'


def telas(slug, itens, celular=False, raiz="../"):
    """Galeria de telas. itens: [(arquivo, legenda)]. Arquivos em assets/telas/<slug>/. Clique amplia."""
    cls = "telas telas--celular" if celular else "telas"
    figs = "".join(
        f'<figure><a href="{raiz}assets/telas/{slug}/{arq}" data-ampliar>'
        f'<img src="{raiz}assets/telas/{slug}/{arq}" alt="{escape(leg)}" loading="lazy"></a>'
        f'<figcaption>{leg}</figcaption></figure>'
        for arq, leg in itens)
    return f'<div class="{cls}">{figs}</div>'


def fluxograma(etapas, nota=""):
    """Fluxo de páginas ou de processo, em níveis de cima para baixo.
    etapas: [(rótulo do nível, [caixa, ...], texto da seta opcional)]
    caixa: "Título" ou ("Título", "detalhe curto")."""
    partes = []
    for i, et in enumerate(etapas):
        rotulo, caixas = et[0], et[1]
        seta = et[2] if len(et) > 2 else ""
        cx = "".join(
            f'<div class="fg__caixa"><strong>{c[0]}</strong><span>{c[1]}</span></div>' if isinstance(c, tuple)
            else f'<div class="fg__caixa"><strong>{c}</strong></div>'
            for c in caixas)
        partes.append(f'<div class="fg__nivel"><b class="fg__rot">{rotulo}</b><div class="fg__caixas">{cx}</div></div>')
        if i < len(etapas) - 1:
            partes.append(f'<div class="fg__seta" aria-hidden="true"><i></i>{f"<span>{seta}</span>" if seta else ""}</div>')
    n = f'<p class="nota">{nota}</p>' if nota else ""
    return f'<div class="fg">{"".join(partes)}</div>{n}'


def achados(itens):
    """Cartões de achados/resultados. itens: [(valor ou título curto, texto)]."""
    return '<div class="achados">' + "".join(
        f'<div class="achado"><strong class="num">{v}</strong><p>{t}</p></div>' for v, t in itens) + "</div>"


def barras(itens, titulo="", casas=0, sufixo="", nota=""):
    """Gráfico de barras horizontais desenhado por assets/js/graficos.js.
    itens: [(rótulo, valor, destaque_bool)]."""
    import json
    dados = json.dumps({"itens": [{"rotulo": r, "valor": v, "destaque": bool(d[0]) if d else False} for r, v, *d in itens],
                        "titulo": titulo, "casas": casas, "sufixo": sufixo}, ensure_ascii=False)
    n = f'<p class="nota">{nota}</p>' if nota else ""
    t = f'<p class="grafico__tit">{titulo}</p>' if titulo else ""
    return f'<figure class="grafico">{t}<div data-barras=\'{escape(dados)}\'></div>{n}</figure>'


def diagrama(svg, legenda=""):
    """Diagrama em SVG inline, desenhado à mão no padrão de cores do portfólio."""
    leg = f"<figcaption>{legenda}</figcaption>" if legenda else ""
    return f'<figure class="diagrama">{svg}{leg}</figure>'


def colunas(*blocos):
    """Coloca blocos HTML lado a lado (empilham no celular)."""
    return '<div class="colunas">' + "".join(f"<div>{b}</div>" for b in blocos) + "</div>"
